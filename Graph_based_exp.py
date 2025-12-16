#DATA RELATED - NUMPY
#GRAPH - MATPLOTLIB
'''
import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.random(100)*200
y_data = np.random.random(100)*200

plt.scatter(x_data,y_data,c="Green",marker="*",aplha = 0.3)
plt.show()
'''

#CASE STUDY - Anaylze the weight from year 2006 to 2021
'''
import numpy as np
import matplotlib.pyplot as plt
years = [2006 + x for x in range(16)]
weights=[28,50,65,55,34,78,66,80,45,86,87,45,55,47,78,65]

print(years)
plt.plot(years,weights,c="r",lw=3)
plt.title("Weight vs Years")
plt.xlabel("Years")
plt.ylabel("Weight")

plt.show()
'''

#CASE STUDY 1- Sales Trend Analysis

#A retail store recorded monthly sales for the year and wants to
#visualze trends.

'''
Jan - dex sales (in Rs. thonsands)
45,52,47,58,65,70,68,75,72,80,85,90

Q1. Use Numpy to store the data and create a Matplotlib line ploting montly sales.
Label months on the X-axis.
'''
'''
import numpy as np

import matplotlib.pyplot as plt

#Data
sales = np.array([45,52,47,58,65,70,68,75,72,80,85,90])
month = np.arange(1,13)

#Plot
plt.plot(month,sales,marker="o")
plt.title("Monthly Sales Trends (2025)")
plt.xlabel("Month")
plt.ylabel("Sales(Rs. in thousands)")
plt.grid(True)
plt.show()
'''

#CASE STUDY 2 - Students's Performance Distribution
'''
A teacher wants to analyze how students scored in a test.
Svores of 40 Students (0-100)
'''

import numpy as np
import matplotlib.pyplot as plt

scores = np.random.randint(40,100,40) #40 and 100 are start and end point that are included and 40 is the how many values we needed.
student = np.arange(1,41)
# markers = *, o,8,1,+,s,
plt.scatter(student,scores,marker ="o")    #(x_Data,y_Data,marker,aplha(makes the overlapped points different shades (0-1)))
plt.title("Student Peformance Distribution")
plt.xlabel("Student Number")
plt.ylabel("Scores")
plt.grid(True)
plt.show()



#CASE STUDY - Record product,pr_price and unit_sold
#plot scatter diagram pr_price vs unit_Sold (in thousands)

'''
import numpy as np
import matplotlib.pyplot as plt

product =["Samsung","Iphone","One Plus","Oppo","Vivo"]
pr_price =[20000,50000,25000,12000,15000]
unit_sold = [100,50,70,200,150]

plt.scatter(pr_price,unit_sold,marker="o")
plt.title("Mobile Price vs Unit Sold")
plt.xlabel("Price")
plt.ylabel("Units (In Thousands)")
plt.grid(True)
plt.show()
'''

#CASE STUDY 3: Temperature Comparison
'''
Two cities want to compare their temperature changes 12 Months

City A: 25,27,30,33,35,34,32,31,30,29,27,26
City B: 18,20,23,28,30,33,34,29,25,21,19,13
'''
'''
import numpy as np
import matplotlib.pyplot as plt

a = np.array([25,27,30,33,35,34,32,31,30,29,27,26])
b = np.array([18,20,23,28,30,33,34,29,25,21,19,13])
months = np.arange(1,13)

plt.plot(months,a,marker="o",label="City A")
plt.plot(months,b,marker="s",label="City B")

plt.title("Temperature Comparison Between City A and B")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
'''


#CASE STUDY 4: Productivity Tracker
'''
A company wants to compare planned vs Acutal production for a week

Planned Units = 120,130,125,140,135,150,155
Acutal Units = 110,125,128,138,130,148,160
'''
'''
import numpy as np
import matplotlib.pyplot as plt

pl_unit = np.array([120,130,125,140,135,150,155])
ac_unit = np.array([110,125,128,138,130,148,160])
#week = np.arange(1,8)
week = ["Mon","Tues","Wed","Thru","Fri","Sat","Sun"]

plt.plot(week,pl_unit,marker="o",label ="Planned Units")
plt.plot(week,ac_unit,marker="s",label="Acutal Unit")
plt.title("Planned Unit Vs Acutal Unit Tracker")
plt.xlabel("week")
plt.ylabel("Units")
plt.grid(True)
plt.legend()
plt.show()
'''


#CASE STUDY 6: Hosptial Patients Monitoring

'''
A hospital tracks the heart rate (in BPM) of a patient every hour
Heart rate:
72,75,70,68,65,64,66,70,74,78,82,85,88,90,92,94,96,95,92,88,84,80,76,72
'''
'''
import numpy as np
import matplotlib.pyplot as plt

h_rate = np.array([72,75,70,68,65,64,66,70,74,78,82,85,88,90,92,94,96,95,92,88,84,80,76,72])
hours = np.arange(1,25)

plt.plot(hours,h_rate,marker="o")
plt.scatter(hours,h_rate)
plt.title("Heart Rate Monitoring")
plt.xlabel("Hours")
plt.ylabel("Heart Rate (in BPM)")
plt.grid(True)
plt.show()
'''
