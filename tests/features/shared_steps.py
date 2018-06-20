from lettuce import *
from Account import Account




@step('User see the balance (\d+) after (deposit|withdrawal) operation')
def check_balance(step, expected, operation):
    expected=int(expected)
    if operation == 'withdrawal':
        assert world.withdrawal_from.balance == expected, \
            "Got %d expected %d" % (world.withdrawal_from.balance,expected)
    if operation == 'deposit':
        assert world.deposit_to.balance == expected, \
            "Got %d expected %d" % (world.deposit_to.balance, expected)


