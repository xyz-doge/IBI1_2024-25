#  Import the required function library
import os
import pandas as pd
import matplotlib.pyplot as plt
#  Read CSV files from the same folder
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(10)) 
print(dalys_data.iloc[0:10, 2])  #  The 10th year of data for Afghanistan is 1999
#  Find all records from 1990 using Boolean conditions
data1990 = dalys_data[dalys_data["Year"] == 1990]
print(data1990.head())
#  Extract data from the UK and France
uk = dalys_data[dalys_data["Entity"] == "United Kingdom"]
france = dalys_data[dalys_data["Entity"] == "France"]
#  Calculate and compare the average values of the UK and France
uk_mean = uk["DALYs"].mean()
france_mean = france["DALYs"].mean()
print("Average DALYs in UK:", uk_mean)
print("Average DALYs in France:", france_mean) #  UK's DALYs are higher
#  Draw a graph of DALYs over time in the UK
plt.plot(uk["Year"], uk["DALYs"], 'b')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("UK DALYs Over Time")
plt.tight_layout()
plt.show()
#  My thinking question: Exploring DALYs in China
china = dalys_data[dalys_data["Entity"] == "China"]
plt.plot(china["Year"], china["DALYs"], 'r-')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("China DALYs Over Time")
plt.tight_layout()
plt.show()
