def paying_debt(balance, annualInterestRate, monthlyPaymentRate):

    for month in range(1,13):
        #calculating the amount of minimum payment being made each month 
        payment = balance * monthlyPaymentRate
        #calculating the unpaind balance amount each month
        balance -= payment
        #updating the balance value by adding interest to unpaid balance
        balance = balance + ((annualInterestRate / 12) * balance)
    
    balance = round(balance, 2)
    print("Remaining balance: " + str(balance))
    return balance
    
