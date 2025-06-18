import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.ticker as ticker

# 设置中文字体
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['axes.unicode_minus'] = False

# 历史时间窗口和F1-Score 数据git
x_labels = ["8", "16", "32", "64","128"]
data = {
    "MSL":         [82.35, 86.71, 90.02, 87.19, 83.51],
    "SWaT":        [87.35, 91.48, 87.52, 84.37, 81.97],
    "WADI":        [83.71, 88.63, 94.58, 94.87, 90.25],
    "港口数据集1": [81.72, 86.28, 89.97, 87.45, 82.64],
    "港口数据集2": [80.42, 84.85, 90.88, 88.59, 85.26]
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

    # 在每个柱子上方添加对应的数值标签
    for xi, yi in zip(x + offset, scores):
        ax.text(xi, yi + 1, f"{yi:.2f}", ha='center', va='bottom', fontsize=10)

    # 绘制每组柱子的中点折线
    # ax.plot(x + offset, scores, marker='o', color=colors[i], linestyle='-', linewidth=2, markersize=6)

# 坐标轴设置
ax.set_xlabel("局部图结构时间序列片段大小", fontsize=14)
ax.set_ylabel("F1-Score", fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(x_labels, fontsize=12)
ax.tick_params(axis='y', labelsize=12)
ax.set_ylim(50, 100)
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))

# ax.legend(fontsize=12)
ax.legend(fontsize=8, ncol=2, loc='upper right', bbox_to_anchor=(1.0, 1.0))

# 保存并显示图表
plt.tight_layout()
plt.savefig("f1_score_history_window_bar_line_chart_individual.svg", format='svg')
plt.show()
