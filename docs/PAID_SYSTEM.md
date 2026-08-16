# Big Brain Ape — Paid Hire System Design

This document outlines how people can hire the bot and how you can make money from it, while keeping the core free.

---

## Overall Philosophy

- Free tier is always available (builds trust and audience)
- Paid features unlock deeper value
- Start simple, then expand

---

## Phase 1: Free Core (Current Focus)

Anyone can use:
- Price checks
- Basic technical info
- Simple market status
- Daily free summary (later)

This builds usage and credibility.

---

## Phase 2: Simple Paid Features (Recommended Next)

### Option A — Telegram Stars (Easiest)
Telegram has a built-in payment system called **Stars**.

Pros:
- Very easy to implement
- No crypto wallet needed for users
- Official Telegram support

Possible paid commands:
- `/deep AAPL` → Full technical + macro context report
- `/scan` → Full daily market scan
- `/portfolio` → Portfolio analysis (user sends tickers)

### Option B — Crypto Payments
Accept USDC (Base or Solana) for paid reports.

Pros:
- Fits the crypto-native audience
- You keep more of the money

Cons:
- Slightly more technical to set up

---

## Phase 3: Full "Hire the Bot" Job System

This is the bigger vision.

### How it could work:

1. User sends a command like:
   ```
   /hire Analyze NVDA, PLTR and BTC for the next 2 weeks. Focus on macro risk.
   ```

2. Bot replies with:
   - Estimated price
   - What they will receive
   - Payment instructions (Stars or crypto)

3. After payment is confirmed, the job is queued.

4. You (or later the automation) deliver the result back in Telegram.

### Job Types that make sense:

| Job Type                    | Difficulty | Price Potential |
|----------------------------|----------|-----------------|
| Single ticker deep dive    | Low      | $3–$10         |
| Multi-ticker scan          | Medium   | $10–$25        |
| Full daily macro brief     | Medium   | $15–$40        |
| Custom research request    | High     | $25–$100+      |
| Ongoing monitoring         | High     | Subscription   |

---

## Recommended Path

1. Finish strong free bot first
2. Add 1–2 paid commands using Telegram Stars
3. Test if people are actually willing to pay
4. Only then build the full job system

---

## Important Notes

- Never promise autonomous trading of other people’s money unless you are properly set up legally.
- Start with **analysis and research** services only. This is much safer.
- Build reputation first. Money comes after people trust the free output.

---

This design will evolve as we build.
