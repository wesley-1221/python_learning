# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月09日
"""

import numpy as np
from sklearn.datasets import load_breast_cancer          #加载数据集
from sklearn.svm import SVC                              #导入svc（函数名称）
from sklearn.model_selection import train_test_split     #对数据进行拆分（分成训练集，测试集）
from sklearn.preprocessing import StandardScaler         #对特征进行标准差标准化
from sklearn.metrics import accuracy_score, precision_score, \
    recall_score, f1_score, cohen_kappa_score             #测试模型性能
from sklearn.metrics import classification_report        #模型分析报告
from sklearn.metrics import roc_curve                   #绘制ROC曲线
import matplotlib.pyplot as plt
cancer = load_breast_cancer()
#print(cancer)
#分别获取数据
cancer_data = cancer['data']
cancer_target = cancer['target']
cancer_names = cancer['feature_names']

#将数据划分为训练集，测试集
#random_stat 接收int， 代表随机种子编号，相同随机种子产生相同随机结果，不同随机种子产生不同随机结果，默认为none
#四组数据
cancer_data_train, cancer_data_test, cancer_target_train, cancer_target_test \
    = train_test_split(cancer_data, cancer_target, test_size=0.2, random_state=22)

#数据标准化
# fit分析特征和目标提取有价值的信息
# transform用来对特征的转换（PCA,LDA降维）
stdScaler = StandardScaler().fit(cancer_data_train)                    #fit用于训练算法（有监督无监督都行）
cancer_trainStd = stdScaler.transform(cancer_data_train)               #这里用于标准化
cancer_testStd = stdScaler.transform(cancer_data_test)

# 建立svm模型
svm = SVC().fit(cancer_trainStd, cancer_target_train)
print('建立得SVM模型为：\n', svm, '\n')

# 预测训练集结果
cancer_target_pred = svm.predict(cancer_testStd)                       #predict用于预测有监督学习的测试集标签
print('预测前20个结果：\n', cancer_target_pred[:20], '\n')

# 求出预测和真实一样得数目
true = np.sum(cancer_target_pred == cancer_target_test)
print('预测对得结果数目：', true)
print('预测错误的结果数目：', cancer_target_test.shape[0]-true)
print('预测结果准确率为：', true/cancer_target_test.shape[0], '\n')

# 准确率不能很好的反应一个模型的好坏，需要结合： 精确率，召回率，F1，Cohen`s Kappa系数 来衡量
"""
Precision(精确率)          1最佳                             
Recall(召回率)             1最佳
F1值                 1最佳
Cohen`s Kappa系数    1最佳
ROC曲线             最靠近y轴最佳
"""



print('使用SVM预测breast_cancer数据准确率：',
      accuracy_score(cancer_target_test, cancer_target_pred))
print('使用SVM预测breast_cancer数据精确率：',
      precision_score(cancer_target_test, cancer_target_pred))
print('使用SVM预测breast_cancer数据召回率：',
      recall_score(cancer_target_test, cancer_target_pred))
print('使用SVM预测breast_cancer数据F1值 ：',
      f1_score(cancer_target_test, cancer_target_pred))
print('使用SVM预测breast_cancer数据Cohen`s Kappa系数 ：',
      cohen_kappa_score(cancer_target_test, cancer_target_pred), '\n')


# print(cancer_target_test)
print('使用SVM预测breast_cancer数据的分类报告：', '\n',
      classification_report(cancer_target_test, cancer_target_pred))

# 绘制ROC曲线
fpr, tpr, thresholds = roc_curve(cancer_target_test, cancer_target_pred)
plt.figure(figsize=(10, 6))
plt.xlim(0, 1)
plt.ylim(0.0, 1.1)
plt.xlabel('False Postive Rate')
plt.ylabel('True Postive Rate')
plt.plot(fpr, tpr, linewidth=2, linestyle="-", color='red')
plt.show()




