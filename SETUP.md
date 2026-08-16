# Big Brain Ape v2 — Setup Guide (Free Telegram Bot)

This guide walks you through running the bot yourself. Everything stays free except your SuperGrok subscription.

---

## 1. Prerequisites

- A computer (Windows, Mac, or Linux)
- Python 3.10 or newer installed
- Your Telegram bot token (from @BotFather)

---

## 2. Get the code

### Option A — Download ZIP (easiest)
1. Go to: https://github.com/Simzy420/big-brain-ape-v2
2. Click the green **Code** button → **Download ZIP**
3. Unzip the folder somewhere easy to find

### Option B — Git clone
```bash
git clone https://github.com/Simzy420/big-brain-ape-v2.git
cd big-brain-ape-v2
```

---

## 3. Create the secret file

1. In the main project folder, create a new file named exactly:
   ```
   .env
   ```
2. Open it with any text editor and put this inside:

```
TELEGRAM_BOT_TOKEN=your_real_token_here
```

Replace `your_real_token_here` with the token you got from BotFather.

**Important:** Never upload or commit the `.env` file. It is already protected by `.gitignore`.

---

## 4. Install the required packages

Open a terminal / command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

If that fails, try:

```bash
python -m pip install -r requirements.txt
```

or

```bash
pip3 install -r requirements.txt
```

---

## 5. Run the bot

In the same terminal, run:

```bash
python bot/main.py
```

or

```bash
python3 bot/main.py
```

You should see a message like:
```
Big Brain Ape bot starting...
```

Leave this window open. As long as it is running, the bot is online.

---

## 6. Test it in Telegram

1. Open Telegram
2. Search for your bot username (the one ending in `bot`)
3. Press **Start**
4. Try these commands:

```
/start
/help
/price BTC-USD
/price AAPL
/info NVDA
/info ETH-USD
/sma BTC-USD
/sma NVDA
/overview
```

---

## 7. Keep the bot running

### Temporary (while testing)
Just leave the terminal open.

### Longer term options (still free or very cheap)
- Run it on your own computer when you need it
- Use a free/cheap VPS later (Railway, Render free tier, Oracle free tier, etc.)
- Use a process manager like `pm2` or `screen`/`tmux` if you leave a computer on

---

## Troubleshooting

**"TELEGRAM_BOT_TOKEN is missing"**  
→ Your `.env` file is missing or in the wrong place, or the name is wrong.

**Module not found**  
→ Run the `pip install -r requirements.txt` step again.

**Bot doesn’t reply**  
→ Make sure the terminal is still running and shows no errors.  
→ Double-check the token is correct.

**yfinance errors**  
→ Sometimes Yahoo Finance rate-limits. Wait a minute and try again. Use correct tickers (BTC-USD, ETH-USD, AAPL, etc.).

---

## Current Free Commands

| Command              | What it does                                      |
|----------------------|---------------------------------------------------|
| `/start`             | Welcome message                                   |
| `/help`              | List of commands                                  |
| `/price <ticker>`    | Current price + daily change                      |
| `/info <ticker>`     | Price, volume, market cap, 52w range, sector      |
| `/sma <ticker>`      | 20 / 50 / 200 day simple moving averages          |
| `/overview`          | Quick look at S&P, Nasdaq, Dow, BTC, ETH, Gold... |

---

## Next Steps After This Works

Once the bot is running, we can add more free features (watchlist, better technicals, alerts, etc.) and later the paid hire system.

Just tell me what you want next.
