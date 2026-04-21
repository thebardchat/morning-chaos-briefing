<div align="center">

<img src=".github/assets/banner.png" alt="Morning Chaos Briefing" width="100%">

<br/>

# 🚛💥 Morning Chaos Briefing

**Daily 6 AM dispatch briefing for Shane — powered by ShaneBrain, delivered via Discord.**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Constitution](https://img.shields.io/badge/Governed%20by-The%20Constitution-gold)](CONSTITUTION.md)
[![ShaneBrain](https://img.shields.io/badge/Powered%20by-ShaneBrain-green)](https://github.com/thebardchat/shanebrain-core)

*Combines real dispatch data, weather, system status, Halo Finance alerts, and unhinged motivational energy.*

</div>

---

## What It Does

Every morning at 6 AM, this briefing fires to Discord with:

- Live weather for the dispatch zone
- ShaneBrain system status (Pi, Weaviate, Ollama cluster health)
- HaloFinance alerts (bills due, budget checkpoints)
- Active driver count + plant routing summary
- A randomized Chaos Score — no mercy, no repeats

---

## Structure

```
morning-chaos-briefing/
├── chaos_line.py          — Chaos Score generator
├── get_weather.py         — Weather data fetcher
├── daily_briefing.md      — Briefing template
├── workflow_placeholder_json.json  — N8N workflow scaffold
└── setup.md               — Full configuration guide
```

---

## How It Works

1. N8N triggers at 6 AM daily
2. Scripts pull live data (weather, Pi status, finance)
3. Template is populated with real data
4. Message fires to Discord
5. Chaos Score randomized — no mercy, no repeats

---

## Setup

See [`setup.md`](setup.md) for full configuration.

---

## Governing Document

This project operates under the [ShaneBrain Constitution](CONSTITUTION.md) — nine pillars, one covenant.

> *"Whatever you do, work at it with all your heart, as working for the Lord, not for human masters."*
> — Colossians 3:23

---

<div align="center">

*Part of the [thebardchat](https://github.com/thebardchat) ecosystem — built on a Pi 5 in Hazel Green, Alabama.*

*Faith · Family · Sobriety · Local AI · The Left-Behind User*

</div>
