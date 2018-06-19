from lettuce import *
from Account import Account
from shared_steps import *


@before.each_outline
def initial_accounts(scenario,outline):
    acc1 = Account('1', 0)
    acc2 = Account('2', 150)
    accounts_dict = {}
    accounts_dict[acc1.id] = acc1
    accounts_dict[acc2.id] = acc2
    world.accounts=accounts_dict
    world.withdrawal_from = accounts_dict


@step('withdrawal from a specific BankAccount (\d+)')
def deposit_to_specific_bank_account(step, id):
    world.withdrawal_from = world.accounts.get(str(id))


@step('User request (\d+) cash')
def cash_amount(step, number):
    world.withdrawal_from.set_withdrawal(int(number))


@step('Balance is higher than (\d+)')
def check_balance_higher_than_requested(step, amountRequested):
    amountRequested = int(amountRequested)
    assert world.withdrawal_from.balance >= amountRequested, \
        "%d is greater than %d" %(world.withdrawal_from.balance,amountRequested)
    world.withdrawal_from.withdrawal_from_balance()





# @after.all
# def say_goodbye(total):
#     print "Congratulations, %d of %d scenarios passed!" % (
#         total.scenarios_ran,
#         total.scenarios_passed
#     )
#     print "Goodbye!"
#
