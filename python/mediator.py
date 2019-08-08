from python.command_operations import Deposit, Withdraw


class Mediator:
    def transfer(self, src_exchange, dst_account_id, value, operation_id):
        pass


class ConcreteMediator(Mediator):

    def __init__(self):
        self._exchange_dct = dict()

    def get_exchange_dct(self):
        return self._exchange_dct

    def add_exchange(self, exchange):
        self._exchange_dct[exchange.get_exchange_id()] = exchange

    def transfer(self, src_exchange, dst_account_id, value, src_operation_id):
        deposit_exchange = None
        for exchange in self._exchange_dct.values():
            try:
                exchange.get_exchange_product_by_id(dst_account_id)
                deposit_exchange = exchange
                break
            except:
                pass

        if not deposit_exchange:
            raise AttributeError('There is no exchange with that account id.')

        dst_operation = Deposit(dst_account_id, value)

        if src_operation_id in src_exchange.get_exchange_history():
            deposit_exchange.store_operation(dst_operation)


class ExchangeMediator:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator
