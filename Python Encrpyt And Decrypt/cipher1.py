import string
import secrets
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time

"""
与cipher1.py 相比， 不同的是 把原来自定义的base36代码转成了base64方式来处理二进制数据,
优点就是省略了代码， 并且安全性应该比base36更高吧
"""


# 自定义字符表，支持 36 进制
CHARSET = string.digits + string.ascii_lowercase

# AES 密钥和 IV（固定示例，实际中应使用安全生成的密钥）
# 定义密钥（16 字节）
# KEY = secrets.token_bytes(16)  
KEY = b"1234567890abcdef"  # 示例密钥，需确保长度为 16 字节
# 16 字节初始向量
# IV = secrets.token_bytes(16)   
IV = b"1234567890abcdef"

def encrypt_to_base64(num):
    """将 8 位数字加密为 Base64 字符串"""
    if num < 10000000 or num > 99999999:
        raise ValueError("数字必须为8位")

    # 转为字节
    plaintext = str(num).encode('utf-8')

    # AES 加密
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    encrypted = cipher.encrypt(pad(plaintext, AES.block_size))

    # 编码为 Base64 字符串
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_from_base64(encoded):
    """将 Base64 字符串解密为原始数字"""
    # 解码为字节
    encrypted = base64.b64decode(encoded)

    # AES 解密
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

    # 转为数字
    return int(decrypted.decode('utf-8'))



# 获取系统当前日期并转换为 8 位数字
def get_current_date_as_original():
    current_time = time.localtime()
    return int(time.strftime("%Y%m%d", current_time))

# 示例
original = get_current_date_as_original()  # 系统日期 YYYYMMDD
encoded = encrypt_to_base64(original)  # 加密并编码为 Base64
# decoded = decrypt_from_base64(encoded)

print(f"16字节密钥: {KEY}")
print(f"原始数字: {original}")
print(f"加密结果: {encoded}")
# print(f"加密结果: {base64.b64encode(encoded).decode('utf-8')}")
# print(f"解密结果: {decoded}")
