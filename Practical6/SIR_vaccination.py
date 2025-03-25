import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
vaccination_rates = [i / 10 for i in range(11)]  # 0.0 到 1.0，共11个值
plt.figure(figsize=(6, 4), dpi=150) 
for rate in vaccination_rates:
    N = 10000
    beta = 0.3       #患病概率
    gamma = 0.05     #康复率
    V = int(N * rate)
    S = N - V - 1      #易感染的人（除去第一个感染者）
    S_list = [S]
    if S < 0:
        continue  
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
    plt.plot(I_list, label=str(int(rate * 100)) + "%")       
plt.xlabel("Time")
plt.ylabel("Number of individuals")
plt.title("SIR Model with Vaccination")
plt.legend(title="Vaccinated Rate")
plt.savefig("sir_vaccination_basic.png")  # 可保存为文件
plt.show()