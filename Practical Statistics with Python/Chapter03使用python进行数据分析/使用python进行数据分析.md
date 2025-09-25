# 第三章 使用python进行数据分析

## 使用Python进行描述统计：单变量

### 统计分析与scipy

scipy中包含用于“计算统计量等基础的数据分析工作”的函数。

执行下面的语句，即可将打印精度设置为3位。

```python
%precision 3
```

### 单变量数据的操作

单变量数据是指只有一种类型的数据，例如鱼的体长。

```python
fish_data = np.ones(10)
```

### 总和与样本容量

```python
import scipy as sp

sp.sum(fish_data) => 10         # 总和
len(fish_data) => 10            # 样本容量
```

### 均值(期望值)

```python
N = len(fish_data)
S = sp.sum(fish_data)
avg = S / N

# 等价替换
sp.mean(fish_data)
```

### 样本方差

```python
sigma_2_sample = sp.sun((fish_data-mu)** 2) / N

# 等价替换
sp.var(fish_data, ddof = 0)
```

### 无偏方差

```python
sigma_2_sample = sp.sun((fish_data-mu)** 2) / (N-1)

# 等价替换
sp.var(fish_data, ddof = 1)
```

### 标准差

```python
sigma_2 = sp.sqrt(sigma_2_sample)

# 等价替换
sp.std(fish_data, ddof = 1)
```

### 标准化

标准化就是把均值转化为0，把标准差(方差)转化为1。

要使均值为0，只需用所有样本减去均值即可。

同样，要使数据的标准差(方差)为1，只需用所有样本除以标准差即可。


### 其他统计量

```python
sp.amax()    # 求最大值
sp.amin()    # 求最小值
sp.median()     # 求中位数
```
