
#numeric data types

#1. int
x = 5
print("the data type is",type(x))

#2. float
y = 3.14
print("the data type is",type(y))

#3. complex
z = 5 +11j
print("the data type is",type(z))


#sequnce data type (string, tuple, list)

#1. String - collection of characters
s = "Saraswati College of Engineering"
print("the data type is",type(s))
print(s[5]) #inexing finding
print(s[-2])

#2. List - Collection of different data types in ordered sequences and is 
L1 = [1,2,3,"Harshit"]
print("my crate",L1)
L1[3]= "Hello" #HERE THE VALUE IS REPLACED WITH NEW VALUE

#3. Tuple  - modification not possible
my_library = ()
print(my_library)
my_library= (1,2,"Average")
print(my_library)
my_library [3] = "Bag" #once created cannot be modified
print(my_library)

