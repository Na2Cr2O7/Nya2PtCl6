import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
import cv2

# 加载预训练的InceptionV3模型
model = InceptionV3(weights='imagenet')

def load_and_preprocess_image(image_path):
    # 加载图像
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 转换为RGB格式
    image = cv2.resize(image, (299, 299))  # 调整大小
    image = np.expand_dims(image, axis=0)  # 增加批次维度
    image = preprocess_input(image)  # 预处理图像
    return image

def predict_image_description(image_path):
    image = load_and_preprocess_image(image_path)
    predictions = model.predict(image)
    decoded_predictions = decode_predictions(predictions, top=3)[0]  # 获取前3个预测
    description = ', '.join([f"{class_name} ({prob:.2f})" for (_, class_name, prob) in decoded_predictions])
    return description

# 使用示例
image_path = 'temp_0.jpg'  # 替换为你的图像路径
description = predict_image_description(image_path)
print("图像描述:", description)
