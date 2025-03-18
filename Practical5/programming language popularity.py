programming_languages_percentage = {'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}# Generating a dictionary
print(programming_languages_percentage)# Output dictionary content
languange_name = ['JavaScript', 'HTML', 'Python', 'SQL', 'TypeScript']# Defines a list of names
corresponding_percentage = [62.3, 52.9, 51.0, 51.0, 38.5]# Defines a list of percentages
import matplotlib.pyplot as plt #Give the required functions
plt.figure(figsize=(10, 6))# Determining the image size
plt.bar(x = languange_name, height = corresponding_percentage )# Define the horizontal and vertical labels
plt.title("Programming Language Popularity (2024)")# Defining an image title
plt.xlabel("Programming Languages")#                 Define the Y-axis name
plt.ylabel("Usage Percentage (%)")#                  Define the X-axis name
plt.show()#                                          Image output

# Pseudocode
#  Define a dictionary that holds the programming language and its usage
#  Print the contents of the dictionary
#  Define a list of language names and a list of usage rates, respectively
#  Import the required functions, matplotlib.pyplot
#  Sets the dimensions of the chart
#  Plot the bar graph with language name on the X-axis and usage on the Y-axis
#  Set the title of the chart to "Programming Language Popularity 2024"
#  Set the X-axis title to "Programming Language" and the Y-axis title to Usage Percentage (%)
#  Displaying the chart