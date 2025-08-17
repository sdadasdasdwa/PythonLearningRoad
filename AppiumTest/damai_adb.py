import subprocess
import time

# -------------------------------------------
# 1️⃣ adb 点击函数
# -------------------------------------------
def adb_tap(x, y):
    """使用 adb 直接点击屏幕坐标"""
    subprocess.call(['adb', 'shell', 'input', 'tap', str(x), str(y)])

# -------------------------------------------
# 2️⃣ adb swipe 函数（可选，用于滑动）
# -------------------------------------------
def adb_swipe(x1, y1, x2, y2, duration_ms=100):
    subprocess.call([
        'adb', 'shell', 'input', 'swipe',
        str(x1), str(y1), str(x2), str(y2), str(duration_ms)
    ])

# -------------------------------------------
# 3️⃣ 等待函数
# -------------------------------------------
def wait_for(seconds):
    time.sleep(seconds)

# -------------------------------------------
# 4️⃣ 坐标定义（根据你用 Appium Inspect 或截图测量）
# 注意：这里是示例，需要自己测量实际位置
# -------------------------------------------
coords = {
    'homepage_item': (850, 1850),         # 首页第 4 个活动图片
    'purchase_btn': (730, 2245),          # 立即购票按钮 FrameLayout
    'select_session': (420, 645),        # 选择场次
    'select_ticket': (235, 930),         # 选择票档
    'confirm_btn': (560, 2260),           # 确定按钮
    'checkbox_viewer': (995, 1050),       # 勾选观演人
    'checkbox_pay': (995, 1925),          # 勾选支付方式
    'submit_btn': (840, 2250),            # 立即提交
}

# -------------------------------------------
# 5️⃣ 抢票流程函数
# -------------------------------------------
def fast_purchase():
    adb_tap(*coords['homepage_item'])
    wait_for(0.05)  # 50ms，可根据实际调整
    adb_tap(*coords['purchase_btn'])
    wait_for(0.05)
    adb_tap(*coords['select_session'])
    wait_for(0.05)
    adb_tap(*coords['select_ticket'])
    wait_for(0.05)
    adb_tap(*coords['confirm_btn'])
    wait_for(0.05)
    adb_tap(*coords['checkbox_viewer'])
    wait_for(0.05)
    adb_tap(*coords['checkbox_pay'])
    wait_for(0.05)
    adb_tap(*coords['submit_btn'])

# -------------------------------------------
# 6️⃣ 循环重试
# -------------------------------------------
def main():
    start_time = time.time()
    max_retries = 1
    for i in range(max_retries):
        try:
            fast_purchase()
            print(f"尝试 {i+1} 完成")
        except Exception as e:
            print("异常:", e)
        # 可以设置每次循环间隔极短，模拟连续点击
        wait_for(0.01)
    print("完成抢票流程, 总耗时:", time.time() - start_time)

if __name__ == "__main__":
    main()
