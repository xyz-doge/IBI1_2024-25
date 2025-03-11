a = 15 #   the walk time to the bus stop 
b = 75 #   bus journey time in minutes
c = a + b #total commute time for the bus method
d = 90 #   the driving time in minutes
e = 5 #    the walking time from the car park in minutes
f = d + e #the total commute time for the car-based method
print("Total time for walking + bus:", c, "minutes")
print("Total time for driving + walking:", f, "minutes")#  Print the total times for both methods
if c < f:
    print("Walking to the bus stop and taking the bus is quicker.")
elif c > f:
    print("Driving to the car park and then walking is quicker.")
else:
    print("Both commuting methods take the same time.")#  Compare the total time (c and f) to decide which method is faster

X = True
Y = False    #    Define Boolean variables
W = X and Y #     Define W as the logical AND of X and Y
print("X:", X)
print("Y:", Y)
print("W (X and Y):", W) 

# Truth table for (X and Y):
#------------------------------------------
# X       Y       X and Y
# True    True    True
# True    False   False
# False   True    False
# False   False   False