from appium import webdriver
import time

desired_caps = {
    "platformName": "Android",         # 平台
    "platformVersion": "13",           # 安卓版本（adb shell getprop ro.build.version.release）
    "deviceName": "MyAndroid",         # 设备名（adb devices 查）
    "appPackage": "com.android.calculator2",  # 应用包名
    "appActivity": ".Calculator",      # 启动的活动
    "noReset": True                    # 不重置应用数据
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

time.sleep(3)  # 等待应用启动
driver.quit()
