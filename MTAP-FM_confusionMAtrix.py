import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.gridspec as gridspec  # 用于更灵活的子图布局

# 解决方案1：使用字体文件（推荐）
font_path = 'C:/Windows/Fonts/msyh.ttc'  # 修改为你的实际字体路径
font_prop = mpl.font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False

# 设置绘图样式
sns.set(font_scale=1.5)
plt.style.use('seaborn-white')

# 定义混淆矩阵数据和标题
datasets = [
    ("SWaT", np.array([[4893, 867], [696, 47273]])),
    ("MSL", np.array([[4769, 616], [1165,38436]])),
    ("WaDI", np.array([[2820, 611], [507,53337]])),
    ("港口数据集1", np.array([[4473, 490], [676,67957]])),
    ("港口数据集2", np.array([[6363, 838], [1073,78101]]))
]

labels = ['Anomaly data', 'Normal data']

# 计算所有混淆矩阵的最大值和最小值
all_values = np.concatenate([conf_matrix.flatten() for _, conf_matrix in datasets])
vmin, vmax = np.min(all_values), np.max(all_values)



# 创建 2x3 的网格布局，但调整第2行的两个图均匀分布
fig = plt.figure(figsize=(18, 10))
gs = gridspec.GridSpec(2, 6)  # 2行6列，方便调整第2行的位置

# 第1行：3个子图（占据前3列）
ax1 = plt.subplot(gs[0, :2])  # 第1行第1-2列
ax2 = plt.subplot(gs[0, 2:4])  # 第1行第3-4列
ax3 = plt.subplot(gs[0, 4:6])  # 第1行第5-6列

# 第2行：2个子图均匀分布（居中）
ax4 = plt.subplot(gs[1, 1:3])  # 第2行第2-3列
ax5 = plt.subplot(gs[1, 3:5])  # 第2行第4-5列

# 绘图
axes = [ax1, ax2, ax3, ax4, ax5]  # 所有子图
for ax, (title, conf_matrix) in zip(axes, datasets):
    df_cm = pd.DataFrame(conf_matrix, index=labels, columns=labels)
    sns.heatmap(
        df_cm, annot=True, fmt='d', cmap='Reds', vmin=vmin, vmax=vmax,
        cbar=True, xticklabels=labels, yticklabels=labels,
        linewidths=0.5, linecolor='gray', ax=ax,annot_kws={'size': 18}
    )
    ax.set_xlabel('True Label', fontsize=20)
    ax.set_ylabel('Predicted Label', fontsize=20)
        # 设置坐标轴刻度标签字体大小
    ax.set_xticklabels(labels, fontsize=18)
    ax.set_yticklabels(labels, fontsize=18)
    ax.set_title(title, fontsize=18, fontproperties=font_prop)

# 隐藏多余的空格（如果有）
for i in range(5, 6):  # 隐藏第6个位置（如果有）
    fig.delaxes(plt.subplot(gs[1, 5]))

# 保存
plt.tight_layout()
plt.savefig("combined_confusion_matrices.svg", format='svg', bbox_inches='tight',dpi=300)
plt.show()