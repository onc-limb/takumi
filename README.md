# takumi

技術記事や技術メモを添削して、校正、推敲するエージェントサービス

## 概要

CLI上で使用できる技術記事や技術メモの添削、校正、推敲エージェントサービスです。
.mdファイルを渡すと、LLMエージェントが内容を分析し、改善された文章を生成します。

## 特徴

- **evidence_agent**: 記載されている内容が正しいかどうかをチェック
- **proofread_agent**: 文章が読みやすいか、誤字脱字がないかをチェック
- **report_agent**: 2つのエージェントの結果を元に推敲した文章を生成

## 技術スタック

- 言語: Python 3.12以上
- フレームワーク: LangChain
- パッケージ管理: uv

## インストール

```bash
# uvがインストールされていない場合
pip install uv

# プロジェクトのクローン
git clone https://github.com/onc-limb/takumi.git
cd takumi

# 依存関係のインストール
uv sync

# または開発用にインストール
uv pip install -e .
```

## 使い方

### 基本的な使い方

```bash
# OpenAI APIキーを環境変数に設定
export OPENAI_API_KEY="your-api-key-here"

# マークダウンファイルを処理
uv run takumi path/to/your/article.md
```

### オプション

```bash
# 出力ファイルを指定
uv run takumi article.md -o improved_article.md

# 詳細なフィードバックを表示
uv run takumi article.md --verbose

# 使用するモデルを指定
uv run takumi article.md --model gpt-4o

# APIキーをコマンドラインで指定
uv run takumi article.md --api-key your-api-key-here
```

### ヘルプ

```bash
uv run takumi --help
```

## サンプルファイル

リポジトリには`sample.md`というサンプルファイルが含まれています：

```bash
uv run takumi sample.md --verbose
```

このコマンドを実行すると、`sample_revised.md`というファイルが生成されます。

## ライセンス

MIT License
