import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# 设置中文支持（确保系统有该字体）
try:
    # 尝试使用微软雅黑
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False
except:
    # 回退到SimHei
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

# 数据准备
equipment_types = ['环保车', '装载车', '集卡车', '叉车', '牵引车', '起重机', '挖掘机', '抓料机']
sensor_counts = [64, 92, 78, 71, 89, 85, 107, 84]

# 创建专业级图表
fig, ax = plt.subplots(figsize=(10, 6))

# 使用渐变色
colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(equipment_types)))

# 绘制柱状图
bars = ax.bar(equipment_types, 
              sensor_counts, 
              color=colors,
              width=0.7,
              edgecolor='black',
              linewidth=0.8)

# 添加数据标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., 
            height + 2, 
            f'{height}',
            ha='center', 
            va='bottom',
            fontsize=10,
            fontweight='bold')

# 图表装饰
ax.set_title('港口设备传感器配置数量对比', 
             fontsize=14, 
             pad=20,
             fontweight='bold')
ax.set_xlabel('设备类型', 
              fontsize=12,
              labelpad=10)
ax.set_ylabel('传感器数量', 
              fontsize=12,
              labelpad=10)

# 调整坐标轴
ax.set_ylim(0, max(sensor_counts)*1.15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 网格线
ax.yaxis.grid(True, 
              linestyle=':', 
              alpha=0.4)

# 旋转x轴标签
plt.xticks(rotation=15, 
           ha='right',
           fontsize=10)

# 紧凑布局并保存为SVG
plt.tight_layout()
plt.savefig('Port_Equipment_Sensors.svg', 
            format='svg',
            bbox_inches='tight')

print("矢量图已保存为 Port_Equipment_Sensors.svg")