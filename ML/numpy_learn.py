# -*- coding: utf-8 -*-
import logging as logger
import numpy as np


# 初始化
def init():
    logger.basicConfig(
        level=logger.DEBUG,
        format='%(levelname)s: %(message)s'
    )
    return


# 矩阵定义的几种方式
def mat_define():
    logger.info('>> 矩阵的定义')
    logger.info('[0]: 定义一个3 x 4的矩阵')
    mat1 = np.array([[1, 2, 3], [11, 12, 13], [4, 5, 6], [14, 15, 16]], dtype=float)
    logger.info('Mat: %r', mat1)
    logger.info('Shape: Row %d, Col %d\n', mat1.shape[0], mat1.shape[1])

    logger.info('[1]: 生成一个3 x 4，元素值为[0, 1]之间随机数的矩阵')
    mat2 = np.random.rand(3, 4)
    logger.info('Mat: %r', mat2)
    logger.info('Shape: Row %d, Col %d\n', mat2.shape[0], mat2.shape[1])

    logger.info('[2]: 生成一个3 x 4，元素值全为0的矩阵')
    mat3 = np.zeros(shape=(3, 4), dtype=float)
    logger.info('Mat: %r', mat3)
    logger.info('Shape: Row %d, Col %d\n', mat3.shape[0], mat3.shape[1])

    logger.info('[3]: 生成一个3 x 4，元素值全为1的矩阵')
    mat4 = np.ones(shape=(3, 4), dtype=float)
    logger.info('Mat: %r', mat4)
    logger.info('Shape: Row %d, Col %d\n', mat4.shape[0], mat4.shape[1])

    logger.info('[4]: 生成一个3 x 3的单位矩阵')
    mat4 = np.identity(3, dtype=float)
    logger.info('Mat: %r', mat4)
    logger.info('Shape: Row %d, Col %d\n', mat4.shape[0], mat4.shape[1])

    return


# 矩阵和向量的运算
def mat_by_vec():
    logger.info('>> 矩阵与向量的加减乘除运算')
    mat1 = np.array([[1, 2, 3], [11, 12, 13], [4, 5, 6], [14, 15, 16]], dtype=float)
    logger.info('Mat: %r', mat1)
    logger.info('[0]: 求矩阵Mat每一行的最大值，最小值，均值')
    maxOfRows = np.max(mat1, axis=1)
    minOfRows = np.min(mat1, axis=1)
    avgOfRows = np.mean(mat1, axis=1)
    logger.info('MaxOfRows: %r', maxOfRows)
    logger.info('MinOfRows: %r', minOfRows)
    logger.info('AvgOfRows: %r', avgOfRows)

    logger.info('* 注意到此时的行最大值、最小值、均值等均为一维数组（特点是只有一对方括号），既不是行向量也不是列向量，某些运算时需要做reshape')
    logger.info('矩阵和向量按行做加减乘除运算时，向量的行数必须和矩阵的行数相同，所以需要对数组做reshape， 转化为列向量\n')

    logger.info('[1]: 矩阵除以向量： 每一行的元素都除以该行的最大值')
    matDivVecOfMax = mat1 / maxOfRows.reshape(-1, 1)
    logger.info('Mat: %r\nVecMax: %r\nMatDivVecOfMax: %r\n', mat1, maxOfRows, matDivVecOfMax)

    logger.info('[2]: 矩阵乘以向量： 每一行的元素都乘以该行的最小值')
    matMulVecOfMin = mat1 * minOfRows.reshape(-1, 1)
    logger.info('Mat: %r\nVecMin: %r\nMatMulVecOfMin: %r\n', mat1, minOfRows, matMulVecOfMin)

    logger.info('[3]: 矩阵加向量： 每一行的元素都加上该行的平均值')
    matAddVecOfAvg = mat1 + avgOfRows.reshape(-1, 1)
    logger.info('Mat: %r\nVecAvg: %r\nMatAddVecOfAvg: %r\n', mat1, avgOfRows, matAddVecOfAvg)

    logger.info('[4]: 矩阵减向量： 每一行的元素都减去该行的平均值')
    matSubVecOfAvg = mat1 - avgOfRows.reshape(-1, 1)
    logger.info('Mat: %r\nVecAvg: %r\nMatSubVecOfAvg: %r\n', mat1, avgOfRows, matSubVecOfAvg)

    logger.info('Mat: %r', mat1)
    logger.info('[0]: 求矩阵Mat每一列的最大值，最小值，均值')
    maxOfCols = np.max(mat1, axis=0)
    minOfCols = np.min(mat1, axis=0)
    avgOfCols = np.mean(mat1, axis=0)
    logger.info('MaxOfCols: %r', maxOfCols)
    logger.info('MinOfCols: %r', minOfCols)
    logger.info('AvgOfCols: %r', avgOfCols)

    logger.info('* 注意到此时的列最大值、最小值、均值等均为一维数组，某些运算时需要做reshape')
    logger.info('矩阵和向量按列做加减乘除运算时，向量的列数必须和矩阵的列数相同，所以需要对数组做reshape， 转化为行向量\n')
    logger.info('* tips： 按列计算时，默认可以不用做reshape， 因为数组可以直接转换为行向量')
    logger.info('[1]: 矩阵除以向量： 每一列的元素都除以该列的最大值')
    matDivVecOfMax = mat1 / maxOfCols.reshape(1, -1)
    logger.info('Mat: %r\nVecMax: %r\nMatDivVecOfMax: %r\n', mat1, maxOfCols, matDivVecOfMax)

    logger.info('[2]: 矩阵乘以向量： 每一列的元素都乘以该列的最小值')
    matMulVecOfMin = mat1 * minOfCols  # reshape可以省去
    logger.info('Mat: %r\nVecMin: %r\nMatMulVecOfMin: %r\n', mat1, minOfCols, matMulVecOfMin)

    logger.info('[3]: 矩阵加向量： 每一列的元素都加上该列的平均值')
    matAddVecOfAvg = mat1 + avgOfCols.reshape(1, -1)
    logger.info('Mat: %r\nVecAvg: %r\nMatAddVecOfAvg: %r\n', mat1, avgOfCols, matAddVecOfAvg)

    logger.info('[4]: 矩阵减向量： 每一列的元素都减去该列的平均值')
    matSubVecOfAvg = mat1 - avgOfCols  # reshape可以省去
    logger.info('Mat: %r\nVecAvg: %r\nMatSubVecOfAvg: %r\n', mat1, avgOfCols, matSubVecOfAvg)
    return


