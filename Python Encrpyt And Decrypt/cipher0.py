import string
import secrets
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time

"""
第一次考虑能够加密且能够解密的方式,下述代码使用了 AES + Base36的方式对 original 输入进行加密，
结果看来 并不是纯数字， 当时写的时候考虑用哈希把它转成对应的数字。
"""


# 自定义字符表，支持 36 进制
CHARSET = string.digits + string.ascii_lowercase

# AES 密钥和 IV（固定示例，实际中应使用安全生成的密钥）
# 定义密钥（16 字节）
KEY = secrets.token_bytes(16)  
# KEY = b"1234567890abcdef"  # 示例密钥，需确保长度为 16 字节
# 16 字节初始向量
IV = secrets.token_bytes(16)   
IV = b"1234567890abcdef"

def encode_to_base36(byte_data):
    """将字节数据编码为 6 位字符串"""
    num = int.from_bytes(byte_data, 'big')  # 将字节数据转为大整数
    print(f"num数值为: {num.bit_length()}")
    base = len(CHARSET)
    encoded = [] 
    for _ in range(6):
        encoded.append(CHARSET[num % base])
        num //= base
    return ''.join(reversed(encoded))

def decode_from_base36(encoded):
    """将 6 位字符串解码为字节数据"""
    base = len(CHARSET)
    num = 0
    for char in encoded:
        num = num * base + CHARSET.index(char)
    byte_length = (num.bit_length() + 7) // 8
    return num.to_bytes(byte_length, 'big')

def encrypt_to_6_digits(num):
    """将 8 位数字加密为 6 位字符串"""
    if num < 10000000 or num > 99999999:
        raise ValueError("数字必须为8位")

    # 转为字节
    plaintext = str(num).encode('utf-8')

    # AES 加密
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    encrypted = cipher.encrypt(pad(plaintext, AES.block_size))

    # 编码为 6 位字符串
    return encode_to_base36(encrypted)  # 截取 3 字节保证 6 位长度
    # return encrypted  # 返回完整密文

def decrypt_from_6_digits(encoded):
    """将 6 位字符串解密为原始数字"""
    # 解码为字节
    # encrypted = decode_from_base36(encoded)

    # 恢复 AES 加密的完整 16 字节密文
    # encrypted_full = encrypted.ljust(16, b'\x00')  # 补全长度为 16 字节

    # AES 解密
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted = unpad(cipher.decrypt(encoded), AES.block_size)

    # 转为数字
    return int(decrypted.decode('utf-8'))

# 获取系统当前日期并转换为 8 位数字
def get_current_date_as_original():
    current_time = time.localtime()
    return int(time.strftime("%Y%m%d", current_time))

# 示例
original = get_current_date_as_original()  # 系统日期 YYYYMMDD
encoded = encrypt_to_6_digits(original)
# decoded = decrypt_from_6_digits(encoded)

print(f"16字节密钥: {KEY}")
print(f"原始数字: {original}")
print(f"加密结果: {encoded}")
# print(f"加密结果: {base64.b64encode(encoded).decode('utf-8')}")
# print(f"解密结果: {decoded}")