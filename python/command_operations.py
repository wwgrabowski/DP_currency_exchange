from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        pass


class AddProduct(Command):
    def __init__(self, currency_exchange, currency_exchange_product):
        self.currency_exchange = currency_exchange
        self.currency_exchange_product = currency_exchange_product

    def execute(self):
        product_id = self.currency_exchange_product.get_id()
        self.currency_exchange._exchange_products[product_id] = self.currency_exchange_product


class Deposit(Command):
    def __init__(self, product, value, val_type):
        self.product = product
        self.value = value
        self.val_type = val_type

    def execute(self):
        self.product.change_saldo(self.value)


class Withdraw(Command):
    def __init__(self, product, value, val_type=None):
        self.product = product
        self.value = value
        self.val_type = val_type

    def execute(self):
        try:
            self.product.change_saldo(-self.value)
        except ValueError:
            print('Withdraw interrupted.')


class Transfer(Command):
    def __init__(self, source_product, destination_product, value, val_type=None):
        self.source_product = source_product
        self.destination_product = destination_product
        self.value = value
        self.val_type = val_type

    def execute(self):
        try:
            self.source_product.change_saldo(-self.value)
            self.destination_product.change_saldo(self.value)
        except ValueError:
            print('Transfer interrupted.')


class AddInterest(Command):
    def __init__(self, bank_account):
        self.bank_account = bank_account

    def execute(self):
        self.bank_account.add_interest()
