<<<<<<< Updated upstream:controller.py
from model import TelegramDBWrapper


class TelegramController:

    @classmethod
    def get_by_location(cls, locat: str):
        return TelegramDBWrapper.get_by_location(locat)

    @classmethod
    def get_by_location_category(cls, locat: str, category: str):
        res = TelegramDBWrapper.get_by_location_category(locat, category)['distance']
        if res is None:
            TelegramController.create_new(locat, category, "jafa resturant in 1500 meters")
        return TelegramDBWrapper.get_by_location_category(locat, category)['distance']

    @classmethod
    def create_new(cls,  location: str, category: str, res: str):
        """
        Receiver is subject to income, if it does not exist it
        creates a new one, and if it does exist it updates it.
        :param my_value: number
        """
        x = []
        for item in TelegramController.get_by_location(location):
            x += item
        if len(x) != 0:
            for item in x:
                if x['category'] == category:
                    return
        else:
            TelegramDBWrapper.create(location, category, res)


    #
    # @classmethod
    # def get_most_popular(cls):
    #     """
    #     Returns a list of all the numbers the user
    #     entered the most times
    #     :return:
    #     """
    #     x = 0
    #     result = []
    #     for item in TelegramDBWrapper.get_all():
    #         if x == item['Number_of_performances']:
    #             result.append(item['id'])
    #         if x < item['Number_of_performances']:
    #             x = item['Number_of_performances']
    #             result.clear()
    #             result.append(item['id'])
    #     return result
=======
from model import TelegramDBWrapper


class TelegramController:

    @classmethod
    def get_by_location(cls, locat: str):
        return TelegramDBWrapper.get_by_location(locat)

    @classmethod
    def get_by_location_category_distance(cls, locat: str, category: str, distance:str):
        res = TelegramDBWrapper.get_by_location_category_distance(locat, category, distance)
        if res == []:
            return " "
        return res[0]['results']

    @classmethod
    def create_new(cls,  location: str, category: str, distance:str,  res: str):
        """
        Receiver is subject to income, if it does not exist it
        creates a new one, and if it does exist it updates it.
        :param my_value: number
        """
        # x = []
        # for item in TelegramController.get_by_location_category_distance(location, category, distance, res):
        #     x += item
        # if len(x) != 0:
        #     for item in x:
        #         if x['category'] == category:
        #             return
        # else:
        TelegramDBWrapper.create(location, category, distance, res)


    #
    # @classmethod
    # def get_most_popular(cls):
    #     """
    #     Returns a list of all the numbers the user
    #     entered the most times
    #     :return:
    #     """
    #     x = 0
    #     result = []
    #     for item in TelegramDBWrapper.get_all():
    #         if x == item['Number_of_performances']:
    #             result.append(item['id'])
    #         if x < item['Number_of_performances']:
    #             x = item['Number_of_performances']
    #             result.clear()
    #             result.append(item['id'])
    #     return result
>>>>>>> Stashed changes:Telegram_Bot_Best_Location/controller.py
