# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月08日
"""

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_lfw_people                # 数据集
from sklearn.svm import SVC
from sklearn.decomposition import PCA                        # 降维
from sklearn.metrics import classification_report            # 分析报告
from sklearn.model_selection import GridSearchCV             # 模型调参利器
from sklearn.model_selection import train_test_split         # 划分训练集 测试集

def get_data():
    faces = fetch_lfw_people(min_faces_per_person=60)
    # 数据的规模
    # print("faces.target_names", faces.target_names, "\n")
    # print("faces.images.shape", faces.images.shape, "\n")
    xtrain, xtest, ytrain, ytest = train_test_split(faces.data, faces.target, random_state=2)  # 划分
    n_components = 100                              # PCA降维后的特征维度数目
    pca = PCA(n_components=n_components, svd_solver='randomized',
              whiten=True, random_state=42).fit(xtrain)
    xtrain_pca = pca.transform(xtrain)              # 拟合
    xtest_pca = pca.transform(xtest)
    return faces, xtrain, xtest, ytrain, ytest, xtrain_pca, xtest_pca

def train_prep_data():
    svc = SVC(kernel='linear', C=10)               # 线性核函数
    svc.fit(xtrain_pca, ytrain)                     # 训练过程
    yfit_linear = svc.predict(xtest_pca)            # 模型预测
    return yfit_linear


def different_kernel_func():
    # json格式的数据
    param_grid = [
        {'kernel': ['linear'], 'C':[1, 5, 10, 50]},                                                     # 线性核函数
        {'kernel': ['rbf'], 'C':[1, 5, 10, 50], 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1]},    # 高斯核函数
        {'kernel': ['poly'], 'C':[1, 5, 10, 50], 'degree':[2, 3, 4], 'gamma':['auto']}                # 多项式核函数
    ]

    grid = GridSearchCV(SVC(class_weight='balanced'), param_grid, cv=3)     # 调参器
    grid.fit(xtrain_pca, ytrain)
    print(grid.best_estimator_)                           # 获取模型最佳参数（得到最好的模型参数）
    model = grid.best_estimator_
    yfit_best = model.predict(xtest_pca)                       # 训练
    return yfit_best

def visualization_part():
    print("-"*10+"可视化部分-分析报告"+"-"*10)
    print("yfit_linear分析报告\n")
    print(classification_report(ytest, yfit_linear, target_names=faces.target_names))
    print("+"*20)
    print("yfit_best分析报告\n")
    print(classification_report(ytest, yfit_best, target_names=faces.target_names))

    print("-" * 10 + "可视化部分-matplotlib画图" + "-" * 10)
    # print("用支持向量机之前的图像：\n")
    fig, ax = plt.subplots(3, 5)                    # 画布
    # print("ax:\t", ax)
    # print("ax.flat:\t", ax.flat)
    for i, axi in enumerate(ax.flat):
        axi.imshow(faces.images[i], cmap='bone')
        axi.set(xticks=[], yticks=[], xlabel=faces.target_names[faces.target[i]])

    # print("用支持向量机之后的图像：\n")
    fig, ax = plt.subplots(4, 6)
    for i, axi in enumerate(ax.flat):
        axi.imshow(xtest[i].reshape(62, 47), cmap='bone')
        axi.set(xticks=[], yticks=[])
        axi.set_ylabel(faces.target_names[yfit_best[i]].split()[-1],
                       color='black' if yfit_best[i] == ytest[i] else 'red')

    plt.show()
    plt.xlabel('true label')
    plt.ylabel('predicted label')

# def main():
#     faces, xtrain, xtest, ytrain, ytest, xtrain_pca, xtest_pca = get_data()
#     yfit_linear = train_prep_data()
#     yfit_best = different_kernel_func()
#     visualization_part()

if __name__ == '__main__':
    # main()
    faces, xtrain, xtest, ytrain, ytest, xtrain_pca, xtest_pca = get_data()
    yfit_linear = train_prep_data()
    yfit_best = different_kernel_func()
    visualization_part()






