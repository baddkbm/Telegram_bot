import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# گرفتن توکن ربات از محیط (Environment Variable)
BOT_TOKEN = os.environ["BOT_TOKEN"]

# هندلر ارسال ویدیو
async def send_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    video_path = "video.mp4"  # نام فایل ویدیویی که باید کنار bot.py باشه

    await context.bot.send_video(
        chat_id=chat_id,
        video=open(video_path, 'rb'),
        caption="🎬 اینم ویدیویی که خواستی!"
    )

# ساخت اپلیکیشن و افزودن دستور
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("video", send_video))

print("ربات در حال اجراست...")
app.run_polling()
