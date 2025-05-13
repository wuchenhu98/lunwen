import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from scipy.fft import fft, fftfreq, ifft

# 设置中文字体
rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置为支持中文的字体（例如 SimHei）
rcParams['axes.unicode_minus'] = False  # 解决负号显示为方框的问题
rcParams['svg.fonttype'] = 'none'  # 保持字体为文本而非路径

# 增加时间序列的密度
N = 5000  # 增大 N 让每个周期有更多的数据点
T = 2 * np.pi
t = np.linspace(0, T, N, endpoint=False)
dt = t[1] - t[0]
y = np.sin(t) + np.sin(2*t) + np.sin(3*t)

# 傅里叶变换
yf = fft(y)
xf = fftfreq(N, d=dt)  # 对应频率（Hz）

# 找出每个成分所在的索引
def get_component_ifft(yf, xf, target_idx):
    """ 保留指定频率的正负对称分量 """
    component = np.zeros_like(yf, dtype=complex)
    component[target_idx] = yf[target_idx]
    component[-target_idx] = yf[-target_idx]  # 保留共轭对称分量
    return ifft(component).real

# 查找目标频率在 xf 中对应的索引
freq_unit = 1 / T
index_1 = np.argmin(np.abs(xf - freq_unit * 1))
index_2 = np.argmin(np.abs(xf - freq_unit * 2))
index_3 = np.argmin(np.abs(xf - freq_unit * 3))

# 提取各分量
y1 = get_component_ifft(yf, xf, index_1)
y2 = get_component_ifft(yf, xf, index_2)
y3 = get_component_ifft(yf, xf, index_3)

# 绘图
fig, axs = plt.subplots(4, 1, figsize=(10, 8), sharex=True)

axs[0].plot(t, y, label='sin(t) + sin(2t) + sin(3t)')
axs[0].set_title('原始信号')
axs[0].legend()

axs[1].plot(t, y1, label='sin(t)', color='r')
axs[1].set_title('频率成分: sin(t)')
axs[1].legend()

axs[2].plot(t, y2, label='sin(2t)', color='g')
axs[2].set_title('频率成分: sin(2t)')
axs[2].legend()

axs[3].plot(t, y3, label='sin(3t)', color='b')
axs[3].set_title('频率成分: sin(3t)')
axs[3].legend()

plt.xlabel('时间 (t)')
plt.tight_layout()
plt.savefig("fourier_decomposition.svg", format='svg')
plt.show()
