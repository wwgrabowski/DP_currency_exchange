
from python.account_state import UnauthorizedAccount, AdvanceAuthorizationAccount, BasicAuthorizationAccount


class BaseAccount:
    def __init__(self, authorization_state):
        self._account_state = authorization_state

    def change_account_state(self, authorization_state):
        self._account_state = authorization_state

