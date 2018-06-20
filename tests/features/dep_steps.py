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
    world.accounts = accounts_dict
    world.deposit_to = accounts_dict

@step('Deposit to a specific BankAccount (\d)')
def deposit_to_specific_bank_account(step ,id):
    world.deposit_to = world.accounts.get(str(id))



@step('User deposit (\d+) cash')
def cash_amount(step,number):
    world.deposit_to.add_cash_to_balance(int(number))


#
# @after.all
# def say_goodbye(total):
#     print "Congratulations, %d of %d scenarios passed!" % (
#         total.scenarios_ran,
#         total.scenarios_passed
#     )
#     print "Goodbye!"