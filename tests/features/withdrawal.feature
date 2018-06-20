Feature: Withdrawal
    As a customer,
    I want to Withdrawal cash from a specific bank account,
    so my balance will decrease.

    Scenario Outline: Withdrawal any amount
        Given Withdrawal from a specific BankAccount <BankAccount>
        When User request <amount> cash
        And Balance is higher than <amount>
        Then User see the balance <TotalAmount> after withdrawal operation


  Examples:
    | amount | BankAccount | TotalAmount
    | 0      | 1           |0
    | 150    | 2           |0
    | 70     | 2           |80

