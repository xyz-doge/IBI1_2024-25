import numpy as np
import matplotlib.pyplot as plt  # Fetch the required library
N = 10000       #    Total number of people
beta = 0.3      #    Probability of disease
gamma = 0.05    #    Probability of recovery
S = N - 1       #    Vulnerable persons (excluding the first infected person)
S_list = [S]
I = 1           #    People who are initially infected
I_list = [I]         
R = 0           #    The recovered person
R_list = [R]
#  Start the loop
for t in range(1000): 
        infection_probability = beta * (I / N) # Calculating the rate of infection
        # Using probability to simulate the course of infection and recovery
        new_infections = np.random.choice(range(2), size=S, p=[1 - infection_probability, infection_probability])
        num_new_infections = np.sum(new_infections)
        recoveries = np.random.choice(range(2), size=I, p=[1 - gamma, gamma])
        num_recoveries = np.sum(recoveries)
        # Update the numbers of the three groups
        S -= num_new_infections
        I += num_new_infections - num_recoveries
        R += num_recoveries
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
#  Set image parameters and output
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel("Time")
plt.ylabel("Number of individuals")
plt.title("Stochastic SIR Model")
plt.legend()
plt.savefig("sir_plot.png")  #  Save the image as a file, but add # in front of the code to avoid duplicate saving
plt.show()

# Pseudocode
# 1. Initialize the model:
#       Set total population, infection rate, recovery rate
#       Initial state: most of them are susceptible, a small number of infected people, and no recovery
#       Create a list to record the number of S, I, and R in each time step
# 2. Cyclic simulation of disease transmission:
#       Calculate the infection probability based on the current proportion of infected persons
#       Simulate how many of the susceptible people are infected
#       Simulate how many of those infected recovered
#       Update the number of S, I, and R
#       Record the current status
# 3. Drawing display:
#       Plot the trend of S, I and R over time as a line graph