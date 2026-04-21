# Setup Guide

## Prerequisites

- N8N running on Pulsar00100 (already live)
- Python 3 + `requests` on Pulsar: `pip install requests`
- Discord webhook URL for a new `#morning-briefing` channel

---

## Step 1 — Create Discord Webhook

1. In Discord, open your server → **Edit Channel** on your briefing channel
2. **Integrations → Webhooks → New Webhook**
3. Copy the webhook URL

---

## Step 2 — Clone repo on Pulsar

```bash
ssh hubby@100.81.70.117
git clone https://github.com/thebardchat/morning-chaos-briefing.git ~/morning-chaos-briefing
```

---

## Step 3 — Set the webhook in N8N

In N8N on Pulsar:
1. **Settings → Environment Variables**
2. Add: `DISCORD_WEBHOOK` = *(your webhook URL)*

---

## Step 4 — Import workflow

1. In N8N: **Workflows → Import from File**
2. Select `workflow.json` from this repo
3. Two nodes: Schedule trigger (6 AM) → Execute Command (runs `send_briefing.py`)

---

## Step 5 — Test manually on Pulsar

```bash
# Dry run — no Discord send
python3 ~/morning-chaos-briefing/send_briefing.py --dry-run

# Live test with webhook
DISCORD_WEBHOOK=https://discord.com/api/webhooks/... python3 ~/morning-chaos-briefing/send_briefing.py
```

---

## Step 6 — Activate in N8N

Toggle the workflow **Active**. Fires every day at 6:00 AM.

---

## What the briefing pulls today

| Field | Source | Status |
|-------|--------|--------|
| Weather + haul risk | NWS API (no key needed) | ✅ Live |
| Chaos Score + line | chaos_line.py | ✅ Live |
| Pi system status | MCP health at 100.67.120.6:8100 | ✅ Live |
| Driver counts | SRM Dispatch system | 🔧 Wire in later |
| HaloFinance alerts | HaloFinance repo | 🔧 Wire in later |

---

## Future Integrations

- [ ] SRM driver roster — pull from MASTER-Scheduler-Dashboard-SRM
- [ ] HaloFinance bill alerts — pull from Google Sheet or HaloFinance API
- [ ] Piper-TTS voice playback via Pico 2 speaker (Phase 2 — see `pico_firmware/`)
