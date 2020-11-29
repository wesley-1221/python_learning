# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月09日
"""

from sklearn import svm

X = [[0, 0], [1, 1]]            #数组作为输入
y = [0, 1]
clf = svm.SVC(gamma='scale')
clf.fit(X, y)                   #拟合
print(clf)
# 在拟合后, 这个模型可以用来预测新的值:
# print(clf.predict([[2., 2.]]))
print(clf.support_vectors_)              # 获得支持向量
print(clf.support_)                      # 获得支持向量的索引
print(clf.n_support_)                    # 为每一个类别获得支持向量的数量





