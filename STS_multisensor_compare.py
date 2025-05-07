import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 时间轴统一为 60 秒，采样频率各不相同
t_med = np.linspace(0, 60, 3000)    # 50Hz
t_low = np.linspace(0, 60, 1200)    # 20Hz
t_vib = np.linspace(0, 60, 60000)   # 1kHz
t_temp = np.linspace(0, 60, 60)     # 1Hz

# 钢丝绳张力（阶跃变化 + 异常骤降）
# tension = np.ones_like(t_med) * 100
# tension[500:700] += 50
# tension[1400:1500] = 30  # 异常骤降

# 液压压力（脉冲波动 + 延迟）
pressure = 10 + np.sin(0.3 * np.pi * t_low) + 0.5 * np.random.randn(len(t_low))
pressure[800:] = np.roll(pressure[800:], 50)  # 响应延迟模拟

# 三维振动（基线 + 高频 + 异常段特征突增）
vib = 0.2 * np.random.randn(len(t_vib)) + 0.5 * np.sin(2 * np.pi * 10 * t_vib)
vib[45000:47000] += 3 * np.sin(2 * np.pi * 200 * t_vib[45000:47000])  # 高频异常

# 红外温度（缓慢升高 + 异常快速升温）
temp = 30 + 0.05 * t_temp
temp[40:] += 0.2 * (t_temp[40:] - 40) ** 1.2  # 异常升温

# 绘图
fig, axs = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

# axs[0].plot(t_med, tension, color='green')
# axs[0].set_ylabel('张力 (kN)')
# axs[0].set_title('钢丝绳张力')

axs[0].plot(t_low, pressure, color='orange')
axs[0].set_ylabel('压力 (MPa)')
axs[0].set_title('液压压力')

axs[1].plot(t_vib[::50], vib[::50], color='purple')  # 下采样显示
axs[1].set_ylabel('加速度 (g)')
axs[1].set_title('三维振动')

axs[2].plot(t_temp, temp, color='red')
axs[2].set_ylabel('温度 (°C)')
axs[2].set_title('红外温度')
axs[2].set_xlabel('时间 (秒)')

plt.tight_layout()
plt.savefig("STS_multisensor_no_current.svg", dpi=300, format='svg')
plt.show()
