from model import TelegramDBWrapper


class TelegramController:

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
        TelegramDBWrapper.create(location, category, distance, res)

