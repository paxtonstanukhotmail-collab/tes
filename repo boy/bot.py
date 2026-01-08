from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from datetime import datetime

TOKEN = "8257237480:AAGxpA6qoOYzQYAL6rXFVc7TsUxZi5mGpws"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        tanggal = datetime.now().strftime("%d/%m/%Y")

        text = f"""
✨ WELCOME DRAMA BINJE✨

• Nama : {member.first_name}
• Username : @{member.username if member.username else "-"}
• ID : {member.id}
• Tanggal : {tanggal}

Selamat bergabung, jangan bandal 🙌
"""

        await update.message.reply_animation(
            animation="https://media.tenor.com/KeqbuC5yrgUAAAAi/deal-with-it-trailblazer.gif",
            caption=text
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.run_polling()
