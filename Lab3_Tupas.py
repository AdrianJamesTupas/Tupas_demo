#input monthly salary and loan amount
salary = float(input("Enter Your Monthly Salary: "))
loan = float(input("Enter Loan Amount: "))
eligible_check = salary * 10
#(1)Identify if salary is higher than or equal to 30,000.00 and if requested loan is less than or equal to 10x their salary
if(salary>=float(30000.00) and loan<=eligible_check):
    print("You are eligible for a loan.")
    months = int(input("How Many Month to Pay: "))
    interest = loan * 0.10
    new_loan = loan + interest
    print("Amount to Pay: ", new_loan / months)
#If salary is lower than 30,000.00, output that the salary is too low
elif(salary<30000):
    print("You are not eligible: Salary too low.")
#If loan requested is higher than 10x the salary, output that the loan requested is too high.
elif(loan>eligible_check):
    print("You are not eligible: Loan requested is too high.")

else:
    print("Error")