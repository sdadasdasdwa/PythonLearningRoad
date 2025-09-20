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

### 均值

```python
N = len(fish_data)
S = sp.sum(fish_data)
avg = S / N
```

