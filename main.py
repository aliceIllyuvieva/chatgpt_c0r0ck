import os
import openai
import telebot
from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper

openai.api_key = "key"

bot = telebot.TeleBot("tg-api")

@bot.message_handler(func=lambda _: True)

def message_handler(message):

    response = openai.Completion.create(
      model="gpt-3.5-turbo",
      prompt=message.text,
      temperature=0.7,
      max_tokens=2048,
      top_p=0,
      frequency_penalty=0,
      presence_penalty=0,
    )
    bot.send_message(chat_id = message.from_user.id, text = response['choices'][0]['text'])

bot.polling()
