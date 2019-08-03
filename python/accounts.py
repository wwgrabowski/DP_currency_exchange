from abc import ABCMeta, abstractmethod
import datetime
from python.interests import InterestZero


class AccountInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_saldo(self):
        pass

    @abstractmethod
    def change_saldo(self, value):
        pass

    @abstractmethod
    def add_interest(self):
        pass

    @abstractmethod
    def change_interest(self, interest):
        pass

    @abstractmethod
    def get_owner(self):
        pass

    @abstractmethod
    def accept(self, visitor) -> None:
        pass


class BasicAccount(AccountInterface):
    def __init__(self, accID, saldo, owner, interest=InterestZero):
        self.id = accID
        self.saldo = saldo
        self._interest = interest()
        self.owner = owner
        self.openning_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self.account_history = []

    def get_id(self):
        return self.id

    def get_saldo(self):
        return self.saldo

    def change_saldo(self, value):
        if self.saldo + value < 0:
            raise ValueError('Saldo can not be less then 0')
        else:
            self.saldo += value

    def add_interest(self):
        self.saldo += self._interest.get_interest(self.saldo)

    def change_interest(self, interest):
        self._interest = interest

    def get_owner(self):
        return self.owner

    def accept(self, visitor):
        return visitor.visit_product_id(self)


class AccountDecorator(AccountInterface, metaclass=ABCMeta):
    def __init__(self, decorated_account):
        self.decorated_account = decorated_account

    @abstractmethod
    def get_id(self):
        return self.decorated_account.get_id()

    @abstractmethod
    def get_saldo(self):
        return self.decorated_account.get_saldo()

    @abstractmethod
    def change_saldo(self, value):
        self.decorated_account.change_saldo(value)

    @abstractmethod
    def add_interest(self):
        self.decorated_account.add_interest()

    @abstractmethod
    def change_interest(self, interest):
        self.decorated_account.change_interest(interest)

    @abstractmethod
    def get_owner(self):
        self.decorated_account.get_owner()


class DebetAccount(AccountDecorator):
    def __init__(self, decorated_account, max_debet):
        AccountDecorator.__init__(self, decorated_account)
        self.max_debet = max_debet

    def get_id(self):
        return self.decorated_account.get_id()

    def get_saldo(self):
        return self.decorated_account.get_saldo()

    def change_saldo(self, value):
        if self.decorated_account.saldo + value < -self.max_debet:
            raise ValueError('Your debet account reached limit')
        else:
            self.decorated_account.saldo += value

    def add_interest(self):
        self.decorated_account.add_interest()

    def change_interest(self, interest):
        self.decorated_account.change_interest(interest)

    def get_owner(self):
        return self.decorated_account.get_owner()

    def accept(self, visitor):
        self.decorated_account.accept(visitor)


class CreditAccount(AccountDecorator):
    def __init__(self, decorated_account):
        AccountDecorator.__init__(self, decorated_account)
        self.creditDebt = 0

    def get_id(self):
        return self.decorated_account.get_id()

    def get_saldo(self):
        return self.decorated_account.get_saldo()

    def change_saldo(self, value):
        self.decorated_account.change_saldo(value)

    def add_interest(self):
        self.decorated_account.add_interest()

    def change_interest(self, interest):
        self.decorated_account.change_interest(interest)

    def get_owner(self):
        return self.decorated_account.get_owner()

    def take_credit(self, creditValue):
        self.decorated_account.change_saldo(creditValue)
        self.creditDebt += creditValue

    def get_credit_debt(self):
        return self.creditDebt

    def accept(self, visitor):
        self.decorated_account.accept(visitor)
