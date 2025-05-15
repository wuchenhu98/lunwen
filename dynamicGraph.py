import matplotlib.pyplot as plt
import numpy as np

# 时间轴划分
segments = 6
segment_len = 100
total_len = segments * segment_len
time = np.arange(total_len)
segment_centers = [segment_len * (i + 0.5) for i in range(segments)]

# 初始化三个变量序列
x1 = np.zeros(total_len)
x2 = np.zeros(total_len)
x3 = np.zeros(total_len)

# 为每段定义不同的依赖结构
for i in range(segments):
    start = i * segment_len
    end = (i + 1) * segment_len
    t = np.linspace(0, 2 * np.pi, segment_len)

    if i in [0, 3, 4]:  # G₁: 无依赖，三条曲线趋势不同
        x1[start:end] = np.sin(t) + 0.1 * np.random.randn(segment_len)
        x2[start:end] = np.cos(t) + 0.1 * np.random.randn(segment_len)
        x3[start:end] = np.sin(2 * t) + 0.1 * np.random.randn(segment_len)

    elif i in [1, 2]:  # G₂: x₂ 与 x₃ 相关，x₁ 独立
        shared = np.sin(t) + 0.1 * np.random.randn(segment_len)
        x1[start:end] = np.cos(2 * t) + 0.1 * np.random.randn(segment_len)
        x2[start:end] = shared
        x3[start:end] = shared + 0.05 * np.random.randn(segment_len)

    elif i == 5:  # G₃: x₁ 与 x₂ 相关，x₃ 独立
        shared = np.cos(t) + 0.1 * np.random.randn(segment_len)
        x1[start:end] = shared
        x2[start:end] = shared + 0.05 * np.random.randn(segment_len)
        x3[start:end] = np.sin(2 * t) + 0.1 * np.random.randn(segment_len)

# 创建子图
fig, axs = plt.subplots(3, 1, figsize=(12, 5), sharex=True)

# 绘制曲线
axs[0].plot(time, x1, color='blue')
axs[1].plot(time, x2, color='blue')
axs[2].plot(time, x3, color='blue')

# 添加标签 x₁, x₂, x₃
axs[0].set_ylabel(r'$x_1$', fontsize=13)
axs[1].set_ylabel(r'$x_2$', fontsize=13)
axs[2].set_ylabel(r'$x_3$', fontsize=13)

# 添加垂直分割线和 G₁~G₃ 标签
G_labels = [r'$G_1$', r'$G_2$', r'$G_2$', r'$G_1$', r'$G_1$', r'$G_3$']
for i in range(1, segments):
    for ax in axs:
        ax.axvline(i * segment_len, color='black', linestyle='--', linewidth=1)

for i, center in enumerate(segment_centers):
    axs[0].annotate(G_labels[i],
                    xy=(center, 1.1), xycoords=('data', 'axes fraction'),
                    ha='center', va='bottom',
                    fontsize=13, fontweight='bold',
                    arrowprops=dict(arrowstyle='->'))

# 添加横坐标标签 t₁~t₆（在每段中心）
axs[2].set_xticks(segment_centers)
axs[2].set_xticklabels([r'$t_1$', r'$t_2$', r'$t_3$', r'$t_4$', r'$t_5$', r'$t_6$'], fontsize=12)


plt.tight_layout()
plt.savefig("temporal_dependency_corrected.svg", format='svg')
plt.show()
