# Big Brain Ape v2 🦍

**Goal:** A usable trading analysis agent that costs **$0 extra** beyond your SuperGrok subscription.

### Core Principles
- Telegram is the main way you talk to it
- Only free data sources
- No Firecrawl, no paid scraping, no paid LLM API keys required
- SuperGrok handles the heavy thinking (via Automations)
- Everything else stays free

---

## Current Free Commands

| Command | What it does |
|---------|--------------|
| `/start` | Welcome message |
| `/help` | Full command list |
| `/price <ticker>` | Current price + daily change |
| `/info <ticker>` | Volume, market cap, 52-week range, sector |
| `/sma <ticker>` | 20 / 50 / 200 day simple moving averages |
| `/overview` | Quick snapshot of major indices + crypto |

**Examples:**
```
/price BTC-USD
/info NVDA
/sma ETH-USD
/overview
```

---

## How to Run It

Full step-by-step instructions are here:

**→ [SETUP.md](SETUP.md)**

---

## Architecture (Free Edition)

```
You (Telegram)
     │
     ▼
Telegram Bot (100% free)
     │
     ├── Free market data (yfinance)
     ├── Simple commands (prices, SMAs, overview)
     └── Daily deep analysis comes from Grok Automations later
```

### Completely free
- Telegram Bot API
- yfinance data
- Running the bot on your own computer

### Uses SuperGrok
- Deep daily macro + technical analysis (planned via Automations)

---

## Paid Features (Later)

See **[docs/PAID_SYSTEM.md](docs/PAID_SYSTEM.md)** for the plan on how people can hire the bot and how you can make money from it.

---

**Repo:** [Simzy420/big-brain-ape-v2](https://github.com/Simzy420/big-brain-ape-v2)  
**Brand:** Big Brain Ape
