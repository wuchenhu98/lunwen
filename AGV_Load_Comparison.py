import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import matplotlib

# 设置支持中文的字体（使用系统自带字体）
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 微软雅黑
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 生成模拟数据
def generate_agv_current():
    np.random.seed(42)
    t = np.linspace(0, 30, 3000)  # 30秒数据，100Hz采样
    
    # 空载电流 (平稳工况)
    base_current = 5.0
    no_load = base_current + 0.1 * signal.sawtooth(2 * np.pi * 0.2 * t, width=0.5)
    no_load += 0.05 * np.random.normal(size=len(t))
    
    # 满载电流 (动态工况)
    base_current = 15.0
    full_load = base_current + 1.2 * signal.sawtooth(2 * np.pi * 0.5 * t, width=0.8)
    full_load += 0.8 * np.sin(2 * np.pi * 2 * t)
    full_load += 1.5 * np.random.normal(size=len(t))
    
    return t, no_load, full_load

# 创建对比图
def create_comparison_plot(t, no_load, full_load):
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # 绘制曲线
    ax.plot(t, no_load, 'b-', linewidth=1.5, alpha=0.8, label='空载工况')
    ax.plot(t, full_load, 'r-', linewidth=1.5, alpha=0.8, label='满载工况')
    
    # 添加统计标注
    ax.text(25, 6, f'空载均值: {np.mean(no_load):.2f}A\n波动: ±{np.std(no_load):.2f}A',
            color='blue', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
    
    ax.text(5, 20, f'满载均值: {np.mean(full_load):.2f}A\n波动: ±{np.std(full_load):.2f}A',
            color='red', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
    
    # 设置图表元素
    ax.set_title('AGV不同负载工况电流特性对比', fontsize=14, pad=15)
    ax.set_xlabel('时间 (秒)', fontsize=12)
    ax.set_ylabel('电机电流 (A)', fontsize=12)
    ax.legend(loc='upper right', fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 25)
    
    plt.tight_layout()
    plt.savefig('AGV_Load_Comparison.svg', dpi=300, bbox_inches='tight')
    plt.close()

# 主程序
if __name__ == "__main__":
    print("正在生成AGV电流对比图表...")
    time, no_load, full_load = generate_agv_current()
    create_comparison_plot(time, no_load, full_load)
    print("图表已保存为 AGV_Load_Comparison.svg")