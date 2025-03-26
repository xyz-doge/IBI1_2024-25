import numpy as np
import matplotlib.pyplot as plt # Fetch the required library
population = np.zeros((100, 100), dtype=int)#   Created map with all initial status 0 (health)
# Pick a random point as the initial infected person and its x and y coordinates
outbreak = np.random.choice(range(100), 2)
x = outbreak[0]
y = outbreak[1]
population[x][y] = 1
beta = 0.3     # Probability of being infected by someone nearby
gamma = 0.05   # Probability of recovery
# Create image window and set its data
plt.figure(figsize=(6, 4), dpi=150)
# Show an image of the initial state
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Time = 0")   
#plt.savefig("spatial_t0.png")  # Save the image as a file, but add # in front of the code to avoid duplicate saving
plt.show()
# Propagate simulation for 100 rounds
for t in range(1, 101):
    new_population = population.copy()  # Prevents changes to the original image from causing confusion
# Find the locations of all currently infected people and return the x and y coordinates
    infected_x, infected_y = np.where(population == 1)
    for k in range(len(infected_x)):
        i = infected_x[k]
        j = infected_y[k]
# start infection
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip yourself
                ni = i + dx
                nj = j + dy

                # Don't let the coordinates exceed the canvas limit
                if 0 <= ni < 100 and 0 <= nj < 100:
                    if population[ni][nj] == 0:
                        # Simulation of infection with probability comparison
                        r = np.random.rand()  
                        if r < beta:
                            new_population[ni][nj] = 1  

        # Simulate rehabilitation with probability comparison
        if np.random.rand() < gamma:
            new_population[i][j] = 2 

    # update the map state
    population = new_population
    # Draw at the time node required by guidance
    if t in [10, 50, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title("Time = " + str(t))
        #plt.savefig("spatial_t" + str(t) + ".png") # same as above
        plt.show()
