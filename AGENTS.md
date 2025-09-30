# takumi - AI 開発エージェント向けドキュメント

## プロジェクト概要

`takumi`は、技術記事や技術メモを添削・校正・推敲するための CLI ベースのエージェントサービスです。
LangChain と OpenAI API を活用し、複数の AI エージェントが協調して動作することで、技術記事の品質向上を支援します。

### 主な機能

- **evidence_agent**: 記載内容の技術的正確性をチェック
- **proofread_agent**: 文章の読みやすさ、誤字脱字をチェック
- **report_agent**: 2 つのエージェントの結果を元に推敲した文章を生成

## ディレクトリ構成

```
takumi/
├── AGENTS.md                    # 本ファイル - AI開発エージェント向けドキュメント
├── README.md                    # ユーザー向けドキュメント
├── demo.py                      # デモスクリプト
├── example_docker.md            # Dockerの使用例
├── sample.md                    # サンプル入力ファイル
├── pyproject.toml               # プロジェクト設定・依存関係管理
├── uv.lock                      # パッケージバージョンロックファイル
└── src/
    └── takumi/                  # メインパッケージ
        ├── __init__.py          # パッケージ初期化
        ├── cli.py               # CLIエントリーポイント
        ├── evidence_agent.py    # 内容チェックエージェント
        ├── proofread_agent.py   # 校正エージェント
        ├── report_agent.py      # 推敲・レポート生成エージェント
        ├── py.typed             # 型情報マーカー
        └── __pycache__/         # Pythonバイトコードキャッシュ
```

### 各ファイルの詳細

#### コアモジュール

- **cli.py**: CLI インターフェースの実装。Click ライブラリを使用してコマンドライン引数を処理し、各エージェントを呼び出します。
- **evidence_agent.py**: 技術的な正確性をチェックするエージェント。事実確認、古い情報の検出、曖昧な表現の検出を行います。
- **proofread_agent.py**: 文章の校正を行うエージェント。誤字脱字、読みやすさ、文体の統一性をチェックします。
- **report_agent.py**: 各エージェントのフィードバックを元に、改善された記事を生成するエージェント。

#### 設定ファイル

- **pyproject.toml**: プロジェクトのメタデータ、依存関係、ビルド設定を定義。
- **uv.lock**: uv パッケージマネージャーによる依存関係のバージョンロックファイル。

## 技術スタック

### 言語・ランタイム

- **Python**: 3.12 以上
- **型ヒント**: py.typed による完全な型サポート

### フレームワーク・ライブラリ

- **LangChain**: 0.3.0 以上 - LLM アプリケーションフレームワーク
- **LangChain-OpenAI**: 0.2.0 以上 - OpenAI 統合
- **LangChain-Google-GenAI**: Google Gemini 統合
- **Click**: 8.0.0 以上 - CLI フレームワーク

### ツール・環境

- **uv**: パッケージマネージャー・ビルドツール
- **OpenAI API**: LLM バックエンド（gpt-4o-mini, gpt-4o など）
- **Google Gemini API**: LLM バックエンド（gemini-1.5-flash, gemini-1.5-pro など）

### アーキテクチャパターン

- **マルチエージェントシステム**: 複数の専門化されたエージェントが協調動作
- **パイプライン処理**: 入力 → チェック → 校正 → 推敲 → 出力

## コーディングルール

### スタイルガイド

（現在空欄 - プロジェクトの進行に応じて追加予定）

### ベストプラクティス

（現在空欄 - プロジェクトの進行に応じて追加予定）

### 命名規則

（現在空欄 - プロジェクトの進行に応じて追加予定）

### テスト方針

（現在空欄 - プロジェクトの進行に応じて追加予定）

## コマンド集

### 環境セットアップ

```bash
# uvのインストール（未インストールの場合）
pip install uv

# プロジェクトのクローン
git clone https://github.com/onc-limb/takumi.git
cd takumi

# 依存関係のインストール
uv sync

# 開発モードでインストール
uv pip install -e .
```

### 基本的な使用方法

#### OpenAI API を使用する場合

```bash
# OpenAI APIキーを環境変数に設定
export OPENAI_API_KEY="your-api-key-here"

# マークダウンファイルを処理（デフォルト: gpt-4o-mini）
uv run takumi path/to/your/article.md

# 使用するモデルを指定
uv run takumi article.md --model gpt-4o

# APIキーをコマンドラインで指定
uv run takumi article.md --api-key your-api-key-here --provider openai
```

#### Google Gemini API を使用する場合

```bash
# Google Gemini APIキーを環境変数に設定
export GOOGLE_API_KEY="your-google-api-key-here"

# Geminiを使用してマークダウンファイルを処理
uv run takumi path/to/your/article.md --provider gemini

# 使用するGeminiモデルを指定
uv run takumi article.md --provider gemini --model gemini-1.5-pro

# APIキーをコマンドラインで指定
uv run takumi article.md --api-key your-api-key-here --provider gemini
```

#### 共通オプション

```bash
# 出力ファイルを指定
uv run takumi article.md -o improved_article.md

# 詳細なフィードバックを表示
uv run takumi article.md --verbose

# ヘルプを表示
uv run takumi --help
```

### サンプル実行

```bash
# サンプルファイルで試す
uv run takumi sample.md --verbose

# 実行すると sample_revised.md が生成される
```

### 開発用コマンド

```bash
# パッケージのビルド
uv build

# 依存関係の更新
uv lock --upgrade

# 特定パッケージの追加
uv add package-name

# 開発用パッケージの追加
uv add --dev package-name

# Pythonの実行
uv run python demo.py

# 仮想環境のアクティベート（必要に応じて）
source .venv/bin/activate
```

### デバッグ・トラブルシューティング

```bash
# 詳細なエラー情報を表示
uv run takumi article.md --verbose

# Python環境の確認
uv run python --version

# インストール済みパッケージの確認
uv pip list

# 依存関係ツリーの表示
uv tree
```

## エージェントの動作フロー

1. **入力**: ユーザーがマークダウンファイルを指定
2. **Evidence Agent**: 技術的正確性をチェックし、フィードバックを生成
3. **Proofread Agent**: 文章の校正を行い、フィードバックを生成
4. **Report Agent**: 両エージェントのフィードバックを統合し、改善された記事を生成
5. **出力**: 推敲された記事を指定ファイルに保存

## 開発メモ

### API 使用に関する注意点

#### OpenAI API

- OpenAI API キーが必須（環境変数 `OPENAI_API_KEY` またはコマンドラインオプション）
- デフォルトモデルは`gpt-4o-mini`（コスト効率重視）
- `gpt-4o`等の上位モデルも`--model`オプションで指定可能
- プロバイダー指定なし、または`--provider openai`で使用

#### Google Gemini API

- Google API キーが必須（環境変数 `GOOGLE_API_KEY` またはコマンドラインオプション）
- デフォルトモデルは`gemini-1.5-flash`（高速・低コスト）
- `gemini-1.5-pro`等の上位モデルも`--model`オプションで指定可能
- `--provider gemini`で使用

### 今後の拡張可能性

- 他の LLM プロバイダーへの対応
- カスタムプロンプトの設定機能
- バッチ処理機能
- Web API としての提供
- 追加のエージェント（コードサンプルチェック、SEO 最適化など）

---

最終更新: 2025 年 10 月 1 日
