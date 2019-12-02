# -*- coding: utf-8 -*-
import logging as logger
import numpy as np
import argparse
import matplotlib.pyplot as plt


# 初始化配置
def init():
    logger.basicConfig(
        level=logger.INFO,
        format='%(levelname)s: %(message)s'
    )


# 解析参数
def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, help='path of data set, which should be a csv file')
    parser.add_argument('--alpha', '-a', type=float, help='learning rate')
    parser.add_argument('--step', '-s', type=int, default=10000, help='max iteration steps')
    parser.add_argument('--thres', '-t', type=float, help='thres of loss function')
    parser.add_argument('--mode', '-m', type=int, default=1, help='using gradient descent(0) or normal equation method(1)')
    return parser.parse_args()


# 载入数据集
def load_data_set(path):
    train = np.loadtxt(path, delimiter=',', skiprows=1)  # 跳过第1行，默认第1行为文件头

    X = train[:, :-1].reshape(train.shape[0], -1).T  # 默认除最后1列外，其他列为特征输入
    ones = np.ones(shape=(1, X.shape[1]), dtype=float)  # 补常数项特征值1，补在原X[0]的位置
    X = np.vstack((ones, X))

    Y = train[:, -1].reshape(1, -1)  # 默认最后1列为结果输出

    logger.debug('DataSet:\nTrain %r\nX %r\nY %r', train, X, Y)
    return X, Y


# 梯度下降法求thetas
def gradient_descent(X, Y, alpha, maxSteps, thresLoss):
    featNum = X.shape[0]
    sampleNum = X.shape[1]

    # 初始化thetas，计算代价函数
    thetas = np.random.rand(featNum).reshape(-1, 1)
    cost = np.sum(np.square(np.dot(thetas.T, X) - Y)) / (2.0 * sampleNum)  # 计算代价函数
    logger.info('Init: thetas %r, cost %r', thetas, cost)

    # 迭代
    for idx in range(0, maxSteps):
        thetas = thetas - alpha / sampleNum * np.sum((np.dot(thetas.T, X) - Y) * X, axis=1).reshape(-1, 1)
        cost = np.sum(np.square(np.dot(thetas.T, X) - Y)) / (2.0 * sampleNum)  # 计算代价函数
        if cost < thresLoss:
            logger.info('Success: thetas %r, cost %r, step %d', thetas, cost, idx)
            break
        logger.debug('Step[%d]:\ncost %.4f\nthetas %r', idx, cost, thetas.T)

    logger.info('Done: thetas %r, cost %.4f', thetas, cost)
    return thetas


# 线性代数方程法求thetas
def normal_equation(X, Y):
    thetas = np.dot(np.dot(np.linalg.pinv(np.dot(X, X.T)), X), Y.T)
    cost = np.sum(np.square(np.dot(thetas.T, X) - Y)) / (2.0 * X.shape[1])  # 计算代价函数
    logger.info('Success: thetas %r, cost %r', thetas, cost)
    return thetas


# 训练预测
def predict(X, Y, alpha, maxSteps, thresLoss, mode):
    featNum = X.shape[0]
    sampleNum = X.shape[1]

    thetas = []
    if mode == 0:
        # using gradient descent method
        logger.info('SampleNum is %d, FeatNum is %d, Using gradient descent method', sampleNum, featNum)
        thetas = gradient_descent(X, Y, alpha, maxSteps, thresLoss)
    else:
        # using normal equation
        logger.info('SampleNum is %d, FeatNum is %d, Using normal equation method', sampleNum, featNum)
        thetas = normal_equation(X, Y)
    return thetas


# main
if __name__ == '__main__':
    # 初始化
    init()
    logger.info('[1]: Init configuration')

    # 解析输入参数
    logger.info('[2]: Parse args')
    args = arg_parse()
    logger.info('Args: %r', args)

    # 载入数据集
    logger.info('[3]: Load data set from file')
    X, Y = load_data_set(args.file)

    # 训练预测
    logger.info('[4]: Train and predict')
    thetas = predict(X, Y, args.alpha, args.step, args.thres, args.mode)

    # 画图
    logger.info('[5]: Draw plot')
    Y_ = np.dot(thetas.T, X)
    featNum = X.shape[0]

    plt.figure()
    if featNum > 2:  # 若特征数大于2，即多元线性回归，则画Y-Y_的散点图，同时以Y-Y曲线作为参照
        plt.scatter(Y_, Y, s=5, color='r')
        plt.plot(Y_.T, Y_.T, color='b')
    else:  # 若特征数等于2，即一元线性回归，则画Y-X散点图和Y_-X的曲线作为参照
        plt.scatter(X[1, :].reshape(1, -1), Y, s=5, color='r')
        plt.plot(X[1, :], Y_.T, color='b')

    plt.show()
    pass
