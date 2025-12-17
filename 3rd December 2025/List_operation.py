
#create shopping cart with six items and perform basic operations on list

my_cart = ["Apple","Banana","Orange","Kiwi","Butter","Bread"]
print("the shopping cart has this items",my_cart)
print(len(my_cart))
my_cart.append("Chips")
print("New List is:",my_cart)
my_cart.remove("Butter")
print("Removed butter list is:",my_cart)

#Create to-do list of your daily operation adn perform list operation

todo = ['Study','Coding','Cooking','Cleaning']
print("My TODO List is:",todo)
print("the length of todo list is:",len(todo))
todo.append("Reading")
print("New Todo list is:",todo)
todo.remove("Cleaning")
print("New Todo List is:",todo)


#create a list of marks of student and find sum and average of it.

marks=[78,98,89.80]
total =sum(marks)
print("Total marks:",total)
avg=total/len(marks)
print("Average of marks:",avg)




