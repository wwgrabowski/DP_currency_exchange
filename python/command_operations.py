from abc import ABCMeta, abstractmethod


def was_executed(func):
    def wrapper_command(self):
        try:
            if not self.executed:
                func(self)
                self.executed = True
            else:
                raise Exception
        except Exception:
            pass
    return wrapper_command


class Command(metaclass=ABCMeta):
    _id_generator = 0

    def __init__(self):
        Command._id_generator += 1
        self.command_id = self._id_generator
        self.executed = False

    @abstractmethod
    def execute(self):
        pass

    def get_id(self):
        return self.command_id


class AddProduct(Command):
    def __init__(self, currency_exchange, currency_exchange_product):
        super().__init__()
        self.currency_exchange = currency_exchange
        self.currency_exchange_product = currency_exchange_product

    @was_executed
    def execute(self):
        product_id = self.currency_exchange_product.get_id()
        self.currency_exchange._exchange_products[product_id] = self.currency_exchange_product


class Deposit(Command):
    def __init__(self, product, value):
        super().__init__()
        self.product = product
        self.value = value

    @was_executed
    def execute(self):
        self.product.change_saldo(self.value)


class Withdraw(Command):
    def __init__(self, product, value):
        super().__init__()
        self.product = product
        self.value = value

    @was_executed
    def execute(self):
        try:
            self.product.change_saldo(-self.value)
        except ValueError:
            print('Withdraw interrupted.')


class Transfer(Command):
    def __init__(self, source_product, destination_product, value):
        super().__init__()
        self.source_product = source_product
        self.destination_product = destination_product
        self.value = value

    @was_executed
    def execute(self):
        try:
            self.source_product.change_saldo(-self.value)
            self.destination_product.change_saldo(self.value)
        except ValueError:
            print('Transfer interrupted.')


class AddInterest(Command):
    def __init__(self, bank_account):
        super().__init__()
        self.bank_account = bank_account

    @was_executed
    def execute(self):
        self.bank_account.add_interest()
