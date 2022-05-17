# Python program to determine whether
# the number is Armstrong number or not
  
# Function to calculate x raised to 
# the power y
def power(x, y):
      
    if y == 0:
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