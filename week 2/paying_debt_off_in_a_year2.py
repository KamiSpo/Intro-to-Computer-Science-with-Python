def paying_debt_off(balance, annualInterestRate):

    monthly_payment = 10
    unpaid_balance = balance

    while unpaid_balance > 0:
        #calculates balance after one year
        for month in range(1,13):
            #calculating the unpaind balance amount each month
            unpaid_balance -= monthly_payment
            #updating the balance value by adding interest to unpaid balance
            unpaid_balance = unpaid_balance + ((annualInterestRate / 12) * unpaid_balance)

        if unpaid_balance <= 0:
            #lowest monthly payment found, stopping loop
            break
        else:
            #monthly payment was too low, need to incremat and reset unpaid balance
            monthly_payment += 10
            unpaid_balance = balance
    
    print("Lowest Payment:" + str(monthly_payment))
    return monthly_payment
   
