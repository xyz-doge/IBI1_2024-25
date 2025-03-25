import numpy as np
import matplotlib.pyplot as plt
N = 10000       #总人口
beta = 0.3       #患病概率
gamma = 0.05     #康复率
S = N - 1       #易感染的人（除去第一个感染者）
S_list = [S]
I = 1           #初始感染的人
I_list = [I]         
R = 0            #康复的人
R_list = [R]
for t in range(1000):
    infection_probability = beta * (I / N)
    new_infections = np.random.choice(range(2), size=S, p=[1 - infection_probability, infection_probability])
    num_new_infections = np.sum(new_infections)
    recoveries = np.random.choice(range(2), size=I, p=[1 - gamma, gamma])
    num_recoveries = np.sum(recoveries)
    S -= num_new_infections
    I += num_new_infections - num_recoveries
    R += num_recoveries
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel("Time")
plt.ylabel("Number of individuals")
plt.title("Stochastic SIR Model")
plt.legend()
plt.savefig("sir_plot.png")  # 可保存为文件
plt.show()


