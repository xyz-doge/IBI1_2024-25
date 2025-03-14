#   Pseudocode:
#   Store a person's weight(kg)in a variable weight and their height(m) in a variable height.
#   Then calculate BMI using the formula BMI = weight/(height ** 2).
#   Use conditional statements to classify BMI:
# - If BMI > 30, consider the person "obese";
# - If BMI < 18.5, consider the person "underweight";
# - Otherwise, the person is considered to be in the "normal" range.
#   Output, which contains the calculated BMI and corresponding health class.
weight = float(input('How many kilograms do you weigh？') ) 
height = float(input('What is your height in meters?'))# get data
bmi = weight / (height ** 2) # Calculate BMI using the formula 
if bmi > 30:
    category = "Obese"
elif bmi < 18.5:
    category = "Underweight"
else:
    category = "Normal" # Determine the BMI category based on the calculated BMI value
print(f"The person's BMI is {bmi} and he/she is {category}.")# result