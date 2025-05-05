import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch, butter, filtfilt
from matplotlib.ticker import FuncFormatter

# 中文支持
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 参数设置
fs = 1000  # 采样频率（1000Hz）
t = np.linspace(0, 30, 30 * fs)
n = len(t)

# 正常信号
signal_normal = 0.05 * np.random.randn(n)
signal_normal -= np.mean(signal_normal)

# 带通滤波函数（195~205Hz）
def bandpass_noise(lowcut, highcut, fs, size):
    b, a = butter(4, [lowcut / (0.5 * fs), highcut / (0.5 * fs)], btype='band')
    noise = np.random.randn(size)
    return filtfilt(b, a, noise)

# 构造异常信号
signal_anomaly = signal_normal.copy()
anomaly_start = int(2 * fs)
anomaly_end = int(4 * fs)
anomaly_band = bandpass_noise(95, 105, fs, anomaly_end - anomaly_start)
signal_anomaly[anomaly_start:anomaly_end] += 0.5 * anomaly_band
signal_anomaly -= np.mean(signal_anomaly)

# 绘图
plt.figure(figsize=(14, 6))

# 时域图
plt.subplot(2, 1, 1)
plt.plot(t, signal_anomaly, color='blue')
plt.title("时域图")
plt.xlabel("时间（秒）")
plt.ylabel("振动幅值")
plt.xlim([0, 30])
plt.grid(True)

# 频域图
f, Pxx = welch(signal_anomaly, fs, nperseg=1024)
plt.subplot(2, 1, 2)
plt.semilogy(f, Pxx, color='red')
plt.title("频域图")
plt.xlabel("频率（Hz）")
plt.ylabel("功率谱密度") # ✅ 增加单位
plt.xlim([0, 250])

# ✅ 高亮 195~205Hz 区域
plt.axvspan(95, 105, color='lightcoral', alpha=0.3, label='异常频段')

# ✅ 自动标注 200Hz 附近最大峰值
mask = (f >= 95) & (f <= 105)
f_peak = f[mask][np.argmax(Pxx[mask])]
p_peak = np.max(Pxx[mask])
plt.annotate(f'峰值：{f_peak:.1f}Hz\n{p_peak:.1e}',
             xy=(f_peak, p_peak),
             xytext=(f_peak + 10, p_peak * 5),
             arrowprops=dict(arrowstyle='->', color='black'),
             fontsize=10, color='black')

# ✅ 科学计数法修正
def sci_notation_formatter(x, _):
    s = f'{x:.0e}'
    base, exp = s.split('e')
    exp = exp.lstrip('+0') if exp.startswith('+') else exp.lstrip('0')
    return f'{base}e{exp}'

formatter = FuncFormatter(sci_notation_formatter)
plt.gca().yaxis.set_major_formatter(formatter)
plt.ylim([1e-8, 1e-2])
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("vibration_200hz_peak_highlighted.svg", format="svg")
plt.show()
