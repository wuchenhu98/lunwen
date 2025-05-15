import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.ticker as ticker
import seaborn as sns
import pandas as pd

# 设置中文字体
matplotlib.rcParams['font.family'] = 'Microsoft YaHei'
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置绘图样式
sns.set(font_scale=1.0)
plt.style.use('seaborn-white')

# 定义混淆矩阵数据和标题
datasets = [
    ("SWaT", np.array([[5095, 664], [790, 47180]])),
    ("MSL", np.array([[4584, 218], [39383, 801]])),
    ("WaDI", np.array([[3278, 221], [53623, 153]])),
    ("港口数据集1", np.array([[4337, 341], [68292, 626]])),
    ("港口数据集2", np.array([[6675, 812], [78362, 526]]))
]

labels = ['Anomaly data', 'Normal data']

# 创建 2x3 子图
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten()  # 展平成1维数组便于索引

# 手动设置要绘图的位置索引
positions = [0, 1, 2, 3, 4]  # 使用前五个位置，第二行的两个图紧密放置

# 绘图
for pos, (title, conf_matrix) in zip(positions, datasets):
    df_cm = pd.DataFrame(conf_matrix, index=labels, columns=labels)
    sns.heatmap(df_cm, annot=True, fmt='d', cmap='Blues',
                cbar=True, xticklabels=labels, yticklabels=labels,
                linewidths=0.5, linecolor='gray', ax=axes[pos])
    axes[pos].set_xlabel('True Label')
    axes[pos].set_ylabel('Predicted Label')
    axes[pos].set_title(title)

# 隐藏第6个空图（index 5）
axes[5].axis('off')

# 自动布局 & 保存
plt.tight_layout()
plt.savefig("combined_confusion_matrices_no_gap_2x3.svg", format='svg')
plt.show()

