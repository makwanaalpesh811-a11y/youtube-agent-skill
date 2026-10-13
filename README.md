# 🎬 YouTube Agent Skill

YouTube content creation, upload, download, strategy skills for Hermes Agent

**Repository by:** [Alpesh Makwana](https://github.com/makwanaalpesh811-a11y)

---

## 📦 What's Inside

15 Hermes Agent skills for youtube agent skill:

- `youtube-content`
- `youtube-content-pipeline` — YouTube download, batch upload, and copyright tests.
---

# YouTube Content Pipeline — Download, ...
- `youtube-full-access` — Use for YouTube video upload, delete, and channel work.
---

# YouTube Full Access — Alpesh's Cha...
- `youtube-strategy-analysis` — "Learn trading strategy from YouTube transcript safely."
---
Always-on: youtube-transcript-api on...
- `yt-audit` — Audit YouTube channel: gaps, uploads, engagement health.
- `yt-chapters` — Generate chapters list from a video transcript.
- `yt-comment` — Reply to YouTube comments with a strategy-aware voice.
- `yt-edit` — Create an edit decision list from a video transcript.
- `yt-package` — Lint YouTube title and thumbnail as a single pairing.
- `yt-plan` — Plan a weekly YouTube content calendar for one channel.
- `yt-retention` — Find where viewers drop off from retention graph data.
- `yt-script` — Write YouTube script: 21 hook formulas, scored hook.
- `yt-seo` — YouTube SEO audit: title, tags, keywords, metadata.
- `yt-shorts` — Cut a long video into candidate Shorts segments.
- `yt-viral` — Find what's working in a niche by outlier multiple.

---


## 🔐 SECURITY NOTICE

**This repo is safe to use publicly.** It contains only skill definitions (SKILL.md) and documentation - no live credentials.

### What NOT to commit:
- API keys (GitHub, YouTube, Gemini, OpenAI, etc.)
- AWS credentials (`~/.aws/credentials`)
- Telegram bot tokens
- Exchange API keys (Delta, Hyperliquid, etc.)
- Private keys or certificates

### Where to store secrets (on your machine):
```
~/.aws/credentials          # AWS
~/.youtube_token.json       # YouTube OAuth
~/.ig_env                   # Instagram/Gemini
~/.signal_bot_env           # Trading bot
~/.gh_token                 # GitHub token
```

All skills are designed to read secrets from your filesystem, not embed them.


## 🚀 Installation

### Option 1: Clone to Hermes skills directory
```bash
git clone https://github.com/makwanaalpesh811-a11y/youtube-agent-skill.git ~/.hermes/skills/youtube-agent-skill
```

### Option 2: Install individual skills
```bash
# Create skills dir if not exists
mkdir -p ~/.hermes/skills

# Clone only what you need
git clone --depth 1 --filter=blob:none https://github.com/makwanaalpesh811-a11y/youtube-agent-skill.git /tmp/youtube-agent-skill
cp -r /tmp/youtube-agent-skill/skills/* ~/.hermes/skills/
```

---

## ⚙️ Prerequisites

Check each skill's `SKILL.md` for specific dependencies. Common ones:
- **Termux** (Android terminal) or Linux/macOS
- **Python 3.11+**
- **Node.js + npm** (for CLI-based skills)
- **API keys** stored in `~/.<name>_env` or `~/.<name>_token.json` files

---

## 🔧 Setup Guide

1. **Install Hermes Agent:** `pip install hermes-agent` or see [Hermes docs](https://hermes-agent.nousresearch.com/docs)
2. **Clone this repo** into `~/.hermes/skills/`
3. **Configure credentials** in your environment (see each skill's SKILL.md)
4. **Use in chat:** Ask Hermes to use any skill by name

---

## 📚 Skill Documentation

Each skill lives in `skills/<skill-name>/SKILL.md` with:
- **YAML frontmatter:** name, description
- **Commands:** CLI/API references
- **Examples:** Ready-to-use snippets
- **Gotchas:** Real-world pitfalls

---

## 🛡️ Security

## 🔐 SECURITY NOTICE

**This repo is safe to use publicly.** It contains only skill definitions (SKILL.md) and documentation - no live credentials.

### What NOT to commit:
- API keys (GitHub, YouTube, Gemini, OpenAI, etc.)
- AWS credentials (`~/.aws/credentials`)
- Telegram bot tokens
- Exchange API keys (Delta, Hyperliquid, etc.)
- Private keys or certificates

### Where to store secrets (on your machine):
```
~/.aws/credentials          # AWS
~/.youtube_token.json       # YouTube OAuth
~/.ig_env                   # Instagram/Gemini
~/.signal_bot_env           # Trading bot
~/.gh_token                 # GitHub token
```

All skills are designed to read secrets from your filesystem, not embed them.

---

## 📜 License

MIT License - see [LICENSE](./LICENSE)

---

## 👨‍💻 Author

**Alpesh Makwana** — Trading, content, and Hermes Agent enthusiast.

- **GitHub:** [makwanaalpesh811-a11y](https://github.com/makwanaalpesh811-a11y)
- **Telegram:** @alpeshalgobot

---

## 🤝 Contributing

Issues and PRs welcome. Follow the SKILL.md format conventions.

## 🏷️ Topics
`youtube` `content-creation` `shorts` `automation` 
