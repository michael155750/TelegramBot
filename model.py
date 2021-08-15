from tinydb import TinyDB, Query, table, where


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
        Telegram_table.insert({'location': location,
                               'category': category,
                               'distance': distance,
                               'results': res})

    @classmethod
    def get_all(cls) -> None:
        '''
        return all instance of Telegram_table
        :return:
        '''
        return Telegram_table.all()
