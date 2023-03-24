import logging
import openai
from aiogram import Bot, Dispatcher, executor, types

openai.api_key = "api_key"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token="bot_token")
dp = Dispatcher(bot)


async def ai(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Your name is 'Dr. Bot'. You were created in the startup 's0r0k'. You are a qualified medical assistant with extensive knowledge of medical literature, articles and research. Doctors come to you with various questions, and you need to answer them, demonstrating your competence and ability to understand situations. Follow the instructions of the doctors, approach the issues systematically, and think through your plans in detail. Minimize the transformation of information into unnecessary banal phrases. Write in Russian."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            max_tokens=2048,
            top_p=0,
            frequency_penalty=0,
            presence_penalty=0,
        )

        return completion.choices[0].message.content
    except:
        return None


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Здравствуйте! Меня зовут Доктор Бот! Я могу ответить на любые ваши вопросы. Однако я пока ещё только учусь, потому некоторые ответы будут откровенно слабыми, но с каждым днём я становлюсь всё умнее, и уже через пару месяцев я буду помогать вам в нескольких задачах каждый день и с каждым пациентом. \n\nВы можете меня спрашивать как о медицине и здоровье, так и о медицинском маркетинге или бизнесе. \nНапример, вы можете попросить помочь поставить диагноз, или помочь разработать методологию лечения конкретного пациента, или можете просто спросить в чём смысл жизни врача или как клинике стать лучше. \nЧем лучше вы сформулируете вопрос, тем лучше я смогу вам ответить. В целом не стесняйтесь задавать мне вопросы, чем больше вопросов вы зададите, тем умнее стану я, и тем мудрее станете вы. \n\nА, чтобы научиться работать со мной максимально эффективно — я рекомендую вам подписаться на канал https://t.me/+0Mxt6K0y83M3MmIy \n\nОт разработчиков: Доктор Бот пока не умеет следить за ходом беседы. Задавайте ему весь ваш вопрос сразу и полностью. \nМы будет благодарны, если вы порекомендуете Доктора Бота вашим коллегам. А также, если будете задавать нам вопросы или предлагать нововведения или пожелания: пишите @c0r0ck")



@dp.message_handler()
async def echo(message: types.Message):
    answer = await ai(message.text)

    if answer != None:
        await message.reply(answer)
    else:
        await message.reply('😞 Извините, слишком много одновременных обращений к Доктору Боту. Попробуйте ещё раз через минуту. Если ошибка повторится, то напишите нам в поддержку: @c0r0ck')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
