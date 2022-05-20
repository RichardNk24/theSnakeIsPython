# Python program to determine whether
# the number is Armstrong number or not
import math
import statistics
import array as arr

princ_amount = float(input(" Please Enter the Principal Amount : "))
rate_of_int = float(input(" Please Enter the Rate Of Interest   : "))
time_period = float(input(" Please Enter Time period in Years   : "))

ci_future = princ_amount * (math.pow((1 + rate_of_int / 100), time_period)) 
compound_int = ci_future - princ_amount

print("Future Compound Interest for Principal Amount {0} = {1}".format(princ_amount, ci_future))
print("Compound Interest for Principal Amount {0} = {1}".format(princ_amount, compound_int))

# list of positive integer numbers   
datasets = [5, 2, 7, 4, 2, 6, 8]     
x = statistics.mean(datasets)     
# Printing the mean   
print("Mean is :", x)  

a = arr.array('i', [2, 4, 6, 8])  
print("First element:", a[0])  
print("Second element:", a[1])  
print("Second last element:", a[-1])  


# Function to calculate x raised to 
# the power y
def power(x, y):
    
    if     y == 0:
        return 1
    if y % 2 == 0:
        return power(x, y // 2) * power(x, y // 2)
          
    return x * power(x, y // 2) * power(x, y // 2)
  
# Function to calculate order of the number
def order(x):
  
    # Variable to store of the number
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
          
    return n

# Function to check whether the given 
# number is Armstrong number or not
def isArmstrong(x):

    n = order(x)
    temp = x
    sum1 = 0

    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + power(r, n)
        temp = temp // 10
  
    # If condition satisfies
    return (sum1 == x)
  
# Driver code
x = 153
print(isArmstrong(x))
  
x = 1253
print(isArmstrong(x))
# using If Statement

yr = int(input("Please Enter the Number you wish: "))

if (( yr%400 == 0)or (( yr%4 == 0 ) and ( yr%100 != 0))):
    print("%d is a Leap year" %yr)
else:
    print("%d is Not" %yr)

# using Elif Statement

ya = int(input("Please Enter as you wish : "))

if (ya%400 == 0):
    print("%d is a Leap year" %ya)
elif (ya%100 == 0):
    print("%d is Not" %ya)
elif (ya%4 == 0):
    print("%d is a Leap year" %ya)
else:
    print("%d is Not" %ya)
    
# Python Program to find Power of a Number

number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
power = 1

for i in range(1, exponent + 1):
    power = power * number
    
print("The Result of {0} Power {1} = {2}".format(number, exponent, power))

# Python Program to find Power of a Number

number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))

power = 1
i = 1

while(i <= exponent):
    power = power * number
    i = i + 1
    
print("The Result of {0} Power {1} = {2}".format(number, exponent, power))

Number = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Number

while(Temp > 0):
    Factorial = 1
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1

    print("\n Factorial of %d = %d" %(Reminder, Factorial))
    Sum = Sum + Factorial
    Temp = Temp // 10

print("\n Sum of Factorials of a Given %d = %d" %(Number, Sum))
    
if (Sum == Number):
    print(" %d is a Strong Number" %Number)
else:
    print(" %d is not" %Number)
    
    
# Python Program to Calculate Profit or Loss

actual_cost = float(input(" Please Enter the Actual Product Price: "))
sale_amount = float(input(" Please Enter the Sales Amount: "))

if(actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    print("Total Loss Amount = {0}".format(amount))
elif(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit No Loss!!!")
    
if(actual_cost > sale_amount):
    amount = actual_cost - sale_amount
    print("Total Loss Amount = {0}".format(amount))
elif(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit No Loss!!!")
