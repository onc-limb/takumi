"""Evidence Agent: Checks if the content in the article is factually correct."""

from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


class EvidenceAgent:
    """Agent that checks the factual accuracy of content in markdown files."""

    def __init__(self, api_key: str = None, model: str = "gpt-4o-mini"):
        """Initialize the evidence agent.
        
        Args:
            api_key: OpenAI API key (if None, uses OPENAI_API_KEY env var)
            model: Model to use for checking
        """
        self.llm = ChatOpenAI(model=model, api_key=api_key, temperature=0)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """あなたは技術記事の内容をチェックする専門家です。
与えられた文章の技術的な正確性をチェックし、以下の観点から評価してください：

1. 技術的な事実が正確かどうか
2. 誤解を招く表現がないか
3. 古い情報や非推奨の情報が含まれていないか
4. 不明確な点や曖昧な表現がないか

結果は以下のフォーマットで返してください：
- 問題の箇所：（該当箇所を引用）
- 指摘内容：（具体的な問題点）
- 提案：（修正案や追加情報）

問題がない場合は「問題は見つかりませんでした」と返してください。"""),
            ("user", "{content}")
        ])

    def check(self, content: str) -> Dict[str, Any]:
        """Check the factual accuracy of the content.
        
        Args:
            content: Markdown content to check
            
        Returns:
            Dictionary with check results
        """
        chain = self.prompt | self.llm
        response = chain.invoke({"content": content})
        
        return {
            "agent": "evidence_agent",
            "result": response.content,
            "has_issues": "問題は見つかりませんでした" not in response.content
        }
