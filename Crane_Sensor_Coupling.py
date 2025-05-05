import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子以确保结果可重复
np.random.seed(42)

# 生成时间序列
time = np.linspace(0, 100, 500)

# 模拟液压压力、电机电流、振动幅度、油温、冷却水流量之间的正相关性
hydraulic_pressure = np.sin(time) + 0.5 * np.random.normal(size=time.shape)
motor_current = hydraulic_pressure + 0.1 * np.random.normal(size=time.shape)
vibration_amplitude = hydraulic_pressure + 0.2 * np.random.normal(size=time.shape)
oil_temperature = hydraulic_pressure + 0.3 * np.random.normal(size=time.shape)
cooling_water_flow = hydraulic_pressure + 0.4 * np.random.normal(size=time.shape)

# 模拟钢丝绳张力与其他变量的负相关性
steel_rope_tension = -hydraulic_pressure + 0.5 * np.random.normal(size=time.shape)

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制各个数据曲线
plt.plot(time, hydraulic_pressure, label="Hydraulic Pressure", color='b')
plt.plot(time, motor_current, label="Motor Current", color='g')
plt.plot(time, vibration_amplitude, label="Vibration Amplitude", color='r')
plt.plot(time, oil_temperature, label="Oil Temperature", color='c')
plt.plot(time, cooling_water_flow, label="Cooling Water Flow", color='m')
plt.plot(time, steel_rope_tension, label="Steel Rope Tension", color='k', linestyle='--')

# 设置标题和标签
plt.title("Correlation between Different Parameters")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()
