
loanAmount = float ( input("How much do you want to borrow?R$ "))
interesRate = float(input("What is the interest rate on yoour loan? R$ "))
repaymentLength = float (input("How many years to repay your loan? R$ "))


interestCalculation = interesRate /100

print(interesRate)
print(interestCalculation)


numberOfPayment = repaymentLength*12

monthlyRepaymentCost = loanAmount * interestCalculation * (1+interestCalculation)* numberOfPayment / ((1+interestCalculation) * numberOfPayment -1)

totalCharge = (monthlyRepaymentCost * numberOfPayment) - loanAmount

print("you want to borrow R$" + str(loanAmount) + " over " + str(repaymentLength) + "years, with an interest rate of " + str(interesRate) + "%!" )
