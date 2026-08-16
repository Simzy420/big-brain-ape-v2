import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing. Put it in your .env file.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    await update.message.reply_text(
        f"Hey {user.first_name} 🦍\n\n"
        "I'm **Big Brain Ape** \u2014 free market analysis bot.\n\n"
        "**Free Commands:**\n"
        "/price <ticker> \u2014 Current price + change\n"
        "/info <ticker> \u2014 Volume, market cap, 52w range, etc.\n"
        "/sma <ticker> \u2014 Simple moving averages (20 / 50 / 200)\n"
        "/overview \u2014 Quick look at major markets\n"
        "/help \u2014 Full command list\n\n"
        "Only free data sources are used.\n"
        "Paid deep analysis features coming later."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    await update.message.reply_text(
        "**Big Brain Ape \u2014 Free Commands**\n\n"
        "/start \u2014 Welcome message\n"
        "/price <ticker> \u2014 Current price + daily change\n"
        "/info <ticker> \u2014 Extra details (volume, market cap, 52w range...)\n"
        "/sma <ticker> \u2014 20 / 50 / 200 day simple moving averages\n"
        "/overview \u2014 Quick snapshot of major indices & crypto\n"
        "/help \u2014 This help message\n\n"
        "**Examples:**\n"
        "`/price AAPL`\n"
        "`/price BTC-USD`\n"
        "`/info NVDA`\n"
        "`/sma ETH-USD`\n"
        "`/overview`\n\n"
        "This bot uses only free data sources (yfinance)."
    )


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /price command using free yfinance data"""
    if not context.args:
        await update.message.reply_text("Usage: `/price <ticker>`\nExample: `/price BTC-USD`")
        return

    ticker = context.args[0].upper()

    try:
        import yfinance as yf
        stock = yf.Ticker(ticker)
        info = stock.info

        price = (
            info.get("regularMarketPrice")
            or info.get("currentPrice")
            or info.get("previousClose")
        )

        if price is None:
            await update.message.reply_text(f"Could not find price data for `{ticker}`.")
            return

        name = info.get("shortName") or info.get("longName") or ticker
        currency = info.get("currency", "USD")
        change = info.get("regularMarketChange")
        change_pct = info.get("regularMarketChangePercent")

        text = f"**{name}** (`{ticker}`)\n"
        text += f"Price: **{price:,.4f} {currency}**\n"

        if change is not None and change_pct is not None:
            sign = "+" if change >= 0 else ""
            text += f"Change: {sign}{change:,.4f} ({sign}{change_pct:.2f}%)"

        await update.message.reply_text(text)

    except Exception as e:
        logger.error(f"Error fetching price for {ticker}: {e}")
        await update.message.reply_text(
            f"Error getting price for `{ticker}`.\n"
            "Make sure the ticker is correct (e.g. AAPL, BTC-USD, ETH-USD)."
        )


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /info command \u2014 more detailed free data"""
    if not context.args:
        await update.message.reply_text("Usage: `/info <ticker>`\nExample: `/info NVDA`")
        return

    ticker = context.args[0].upper()

    try:
        import yfinance as yf
        stock = yf.Ticker(ticker)
        info = stock.info

        name = info.get("shortName") or info.get("longName") or ticker
        price = info.get("regularMarketPrice") or info.get("currentPrice") or info.get("previousClose")
        currency = info.get("currency", "USD")

        if price is None:
            await update.message.reply_text(f"Could not find data for `{ticker}`.")
            return

        lines = [f"**{name}** (`{ticker}`)", f"Price: **{price:,.4f} {currency}**"]

        if info.get("regularMarketVolume"):
            lines.append(f"Volume: {info['regularMarketVolume']:,}")

        if info.get("marketCap"):
            lines.append(f"Market Cap: {info['marketCap']:,.0f} {currency}")

        if info.get("fiftyTwoWeekLow") and info.get("fiftyTwoWeekHigh"):
            lines.append(
                f"52w Range: {info['fiftyTwoWeekLow']:,.2f} \u2013 {info['fiftyTwoWeekHigh']:,.2f}"
            )

        if info.get("averageVolume"):
            lines.append(f"Avg Volume: {info['averageVolume']:,}")

        if info.get("sector"):
            lines.append(f"Sector: {info['sector']}")

        if info.get("industry"):
            lines.append(f"Industry: {info['industry']}")

        await update.message.reply_text("\n".join(lines))

    except Exception as e:
        logger.error(f"Error fetching info for {ticker}: {e}")
        await update.message.reply_text(
            f"Error getting info for `{ticker}`. Try a different ticker."
        )


async def sma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /sma command \u2014 free simple moving averages"""
    if not context.args:
        await update.message.reply_text("Usage: `/sma <ticker>`\nExample: `/sma BTC-USD`")
        return

    ticker = context.args[0].upper()

    try:
        import yfinance as yf
        import pandas as pd

        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y")

        if hist.empty or len(hist) < 200:
            await update.message.reply_text(
                f"Not enough historical data for `{ticker}` to calculate 200-day SMA."
            )
            return

        close = hist["Close"]
        sma20 = close.rolling(window=20).mean().iloc[-1]
        sma50 = close.rolling(window=50).mean().iloc[-1]
        sma200 = close.rolling(window=200).mean().iloc[-1]
        current = close.iloc[-1]

        name = stock.info.get("shortName") or stock.info.get("longName") or ticker

        def position(price, ma):
            if price > ma:
                return "above"
            elif price < ma:
                return "below"
            return "at"

        text = (
            f"**{name}** (`{ticker}`)\n"
            f"Current: **{current:,.4f}**\n\n"
            f"SMA 20:  {sma20:,.4f}  ({position(current, sma20)})\n"
            f"SMA 50:  {sma50:,.4f}  ({position(current, sma50)})\n"
            f"SMA 200: {sma200:,.4f}  ({position(current, sma200)})"
        )

        await update.message.reply_text(text)

    except Exception as e:
        logger.error(f"Error calculating SMA for {ticker}: {e}")
        await update.message.reply_text(
            f"Error calculating SMAs for `{ticker}`.\n"
            "Make sure the ticker is valid and has enough history."
        )


async def overview(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Quick free overview of major markets"""
    tickers = {
        "S&P 500": "^GSPC",
        "Nasdaq": "^IXIC",
        "Dow": "^DJI",
        "BTC": "BTC-USD",
        "ETH": "ETH-USD",
        "Gold": "GC=F",
        "Oil": "CL=F",
        "VIX": "^VIX",
    }

    try:
        import yfinance as yf

        lines = ["**Market Overview** (free data)\n"]

        for name, symbol in tickers.items():
            try:
                t = yf.Ticker(symbol)
                info = t.info
                price = info.get("regularMarketPrice") or info.get("previousClose")
                change_pct = info.get("regularMarketChangePercent")

                if price is None:
                    continue

                if change_pct is not None:
                    sign = "+" if change_pct >= 0 else ""
                    lines.append(f"{name}: **{price:,.2f}** ({sign}{change_pct:.2f}%)")
                else:
                    lines.append(f"{name}: **{price:,.2f}**")
            except Exception:
                continue

        if len(lines) <= 1:
            await update.message.reply_text("Could not fetch market overview right now. Try again in a minute.")
            return

        await update.message.reply_text("\n".join(lines))

    except Exception as e:
        logger.error(f"Error in overview: {e}")
        await update.message.reply_text("Error fetching market overview. Please try again later.")


def main():
    """Start the bot"""
    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("sma", sma))
    app.add_handler(CommandHandler("overview", overview))

    logger.info("Big Brain Ape bot starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
