from abc import ABCMeta, abstractmethod


class Interest(metaclass=ABCMeta):
    @abstractmethod
    def get_interest(self, *args):
        pass


class InterestZero(Interest):
    def get_interest(self, saldo):
        return 0


class InterestFive(Interest):
    def get_interest(self, saldo):
        return saldo * 0.05


class InterestTen(Interest):
    def get_interest(self, saldo):
        return saldo * 0.1
