uk_names = ["England", "Wales", "Northern Ireland", "Scotland"]
uk_populations = [57.11, 3.13, 1.91, 5.45]#              Create a list of the populations of each country in the UK
china_populations = [65.77, 41.88, 45.28, 61.27, 85.15]
china_names = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]# Create a list of populations in neighboring provinces of Zhejiang, China
sorted_uk_data = sorted(uk_populations)#             Sort the data for the UK
print("Sorted UK populations:", sorted_uk_data,'(million)')#     Output results
sorted_china_data = sorted(china_populations)#       Sort the Chinese data
print("Sorted China populations:", sorted_china_data,'(million)')#Output results
import matplotlib.pyplot as plt #                     Give the required functions
plt.pie(uk_populations, labels=uk_names,autopct='%.2f%%')# Plot the data image for the UK
plt.axis('equal')#                                    Make sure the image is circular
plt.show()  #                                         Output image                                                                    
plt.pie(china_populations, labels=china_names,autopct='%.2f%%')#Plot the data image for china
plt.axis('equal')#                                    Make sure the image is circular
plt.show()       #                                    Output image

# Pseudocode
# Defines a list of names that defines the countries of the United Kingdom
# Define corresponding UK population data (in millions)
# Defines a list of names for Zhejiang, China and neighboring provinces
# Sort the list of UK populations and save it as a new sorted list
# Prints the sorted population of the United Kingdom in millions
# Same for China data manipulation
# Import the plotting library matplotlib.pyplot and name it plt for plotting
# Plot a pie chart of the population distribution in the United Kingdom, labeled with country names and percentages with two decimal places
# Sets the shape to be an equal scale circle 
# Display the UK population pie chart
# Do the same for the Chinese data
