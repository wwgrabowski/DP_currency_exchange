
class CurrencyExchange:
    __id_generator = 0
    __id_generator += 1

    def __init__(self):
        self.exchange_id = self.__id_generator

    def __str__(self):
        return f'Currency exchange ID: {self.exchange_id}'
