from fastapi import FastAPI, Header, Depends
import telebot
import traceback
import uvicorn

app = FastAPI()
bot = telebot.TeleBot(token="")

@app.post("/request")
def request(short = str, full = str):
    bot.send_message(chat_id = "", text=f"<b>Поступила новая заявка:</b>\nКороткое сообщение: {short}\nПолное сообщение: {full}", parse_mode="HTML")

    return {"response": "200"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

    while True: # чтобы бот не умирал при каждой ошибке, это делает возможным постоянную работу бота
        try:
            bot.polling()
        except Exception as ex:
            print(traceback.format_exc())