# 数値項目にラベルを付けてテキスト化する関数
def label_numeric_columns(row):
    labeled_text = []
    for col in ["Gold Medal", "Silver Medal", "Bronze Medal", "Total"]:
        # 項目名と値を組み合わせる
        labeled_text.append(f"{col}: {row[col]}")
    return ", ".join(labeled_text)


# テキスト項目と数値項目を結合する関数
def combine_columns(row):
    # テキスト項目を結合
    text_parts = [str(row[col]) for col in ["country"]]
    # 数値項目をラベル付けして結合
    numeric_text = label_numeric_columns(row)
    # すべての項目を結合
    combined_text = ". ".join(text_parts + [numeric_text])
    return combined_text
