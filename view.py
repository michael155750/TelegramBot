import datetime

from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from controller import TelegramController


api_file = open("key.txt", 'r')
api_key = api_file.read()
api_file.close()

api_file_weather = open("WeatherKey.txt", 'r')
weather_key = api_file_weather.read()
api_file_weather.close()

STATE = None
LOCATION = 1
CATEGORY = 2
DISTANCE = 3
RESULT = 4
WEATHER = 5


def find_weather(lat, lon):
    #get place coordinates and return the day with the lowest temprature in the next 5 days
    weather_exc = "current,minutely,hourly,alerts"
    url_find_weather = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid=' \
                       f'{weather_key}&units=metric&exclude={weather_exc}'
    weather_info = requests.get(url_find_weather).json()

    weather_daily_predict = [(datetime.datetime.fromtimestamp(x["dt"]).day, x["temp"]["day"]) for x in weather_info["daily"]]
    best_day = min(weather_daily_predict, key=lambda x: x[1])
    return best_day


# function to handle the /start command
def start(update, context):
    first_name = update.message.chat.first_name
    update.message.reply_text(f"Hi {first_name}, nice to meet you!")
    start_info(update, context)


def start_info(update, context):
    global STATE
    STATE = LOCATION
    update.message.reply_text(
        f"I would need to know your location, so tell me your address...")


def received_location(update, context):
    global STATE

    try:
        location = update.message.text
        context.user_data['address'] = location
        update.message.reply_text(
            f"ok, now I need to know What is the distance from you, which you want to search?")
        STATE = DISTANCE
    except:
        update.message.reply_text(
            "it's funny but it doesn't seem to be correct...")


def received_distance(update, context):
    global STATE

    try:
        context.user_data['distance'] = update.message.text

        keyboard = [[KeyboardButton("restaurant", callback_data='restaurant'),
                     KeyboardButton("bank", callback_data='bank')],
                    [KeyboardButton("park", callback_data='park'),
                     KeyboardButton("university", callback_data='university')],
                    [KeyboardButton("hotel", callback_data='hotel'),
                     KeyboardButton("museum", callback_data='museum')]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        update.message.reply_text(f"ok, now I need to know category you want to find...", reply_markup=reply_markup)
        ReplyKeyboardRemove()
        STATE = CATEGORY
    except:
        update.message.reply_text(
            "it's funny but it doesn't seem to be correct...")


def received_category(update, context):
    global STATE

    try:
        context.user_data['category'] = update.message.text
        STATE = RESULT
        received_result(update, context)
    except:
        update.message.reply_text(
            "it's funny but it doesn't seem to be correct...")


def received_result(update, context):
    global STATE
    try:
        category = str(context.user_data['category']).lower()
        address = context.user_data['address'].lower()
        distance = context.user_data['distance'].lower()

        resultDB = TelegramController.get_by_location_category_distance(address, category, distance)

        if resultDB == " ":
            url_find_location = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + \
                                "&key=" + str(api_key)
            request = requests.get(url_find_location)
            lat = request.json()["results"][0]["geometry"]["location"]["lat"]
            lon = request.json()["results"][0]["geometry"]["location"]["lng"]

            url_find_place = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(
                lat) + "," + str(lon) + \
                             f"&radius={distance}&type={category}&key=" + str(api_key)

            place_req = requests.get(url_find_place)
            n = 1
            result = " "
            for item in place_req.json()['results']:
                result += f"result number {n}:\n"
                result += f"name: {item['name']} \naddress: {item['vicinity']}\n"
                result += "\n"
                n += 1

            if result == " ":
                update.message.reply_text(f'Sorry, there is no place in {category} category, {distance} meters from you')
            else:
                TelegramController.create_new(address, category, distance, result)
                update.message.reply_text(result)
        else:
            update.message.reply_text(resultDB)
        STATE = WEATHER
        keyboard2 = [[KeyboardButton("weather", callback_data='weather'),
                     KeyboardButton("/start", callback_data='/start')]]
        reply_markup2 = ReplyKeyboardMarkup(keyboard2, one_time_keyboard=True)
        update.message.reply_text(f"Do you want to know which day of the week is best to go out?\nIf so, "
                                  f"then press the weather button.\nOtherwise, you can select the Start button",
                                  reply_markup=reply_markup2)
        ReplyKeyboardRemove()
        # return_best_day(update, context)
        # STATE = WEATHER
    except:
        update.message.reply_text("Unable to calculate")


def return_best_day(update, context):
    global STATE

    try:
        if update.message.text == "weather":
            address = context.user_data['address'].lower()
            url_find_location = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + \
                                "&key=" + str(api_key)
            request = requests.get(url_find_location)
            lat = request.json()["results"][0]["geometry"]["location"]["lat"]
            lon = request.json()["results"][0]["geometry"]["location"]["lng"]
            result = find_weather(lat, lon)

            current_day = datetime.datetime.today().day
            current_month = datetime.datetime.today().month

            if result[0] < current_day:
                res_month = current_month + 1
            else:
                res_month = current_month

            update.message.reply_text(f"The best day to go out is: {result[0]}/{res_month} "
                                      f"\nAnd the average weather that day is: {result[1]}°C")
        STATE = None
    except:
        update.message.reply_text(
            "it's funny but it doesn't seem to be correct...")


# function to handle normal text
def text(update, context):
    global STATE
    if STATE == LOCATION:
        return received_location(update, context)
    if STATE == CATEGORY:
        return received_category(update, context)
    if STATE == DISTANCE:
        return received_distance(update, context)
    if STATE == RESULT:
        return received_result(update, context)
    if STATE == WEATHER:
        return return_best_day(update, context)


def main():
    TOKEN = '1913134577:AAF9esAnKvRBY1vSlUfCkX_Oq1qFPpv4PzA'

    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    # dispatcher.add_handler(CommandHandler("help", help))
    # add an handler for our biorhythm command
    # dispatcher.add_handler(CommandHandler("biorhythm", biorhythm))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))
    #
    # # add an handler for errors
    # dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()


