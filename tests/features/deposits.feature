Feature: Deposit
    As a customer,
    I want to deposit cash to a specific bank account,
    so my balance will increase.

    Scenario: Deposit cash
        Given Deposit to a specific BankAccount <BankAccount>
        When User deposit <amount> cash
        Then User see the balance <TotalAmount> after deposit operation


  Examples:
    | amount | BankAccount |TotalAmount
    | 0      | 1           |0
    | 150    | 2           |300
    | 200    | 1           |200
    | 100    | 2           |250
