# Big Brain Ape v2 🦍

**Goal:** A usable trading analysis agent that costs **$0 extra** beyond your SuperGrok subscription.

### Core Principles
- Telegram is the main way you talk to it
- Only free data sources
- No Firecrawl, no paid scraping credits, no paid LLM API keys
- SuperGrok handles the heavy thinking (via Automations)
- Everything else stays free

---

## Architecture (Free Edition)

```
You (Telegram)
     │
     ▼
Telegram Bot (100% free)
     │
     ├── Free market data (yfinance, CoinGecko free, FRED free tier)
     ├── Simple commands (prices, basic technicals, alerts)
     └── Daily deep analysis comes from Grok Automations
```

### What is completely free
- Telegram Bot API
- yfinance
- CoinGecko free endpoints
- FRED free API (macro data)
- Running the bot on your own computer or free-tier hosting

### What uses SuperGrok
- Deep daily macro + technical analysis
- Complex trade ideas and reasoning

---

## Current Status

Building the free Telegram bot + data layer first.

### Priority Order
1. Telegram bot + basic free commands
2. Free price & simple technical data
3. Clean daily report format
4. Easy hand-off to Grok Automations for deep analysis

---

**Repo:** Simzy420/big-brain-ape-v2  
**Brand:** Big Brain Ape
