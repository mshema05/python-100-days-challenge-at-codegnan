"""#if number is zero print like "entered number is zero"
n=int(input())
if n==0:
 print ("entered number is zero")
print ("program done")

#2. check if number is zero or not
num = int(input("enter a number:"))
if num==0:
    print("number is zero")
else:
    print("number is not equal to zero")

# approach 2
num = int(input("enter a number:"))
if num!=0:
    print("number is not equal to zero")
else:
    print("number is zero")

# 3 .check if number is zero or not
num = int(input("enter a number:"))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")"""


#check if number is even or odd and positive or negative
n=int(input("enter a number"))
if (n>=0 and n%2==0):
    print("positive and even")
elif (n<0 and n%2==0):
    print("negative and even")
elif (n>=0 and n%2!=0):
    print("positive and odd")
elif (n<0 and n%2!=0):
    print("negative and odd")
else:
    print("done")
