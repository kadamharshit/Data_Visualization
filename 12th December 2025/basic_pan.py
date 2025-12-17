#PANDAS - READ FILE FROM EXTERNAL SOURCE

#CREATE CSV TO ANALYSIS STUDENT PERFORMANCE DASHBOARD AND DATA
#THIS CSV CONTAINS STUDENT, SUBJECT (MATH, SCIENCE, ENGLISH)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\anudip\\marks.csv")


print(df.head()) #(preview the data)
df['Total'] = df['English'] + df['Maths'] + df['Science']
##df['Total'] = df['English'] + df['Maths'] + df['Science'].sum(axis=1) sum from begining
df['Average'] = df['Total']/3

df['Result'] = df['Average'].apply(lambda x: "pass" if x>50 else "fail")
#lambda - when we have to short the if else function
print("-------------Student Performance--------------")
print("Class Average:",df['Average'].mean())
print("Top Studnet:",df.loc[df['Total'].idxmax(),"Studnet"])
print("Lowest Scored Studnet:",df.loc[df['Total'].idxmin(),"Studnet"]) #idxmax - gives the row index of max value
plt.bar(df['Studnet'],df['Total'])
plt.title("Students Performance")
plt.xlabel("Students")
plt.ylabel("Total Marks")
plt.show()
