
class Account(object):
    def __init__(self,id,balance):
        self._id = id
        self._balance = balance
        self._deposit=0
        self._withdrawal=0

    @property
    def balance(self):
        return self._balance

    @property
    def id(self):
        return self._id

    @property
    def deposit(self):
        return self._deposit

    @property
    def withdrawal(self):
        return self._withdrawal


    def set_withdrawal(self,amount):
        self._withdrawal=amount

    def set_deposit(self,amount):
        self._deposit=amount

    def add_cash_to_balance(self,amount):
        self._balance=self.balance+amount

    def withdrawal_from_balance(self):
        self._balance-=self.withdrawal



