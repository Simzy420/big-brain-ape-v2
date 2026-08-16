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
        "Available commands:\n"
        "/start \u2014 Show this message\n"
        "/price <ticker> \u2014 Current price\n"
        "/info <ticker> \u2014 More details (name, volume, market cap, etc.)\n"
        "/help \u2014 Show help\n\n"
        "This bot uses only free data sources.\n"
        "Paid deep analysis features coming later."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    await update.message.reply_text(
        "**Big Brain Ape — Free Commands**\n\n"
        "/start \u2014 Welcome message\n"
        "/price <ticker> \u2014 Current price\n"
        "/info <ticker> \u2014 Extra info (volume, market cap, 52w range, etc.)\n"
        "/help \u2014 This help message\n\n"
        "**Examples:**\n"
        "`/price AAPL`\n"
        "`/price BTC-USD`\n"
        "`/info ETH-USD`\n"
        "`/info NVDA`\n\n"
        "Only free data sources are used."
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
    """Handle /info command — more detailed free data"""
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

        # Add useful free fields when available
        if info.get("regularMarketVolume"):
            lines.append(f"Volume: {info['regularMarketVolume']:,}")

        if info.get("marketCap"):
            lines.append(f"Market Cap: {info['marketCap']:,.0f} {currency}")

        if info.get("fiftyTwoWeekLow") and info.get("fiftyTwoWeekHigh"):
            lines.append(
                f"52w Range: {info['fiftyTwoWeekLow']:,.2f} – {info['fiftyTwoWeekHigh']:,.2f}"
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


def main():
    """Start the bot"""
    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))
    app.add_handler(CommandHandler("info", info))

    logger.info("Big Brain Ape bot starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
