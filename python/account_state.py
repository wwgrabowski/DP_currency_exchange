"""
State pattern for maneging different level of account validation.
"""

from abc import abstractmethod, ABCMeta


class AccountState(metaclass=ABCMeta):

    @abstractmethod
    def handle(self):
        pass


class UnauthorizedAccount(AccountState):

    def handle(self):
        pass


class BasicAuthorizationAccount(AccountState):

    def handle(self):
        pass


class AdvanceAuthorizationAccount(AccountState):

    def handle(self):
        pass
