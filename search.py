import pandas as pd  # for storing text and embeddings data
from scipy import spatial  # for calculating vector similarities for search
import tiktoken  # for counting tokens
from config import client, EMBEDDING_MODEL, GPT_MODEL


# 検索関数
def strings_ranked_by_relatedness(
    query: str,
    df: pd.DataFrame,
    relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
    top_n: int = 100,
) -> tuple[list[str], list[float]]:
    """Returns a list of strings and relatednesses, sorted from most related to least."""
    query_embedding_response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=query,
    )
    query_embedding = query_embedding_response.data[0].embedding

    strings_and_relatednesses = [
        (
            row["combined"],
            relatedness_fn(query_embedding, row["combined_embedding"]),
        )
        for i, row in df.iterrows()
    ]
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]


# トークン数を数える関数
def num_tokens(text: str, model: str = GPT_MODEL) -> int:
    """Return the number of tokens in a string."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))


# GPTへのメッセージを作成する関数
def query_message(query: str, df: pd.DataFrame, model: str, token_budget: int) -> str:
    """Return a message for GPT, with relevant source texts pulled from a dataframe."""
    strings, relatednesses = strings_ranked_by_relatedness(query, df)
    introduction = 'Use the below data on the 2024 Summer Olympics to answer the subsequent question. If the answer cannot be found in the data, write "I could not find an answer."'
    question = f"\n\nQuestion: {query}"
    message = introduction
    for string in strings:
        if num_tokens(message + question, model=model) > token_budget:
            break
        else:
            message += string
    return message + question


# 質問に回答する関数
def ask(
    query: str,
    df: pd.DataFrame,
    model: str = GPT_MODEL,
    token_budget: int = 4096 - 500,
    print_message: bool = False,
) -> str:
    """Answers a query using GPT and a dataframe of relevant texts and embeddings."""
    message = query_message(query, df, model=model, token_budget=token_budget)
    if print_message:
        print(message)
    messages = [
        {
            "role": "system",
            "content": "You answer questions about the 2024 Summer Olympics.",
        },
        {"role": "user", "content": message},
    ]
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=0
    )
    response_message = response.choices[0].message.content
    if print_message:
        print(response_message)
    return response_message
