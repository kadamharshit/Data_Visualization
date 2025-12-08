#Dictionary is a key - value paired data structure which starts with {}
'''
syntax :
d1 = {"e": 1,"r":2}
'''

'''
#Example 1: Student Profile System

student = {
    "name":"Harshit",
    "age":21,
    "course":"Information Technology"
    }
# Accessing values using key
print("Studnet name:",student["name"])
print("Studnet course:",student["course"])
'''

#Create new phone_book to store 5 friends contact.
'''
phone_book ={
    "Sahil": 9876543213,
    "Vihas":9876543212,
    "Harsh":9876543211,
    "Ram":9123456789,
    "Raj":9172421039
    }
#print(phone_book,end="\n")
phone_book['Vihas'] = 9876543216
print(phone_book['Vihas'])
print(phone_book.values())

for i in phone_book.values():
    print(i)
print(phone_book.keys())
'''


# Students marks management
'''
students ={
    101:78,
    102:85,
    103:79,
    104:85}

total = 0
for i in students.values():
    total += i

avg = total/len(students)
print("Students Marks:",students)
print("Average Marks:",avg)
'''



#Ecommerce billing system

cart={}
cart["Rice"] = 60
cart["sugar"]= 80
cart["Rice"] += 100
print("Cart:",cart)
print("Sum of Quantity:",sum(cart.values()))
