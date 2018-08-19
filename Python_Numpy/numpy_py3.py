import numpy as np
# numpy 数组的属性

# 设置随机数种子，确保每次程序执行时都可以生成相同的随机数组
np.random.seed(0)

x1 = np.random.randint(10, size=6)  # 一维数组
x2 = np.random.randint(10, size=(3, 4))  # 二维数组
x3 = np.random.randint(10, size=(3, 4, 5))  # 三维数组

# 每个数组有nidm(数组的维度)、shape(数组每个维度的大小)和size（数组的总大小）属性
print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)

# 数组的数据类型
print("dtype: ", x3.dtype)

# 每个数组元素字节大小的itemsize，数组总字节大小的属性nbytes
print("itemsize: ", x3.itemsize, "bytes")
print("nbytes: ", x3.nbytes, "bytes")
