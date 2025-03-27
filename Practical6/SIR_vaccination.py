import numpy as np
import matplotlib.pyplot as plt # Fetch the required library
from matplotlib import cm
vaccination_rates = [i / 10 for i in range(11)]  # 0.0 to 1.0 with 11 values to construct different rates
plt.figure(figsize=(6, 4), dpi=150) 
for rate in vaccination_rates:
    N = 10000        # Total number of people
    beta = 0.3       # Probability of disease
    gamma = 0.05     # Probability of recovery 
    V = int(N * rate)
    S = N - V - 1    # 0.0 to 1.0 with 11 values to construct different rates
    if S < 0:
       S = 0         # Force a value of 0 to indicate no susceptible individuals (100% vaccinated).
    S_list = [S]
    I = 1            # People who are initially infected 
    I_list = [I]         
    R = 0            # The recovered person
    R_list = [R]
    #  Start the loop
    for t in range(1000): 
        infection_probability = beta * (I / N) # Calculating the rate of infection
        #   Probability is used to model the process of contagion and recovery
        new_infections = np.random.choice(range(2), size=S, p=[1 - infection_probability, infection_probability])
        num_new_infections = np.sum(new_infections)
        recoveries = np.random.choice(range(2), size=I, p=[1 - gamma, gamma])
        num_recoveries = np.sum(recoveries)
        #   The number of the three groups of people is updated
        S -= num_new_infections
        I += num_new_infections - num_recoveries
        R += num_recoveries
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
#   Set image parameters and output
    plt.plot(I_list, label=str(int(rate * 100)) + "%")       
plt.xlabel("Time")
plt.ylabel("Number of individuals")
plt.title("SIR Model with Vaccination")
plt.legend(title="Vaccinated Rate")
#plt.savefig("sir_vaccination_basic.png")   # Save the image as a file, but add # in front of the code to avoid duplicate saving
plt.show()

# Pseudocode
#  First, set a set of different vaccination rates (ranging from 0% to 100%, with intervals of every 10%)
#  For each vaccination rate, conduct a complete simulation:
#     Assuming the total population is fixed, set the infection rate and recovery rate of the disease
#     According to the vaccination rate, some people have been marked as "immune" in advance
#     Initial state: 1 person infected, the rest are uninfected susceptible individuals
#     Create a list to record the number of susceptible, infected, and recovered individuals at each time point
#  Then start the time loop:
#     Calculate the probability of infection based on the current number of infected individuals
#     Randomly determine how many susceptible individuals are infected
#     Randomly determine how many infected individuals will recover
#     Update the numbers of the three groups and record them
#  After this round of simulation is completed, draw the curve of the number of infected people's changes
#  After running all vaccination rates, draw the results on a single graph
#     Observe the differences in epidemic transmission under different vaccination rates