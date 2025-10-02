# takumi

技術記事や技術メモを添削して、校正、推敲するエージェントサービス

## 概要

CLI 上で使用できる技術記事や技術メモの添削、校正、推敲エージェントサービスです。
.md ファイルを渡すと、LLM エージェントが内容を分析し、改善された文章を生成します。

## 特徴

- **evidence_agent**: 記載されている内容が正しいかどうかをチェック
- **proofread_agent**: 文章が読みやすいか、誤字脱字がないかをチェック
- **report_agent**: 2 つのエージェントの結果を元に推敲した文章を生成

## 技術スタック

- 言語: Python 3.12 以上
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

#### OpenAI API を使用する場合

```bash
# OpenAI APIキーを環境変数に設定
export OPENAI_API_KEY="your-api-key-here"

# マークダウンファイルを処理（デフォルトモデル: gpt-4o-mini）
uv run takumi path/to/your/article.md --provider openai
```

#### Google Gemini API を使用する場合（デフォルト）

```bash
# Google Gemini APIキーを環境変数に設定
export GOOGLE_API_KEY="your-google-api-key-here"

# Geminiを使用してマークダウンファイルを処理（デフォルトモデル: gemini-2.0-flash）
uv run takumi path/to/your/article.md

# または明示的に指定
uv run takumi path/to/your/article.md --provider gemini
```

### オプション

```bash
# 出力ファイルを指定
uv run takumi article.md -o improved_article.md

# 詳細なフィードバックを表示
uv run takumi article.md --verbose

# LLMプロバイダーを指定（openai または gemini、デフォルト: gemini）
uv run takumi article.md --provider gemini

# 使用するモデルを指定
uv run takumi article.md --provider openai --model gpt-4o  # OpenAIの場合（デフォルト: gpt-4o-mini）
uv run takumi article.md --provider gemini --model gemini-1.5-pro  # Geminiの場合（デフォルト: gemini-2.0-flash）

# APIキーをコマンドラインで指定
uv run takumi article.md --api-key your-api-key-here --provider openai
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