# 数组定义
def array_define():
    logger.info('[1]: 初始化一个指定值的数组')
    arr1 = np.array([1, 2, 3, 4, 5])
    logger.info('Arr: %r', arr1)
    logger.info('Shape: %r', arr1.shape)

    logger.info('[2]: 初始化一个随机数数组，数组元素为[0, 1]之间的随机数')
    arr2 = np.random.rand(5)
    logger.info('Arr: %r', arr2)
    logger.info('Shape: %r', arr2.shape)

    logger.info('[3]: 初始化一个元素值全为1的数组')
    arr3 = np.ones(shape=5, dtype=float)
    logger.info('Arr: %r', arr3)
    logger.info('Shape: %r\n', arr3.shape)

    logger.info('[4]: 初始化一个元素值全为0的数组')
    arr4 = np.zeros(shape=5, dtype=float)
    logger.info('Arr: %r', arr4)
    logger.info('Shape: %r\n', arr4.shape)

    logger.info('[5]: 初始化一个元素值为[0, 1)之间，步长为0.1的有序数列的数组')
    arr5 = np.arange(0, 1, 0.1)
    logger.info('Arr: %r', arr5)
    logger.info('Shape: %r\n', arr5.shape)

    pass

# 向量定义的几种形式，分为行向量和列向量
def vec_define():
    logger.info('向量的定义与使用')
    logger.info('* tips: 一位数组不是向量！一维数组的特征是只有一对[]，向量和矩阵至少有两对[[]]')

    logger.info('[1]: 初始化一个1 x 3的行向量')
    vec1 = np.array([[1, 2, 3]], dtype=float)
    logger.info('Vec: %r', vec1)
    logger.info("Shape: Row %d, Col %d\n", vec1.shape[0], vec1.shape[1])

    logger.info('[2]: 初始化一个1 x 3的行向量，元素值为[0, 1]之间随机数')
    vec2 = np.random.rand(1, 3)
    logger.info('Vec: %r', vec2)
    logger.info("Shape: Row %d, Col %d\n", vec2.shape[0], vec2.shape[1])

    logger.info('[3]: 初始化一个1 x 3的行向量，元素值全为0')
    vec3 = np.zeros((1, 3), dtype=float)
    logger.info('Vec: %r', vec3)
    logger.info("Shape: Row %d, Col %d\n", vec3.shape[0], vec3.shape[1])

    logger.info('[4]: 初始化一个1 x 3的行向量，元素值全为1')
    vec4 = np.ones((1, 3), dtype=float)
    logger.info('Vec: %r', vec4)
    logger.info("Shape: Row %d, Col %d\n", vec4.shape[0], vec4.shape[1])

    logger.info('[5]: 初始化一个3 x 1的列向量')
    vec1 = np.array([[1], [2], [3]], dtype=float)
    logger.info('Vec: %r', vec1)
    logger.info("Shape: Row %d, Col %d\n", vec1.shape[0], vec1.shape[1])

    logger.info('[6]: 初始化一个3 x 1的列向量，元素值为[0, 1]之间随机数')
    vec2 = np.random.rand(3, 1)
    logger.info('Vec: %r', vec2)
    logger.info("Shape: Row %d, Col %d\n", vec2.shape[0], vec2.shape[1])

    logger.info('[7]: 初始化一个3 x 1的列向量，元素值全为0')
    vec3 = np.zeros((3, 1), dtype=float)
    logger.info('Vec: %r', vec3)
    logger.info("Shape: Row %d, Col %d\n", vec3.shape[0], vec3.shape[1])

    logger.info('[8]: 初始化一个3 x 1的列向量，元素值全为1')
    vec4 = np.ones((3, 1), dtype=float)
    logger.info('Vec: %r', vec4)
    logger.info("Shape: Row %d, Col %d\n", vec4.shape[0], vec4.shape[1])

    return

if __name__ == '__main__':
    init()
    # logger.info('[1]: 矩阵定义')
    # mat_define()

    # logger.info('[2]: 向量定义')
    # vec_define()

    logger.info('[3]: 数组定义')
    array_define()

    # logger.info('[4]: 矩阵与向量的加减乘除运算')
    # mat_by_vec()

    pass
