import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("8257237480:AAGJkgXMrvuF3LVTEehqptu_htBz3QOgtkI")
GIF_URL = "https://media.tenor.com/KeqbuC5yrgUAAAAi/deal-with-it-trailblazer.gif"

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        username = f"@{member.username}" if member.username else member.first_name
        text = f"""
Halo {username} 👋

SELAMAT BERGABUNG DI GRUP
🔥 DRAMA BINJE BUJANG 🔥

📛 RULES GRUP 📛
🚫 DILARANG BAPER
🚫 DILARANG BERCANDA BERLEBIHAN
🚫 DILARANG KIRIM P*NO
🚫 DILARANG BAWA ORANG TUA

😄 selebihnya santai, yang penting waras
"""
        msg = await update.message.reply_animation(animation=GIF_URL, caption=text)
        await asyncio.sleep(60)
        try:
            await msg.delete()
        except:
            pass

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))
app.run_polling()
