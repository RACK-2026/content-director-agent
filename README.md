# Content Director Agent

A privacy-safe portfolio demo for turning a creative brief into a structured short-form video script, reviewing it against reusable quality dimensions, and generating a revision plan.

This repository intentionally contains no company names, customer data, brand assets, proprietary scripts, private prompts, platform credentials, or production infrastructure.

## What it demonstrates

- Structured brief-to-script generation
- Rule-based quality review with explainable scores
- Revision planning from review findings
- A small, testable Python core with no external API dependency

## Run

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\Activate.ps1
pip install -e .
python -m content_director.cli
```

Run tests with `python -m pytest`.

## Scope

The demo uses fictional content and generic creative constraints. Connect an LLM through your own adapter if needed; never commit API keys or private business materials.


