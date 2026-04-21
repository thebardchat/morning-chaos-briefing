# 🚛💥 Morning Chaos Briefing

Daily 6 AM dispatch briefing for Shane — powered by ShaneBrain, delivered via Discord.

Combines real dispatch data, weather, system status, Halo Finance alerts, and unhinged motivational energy.

## Structure

- `templates/` — Briefing message templates
- `n8n/` — N8N workflow JSON for automation
- `scripts/` — Data-fetching scripts (weather, ShaneBrain, finance)
- `docs/` — Setup and configuration notes

## How It Works

1. N8N triggers at 6 AM daily
2. Scripts pull live data (weather, Pi status, bills due)
3. Template is populated with real data
4. Message fires to Discord
5. Chaos Score randomized — no mercy, no repeats

## Setup

See `docs/setup.md` for full configuration.
