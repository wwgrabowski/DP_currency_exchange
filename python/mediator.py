from python.command_operations import Deposit, Withdraw


class Mediator:
    def transfer(self, src_account_id, dst_account_id, value):
        pass


class ConcreteMediator(Mediator):
    def __init__(self, exchange_1, exchange_2) -> None:
        self._exchange_1 = exchange_1
        self._exchange_1.mediator = self
        self._exchange_2 = exchange_2
        self._exchange_2.mediator = self

    def transfer(self, src_account_id, dst_account_id, value):
        account_1 = self._exchange_1.get_exchange_product_by_id(src_account_id)
        account_2 = self._exchange_2.get_exchange_product_by_id(dst_account_id)

        operation_1 = Withdraw(account_1, 100)
        operation_2 = Deposit(account_2, 100)

        self._exchange_1.execute_operation(operation_1)
        self._exchange_2.execute_operation(operation_2)


class ExchangeMediator:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator
