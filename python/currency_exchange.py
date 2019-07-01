
class CurrencyExchange:
    __id_generator = 0

    def __init__(self):
        self.__id_generator += 1
        self.exchange_id = self.__id_generator
        self._exchange_operations = list()
        self._exchange_history = list()

    def __str__(self):
        return f'Currency exchange ID: {self.exchange_id}'

    def store_operations(self, exchange_operation):
        self._exchange_operations.append(exchange_operation)

    def execute_operations(self):
        for operation in self._exchange_operations:
            operation.execute()
            self._exchange_history.append(operation)
        self._exchange_operations.clear()

