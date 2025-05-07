import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体（适用于 Windows）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 时间轴
t = np.linspace(0, 20, 2000)
tension = np.zeros_like(t)

# 构造张力数据
idx1 = (t >= 0) & (t < 5)
tension[idx1] = np.linspace(40, 70, idx1.sum())

idx2 = (t >= 5) & (t < 7)
tension[idx2] = 70 + 5 * np.sin(2 * np.pi * 10 * t[idx2])

idx3 = (t >= 7) & (t < 9)
tension[idx3] = np.linspace(70, 40, idx3.sum())

idx4 = (t >= 9) & (t < 16)
steps = np.linspace(40, 70, 5)
segment_len = idx4.sum() // 5
for i in range(5):
    start = idx4.nonzero()[0][0] + i * segment_len
    end = start + segment_len
    tension[start:end] = steps[i]

idx5 = (t >= 16) & (t <= 20)
tension[idx5] = 70 + 4 * np.sin(2 * np.pi * 1.5 * t[idx5]) + np.random.randn(idx5.sum())

# 绘图
plt.figure(figsize=(12, 6))
plt.plot(t, tension, label='张力传感器数据', color='steelblue')

# 注释（避免遮挡数据，放在空白区域）
plt.text(0.5, 57, '正常加速起吊', fontsize=12)
plt.text(4.5, 61, '集装箱摇摆导致共振', fontsize=12)
plt.text(4.5, 50, '吊具与集装箱短暂脱钩', fontsize=12)
plt.text(10.5, 58, '分段式载荷补偿', fontsize=12)
plt.text(17, 62, '海风扰动', fontsize=12)

# 图形美化

plt.xlabel('时间（秒）', fontsize=12)
plt.ylabel('张力（kN）', fontsize=12)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('STS_tension_case2_labeled.svg', format='svg', dpi=300)
plt.show()
