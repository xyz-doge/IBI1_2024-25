import numpy as np
import matplotlib.pyplot as plt
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

# 显示初始状态，使用“viridis”颜色映射：紫=健康，绿色=感染，黄=康复
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Time = 0")   # 添加标题
#plt.savefig("spatial_t0.png")  # 保存图片为文件
plt.show()

# 传播模拟，共进行100轮
for t in range(1, 101):
    new_population = population.copy()  # 复制地图，防止修改原图导致混乱

    # 使用 np.where 找到当前所有感染者的位置
    # 它会返回两个数组，分别是所有感染者的 x 和 y 坐标
    infected_x, infected_y = np.where(population == 1)

    # 遍历所有感染者的位置
    for k in range(len(infected_x)):
        i = infected_x[k]
        j = infected_y[k]

        # 感染邻居（共8个方向）
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # 跳过自己
                ni = i + dx
                nj = j + dy

                # 检查边界，不让坐标越界
                if 0 <= ni < 100 and 0 <= nj < 100:
                    if population[ni][nj] == 0:
                        r = np.random.rand()  # 生成0~1之间的随机数
                        if r < beta:
                            new_population[ni][nj] = 1  # 邻居被感染

        # 感染者可能康复
        if np.random.rand() < gamma:
            new_population[i][j] = 2  # 康复（变为2）

    # 更新地图状态
    population = new_population

    # 在几个关键时间点绘图
    if t in [10, 50, 100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title("Time = " + str(t))
        #plt.savefig("spatial_t" + str(t) + ".png")
        plt.show()
