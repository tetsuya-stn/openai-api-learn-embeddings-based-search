# OpenAI APIを活用した埋め込みベースの検索

このリポジトリでは、OpenAI APIを使用して埋め込みベースの検索を実装する方法を学習できます。テキストデータから埋め込み（Embeddings）を生成し、それを基に類似度検索を行う実装例が含まれています。

## 概要

埋め込み（Embeddings）とは、テキストの意味を数値ベクトルに変換したもので、検索やクラスタリング、レコメンデーションシステムに利用できます。このプロジェクトでは、OpenAI APIを使ってテキストから埋め込みを生成し、生成したベクトルを用いて類似度検索を行う基本的な方法を学習できます。

## 主な機能

- テキストと数値データを組み合わせた埋め込みベクトルの生成
- コサイン類似度を用いた類似度検索
- データフレーム内のデータに基づく質問応答システム

## 前提条件

- Python 3.7以上
- OpenAI APIキー

## インストール手順

1. **リポジトリをクローンします**

   ```bash
   git clone https://github.com/tetsuya-stn/openai-api-learn-embeddings-based-search.git
   cd openai-api-learn-embeddings-based-search
   ```

2. **仮想環境を作成し、アクティブ化します**（オプションですが推奨）

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
   ```

3. **必要なパッケージをインストールします**

   ```bash
   pip install -r requirements.txt
   ```

## セットアップ

1. **OpenAI APIキーの取得**

   OpenAIのAPIサービスを使用するためには、APIキーが必要です。まだ取得していない場合は、[OpenAIの公式ウェブサイト](https://platform.openai.com/)から取得できます。

2. **APIキーの設定**

   APIキーを環境変数としてエクスポートします：

   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## 使用方法

メインのスクリプトである`main.py`を実行することで、埋め込みベースの検索と質問応答機能を試すことができます。

### 実行方法

```bash
python main.py
```

### スクリプトの流れ

1. **データの読み込み**
   サンプルデータとして、`medals_total.csv`からオリンピックのメダル獲得情報を読み込みます。

2. **データの前処理**
   テキストデータと数値データを組み合わせて、検索に利用するテキストを生成します。

3. **埋め込みの生成**
   OpenAI APIのEmbeddings機能を用いて、各行のテキストから埋め込みベクトルを生成します。

4. **類似度検索**
   ユーザーのクエリに基づいてデータ内で最も関連性の高い項目を検索し、結果を返します。

5. **質問応答**
   類似度が高い結果を基にして、GPTモデルを用いた質問応答を行います。

## ファイル構成

- `main.py`：アプリケーションのメインスクリプト
- `config.py`：API設定やモデル名を管理
- `data_processing.py`：データ前処理用の関数を含む
- `embeddings.py`：埋め込み生成に関連する関数を含む
- `search.py`：類似度検索と質問応答に関する関数を含む
- `requirements.txt`：必要なパッケージを記載
- `medals_total.csv`：サンプルデータとしてのCSVファイル

## カスタマイズ

- **データ**
   `medals_total.csv`を他のデータセットに置き換えることで、異なるデータを対象に埋め込みベースの検索を行うことが可能です。必要に応じて前処理関数を調整してください。

- **モデル**
   `config.py`の`EMBEDDING_MODEL`および`GPT_MODEL`変数を変更することで、使用する埋め込みモデルや生成モデルを変更できます。
