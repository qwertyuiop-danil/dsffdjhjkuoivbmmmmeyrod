import telebot
import time

token = '7994402203:AAEMR0lBGlNtLTyg9RUJOsYvfVMV1uz9rjQ'

id_user = 6489937469

bot = telebot.TeleBot(token)

bot.send_message(id_user, 'Hello!')
time.sleep(30)
#import requests as r
#from time import sleep

#url = 'https://raw.githubusercontent.com/qwertyuiop-danil/dsffdjhjkuoivbmmmmeyrod/main/main.py'

#code = r.get(url).text

#new_code = code
#while code == new_code:
#  new_code = r.get(url).text
#  print("Check...")
#  sleep(10)
