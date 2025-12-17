'''
###Use of tuple (immutable - cannot change)
##
##aadhar_details = ("Harshit",9172421038,"Male","07-10-2004")
##print("The Aadhar details are:",aadhar_details)
##aadhar_details[0]="Vihas"
##print("New Aadhar Details are:",aadhar_details)

#Example 2: Restaurant Menu

menu = [("Pav Bhaji",100,"Veg"),("Egg Omellete",60,"Non-Veg"),("Poha",30,"Veg")]
for item in menu:
    print(item)
'''

#CREATE TRANSACTION RECORD SYSTEM TO STORE TRANSACTION_ID,AMOUNT.TRANSACTION(DEBIT/CREDIT)

transaction = [("10001",5000,"Credit"),("10002",2500,"Debit"),("10003",1000,"Credit"),("10004",10000,"Credit")]


for i in transaction:
    print(i)

