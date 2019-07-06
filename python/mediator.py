

class Mediator:
    pass


class ConcreteMediator(Mediator):
    def __init__(self, exchange_1, exchange_2) -> None:
        self._exchange_1 = exchange_1
        self._exchange_1.mediator = self
        self._exchange_2 = exchange_2
        self._exchange_2.mediator = self


class ExchangeMediator:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator
