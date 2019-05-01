from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    def __init__(self, receiver):
        self._receiver = receiver

    @abstractmethod
    def execute(self):
        pass


class AddProduct(Command):
    def __init__(self, currency_exchange, currency_exchange_product):
        self.currency_exchange = currency_exchange
        self.currency_exchange_product = currency_exchange_product

    def execute(self):
        pass


class Deposit(Command):
    def __init__(self, product, value, val_type):
        self.product = product
        self.value = value
        self.val_type = val_type

    def execute(self):
        pass


class Withdraw(Command):
    def __init__(self, product, value, val_type):
        self.product = product
        self.value = value
        self.val_type = val_type

    def execute(self):
        pass


class Transfer(Command):
    def __init__(self, source_product, destination_product, value, val_type):
        self.source_product = source_product
        self.destination_product = destination_product
        self.value = value
        self.val_type = val_type

    def execute(self):
        pass
