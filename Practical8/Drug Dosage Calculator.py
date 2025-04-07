#    Allow users to output
weight = float(input("Please enter your weight (kg):"))
concentration = input("Please enter the drug concentration (120 mg/5ml or 250 mg/5ml):")
#    Define function name
def dosage_calculator(weight, concentration):
    if weight < 10 or weight > 100:
        return "Error: Weight must be between 10kg and 100kg"# Adding weight restrictions
    if concentration == "120 mg/5ml":
        return round(weight * 15 / (120 / 5), 2)
    elif concentration == "250 mg/5ml":
         return round(weight * 15 / (250 / 5), 2)
    else:
        return "drug concentration error"        #  Limit the concentration of other drugs        
#   Output the final required result
print("required dose (ml):", dosage_calculator(weight, concentration))