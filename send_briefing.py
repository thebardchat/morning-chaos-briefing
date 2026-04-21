#!/usr/bin/env python3
"""
send_briefing.py — Morning Chaos Briefing
Builds the full morning message and POSTs it to a Discord webhook.

Usage:
  python3 send_briefing.py                          # reads DISCORD_WEBHOOK env var
  python3 send_briefing.py --webhook https://...    # explicit webhook URL
  python3 send_briefing.py --dry-run                # print message, no send

Run on Pulsar00100 via N8N Execute Command node, or manually.
Pi status is fetched via Tailscale (100.67.120.6).
"""

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).parent))
from chaos_line import get_chaos_line, get_chaos_score
from get_weather import get_weather

PI_MCP_URL = "http://100.67.120.6:8100/health"


def get_pi_status() -> str:
    try:
        r = requests.get(PI_MCP_URL, timeout=4)
        d = r.json()
        if d.get("status") == "healthy":
            weaviate = "✅" if d.get("weaviate") == "ok" else "⚠️"
            ollama   = "✅" if d.get("ollama")   == "ok" else "⚠️"
            return f"Online — Weaviate {weaviate} Ollama {ollama}"
        return "Degraded ⚠️"
    except Exception:
        return "Unreachable ❌"


def build_message() -> str:
    weather_summary, haul_risk = get_weather()
    chaos_score = get_chaos_score()
    chaos_line  = get_chaos_line()
    pi_status   = get_pi_status()
    today       = date.today().strftime("%A, %B %-d")

    return f"""# SHANE! CLOCK IN!! 🚛💥
**{today}**

## DISPATCH STATUS
- Drivers rolling: *(wire in from SRM when ready)*
- First loads dropping: *(wire in from SRM when ready)*

## WEATHER ☁️
- Conditions: {weather_summary}
- Haul risk: **{haul_risk}**

## SHANEBRAIN SYSTEMS 🧠
- Pi status: {pi_status}

## HALO FINANCE 💸
- *(wire in from HaloFinance when ready)*

---
**CHAOS SCORE: {chaos_score}/10 🔥**
*{chaos_line}*"""


def send_to_discord(message: str, webhook_url: str) -> bool:
    payload = {"content": message, "username": "Morning Chaos Briefing"}
    r = requests.post(webhook_url, json=payload, timeout=10)
    if r.status_code in (200, 204):
        print(f"[briefing] Sent — {r.status_code}")
        return True
    print(f"[briefing] Discord error {r.status_code}: {r.text[:200]}")
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--webhook",  default=os.getenv("DISCORD_WEBHOOK", ""))
    parser.add_argument("--dry-run",  action="store_true")
    args = parser.parse_args()

    message = build_message()
    print(message)

    if args.dry_run:
        print("\n[briefing] Dry run — not sent")
        return

    if not args.webhook:
        print("[briefing] ERROR: no webhook URL. Set DISCORD_WEBHOOK env var or pass --webhook", file=sys.stderr)
        sys.exit(1)

    success = send_to_discord(message, args.webhook)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
