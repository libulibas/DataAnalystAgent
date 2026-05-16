# DataAnalystAgent

Analyzes a CSV for trends and anomalies and writes an insights report.

## Installation

```bash
pip install -r requirements.txt
cp .env.example .env  # add your ANTHROPIC_API_KEY
```

## Usage

```bash
python data_analyst_agent.py data.csv
```

## Model

`claude-sonnet-4-20250514` via the Anthropic Python SDK.

## License

MIT
