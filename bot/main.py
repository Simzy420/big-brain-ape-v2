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
        "I'm **Big Brain Ape** — free market analysis bot.\n\n"
        "Available commands:\n"
        "/start - Show this message\n"
        "/price <ticker> - Get current price (e.g. /price BTC-USD)\n"
        "/help - Show help\n\n"
        "More features coming soon."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    await update.message.reply_text(
        "**Big Brain Ape Commands**\n\n"
        "/start - Welcome message\n"
        "/price <ticker> - Current price (stocks or crypto)\n"
        "   Examples:\n"
        "   /price AAPL\n"
        "   /price BTC-USD\n"
        "   /price ETH-USD\n"
        "/help - This help message\n\n"
        "This bot uses only free data sources."
    )


async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /price command using free yfinance data"""
    if not context.args:
        await update.message.reply_text("Usage: /price <ticker>\nExample: /price BTC-USD")
        return

    ticker = context.args[0].upper()

    try:
        import yfinance as yf
        stock = yf.Ticker(ticker)
        info = stock.info

        # Try different possible price fields
        price = info.get("regularMarketPrice") or info.get("currentPrice") or info.get("previousClose")

        if price is None:
            await update.message.reply_text(f"Could not find price data for `{ticker}`.")
            return

        name = info.get("shortName") or info.get("longName") or ticker
        currency = info.get("currency", "USD")

        await update.message.reply_text(
            f"**{name}** (`{ticker}`)\n"
            f"Price: **{price:,.4f} {currency}**"
        )

    except Exception as e:
        logger.error(f"Error fetching price for {ticker}: {e}")
        await update.message.reply_text(
            f"Error getting price for `{ticker}`.\n"
            "Make sure the ticker is correct (e.g. AAPL, BTC-USD, ETH-USD)."
        )


def main():
    """Start the bot"""
    app = Application.builder().token(TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("price", price))

    logger.info("Big Brain Ape bot starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
