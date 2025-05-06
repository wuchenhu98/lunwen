import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.ticker as ticker

# 设置中文字体
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['axes.unicode_minus'] = False

# 历史时间窗口和F1-Score 数据
x_labels = ["2", "4", "8", "2,4", "2,8", "2,16", "4,8", "2,4,8", "2,4,8,16"]
data = {
    "MSL":         [75.35, 76.12, 78.24, 80.15, 77.64, 72.18, 79.57, 84.28, 81.36],
    "SWaT":        [76.54, 77.19, 76.75, 79.08, 78.13, 71.48, 82.37, 80.75, 81.03],
    "WADI":        [71.84, 73.79, 75.59, 73.54, 74.38, 72.56, 78.52, 77.53, 82.19],
    "港口数据集1": [76.84, 76.32, 79.15, 82.57, 78.59, 75.62, 81.47, 88.46, 85.29],
    "港口数据集2": [74.59, 73.54, 76.02, 83.42, 80.12, 77.82, 80.18, 86.94, 83.23]
}

# 柱状图设置
bar_width = 0.15
x = np.arange(len(x_labels))
colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B3', '#CCB974']

# 创建图表
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制每组柱子并绘制折线连接每个数据集的中点
for i, (label, scores) in enumerate(data.items()):
    offset = (i - 2) * bar_width
    ax.bar(x + offset, scores, width=bar_width, label=label, color=colors[i])

    # 绘制每组柱子的中点折线
    ax.plot(x + offset, scores, marker='o', color=colors[i], linestyle='-', linewidth=2, markersize=6)

# 坐标轴设置
ax.set_xlabel("历史时间窗口", fontsize=14)
ax.set_ylabel("F1-Score", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(x_labels, fontsize=12)
ax.tick_params(axis='y', labelsize=12)
ax.set_ylim(50, 100)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax.legend(fontsize=12)

# 保存并显示图表
plt.tight_layout()
plt.savefig("f1_score_history_window_bar_line_chart_individual.svg", format='svg')
plt.show()
