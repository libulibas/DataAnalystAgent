import os, sys
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
MODEL = "claude-sonnet-4-20250514"

def claude(prompt, system="", max_tokens=2000):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("Set ANTHROPIC_API_KEY (copy .env.example to .env).")
    c = Anthropic(api_key=key)
    kw = dict(model=MODEL, max_tokens=max_tokens,
              messages=[{"role": "user", "content": prompt}])
    if system:
        kw["system"] = system
    r = c.messages.create(**kw)
    return "".join(b.text for b in r.content if b.type == "text")



import pandas as pd

def analyze(csv_path: str) -> str:
    df = pd.read_csv(csv_path)
    profile = {
        "shape": df.shape,
        "columns": list(df.columns),
        "describe": df.describe(include="all").to_string(),
        "nulls": df.isnull().sum().to_dict(),
    }
    sys_p = ("You are a data analyst. Given a dataset profile, write a markdown "
             "report: ## Overview, ## Trends, ## Anomalies, ## Recommendations.")
    return claude(f"Dataset profile:\n{profile}", system=sys_p, max_tokens=2500)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: python data_analyst_agent.py <data.csv>")
    print(analyze(sys.argv[1]))
