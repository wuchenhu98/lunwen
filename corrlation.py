import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 设置中文字体
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

# 只用中文维度标签
dims = ['加速度', '电流', '张力', '液压压力', '振动']

# 生成时间段1：正常作业数据
np.random.seed(0)
data_t1 = np.random.normal(0, 1, (300, 5))
data_t1[:, 4] = data_t1[:, 0] * 0.85 + np.random.normal(0, 0.2, 300)  # 加速度-振动强相关
data_t1[:, 1] = data_t1[:, 0] * 0.6 + np.random.normal(0, 0.3, 300)   # 加速度-电流中等相关
data_t1[:, 2] = data_t1[:, 1] * 0.6 + np.random.normal(0, 0.3, 300)   # 电流-张力相关
data_t1[:, 3] = data_t1[:, 2] * 0.7 + np.random.normal(0, 0.3, 300)   # 张力-液压相关

df_t1 = pd.DataFrame(data_t1, columns=dims)

# 时间段2：大风扰动数据
data_t2 = np.random.normal(0, 1, (300, 5))
wind_disturbance = np.random.normal(3, 1, 300)

data_t2[:, 0] = wind_disturbance * 0.6 + np.random.normal(0, 0.5, 300)  # 加速度由风主导
data_t2[:, 4] = wind_disturbance * 0.8 + np.random.normal(0, 0.3, 300)  # 振动由风主导，加速度振动更相关
data_t2[:, 1] = np.random.normal(0, 1, 300)  # 电流独立，扰动影响小
data_t2[:, 2] = data_t2[:, 1] * 0.6 + np.random.normal(0, 0.3, 300)
data_t2[:, 3] = data_t2[:, 2] * 0.6 + np.random.normal(0, 0.3, 300)

df_t2 = pd.DataFrame(data_t2, columns=dims)

# 计算相关矩阵
corr_t1 = df_t1.corr()
corr_t2 = df_t2.corr()

# 绘图
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.heatmap(corr_t1, annot=True, cmap="coolwarm", vmin=-1, vmax=1,
            ax=axes[0], annot_kws={"size": 10},
            xticklabels=True, yticklabels=True,
            cbar_kws={"shrink": .75})
axes[0].set_xlabel('')
axes[0].set_ylabel('')
axes[0].set_title('正常作业工况', fontsize=14)

sns.heatmap(corr_t2, annot=True, cmap="coolwarm", vmin=-1, vmax=1,
            ax=axes[1], annot_kws={"size": 10},
            xticklabels=True, yticklabels=True,
            cbar_kws={"shrink": .75})
axes[1].set_xlabel('')
axes[1].set_ylabel('')
axes[1].set_title('大风扰动工况', fontsize=14)

plt.tight_layout(pad=1.0, w_pad=1.5)

plt.savefig("港口设备五维度动态相关性示意图.svg", format='svg')
plt.close()

print("热力图已保存为 SVG：港口设备五维度动态相关性示意图.svg")
