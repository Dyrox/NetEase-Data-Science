import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# 读取CSV文件
data = pd.read_csv('your_dataset.csv')

# 提取输入特征和目标输出
features = data[['歌单热度', '歌单排名']].values
labels = data['每日贡献播放量'].values

# 数据归一化
scaler = MinMaxScaler()
features = scaler.fit_transform(features)

# 划分训练集和测试集
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.2, random_state=42)

# 构建模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# 编译模型
model.compile(loss='mean_squared_error', optimizer='adam')

# 训练模型
model.fit(train_features, train_labels, epochs=100, batch_size=32, verbose=1)

# 评估模型
mse = model.evaluate(test_features, test_labels)
print('均方误差 (MSE):', mse)

# 使用模型进行预测
input_data = np.array([[4535435, 3], [53436546, 1]])
input_data = scaler.transform(input_data)
predictions = model.predict(input_data)
print('预测的每日贡献播放量:', predictions)
