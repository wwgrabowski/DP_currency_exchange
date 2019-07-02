
class CurrencyExchange:
    __id_generator = 0

    def __init__(self):
        self.__id_generator += 1
        self.exchange_id = self.__id_generator
        self._exchange_operations = list()
        self._exchange_history = list()
        self._exchange_products = {}

    def __str__(self):
        return f'Currency exchange ID: {self.exchange_id}'

    def get_exchange_id(self):
        return self.exchange_id

    def store_operations(self, exchange_operation):
        self._exchange_operations.append(exchange_operation)

    def get_exchange_history(self):
        return self._exchange_history

    def execute_operations(self):
        for operation in self._exchange_operations:
            operation.execute()
            self._exchange_history.append(operation)
        self._exchange_operations.clear()

    def get_exchange_product_by_id(self, product_id):
        try:
            return self._exchange_products[product_id]
        except KeyError:
            print(f'Product with key: {product_id} do not exist.')
            return None

    def get_exchange_products(self):
        return self._exchange_products


