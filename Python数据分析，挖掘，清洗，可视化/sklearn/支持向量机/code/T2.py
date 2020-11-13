# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月09日
"""
"""
SVC 和 NuSVC 为多元分类实现了 “one-against-one” 的方法 (Knerr et al., 1990)  
如果 n_class 是类别的数量, 那么 n_class * (n_class - 1) / 2 分类器被重构, 
而且每一个从两个类别中训练数据. 为了提供与其他分类器一致的接口, 
decision_function_shape 选项允许聚合 “one-against-one” 分类器的结果成 (n_samples, n_classes) 的大小到决策函数:
"""


from sklearn import svm

X = [[0], [1], [2], [3]]
Y = [0, 1, 2, 3]
# clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
# clf.fit(X, Y)
# print(clf)
#
# dec = clf.decision_function([[1]])
# print(dec.shape[1])               # 4 classes: 4*3/2 = 6
#
# clf.decision_function_shape = "ovr"
# dec = clf.decision_function([[1]])
# print(dec.shape[1])               # 4 classes


lin_clf = svm.LinearSVC()
lin_clf.fit(X, Y)
print(lin_clf)

dec = lin_clf.decision_function([[1]])
print(dec.shape[1])