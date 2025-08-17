from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time
from config import Config
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

print("当前工作目录:", os.getcwd())

# 加载配置信息
config = Config.load_config()

def fast_click(driver, xpath, max_retry=5, interval=0.05):
    """
    秒杀抢票专用点击函数
    driver: Appium driver
    xpath: 目标控件 XPath
    max_retry: 最大重试次数
    interval: 每次重试间隔（秒）
    """
    for attempt in range(max_retry):
        try:
            el = driver.find_element(AppiumBy.XPATH, xpath)
            if el.is_displayed() and el.is_enabled():
                # 获取控件中心坐标
                loc = el.location
                size = el.size
                center_x = loc['x'] + size['width'] / 2
                center_y = loc['y'] + size['height'] / 2
                
                # 直接点击坐标，比 el.click() 更快
                driver.tap([(center_x, center_y)])
                print(f"[INFO] 点击成功，尝试次数: {attempt+1}")
                return True
        except NoSuchElementException:
            pass
        time.sleep(interval)
    print("[WARN] 点击失败，目标控件未找到或不可点击")
    return False

desired_caps = {
    "platformName": "Android",         # 平台
    "platformVersion": "14",           # 安卓版本（adb shell getprop ro.build.version.release）
    "deviceName": "c813a9aa",         # 设备名（adb devices 查）
    "appPackage": "cn.damai",  # 应用包名
    "appActivity": ".homepage.MainActivity",      # 启动的活动
    "unicodeKeyboard": True,        # 使用unicode输入
    "resetKeyboard": True,      # 隐藏键盘
    "noReset": True,                    # 不重置应用数据
    "newCommandTimeout": 6000,           # 增加超时时间
    "automationName": "UiAutomator2",
   
}

options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# print(driver.page_source)
time.sleep(2)

# 隐式等待：设置查找元素时的最大等待时间为 5秒。
driver.implicitly_wait(2)

# 在界面“空闲”多少毫秒后才进行下一步操作，能加快测试速度，避免 Appium 等太久
driver.update_settings({"waitForIdleTimeout": 10})

# 机器人运动会图块
xpath_btn = '(//android.widget.ImageView[@resource-id="cn.damai:id/homepage_item_image_border"])[4]'
fast_click(driver, xpath_btn)

# 点击立即购票进入页面
xpath_btn = '//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]'
fast_click(driver, xpath_btn)

# 点击选择场次
xpath_btn = '(//android.widget.LinearLayout[@resource-id="cn.damai:id/ll_perform_item"])[1]'
fast_click(driver, xpath_btn)

# 点击选择票档
xpath_btn = '(//android.widget.LinearLayout[@resource-id="cn.damai:id/ll_perform_item"])[4]'
fast_click(driver, xpath_btn)

# 点击确定
xpath_btn = '//android.widget.LinearLayout[@resource-id="cn.damai:id/btn_buy_view"]'
fast_click(driver, xpath_btn)
# print(f"点击确定按钮的xpath文字打印尝试:",driver.find_element(By.XPATH,xpath_btn).text)

# 勾选观演人
xpath_btn = '(//android.widget.CheckBox[@resource-id="cn.damai:id/checkbox"])'
fast_click(driver, xpath_btn)

# 勾选支付方式
xpath_btn = '(//android.widget.CheckBox[@resource-id="cn.damai:id/cb_pay_check"])[1]'
fast_click(driver, xpath_btn)

# 点击立即提交
xpath_btn = '//android.widget.TextView[@text="立即提交"]'
fast_click(driver, xpath_btn)

driver.quit()
