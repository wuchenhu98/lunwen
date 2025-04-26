import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch

# 设置绘图样式
plt.style.use('seaborn-whitegrid')
plt.rcParams.update({
    'font.size': 10,
    'axes.linewidth': 1.2,
    'font.family': 'Arial'
})

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# 绘制输入图结构
def draw_graph(x, y, radius=0.3, color='#4C72B0'):
    nodes = []
    for i in range(3):
        circle = Circle((x+i*1.5, y), radius, fill=True, color=color, alpha=0.8)
        ax.add_patch(circle)
        nodes.append((x+i*1.5, y))
    # 绘制边
    ax.annotate("", xy=nodes[1], xytext=nodes[0],
               arrowprops=dict(arrowstyle="-", color='gray', lw=2, alpha=0.6))
    ax.annotate("", xy=nodes[2], xytext=nodes[1],
               arrowprops=dict(arrowstyle="-", color='gray', lw=2, alpha=0.6))
    ax.annotate("", xy=nodes[0], xytext=nodes[2],
               arrowprops=dict(arrowstyle="-", color='gray', lw=2, alpha=0.6))
    return nodes

# 绘制GNN层
def draw_layer(x, y, label, color='#DD8452'):
    circle = Circle((x, y), 0.8, fill=True, color=color, alpha=0.7)
    ax.add_patch(circle)
    ax.text(x, y, label, ha='center', va='center', color='white', fontweight='bold')
    return (x, y)

# 绘制箭头
def draw_arrow(start, end, style='-|>'):
    arrow = FancyArrowPatch(start, end, 
                           arrowstyle=style, 
                           color='#555555', 
                           mutation_scale=20, 
                           lw=1.5, 
                           alpha=0.8)
    ax.add_patch(arrow)

# 绘制输入图
input_nodes = draw_graph(1, 2)
ax.text(np.mean([n[0] for n in input_nodes]), 1.2, "Input Graph", 
       ha='center', fontsize=10)

# 绘制GNN层
layer1 = draw_layer(5, 4, "GNN\nLayer 1")
layer2 = draw_layer(5, 3, "GNN\nLayer 2")
layer3 = draw_layer(5, 2, "GNN\nLayer 3")

# 连接输入到第一层
for node in input_nodes:
    draw_arrow((node[0]+0.3, node[1]+0.1), (layer1[0]-0.8, layer1[1]), '->')

# 连接各层
draw_arrow((layer1[0], layer1[1]-0.8), (layer2[0], layer2[1]+0.8), '->')
draw_arrow((layer2[0], layer2[1]-0.8), (layer3[0], layer3[1]+0.8), '->')

# 绘制输出
output = draw_graph(8, 2)
ax.text(np.mean([n[0] for n in output]), 1.2, "Output Graph", 
       ha='center', fontsize=10)
draw_arrow((layer3[0]+0.8, layer3[1]), (output[0][0]-0.3, output[0][1]+0.1), '->')

# 添加标题
ax.text(5, 5.5, "Graph Neural Network Architecture", 
       ha='center', fontsize=12, fontweight='bold')

# 保存为SVG
plt.savefig('gnn_architecture.svg', 
           format='svg', 
           bbox_inches='tight', 
           pad_inches=0.1, 
           dpi=300)

plt.close()