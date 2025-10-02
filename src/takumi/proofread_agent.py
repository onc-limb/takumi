"""Proofread Agent: Checks readability and grammar of the article."""

from typing import Dict, Any
from pydantic import SecretStr
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate


class ProofreadAgent:
    """Agent that checks readability and grammar of markdown content."""

    def __init__(self, api_key: str | None = None, model: str = "gemini-2.0-flash", provider: str = "gemini"):
        """Initialize the proofread agent.
        
        Args:
            api_key: API key (if None, uses OPENAI_API_KEY or GOOGLE_API_KEY env var)
            model: Model to use for proofreading
            provider: LLM provider ("openai" or "gemini")
        """
        secret_key = SecretStr(api_key) if api_key else None
        if provider == "gemini":
            self.llm = ChatGoogleGenerativeAI(model=model, google_api_key=secret_key, temperature=0)
        else:
            self.llm = ChatOpenAI(model=model, api_key=secret_key, temperature=0)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """あなたは技術記事の文章を校正する専門家です。
与えられた文章を以下の観点からチェックしてください：

1. 誤字脱字がないか
2. 文章が読みやすいか（冗長な表現、不自然な言い回し）
3. 専門用語の使い方が適切か
4. 文体が統一されているか（です・ます調、である調）
5. 段落構成が適切か

結果は以下のフォーマットで返してください：
- 問題の箇所：（該当箇所を引用）
- 指摘内容：（具体的な問題点）
- 修正案：（改善された文章）

問題がない場合は「問題は見つかりませんでした」と返してください。"""),
            ("user", "{content}")
        ])

    def check(self, content: str) -> Dict[str, Any]:
        """Check the readability and grammar of the content.
        
        Args:
            content: Markdown content to check
            
        Returns:
            Dictionary with check results
        """
        chain = self.prompt | self.llm
        response = chain.invoke({"content": content})
        
        return {
            "agent": "proofread_agent",
            "result": response.content,
            "has_issues": "問題は見つかりませんでした" not in response.content
        }
