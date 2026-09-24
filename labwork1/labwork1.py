# Functions
def isPrime(n):     # Prime number check
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def isPerfect(n):    # Perfect number check
    sumDivs = 0
    for i in range(1,n):
        if n%i == 0:
            sumDivs += i
    if sumDivs == n:
        return True
    return False

def getDivisors(n):    # Get all divisors
    divs = []
    sign = 1
    n1 = n
    if n == 0:
        return "None"
    if (n1 > 0):
        n1 += 1
    else:
        sign = -1
        n1 = (-1*n1) + 1
    for i in range (1, n1):
        if n%i == 0:
            divs.append(i*sign)
    return divs

def remove_dollar_sign(s):    # Remove dollar signs $ by split String to List and join List to String
    s1 = s.split('$')
    s = ''.join(s1)
    return s

def toIntList(t):    # Convert String into List for convenience
    # Expected input [1, 2, 3]; 1, 2, 3; 1 2 3; 123
    if (type(t) == list):
        return t
    t1 = t
    t1 = t1.split('[')
    t1 = ''.join(t1)
    t1 = t1.split(']')
    t1 = ''.join(t1)
    if ',' in t:
        t1 = t1.split(' ')
        t1 = ''.join(t1)
        t1 = t1.split(',')
    elif ' ' in t:
        t1 = t1.split(' ')
    t2 = []
    for i in t1:
        t2.append(int(i))
    return t2

def extract_even(t):    # Even number extractor
    t1 = []
    if (type(t) != list):
        t = toIntList(t)
    for i in t:
        if int(i)%2 == 0:
           t1.append(int(i))
    return t1

def factRecursive(n):    # Factorial - Recurssion function
    if n < 0:
        return -1;
    # convention: 0! = 1; 1! = 1
    if n == 0 or n == 1:
        return 1
    
    # n! = n*(n-1)!
    else:
        return n*fact(n-1)

def fact(n):    # Factorial - Preferred function
    temp = 1
    if n < 0:
        return -1;
    for i in range(1,n+1):
        temp *= i
    return temp

def getDist(t1, t2):    # Distance between 2 points (maximum 3-dimensional space)
    if len(t1) == 1:
        if t2[0] > t1[0]:
            return t2[0] - t1[0]
        return t1[0] - t2[0]
    if len(t1) == 2:
        return ((t2[0] - t1[0])**2 + (t2[1] - t1[1])**2)**0.5
    if len(t1) == 3:
        return ((t2[0] - t1[0])**2 + (t2[1] - t1[1])**2 + (t2[2] - t1[2])**2)**0.5
    return -1;

# Main
#Ex 1
pi = 3.14
temp = float(input("Enter Radius: "))
print(f"Circle Area = {temp*temp*pi}")
print()

#Ex 2
temp = float(input("Enter Temperature in Celsius: "))
print(f"{temp} (C) = {temp*1.8+32} (F)\n")

#Ex 3
temp = int(input("Enter a Number (Prime Check): "))
if isPrime(temp):
    print(f"{temp} is a prime number\n")
else:
    print(f"{temp} is NOT a prime number\n")

#Ex 4
temp = int(input("Enter a Number (Perfect Check): "))
if isPerfect(temp):
    print(f"{temp} is a perfect number\n")
else:
    print(f"{temp} is NOT a perfect number\n")

#Ex 5
color = ('Red', 'red', 'Green', 'green', 'Blue', 'blue')
temp = input("What is your favourite color? ")
if temp in color:
    print(f"Your color is at index {color.index(temp) + 1} in my list\n")
else:
    # Êxpected: Yellow, Brown, Orange, gReEN, BLUE...
    print("Sorry, I could not find your color\n")

#Ex 6
range1 = []
range2 = []
range3 = []
range4 = []

for i in range(0,7):
    range1.append(i)
for i in range(1,11,3):
    range2.append(i)
for i in range(5,0,-1):
    range3.append(i)
for i in range(6,-3,-2):
    range4.append(i)
print(f"{range1}\n{range2}\n{range3}\n{range4}\n")

#Ex 7
temp = input("Enter a string (Remove Dollars): ")
print(f"{remove_dollar_sign(temp)}\n")

#Ex 8
temp = input("Enter a list (eg: 2 4 6 -8 -10): ")
print(f"{extract_even(temp)}\n")

#Ex 9
temp = int(input("Enter a non-negative integer (Return Factorial): "))
print(f"Factorial of {temp} is {fact(temp)}\n")

#Ex 10
temp = int(input("Enter a non-negative integer (Return Divisors): "))
print(f"Divisors of {temp}: {getDivisors(temp)}\n")

#Ex 11
temp = int(input("Enter number of axes (maximum 3): "))
p1 = []
p2 = []
ax = ('x', 'y', 'z')

for i in range(0, temp):
    p1.append(float(input(f"point 1's {ax[i]}: ")))
    
for i in range(0, temp):
    p2.append(float(input(f"point 2's {ax[i]}: ")))

print(f"The distance between point 1 and point 2 is about {round(getDist(p1, p2), 3)}\n")

#Ex 12
temp = int(input("Enter m (rows): "))
temp2 = int(input("Enter n (columns): "))
# rows
for i in range(0, temp):
    # message in row i
    if i == 0 or i == temp-1:
        print("* "*(temp2-1) + "*")
    else:
        print("*" + " "*((temp2-1)*2-1) + "*")
