import pandas as pd  # for storing text and embeddings data
from data_processing import combine_columns
from embeddings import get_embedding
from search import ask


def main():
    # データの読み込み
    input_csv_path = "./medals_total.csv"

    df = pd.read_csv(input_csv_path)
    df = df[["country", "Gold Medal", "Silver Medal", "Bronze Medal", "Total"]]

    # データの前処理
    df["combined"] = df.apply(combine_columns, axis=1)

    # 埋め込みベクトルの計算
    df["combined_embedding"] = df["combined"].apply(lambda x: get_embedding(x))

    # ベクトルデータの出力
    # print(df["combined"].head(), df["combined_embedding"].head())

    # 質問の実行
    ask(
        "How many gold medals did Japan win at the 2024 Paris Olympics?",
        df,
        print_message=True,
    )
    ask(
        "Who won the gold medal in curling at the 2018 Winter Olympics?",
        df,
        print_message=True,
    )


if __name__ == "__main__":
    main()
