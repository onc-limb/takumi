"""CLI module for Takumi - Technical Article Proofreading Agent Service."""

import os
import sys
import click
from pathlib import Path
from typing import Optional

from .evidence_agent import EvidenceAgent
from .proofread_agent import ProofreadAgent
from .report_agent import ReportAgent


@click.command()
@click.argument('input_file', type=click.Path(exists=True, path_type=Path))
@click.option(
    '--output', '-o',
    type=click.Path(path_type=Path),
    help='Output file path (default: {input}_revised.md)'
)
@click.option(
    '--api-key',
    help='API key for the LLM provider (can also be set via OPENAI_API_KEY or GOOGLE_API_KEY env var)'
)
@click.option(
    '--provider',
    type=click.Choice(['openai', 'gemini'], case_sensitive=False),
    default='gemini',
    help='LLM provider to use (default: gemini)'
)
@click.option(
    '--model',
    help='Model to use. Defaults: gemini-2.0-flash (Gemini), gpt-4o-mini (OpenAI)'
)
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Show detailed feedback from agents'
)
def main(
    input_file: Path,
    output: Optional[Path],
    api_key: Optional[str],
    provider: str,
    model: Optional[str],
    verbose: bool
):
    """Takumi - Technical Article Proofreading Agent Service.
    
    Reads a markdown file, checks its content for factual accuracy and readability,
    then generates an improved version.
    
    INPUT_FILE: Path to the markdown file to process
    """
    # Set default model based on provider if not specified
    if model is None:
        model = "gemini-2.0-flash" if provider == "gemini" else "gpt-4o-mini"
    
    # Get API key from environment if not provided
    if not api_key:
        if provider == "gemini":
            api_key = os.environ.get('GOOGLE_API_KEY')
            if not api_key:
                click.echo("Error: Google API key is required. Set GOOGLE_API_KEY environment variable or use --api-key option.", err=True)
                sys.exit(1)
        else:
            api_key = os.environ.get('OPENAI_API_KEY')
            if not api_key:
                click.echo("Error: OpenAI API key is required. Set OPENAI_API_KEY environment variable or use --api-key option.", err=True)
                sys.exit(1)
    
    # Read input file
    click.echo(f"📖 Reading file: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        click.echo(f"Error reading file: {e}", err=True)
        sys.exit(1)
    
    if not content.strip():
        click.echo("Error: Input file is empty", err=True)
        sys.exit(1)
    
    # Initialize agents
    click.echo(f"🤖 Initializing agents with {provider} ({model})...")
    evidence_agent = EvidenceAgent(api_key=api_key, model=model, provider=provider)
    proofread_agent = ProofreadAgent(api_key=api_key, model=model, provider=provider)
    report_agent = ReportAgent(api_key=api_key, model=model, provider=provider)
    
    # Run evidence check
    click.echo("🔍 Checking factual accuracy...")
    evidence_result = evidence_agent.check(content)
    
    if verbose:
        click.echo("\n--- Evidence Agent Feedback ---")
        click.echo(evidence_result["result"])
        click.echo()
    
    # Run proofread check
    click.echo("✍️  Proofreading content...")
    proofread_result = proofread_agent.check(content)
    
    if verbose:
        click.echo("\n--- Proofread Agent Feedback ---")
        click.echo(proofread_result["result"])
        click.echo()
    
    # Generate improved version
    click.echo("📝 Generating improved version...")
    improved_content = report_agent.generate_report(
        content,
        evidence_result,
        proofread_result
    )
    
    # Determine output path
    if output is None:
        output = input_file.parent / f"{input_file.stem}_revised{input_file.suffix}"
    
    # Save output
    click.echo(f"💾 Saving to: {output}")
    try:
        report_agent.save_report(improved_content, str(output))
        click.echo("✅ Done!")
        
        # Show summary
        click.echo(f"\n📊 Summary:")
        click.echo(f"  - Evidence check: {'⚠️  Issues found' if evidence_result['has_issues'] else '✓ No issues'}")
        click.echo(f"  - Proofread check: {'⚠️  Issues found' if proofread_result['has_issues'] else '✓ No issues'}")
        click.echo(f"  - Output saved to: {output}")
        
        if not verbose and (evidence_result['has_issues'] or proofread_result['has_issues']):
            click.echo("\n💡 Use --verbose flag to see detailed feedback from agents")
        
    except Exception as e:
        click.echo(f"Error saving file: {e}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
