#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2020/5/27 9:30
# @Author : Snowball

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#%matplotlib inline


data = pd.read_csv("creditcard.csv")
count_classes = pd.value_counts(data.Class).sort_index()

# 画图
# count_classes.plot(kind="bar")
# plt.title("Fraud class histogram")
# plt.xlabel("Class")
# plt.ylabel("Frequency")

from sklearn.preprocessing import StandardScaler
data["normAmount"] = StandardScaler().fit_transform(data["Amount"].values.reshape(-1, 1))
data = data.drop(["Amount", "Time"], axis=1)

# 下采样方案
X = data.iloc[:, data.columns != "Class"]
y = data.iloc[:, data.columns == "Class"]

# 得到所有异常样本的索引
number_records_fraud = len(data[data.Class == 1])
fruad_indices = np.array(data[data.Class == 1].index)

# 得到所有正常样本的索引
normal_indices = data[data.Class == 0].index

# 在正常样本中随机采样出指定个数的样本，并取其索引
random_normal_indices  = np.random.choice(normal_indices, number_records_fraud, replace=False)
random_normal_indices = np.array(random_normal_indices)
# 有了正常和异常样本后把它们的索引都拿到手
under_sample_indices = np.concatenate([fruad_indices,random_normal_indices])
# 根据索引得到下采样所有样本点
under_sample_data = data.iloc[under_sample_indices, :]
X_undersample = under_sample_data.iloc[:, under_sample_data.columns != 'Class']
y_undersample = under_sample_data.iloc[:, under_sample_data.columns == 'Class']
# 下采样 样本比例
print("正常样本所占整体比例: ", len(under_sample_data[under_sample_data.Class == 0])/len(under_sample_data))
print("异常样本所占整体比例: ", len(under_sample_data[under_sample_data.Class == 1])/len(under_sample_data))
print("下采样策略总体样本数量: ", len(under_sample_data))

# 数据集划分
from sklearn.model_selection import train_test_split
# 整个数据集进行划分
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3, random_state=0)
print("原始训练集包含样本数量: ", len(X_train))
print("原始测试集包含样本数量: ", len(X_test))
print("原始样本总数: ", len(X_train)+len(X_test))

# 下采样数据集进行划分
X_train_undersample, X_test_undersample, y_train_undersample, y_test_undersample = train_test_split(X_undersample
                                                                                                   ,y_undersample
                                                                                                   ,test_size = 0.3
                                                                                                   ,random_state = 0)
print("")
print("下采样训练集包含样本数量: ", len(X_train_undersample))
print("下采样测试集包含样本数量: ", len(X_test_undersample))
print("下采样样本总数: ", len(X_train_undersample)+len(X_test_undersample))