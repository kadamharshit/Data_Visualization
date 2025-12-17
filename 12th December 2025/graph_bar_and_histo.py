#Graph based 

#bar graph - uncontinous/discontinous
#histogram - continous


#CASE STUDY 1: Sports Popularity Analysis

'''
sports : Football, Cricket, BasketBall, Badminton
count: 10,34,16,6
plot of barchart to know interest of people about space
'''
'''
import numpy as np
import matplotlib.pyplot as plt


sport= np.array(['Football', 'Cricket', 'BasketBall', 'Badminton'])
count = np.array([10,34,16,6])

plt.figure(figsize=(8,6))    #plots graph based on width and height in inches
plt.bar(sport,count,color ="yellow")
plt.title("Sports Popularity Analysis (Bar Chart)")
plt.xlabel("Sports")
plt.ylabel("Count")
plt.show()
'''
#Analysis is done = No. of population (no.of samples) is must

#CASE STUDY 2: Analysis on Rice

'''
How many People opt for which particular rice

Category: 'Indrayani','Wada Kolam', 'Basmati','Surti Kolam','Mogara','Ukdama'
Count: 57,90,54,78,35,20

'''
'''
import numpy as np
import matplotlib.pyplot as plt

category = np.array(['Indrayani','Wada Kolam', 'Basmati','Surti Kolam','Mogara','Ukdama'])
count = np.array([57,90,54,78,35,20])


plt.figure(figsize=(10,5))
plt.bar(category,count,color="Blue")
plt.title("Rice Analysis (Bar Graph)")
plt.xlabel("Rice")
plt.ylabel("No. of People")
plt.grid(True)
plt.show()
'''


#HISTOGRAPH - FOR CONTINOUS DATA (NO SPACE IN THE BARS)

#FUNCTION AND

#CASE STUDY : OBSERVATION OF MATHEMATICS SCORE FOR 30 STUDENTS.
#PLOT HISTOGRAM BASED ON SCORE PINS - HOW MANY BARS WE WANT,
'''
import numpy as np
import matplotlib.pyplot as plt

#records scores
scores = [
    45,67,34,56,78,12,34,56,34,12,
    12,57,89,56,99,23,45,67,45,76,
    45,12,45,56,75,34,66,87,23,100
    ]
# plt.figure(figsize=(10,5))
plt.hist(scores,bins= [0,10,20,30,40,50,60,70,80,90,100],color="teal",edgecolor="black")
plt.title("ANALYSIS ON SCORES OF 30 STUDENTS")
plt.xlabel("Score Range")
plt.ylabel("No. of Studnets")
plt.show()
'''

#CASE STUDY : SALES COMPARSION OF PRODUCTS.

'''
A company sales 5 products: 'Laptop','Mobile,'Tablet','Smart-Watch','TV'
Their Quaterly sales (in units) are : 150,300,180,120,140
Create Bar Graph.
'''
'''
import numpy as np
import matplotlib.pyplot as plt

product = np.array(['Laptop','Mobile','Tablet','Smart-Watch','TV'])
units = np.array([150,300,180,120,140])


plt.figure(figsize=(10,5))
plt.bar(product,units,color="Teal",edgecolor="Black")
plt.title("SALES COMPARSION OF PRODUCTS")
plt.xlabel("Products")
plt.ylabel("No. of Units Sold")
plt.show()
'''










