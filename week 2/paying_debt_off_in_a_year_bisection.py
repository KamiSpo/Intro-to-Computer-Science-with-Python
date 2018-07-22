def payingDebtOff(balance, annualInterestRate):

    monthlyInterestRate = annualInterestRate / 12.0
    #monthly payment lower bound
    lowerBound = balance / 12
    #monthly payment upper bound
    upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
    epsilon = 0.01

    while True:
        #creating a new search area
        monthlyPayment = (lowerBound + upperBound) / 2
        #resetting the balance
        testBalance = balance

        #calculating the balance after one year
        for month in range(1,13):
            #calculating the unpaind balance amount each month
            testBalance -= monthlyPayment
            #updating the balance value by adding interest to unpaid balance
            testBalance = testBalance + (monthlyInterestRate * testBalance)

        if abs(testBalance) <= epsilon:
            #balance is paid with the one cent acurracy
            break
        elif testBalance > 0:
            #balance is bigger than 0, need to increase the monthly payment
            lowerBound = monthlyPayment
        elif testBalance < 0:
            #balance is lower than 0, need to decrease the monhly payment
            upperBound = monthlyPayment

    print("Lowest payment: " + str(round(monthlyPayment, 2)))
    return round(monthlyPayment, 2)





        
