from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import os
import requests




from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


API_URL = "http://127.0.0.1:8000/query"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "👋 Hello!\n\nAsk me anything about your enterprise documents."
    )


async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE):

    question = update.message.text

    try:

        response = requests.post(
            API_URL,
            json={
                "question": question
            }
        )

        data = response.json()
    
        answer = data["answer"]

        sources = "\n".join(
            [
                f"• {os.path.basename(doc['source'])}"
                for doc in data["documents"]
            ]
        )

        msg = (
            f"🤖 {answer}\n\n"
            f"📄 Sources:\n{sources}"
        )

        await update.message.reply_text(msg)

    except Exception as e:

        await update.message.reply_text(str(e))


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        ask
    )
)

print("Bot Running...")

app.run_polling()
