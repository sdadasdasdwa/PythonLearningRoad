import hashlib
import time

"""
需求： 只需要把8位数字压缩成6位数字,不需要考虑要不要进行解密还原，
一下子思路就不一样了，既然不需要还原，那么只需要单纯的加密哈希运算就行了。
"""

# 定义一个固定的盐值，建议更换为随机生成的安全盐值
SALT = b"random_salt_value"

def encrypt_to_6_digits(num):
    """将 8 位数字加密为 6 位数字"""
    if num < 10000000 or num > 99999999:
        raise ValueError("输入必须为 8 位数字")
    
    # 转为字符串并计算哈希值
    num_str = str(num).encode('utf-8')
    # hash_bytes = hashlib.sha256(dynamic_salt + num_str).digest()  # 加动态盐计算哈希值
    hash_bytes = hashlib.pbkdf2_hmac(
        'sha256',              # 使用的哈希算法
        num_str,               # 原始数据
        SALT,                  # 盐
        100_000                # 迭代次数（越高越安全，但计算越慢）
    )
    
    # 取前 4 个字节，转换为整数
    hash_int = int.from_bytes(hash_bytes[:4], 'big')
    
    # 限制结果为 6 位数字
    return hash_int % 10**6

# 获取系统当前日期并转换为 8 位数字
def get_current_date_as_original():
    current_time = time.localtime()
    return int(time.strftime("%Y%m%d", current_time))


# 示例
original = get_current_date_as_original()  # 输入 8 位数字
encrypted = encrypt_to_6_digits(original)

print(f"原始数字: {original}")
print(f"加密结果(6位数字): {encrypted}")
