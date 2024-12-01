import string
import secrets
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 自定义字符表，支持 36 进制
CHARSET = string.digits + string.ascii_lowercase

# AES 密钥和 IV（固定示例，实际中应使用安全生成的密钥）
KEY = secrets.token_bytes(16)  # 16 字节密钥
# KEY = "1231231212312312"  # 16 字节密钥
IV = secrets.token_bytes(16)   # 16 字节初始向量

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

# 示例
original = 12345678
encoded = encrypt_to_6_digits(original)
# decoded = decrypt_from_6_digits(encoded)

print(f"16字节密钥: {KEY}")
print(f"原始数字: {original}")
print(f"加密结果: {encoded}")
# print(f"加密结果: {base64.b64encode(encoded).decode('utf-8')}")
# print(f"解密结果: {decoded}")
