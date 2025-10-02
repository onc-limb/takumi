"""Report Agent: Generates a refined version of the article based on feedback."""

from typing import Dict, Any, List
from pydantic import SecretStr
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate


class ReportAgent:
    """Agent that generates an improved version of the article based on feedback."""

    def __init__(self, api_key: str | None = None, model: str = "gemini-2.0-flash", provider: str = "gemini"):
        """Initialize the report agent.
        
        Args:
            api_key: API key (if None, uses OPENAI_API_KEY or GOOGLE_API_KEY env var)
            model: Model to use for generating report
            provider: LLM provider ("openai" or "gemini")
        """
        secret_key = SecretStr(api_key) if api_key else None
        if provider == "gemini":
            self.llm = ChatGoogleGenerativeAI(model=model, google_api_key=secret_key, temperature=0.3)
        else:
            self.llm = ChatOpenAI(model=model, api_key=secret_key, temperature=0.3)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """あなたは技術記事を推敲する専門家です。
元の記事と、各エージェントからのフィードバックを元に、改善された記事を作成してください。

以下の点に注意してください：
1. 元の記事の構造と形式（マークダウン）を維持する
2. 技術的な正確性を確保する
3. 読みやすく、分かりやすい文章にする
4. 指摘された問題点を適切に修正する
5. 元の記事の意図を損なわない

改善された記事全体をマークダウン形式で返してください。
解説や説明は不要で、改善された記事のみを返してください。"""),
            ("user", """元の記事：
{original_content}

--- フィードバック ---

【事実確認エージェントからのフィードバック】
{evidence_feedback}

【校正エージェントからのフィードバック】
{proofread_feedback}

--- 

上記のフィードバックを元に、改善された記事を作成してください。""")
        ])

    def generate_report(
        self,
        original_content: str,
        evidence_result: Dict[str, Any],
        proofread_result: Dict[str, Any]
    ) -> str:
        """Generate an improved version of the article.
        
        Args:
            original_content: Original markdown content
            evidence_result: Result from evidence agent
            proofread_result: Result from proofread agent
            
        Returns:
            Improved markdown content
        """
        chain = self.prompt | self.llm
        response = chain.invoke({
            "original_content": original_content,
            "evidence_feedback": evidence_result["result"],
            "proofread_feedback": proofread_result["result"]
        })
        
        # response.contentはstr | list[str | dict]の可能性があるため、strに変換
        content = response.content
        if isinstance(content, list):
            # リストの場合は文字列要素を結合
            return "".join(str(item) for item in content if isinstance(item, str))
        return str(content)

    def save_report(self, content: str, output_path: str) -> None:
        """Save the improved content to a file.
        
        Args:
            content: Improved markdown content
            output_path: Path to save the file
        """
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
