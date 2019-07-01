from abc import ABCMeta, abstractmethod
import datetime


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
    def changeInterest(self, interest):
        pass

    @abstractmethod
    def getOwner(self):
        pass


class BasicAccount(AccountInterface):
    def __init__(self, accID, saldo, owner, interest):
        self.id = accID
        self.saldo = saldo
        self._interest = interest
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
        self.saldo += self._interest.getInterest(self.saldo)

    def changeInterest(self, interest):
        self._interest = interest

    def getOwner(self):
        return self.owner


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
    def changeInterest(self, interest):
        self.decorated_account.changeInterest(interest)

    @abstractmethod
    def getOwner(self):
        self.decorated_account.getOwner()


class DebetAccount(AccountDecorator):
    def __init__(self, decorated_account):
        AccountDecorator.__init__(self, decorated_account)

    def get_id(self):
        return self.decorated_account.get_id()

    def get_saldo(self):
        return self.decorated_account.get_saldo()

    def change_saldo(self, value):
        if self.decorated_account.saldo + value < -1000:
            raise ValueError('Your debet account reached limit')
        else:
            self.decorated_account.saldo += value

    def add_interest(self):
        self.decorated_account.add_interest()

    def changeInterest(self, interest):
        self.decorated_account.changeInterest(interest)

    def getOwner(self):
        return self.decorated_account.getOwner()


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

    def changeInterest(self, interest):
        self.decorated_account.changeInterest(interest)

    def getOwner(self):
        return self.decorated_account.getOwner()

    def takeCredit(self, creditValue):
        self.decorated_account.change_saldo(creditValue)
        self.creditDebt += creditValue

    def getCreditDebt(self):
        return self.creditDebt
