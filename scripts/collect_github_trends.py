#!/usr/bin/env python3
"""Collect GitHub trending AI/agent repos into data/auto/github_trends.json.

Uses the public GitHub Search API (no token needed, 10 req/min unauth).
Run from project root:  python scripts/collect_github_trends.py
"""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "data" / "auto"
OUT_FILE = OUT_DIR / "github_trends.json"

QUERY = "topic:ai topic:agent created:>{cutoff} stars:>50"
TOPICS = ["ai", "agent", "llm", "rag", "mcp", "autonomous-agent", "coding-agent"]
LIMIT = 20

USER_AGENT = "ai-wealth-monitor/0.1 (self-hosted observatory)"


def gh_get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_trending(days: int) -> list[dict]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).date().isoformat()
    results = {}
    for topic in TOPICS:
        q = urllib.parse.quote(f"topic:{topic} created:>{cutoff} stars:>30")
        url = f"https://api.github.com/search/repositories?q={q}&sort=stars&order=desc&per_page=10"
        try:
            data = gh_get(url)
        except Exception as exc:
            print(f"WARN: topic {topic} failed: {exc}")
            continue
        for item in data.get("items", []):
            full = item["full_name"]
            if full not in results or item["stargazers_count"] > results[full]["stars"]:
                results[full] = {
                    "full_name": full,
                    "url": item["html_url"],
                    "stars": item["stargazers_count"],
                    "forks": item.get("forks_count", 0),
                    "open_issues": item.get("open_issues_count", 0),
                    "created_at": item.get("created_at", ""),
                    "pushed_at": item.get("pushed_at", ""),
                    "description": (item.get("description") or "")[:160],
                }
    ranked = sorted(results.values(), key=lambda r: r["stars"], reverse=True)[:LIMIT]
    for r in ranked:
        # relative age in days since creation
        created = datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))
        r["age_days"] = round((datetime.now(timezone.utc) - created).total_seconds() / 86400, 1)
    return ranked


def main() -> None:
    days = 14
    if "--days" in sys.argv:
        try:
            days = int(sys.argv[sys.argv.index("--days") + 1])
        except (ValueError, IndexError):
            pass
    items = fetch_trending(days)
    doc = {
        "source": "GitHub Search API (public, no token)",
        "window_days": days,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": "LIVE" if items else "STALE",
        "items": items,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"WROTE {OUT_FILE}  status={doc['status']}  items={len(items)}")


if __name__ == "__main__":
    main()
