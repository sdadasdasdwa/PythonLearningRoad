import time
from appium import webdriver
from selenium.common.exceptions import WebDriverException

# Appium capabilities
caps = {
    "platformName": "Android",
    "deviceName": "c813a9aa",  # 你的 adb devices 里的 ID
    "appPackage": "com.xxx.yyy",  # 目标应用包名
    "appActivity": ".MainActivity",  # 启动 Activity
    "automationName": "UiAutomator2",
    "newCommandTimeout": 300
}

APPIUM_SERVER = "http://127.0.0.1:4723"  # 注意不要加 /wd/hub
MAX_RETRY = 5
RETRY_DELAY = 5


def start_driver():
    """尝试启动 driver，失败自动重试"""
    for attempt in range(1, MAX_RETRY + 1):
        try:
            print(f"[INFO] 第 {attempt} 次尝试连接 Appium...")
            driver = webdriver.Remote(APPIUM_SERVER, options=None, desired_capabilities=caps)
            print("[INFO] 成功连接 Appium")
            return driver
        except WebDriverException as e:
            print(f"[ERROR] 启动失败: {e}")
            time.sleep(RETRY_DELAY)
    raise RuntimeError("[FATAL] 多次重试后仍无法连接 Appium")


def safe_execute(driver, func, *args, **kwargs):
    """安全执行 Appium 操作，断开时自动重连"""
    try:
        return func(*args, **kwargs)
    except WebDriverException as e:
        print(f"[WARN] 会话中断，尝试重连... 错误信息: {e}")
        driver.quit()
        new_driver = start_driver()
        return func(*args, **kwargs), new_driver


if __name__ == "__main__":
    driver = start_driver()

    try:
        for i in range(10):
            print(f"[INFO] 当前 Activity: {driver.current_activity}")
            time.sleep(3)
    except WebDriverException:
        print("[ERROR] 执行时会话断开，准备重连")
        driver = start_driver()
    finally:
        driver.quit()
        print("[INFO] 测试结束")
