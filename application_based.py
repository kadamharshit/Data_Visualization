#INVERTORY MANAGEMENT SYSTEM

#CASE STUDY:
'''
MANAGE PRODUCT STOCK AND CALCULATE TOTAL INVENTORY VALUE.
LIST - STORE THE PRODUCT
'''

'''
products =["Apple","Orange","Banana","Grapes","Mango","Kiwi","Jack Fruit","Dragon Fruit"]
quantity = [0,10,35,00,46,10,28,68]
price=[50,30,30,20,90,60,40,90]

total_value =0

for i in range(len(products)):
    investment = quantity[i]*price[i]
    #print("Cost of product",products[i],"is:",quantity[i]*price[i])
    print("Cost of product",products[i],"is:",investment)
    total_value += investment
    

print("The Total Inventory Cost is:",total_value)
print("OUT OF STOCK PRODUCTS")
#if qty - 0, print outof stock
for i in range(len(products)):
    if (quantity[i] == 0):
        print("Product",products[i],"is Out of Stock!!!")
'''

#CASE STUDY: Calculate employee salary based on attendance and daily wages/day
'''
emp = ['Ramesh','Vihas','Sahil','Prasad','Harsh']
attend =[15,20,18,16,10]
wages = [1000,2000,500,700,800]
total_sal=0
for i in range(len(emp)):
    sal = attend[i] *wages[i]
    print("Total Salary of",emp[i],"is ₹",sal,"As they have attended",attend[i],"days")

'''

#CASE STUDY: SHOPPING CART SYSTEM
'''
1) ADD FIVE ITEMS TO THE CART AND STORE COST OF EACH PRODUCT
2) CALCULATE TOTAL_BIL
3) IF (TOTAL_BIL) IS GREATER THAN 2000 GIVE 10% OF DISCOUNT ON TOTLA_BIL
4) PRINT FINAL_BILL
'''
'''
product = ["T-Shirt","Jeans","Cap","Shocks","Shoes"]
qty =[5,2,5,2,5]
price =[200,500,50,50,800]
total_bill = 0
for i in range (len(product)):
    total_bill += qty[i]*price[i]

##print("The total bill is",total_bill)

if (total_bill > 2000):
    final_bill = total_bill *(10/100)
    print("The final Bill with discount is:",total_bill - final_bill)
else:
    print("The total bill is",total_bill)
'''






#CASE STUDY
'''
DAILY TEMPERATURE TRACKER

1) FIND THE HOTTEST AND COLDEST DAY
2) AVERAGE OF TEMPERATURE
3) LIST DATS WHERE TEMP> AVERGAE)
'''
'''
temp = [30,40,33,28,36,36,38]

avg=sum(temp)/len(temp)

above_avg =[]
for i in temp:
    if i >avg:
        above_avg.append(i)
print("Average temperature is:",avg)
print("Hottest Days:",max(temp))
print("Coldest Days:",min(temp))
print("Above Average:",above_avg)
'''



#salary_slip Generator
'''
Store monthly salaries of employees in list.
a) if salary <20000 then add 15% increment
b) display updated salary adn total payroll
'''
'''
sal = [10000,40000,30000,15000,19000]
updated_sal = []

for s in sal:
    if (s<20000):
        s += s*0.15
    updated_sal.append(s)
print("Updated Salaries:",updated_sal)
print("Total PayRoll:",sum(updated_sal))
'''             



