from datetime import datetime
name = input("Enter Customer name ")
current_bal = int(input("Enter customer current balance "))
deposit_amount = int(input("Enter Deposit amount "))

total_dep_amount = current_bal + deposit_amount
print("Total balance after deposit ", total_dep_amount)

with_amount = int(input("Enter Withdrawl amount "))

total_with_amount = total_dep_amount - with_amount
print("Total balance after withdrawl ", total_with_amount)

#how to make it invalid statement if not entered a integer
if deposit_amount and with_amount:
    print(name,"you have entered invalid deposit and withdrawl amount")
elif with_amount > current_bal:
    print (name,"you have withdrawl more then current balance")
    
print("\nyou must deposit 500rs and maximum 10000 rs perday")

x = datetime.today()
print("Today's date and time ",x)