# Setup Guide

## Prerequisites
- N8N running on Pulsar0100
- Discord webhook URL from your server
- Python 3 with `requests` installed (`pip install requests --break-system-packages`)
- Repo cloned on Pulsar0100 or shanebrain-1

## Steps

1. Clone repo: `git clone https://github.com/thebardchat/morning-chaos-briefing`
2. Set your Discord webhook URL in `n8n/workflow-placeholder.json`
3. Import the N8N workflow JSON into your N8N instance at Pulsar0100
4. Update script paths in the N8N Execute Command nodes
5. Test the workflow manually in N8N first
6. Enable the 6 AM cron trigger

## Testing Scripts Manually

```bash
python3 scripts/get_weather.py
python3 scripts/chaos_line.py
```

## Future Integrations
- [ ] Halo Finance bill data feed (pull from Google Sheet)
- [ ] ShaneBrain Pi health check via SSH or API call
- [ ] Driver roster pull from SRM dispatch system
- [ ] Personalized chaos lines referencing real current events
- [ ] Voice-mode compatible formatting for Discord
