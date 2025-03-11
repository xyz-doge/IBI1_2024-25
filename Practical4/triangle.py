# Pseudocode:
# 1. The loop from n = 1 to 10.
# 2. For each n, the trigonometric number is calculated using the formula: T = n*(n+1)/2.
# 3. Print out the number of each triangle.
for n in range(1, 11):#                   n goes from 1 to 10
    triangular_number = n * (n + 1) / 2#  Calculate the nth triangular number using the formula
    print("T", n, "=", triangular_number)# Print the result