# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
import logging as logger
import argparse
import math


# 算法初始化
def init():
    logger.basicConfig(
        level=logger.DEBUG,
        format='%(levelname)s: %(message)s'
    )
    return


# parse args
def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-F', type=str, help='file path of data set csv')
    parser.add_argument('--alpha', '-A', type=float, default=1e-3, help='alpha, learning rate')
    parser.add_argument('--step', '-S', type=int, default=1e8, help='max step of iteration')
    return parser.parse_args()


# 加载训练和测试数据
def load_data(file, isNormed):
    logger.info('读取数据集，打乱顺序')
    data = np.loadtxt(file, dtype=float, delimiter=',')[1:, :]
    np.random.shuffle(data)
    # logger.info('Data shuffled: %r', data)

    logger.info('拆分训练数据为X和Y')
    x_all_org = data[:, :-1].T
    y_all = data[:, -1].reshape(1, -1)

    logger.info('输入数据X归一化：mean norm，每个特征，减均值，除以极差')
    avg_of_rows = np.mean(x_all_org, axis=1).reshape(-1, 1)
    max_of_rows = np.max(x_all_org, axis=1).reshape(-1, 1)
    min_of_rows = np.min(x_all_org, axis=1).reshape(-1, 1)

    if isNormed:
        x_all_normed = (x_all_org - avg_of_rows) / (max_of_rows - min_of_rows)
    else:
        x_all_normed = x_all_org

    logger.info('输入数据添加常数项特征值1，即thetas[0]的系数')
    ones = np.ones(shape=(1, x_all_org.shape[1]), dtype=float)
    x_all = np.vstack((ones, x_all_normed))

    logger.info('分割测试集和训练集-1：获取分割比例')
    sample_sum = x_all.shape[1]  # 获取总样本数

    # train_num = math.floor(sample_sum * 0.9)  # 90%训练集 - 10%测试集
    train_num = sample_sum
    test_num = sample_sum - train_num

    logger.info('SampleNum %d, TrainNum %d, TestNum %d', sample_sum, train_num, test_num)
    logger.info('分割测试集和数据集：分割')
    x_train = x_all[:, :train_num]
    y_train = y_all[:, :train_num]

    x_test = x_all[:, train_num:]
    y_test = y_all[:, train_num:]

    logger.info('DataSet: X_All %r\nY_All %r\nX_Train %r\nY_Train %r\nX_Test %r\nY_Test %r', x_all, y_all, x_train, y_train, x_test, y_test)

    logger.info('数据集载入完成')

    offset ={'Max': max_of_rows, 'Min': min_of_rows, 'Avg': avg_of_rows}
    return (x_train, y_train, x_test, y_test, offset)


# 训练预测
def predict(x_train, y_train, x_test, y_test, alpha, max_steps):
    logger.info('初始化随机thetas向量，[0, 1)之间浮点数')
    # thetas = np.random.rand(x_train.shape[0]).reshape(-1, 1)
    thetas = np.array([[10.28], [0.304]])
    logger.info('Thetas inited as %r', thetas)

    steps = 0
    cost = np.sum(np.square(np.dot(thetas.T, x_train) - y_train)) * 0.5 / x_train.shape[1]
    logger.info('Cost inited as %.4f', cost)

    while steps < max_steps and cost > 0.1:
        steps += 1
        bias = []
        for ii in range(0, thetas.shape[0]):
            bias.append(
                np.sum(np.multiply(np.dot(thetas.T, x_train) - y_train, x_train[ii].reshape(1, -1))) / x_train.shape[1]
            )
        for jj in range(0, thetas.shape[0]):
            thetas[jj] = thetas[jj] - alpha * bias[jj]
        cost = np.sum(np.square(np.dot(thetas.T, x_train) - y_train)) * 0.5 / x_train.shape[1]
        if steps % 1000 == 0:
            logger.info('Step[%d]: Cost %.4f, Thetas %r', steps, cost, thetas)
    return thetas


# main
if __name__ == '__main__':
    init()
    # args = arg_parse()
    # logger.info('Args: File %s, Alpha %f, MaxSteps %d', args.file, args.alpha, args.step)

    path = '../source/kg2pressure.csv'
    alpha = 1e-5
    max_steps = 1e8

    logger.info('1: 载入数据集')
    (x_train, y_train, x_test, y_test, offset) = load_data(path, isNormed=False)

    logger.info('2: 训练预测')
    thetas = predict(x_train, y_train, x_test, y_test, alpha, max_steps)

    logger.info('3: 模型评估')
    x_test = x_train
    y_test = y_train
    r2_score = 1 - np.sum(np.square(np.dot(thetas.T, x_test) - y_test)) / np.sum(np.square(y_test - np.mean(y_test)))

    logger.info('Res: Thetas %r, R2 Score %.2f', thetas, r2_score)
