import pandas as pd
import matplotlib.pyplot as plt

# 读取训练损失数据
train_path = 'train.csv'
train_df = pd.read_csv(train_path)

# 读取测试损失数据
test_path = 'test.csv'
test_df = pd.read_csv(test_path)

# 提取训练损失数据
train_x_data = train_df['Step'].astype(int)  # Step 列作为 x 轴数据，转换为整数
train_y_data = train_df['Value'].astype(float)  # Value 列作为 y 轴数据

# 提取测试损失数据
test_x_data = test_df['Step'].astype(int)  # Step 列作为 x 轴数据，转换为整数
test_y_data = test_df['Value'].astype(float)  # Value 列作为 y 轴数据

# 创建图形
plt.figure(figsize=(10, 6))

# 添加浅灰色虚线网格
plt.grid(color='lightgray', linestyle='--', linewidth=0.5, alpha=0.7)

# 绘制训练损失曲线，并为每个数据点添加实心圆点
plt.plot(train_x_data, train_y_data, color='blue', linewidth=1, marker='o', markerfacecolor='blue',
         label='Train Loss')

# 绘制测试损失曲线，并为每个数据点添加实心圆点
plt.plot(test_x_data, test_y_data, color='orange', linewidth=1, marker='o', markerfacecolor='orange', label='Test Loss')

# 添加图例
plt.legend()

# 添加坐标轴标签和标题
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Train and Test Loss for Tn BGE-VL-base Text Model')

# 设置 x 轴刻度为整数
plt.xticks(train_x_data)

# 保存图像
plt.savefig('Tn BGE-VL-base Text Model 5 epoch on flickr.pdf')

# 显示图像
plt.show()
