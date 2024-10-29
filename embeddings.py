from config import client, EMBEDDING_MODEL


# 埋め込みベクトルを取得する関数
def get_embedding(text):
    response = client.embeddings.create(input=text, model=EMBEDDING_MODEL)
    return response.data[0].embedding
