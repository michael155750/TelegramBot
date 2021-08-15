from flask import Flask, redirect, url_for, request, Response
import requests
import math
# import telegram
import telebot
from controller import TelegramController

telegram_app = Flask(__name__)
telegram_app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

TOKEN = '1913134577:AAF9esAnKvRBY1vSlUfCkX_Oq1qFPpv4PzA'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://6902b0f882fe.ngrok.io'.format(TOKEN)
# requests.get(TELEGRAM_INIT_WEBHOOK_URL)
# bot = telebot.TeleBot(TOKEN)
# bot.remove_webhook()
# bot.set_webhook(url="https://api.telegram.org/bot{}/setWebhook?url=https://3f0b78d1eb5e.ngrok.io/locat{}".format(TOKEN, telegram_app.secret_key))
bot = telebot.TeleBot(TOKEN, threaded=False)
bot.set_webhook(TELEGRAM_INIT_WEBHOOK_URL)

global location
global category
global name


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,
                 ("Hi there, I am EchoBot.\n"
                  "I am here to echo your kind words back to you."))
#
#
# @telegram_app.route('/', methods=['GET', 'POST'])
# def start():
#     if request.method == 'POST':
#         print(request.get_json()['message']['chat']['id'])
#         chat_id = request.get_json()['message']['chat']['id']
#         # massage_id = request.get_json()['message']['message']['id']
#         msg = f'Hi, please write your name'
#         requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
#                      .format(TOKEN, chat_id, msg))
#         return "" #redirect(url_for('locat'))
#
#
# @telegram_app.route('/locat', methods=['GET', 'POST'])
# def locat():
#     global name
#     if request.method == 'POST':
#         name = request.get_json()['message']['text']
#         chat_id = request.get_json()['message']['chat']['id']
#         # massage_id = request.get_json()['message']['message']['id']
#         msg = f'Hi {name}, please write your location'
#         requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
#                      .format(TOKEN, chat_id, msg))
#         return ""
#     # bot.sendMessage(chat_id=chat_id, text=msg, reply_to_message_id=massage_id)
#
#     # Receives the input from the user
#     name = request.get_json()['message']['text']
#     chat_id = request.get_json()['message']['chat']['id']
#     msg = f'Hi {name}, please write your location'
#     requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
#                  .format(TOKEN, chat_id, msg))
#
#     location = request.get_json()['message']['text']
#     chat_id = request.get_json()['message']['chat']['id']
#     msg = "good, please write a category"
#     requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
#                  .format(TOKEN, chat_id, msg))
#
#     category = request.get_json()['message']['text']
#     chat_id = request.get_json()['message']['chat']['id']
#     msg = f'thank you! the places closest to you:\n {TelegramController.get_by_location_category(location, category)}'
#     requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
#                  .format(TOKEN, chat_id, msg))
#     return redirect(url_for('location'))
#
#
# @telegram_app.route('/location', methods=['GET', 'POST'])
# def start2():
#     # Receives the input from the user
#     location = request.get_json()['message']['text']
#     chat_id = request.get_json()['message']['text']['id']
#     msg = f'Hi {location}, please write your location'
#     requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
#                  .format(TOKEN, chat_id, msg))
#     return redirect(url_for('index'))
#
#
#
#
#
# @telegram_app.route('/message', methods=['GET', 'POST'])
# def message_from_bot():
#     """
#     A function that manages our program and the data received
#     from the user, and returns things as needed.
#     :return: "success" if program did not fall through
#     """
#     # Receives the input from the user
#     data = request.get_json()['message']['text']
#     # Gets the id of the chat
#     chat_id = request.get_json()['message']['chat']['id']
#     msg = 'Invalid input'
#     try:
#         data = data.split(" ")
#         # get text of command
#         command = data[0].lower()
#         # get text of number
#         number = data[-1]
#         if command == 'prime':
#             msg = prime(number)
#         elif command == 'palindrome':
#             msg = palindrome(number)
#         elif command == 'factorial':
#             msg = factorial(number)
#         elif command == 'sqrt':
#             msg = sqrt(number)
#         elif command == 'popular':
#             msg = popular()
#         if command in ['prime', 'palindrome', 'factorial', 'sqrt']:
#             # Puts data in a database
#             TelegramController.create_new(number)
#     except Exception:
#         msg = 'Invalid input'
#     requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'"
#                  .format(TOKEN, chat_id, msg))
#     return Response("success")
#
#
# @telegram_app.route('/prime', methods=['GET', 'POST'])
# def prime(number):
#     """
#     Checks if the number we received is prime
#     :param number: number
#     :return: True if number is primary otherwise False
#     """
#     try:
#         if check_prime(int(number)):
#             return 'prime'
#         else:
#             if int(number) % 2 == 0:
#                 return 'Come on dude, you know even numbers are not prime!'
#             else:
#                 return 'not prime'
#     except Exception:
#         return 'Invalid input'
#     return Response("success")
#
#
# @telegram_app.route('/factorial', methods=['GET', 'POST'])
# def factorial(number):
#     """
#     Returns the factorial of number we received
#     :param number: number
#     :return:factorial number
#     """
#     try:
#         return math.factorial(int(number))
#     except Exception:
#         return 'Invalid input'
#     return Response("success")
#
#
# @telegram_app.route('/palindrome', methods=['GET', 'POST'])
# def palindrome(number):
#     """
#     Checks if the number we got is a palindrome
#     :param number: number
#     :return: True if number is palindrome otherwise False
#     """
#     try:
#         opposite_data = number[::-1]
#         if int(number) == int(opposite_data):
#             return 'This number is palindrome'
#         else:
#             return 'This number is NOT palindrome'
#     except Exception:
#         return 'Invalid input'
#     return Response("success")
#
#
# @telegram_app.route('/sqrt', methods=['GET', 'POST'])
# def sqrt(number):
#     """
#     does the number have an integer square root
#     :param number: number
#     :return:True if have otherwise False
#     """
#     try:
#         sqrt_int_data = int(math.sqrt(eval(number)) + 0.5)
#         if eval(number) == sqrt_int_data ** 2:
#             return 'This number has integer root'
#         else:
#             return 'This number has no integer root'
#     except Exception:
#         return 'Invalid input'
#     return Response("success")
#
#
# @telegram_app.route('/popular ', methods=['GET', 'POST'])
# def popular():
#     """
#     :return: The number we received from the user the most times
#     """
#     try:
#         return TelegramController.get_most_popular()
#     except Exception:
#         return 'Invalid input'
#     return Response("success")
#
# @telegram_app.route('/', methods=['GET', 'POST'])
# def factorial2():
#     """
#     Returns the factorial of number we received
#     :param number: number
#     :return:factorial number
#     """
#     return Response("success")
#

def main():
    bot.polling()
    # telegram_app.run(port=9005, debug=True)


if __name__ == '__main__':
    main()
