#CONDITIONAL STATEMENT


'''THREE TYPES
if
if....else
if...elif....else
'''
'''
#CONDITIONAL STATEMENT
#1. if conditon statment

#upon positive input greet a welcome message to person

user_input = int(input("Enter a positive number:"))
if (user_input>0):
    print("Welcome to the World")
print("Congrats!!!")
'''

#2. if else condition statement

#wap to check whether the person is eligibe to vote or not
'''
age = int(input("Enter Age:"))
if(age>=18):
    print("Eligible to vote!!!!")
else:
    print("Not Elgigble to vote still you have to wait",18-age,"years")

'''
'''
#2. if else condition statement

#wap to check whether the person is eligibe to vote or not

age = int(input("Enter Age:"))
if(age>0):
    if(age>=18):
        print("Eligible to vote!!!!")
    else:
        print("Not Elgigble to vote still you have to wait",18-age,"years")
else:
    print("Enter positive number")
'''
'''
#WAP TO ACCEPT SCORES OF TWO TEAMS SAY(IND, PAK) AND MAKE A DECISION WHO WON THE MATCH (WON,OR DRAW)

ind = int(input("Enter the Score of India:"))
pak = int(input("Enter the Score of Pakistan:"))

if (ind>pak):
    print("India Won the Match by",ind-pak,"runs")
elif (pak==ind):
    print("Match Draw!!!")
else:
    print("Pakistan won the Match by",pak-ind,"runs")    
'''

'''
#EXAMPLE: Accept percentage from user and make decision about Grades

##if per>=60 print you got A Grade
##if per>=75 print you recieve O grade
##if per>= 50 print you recieve C grade
##otherwise you are failed need to improvement in the result
'''
'''
per = int(input("Enter Percentage:"))
if (per >= 75):
    print("You Recieve O Grade.")
elif (per >=65):
    print("You Recieve A Grade.")
elif (per>= 50):
    print("You Recieve C Grade.")
else:
    print("You Have Failed need to Imporvement in Result.")
'''
'''
#EXAMPLE 3: ONLINE SHOPPING DISCOUNT SYSTEM

'''
##ACCEPT TOTAL_PURCHASE AMOUNT IF
##TOTAL_PURCHASE >=5000 PRINT DISCOUNT MESSAGE OF 15%
##TOTAL_PURCHASE >=2000 PRINT DISCOUNT MESSAGE OF 10%
##TOTAL_PURCHASE >=10000 PRINT DISCOUNT MESSAGE OF 20% 
##OTHERWISE PRINT DISCOUNT NOT AVAIABLE
'''

total_pur = int(input("Enter the Purchase Amount:"))
if(total_pur >=10000):
    print("You got Discount of 20%")
elif(total_pur>=5000):
    print("You got Discount of 15%")
elif(total_pur>=2000):
    print("You got Discount of 10%")
else:
    print("Sorry, You are Not Eligible for Any Discount.")
'''



#EXAMPLE 4: TEMPERATURE BASED CLOTHING SUGGESTION
'''
IF TEMP<10 PRINT "WEAT THICK JACKET"
IF TEMP<20 PRINT "WEAR A SWEATER"
IF TEMP<30 PRINT "Wear Normal Clothes"
if temp> 40 print "High Alear! stay hydrated"
else print "it's hot wear cotton cloths"

'''

temp = int(input("Enter the Temperature:"))
if (temp<10):
    print("Wear Thick Jacket")
elif (temp<20):
    print("Wear A Sweater")
elif (temp<30):
    print("Normal Clothes are Allowed")
elif (temp>40):
    print("High Alear! stay hydrated")
else:
    print("it's hot wear cotton cloths")









    







