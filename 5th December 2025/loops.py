#Loops in Python - to iterate particular Block of Code

#1. For Loop. when start and end is known - use for loop


#WAP TO PRINT YOUR NAME 10 TIMES

#(n) - start from 0 till n-1
'''
for i in range(5):
    print(i,"Harshit",end=" ")
print()
#(n,m) - start with n and ends till m-1. it exclued the end point

for i in range(12,25):
    print(i,"Hello",end=" ")
print()
#(n,m,z) - start with n, till m-1 and step value by 2
for i in range (10,30,2):
    print(i,end=" ")    #10,12.....
print()
'''
#WAP TO ACCEPT NUMBER FROM USER AND DISPLAY TABLE TO IT.

##num = int(input("Enter the number:"))
##
##for i in range(0,11):
##    print(num,"x",i,"=",num*i)
'''
start = int(input("Enter the start number:"))
end = int(input("Enter the End number"))
for num in range(start,end +1):
    for i in range(0,11):
        print(num,"x",i,"=",num*i)
    print()
'''
'''
#FIBONACCI SERIES 0,1 WILL BE GIVEN 0,1,1,2,3
c = int(input("Enter the end point:"))
a = 0
b = 1
print(a,end=" ")
print(b,end=" ")
for i in range(1,c+1):
    sum1 = a+b
    print(sum1, end=" ")
    a = b #assign from right to left
    b = sum1
'''

#PATTERN - OUTER LOOP = ROWS, INNER LOOP= COLUMN
'''
##*
##* *
##* * *
##* * * *

for i in range (1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''

'''
##1 
##1 2 
##1 2 3 
##1 2 3 4 
##1 2 3 4 5

for i in range (1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''

'''
##1 2 3 4 5
##1 2 3 4
##1 2 3
##1 2
##1

for i in range(5,0,-1):# starts with 5 and goes till 0 with -1 step means 5,4,3,2,1
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
'''
##* * *
##* *
##*

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
'''

'''
for i in range(1,6):
    for j in range(6,i+1,-1):
        print(end=" ")
    print(" *",i)
'''
#WAP TO GET FACTORIAL OF A NUMBER
'''
n = int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact = fact *i
print("Factorial of",n,"is:",fact)
'''
'''
#WAP TO GET first 10 OF A NUMBER
#n = int(input("Enter the number:"))
sum1=0
for i in range(1,11):
    sum1 = sum1 +i
print("The sum of first 10 natural numbers:",sum1)
'''
'''
#WAP TO GET EVEN NUMBER BETWEEN 1 TO 100

for i in range(0,101):
    if(i%2==0):
        print(i,end=" ")
'''



#2. While Loop


#WAP TO PRINT "HELLO WORLD" 10 TIMES
'''
i = 1
while(i<=10):
    print("HELLO WORLD")
    i = i+1
'''
'''

#WAP TO GET TABLE OF NUMBER:

n = int(input("Enter the number:"))
i = 1
while(i<=10):
    print(n,"x",i,"=",n*i)
    i = i+1
print("USING WHILE LOOP")
'''



#WAP TO REVERSE A GIVEN NUMBER eg. 156 = 651
'''
n = int(input("Enter the number:"))
rev =0
while(n>0):
    rem = n % 10
    rev = rev*10+rem
    n = n//10
    print(rev)
print("The reverse of",n,"is:",rev)
'''

#WAP TO CHECK PALINDROME
'''
n = int(input("Enter The Number:"))
temp = n
rev = 0
while(n>0):
    rem = n %10
    rev = rev*10 + rem
    n = n//10
if (temp == rev):
    print("NUMBER IS PALINDROME")
else:
    print("NUMBER IS NOT PALINDROME")
'''
'''
#WAP TO GET SUM OF DIGIT OF A NUMBER eg: 153 o/p= 9
n= int(input("Enter the number:"))
sum = 0
while(n>0):
    digit = n %10
    sum = sum+ digit
    n = n//10
print("the sum of digit of a number:",sum)
'''

#WAP TO CHECK WHETHER THE NUMBER IS ARMSTRONG NUMBER OR NOT
'''
#153 1+125+27= 153
n= int(input("Enter the number:"))
temp = n
sum = 0
while(n>0):
    digit = n %10
    sum = sum + digit*digit*digit
    n = n//10
if (temp == sum):
    print("NUMBER IS ARMSTRONG NUMBER")
else:
    print("NUMBER IS NOT ARMSTRONG NUMBER")
'''



        
