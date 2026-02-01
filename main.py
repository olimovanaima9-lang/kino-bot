from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_USERNAME = "@kinouzbek001"   # o'z kanaling username

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)

    if member.status in ["member", "administrator", "creator"]:
        await update.message.reply_text("🎬 Kino linki shu yerda")
    else:
        await update.message.reply_text(
            f"❌ Avval kanalga obuna bo‘ling:\nhttps://t.me/{CHANNEL_USERNAME[1:]}\n\nKeyin /start bosing."
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
