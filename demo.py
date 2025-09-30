#!/usr/bin/env python3
"""Demo script showing how takumi agents work without API calls."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from takumi import EvidenceAgent, ProofreadAgent, ReportAgent


def demo_agent_structure():
    """Demonstrate the agent structure and workflow."""
    
    print("=" * 60)
    print("Takumi - Technical Article Proofreading Agent Service")
    print("=" * 60)
    print()
    
    # Read sample file
    sample_file = Path(__file__).parent / "sample.md"
    print(f"📖 Reading sample file: {sample_file.name}")
    
    with open(sample_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"   Content length: {len(content)} characters")
    print()
    
    # Show agent workflow (without actual API calls)
    print("🤖 Agent Workflow:")
    print()
    
    print("1. EvidenceAgent")
    print("   - Purpose: Check factual accuracy of technical content")
    print("   - Checks: Technical facts, misleading expressions, outdated info")
    print("   - Model: ChatOpenAI (gpt-4o-mini)")
    print()
    
    print("2. ProofreadAgent")
    print("   - Purpose: Check readability and grammar")
    print("   - Checks: Typos, readability, terminology usage, writing style")
    print("   - Model: ChatOpenAI (gpt-4o-mini)")
    print()
    
    print("3. ReportAgent")
    print("   - Purpose: Generate improved version based on feedback")
    print("   - Input: Original content + feedback from other agents")
    print("   - Output: Revised markdown file")
    print("   - Model: ChatOpenAI (gpt-4o-mini, temperature=0.3)")
    print()
    
    print("=" * 60)
    print("To use the tool with an actual API key:")
    print("=" * 60)
    print()
    print("1. Set your OpenAI API key:")
    print("   export OPENAI_API_KEY='your-api-key'")
    print()
    print("2. Run the tool:")
    print(f"   uv run takumi {sample_file.name}")
    print()
    print("3. Check the output:")
    print(f"   cat {sample_file.stem}_revised{sample_file.suffix}")
    print()
    print("4. For verbose output:")
    print(f"   uv run takumi {sample_file.name} --verbose")
    print()


if __name__ == "__main__":
    demo_agent_structure()
