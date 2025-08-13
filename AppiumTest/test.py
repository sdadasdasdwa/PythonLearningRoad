from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

desired_caps = {
    "platformName": "Android",         # 平台
    "platformVersion": "14",           # 安卓版本（adb shell getprop ro.build.version.release）
    "deviceName": "c813a9aa",         # 设备名（adb devices 查）
    "appPackage": "cn.damai",  # 应用包名
    "appActivity": ".homepage.MainActivity",      # 启动的活动
    "noReset": True,                    # 不重置应用数据
    "automationName": "UiAutomator2"
}

options = UiAutomator2Options().load_capabilities(desired_caps)


driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# print(driver.page_source)
time.sleep(3)
driver.quit()
