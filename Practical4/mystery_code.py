# What does this piece of code do?
# Answer: This code simulates rolling two dice until the result is the same, and then prints the total number of rolls.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0#                      Initialize the progress counter to 0 to keep track of the number of dice rolls
while progress>=0:#              The loop continues while progress is greater than or equal to 0
	progress+=1#                 At the beginning of each loop, the progress counter is incremented by 1
	first_n = randint(1,6)#      Generate the first random number, from 1 to 6, to simulate the result of the first dice roll
	second_n = randint(1,6)#     Generate a second random number, in the range 1 to 6, to simulate the result of a second dice roll
	if first_n == second_n:#     Determine whether two dice rolls give the same result
		print(progress)#         If it's the same, print the current loop count, which is the number of times it takes to roll the dice until it's the same
		break#                   Exit the loop, ending the program

