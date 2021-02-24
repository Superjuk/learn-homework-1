"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging
import settings as stg
import datetime as dt
import planets_list as pll

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def show_constellation(update, context):
    text = update.message.text.lower().split()
    if len(text) != 2:
        update.message.reply_text('Неверно задана планета. Попробуйте ещё раз.')
        return
    
    currentDate = dt.date.today().strftime('%Y/%m/%d')
    planet = ephem.Planet
    if text[1] == 'mercury':
        planet = ephem.Mercury(currentDate)
    elif text[1] == 'venus':
        planet = ephem.Venus(currentDate)
    elif text[1] == 'mars':
        planet = ephem.Mars(currentDate)
    elif text[1] == 'jupiter':
        planet = ephem.Jupiter(currentDate)
    elif text[1] == 'saturn':
        planet = ephem.Saturn(currentDate)
    elif text[1] == 'uranus':
        planet = ephem.Uranus(currentDate)
    elif text[1] == 'neptune':
        planet = ephem.Neptune(currentDate)
    elif text[1] == 'pluto':
        planet = ephem.Pluto(currentDate)
    else:
        response = f'Планета введена неверно. Повторите ввод.\n Список планет: {pll.planets}'
        print(response)
        update.message.reply_text(response)
        return

    constellation = ephem.constellation(planet)
    print(constellation)
    response = f'{pll.planets_rus.get(planet.name, planet.name)} сегодня находится в созвездии {constellation[1]}.'
    update.message.reply_text(response)



def main():
    mybot = Updater(stg.token, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", show_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
