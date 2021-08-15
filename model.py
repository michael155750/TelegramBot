<<<<<<< Updated upstream:model.py
from tinydb import TinyDB, Query, table, where
import tinydb

TelegramDBPath = r'C:\Users\elyasaf\PycharmProjects\GitHub\telegrambot-elyasaf-michael\Telegram_Bot_Best_Location\data_9_bot_telegram.json'
TelegramDBTable = TinyDB(TelegramDBPath)
Telegram_table = TelegramDBTable.table('Telegram')


class TelegramDBWrapper:

    @classmethod
    def get_by_location(cls, locat: str):
        """
        :param my_number: number
        :return: Returns the instance from the database
        """
        q = Query
        return Telegram_table.search(q.location == locat)

    @classmethod
    def get_by_location_category(cls, locat: str, category: str):
        q = Query
        return Telegram_table.search((q.location == locat) & (q.Category == category))

    @classmethod
    def create(cls, location: str, category: str, res: str):
        """
        create new instance into database
        :param location:
        :param my_number:
        """
        # if cls.get_by_id(my_number):
        #     TelegramDBWrapper.update_number(2, '9')
        Telegram_table.insert({'location': location,
                               'category': category,
                               'results': res})

    # @classmethod
    # def update_number(cls, my_number: str, new_update_value):
    #     """
    #     update Number_of_performances of instance in database
    #     :param my_number: id of instance
    #     :param new_update_value: Number_of_performances instance
    #     """
    #     Telegram_table.update({'Number_of_performances': new_update_value}, Query().id == str(my_number))

    @classmethod
    def get_all(cls) -> None:
        '''
        return all instance of Telegram_table
        :return:
        '''
        return Telegram_table.all()
=======
from tinydb import TinyDB, Query, table, where
import tinydb

TelegramDBPath = r'C:\Users\elyasaf\PycharmProjects\GitHub\telegrambot-elyasaf-michael\Telegram_Bot_Best_Location\data_9_bot_telegram.json'
TelegramDBTable = TinyDB(TelegramDBPath)
Telegram_table = TelegramDBTable.table('Telegram')


class TelegramDBWrapper:

    @classmethod
    def get_by_location(cls, locat: str):
        """
        :param my_number: number
        :return: Returns the instance from the database
        """
        q = Query()
        return Telegram_table.search(q.location == locat)

    @classmethod
    def get_by_location_category_distance(cls, locat: str, category: str, distance: str):
        q = Query()
        res = Telegram_table.search(q.location == "location")
        res = Telegram_table.search((q.location == locat) & (q.category == category) & (q.distance == distance))
        return res
    @classmethod
    def create(cls, location: str, category: str, distance:str, res: str):
        """
        create new instance into database
        :param location:
        :param my_number:
        """
        # if cls.get_by_id(my_number):
        #     TelegramDBWrapper.update_number(2, '9')
        Telegram_table.insert({'location': location,
                               'category': category,
                               'distance': distance,
                               'results': res})

    # @classmethod
    # def update_number(cls, my_number: str, new_update_value):
    #     """
    #     update Number_of_performances of instance in database
    #     :param my_number: id of instance
    #     :param new_update_value: Number_of_performances instance
    #     """
    #     Telegram_table.update({'Number_of_performances': new_update_value}, Query().id == str(my_number))

    @classmethod
    def get_all(cls) -> None:
        '''
        return all instance of Telegram_table
        :return:
        '''
        return Telegram_table.all()
>>>>>>> Stashed changes:Telegram_Bot_Best_Location/model.py
