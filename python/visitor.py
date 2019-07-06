from abc import ABC, abstractmethod


class Visitor(ABC):

    @abstractmethod
    def visit_exchange_history(self, exchange) -> None:
        pass

    @abstractmethod
    def visit_product_id(self, product) -> None:
        pass


class ExchangeVisitor(Visitor):

    def visit_exchange_history(self, exchange) -> None:
        return exchange.get_exchange_history()

    def visit_product_id(self, product) -> None:
        return product.get_id()
