from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
import time
from config import Config
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput

print("当前工作目录:", os.getcwd())

# 加载配置信息
config = Config.load_config()

def tap(driver, x, y):
    # driver.tap(坐标列表, 持续时间ms)
    driver.tap([(x, y)], 100)

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
driver.implicitly_wait(5)

# 在界面“空闲”多少毫秒后才进行下一步操作，能加快测试速度，避免 Appium 等太久
driver.update_settings({"waitForIdleTimeout": 10})

# 点击搜索框
driver.find_element(by=By.ID, value='cn.damai:id/channel_search_text').click()

# 输入搜索关键词
driver.find_element(by=By.ID, value='cn.damai:id/header_search_v2_input').send_keys(config.keyword)

# 找到一个安卓滚动列表,在它的子节点里找到第一个RelativeLayout,执行模拟点击
driver.find_element(by=By.XPATH,
                    value='//androidx.recyclerview.widget.RecyclerView[@resource-id="cn.damai:id/search_v2_suggest_recycler"]/android.widget.RelativeLayout[1]').click()
	

# 找到所有 LinearLayout 元素，取第一个，点击它
driver.find_element(by=By.XPATH,
                    value='(//android.widget.LinearLayout[@resource-id="cn.damai:id/ll_search_item"])[1]').click()


if driver.find_elements(by=By.XPATH,
                        value='//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]'):
    print("寻找预约抢票按钮测试成功")
    buy_btn_list = driver.find_elements(by=By.XPATH,
                                  value='//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]')
    print(f"找到的元素数量: {len(buy_btn_list)}")
    if buy_btn_list:
        buy_btn_text = buy_btn_list[0].get_attribute("contentDescription")
        print(f"打印文字看看：{buy_btn_text}")
    else:
        print(f"TextView 元素没有找到")

# 预约抢票点击
# driver.find_element(by=By.XPATH,
#                         value='//android.widget.FrameLayout[@resource-id="cn.damai:id/trade_project_detail_purchase_status_bar_container_fl"]').click()

# # 找到预约场次
# el = driver.find_elements(by=By.XPATH,
#                          value='//android.widget.LinearLayout[@resource-id="cn.damai:id/ll_perform_item"]')

# print("找到的元素数量:", len(el))
# rect = el[1].rect

# # 计算点击位置
# x = rect['x'] + rect['width'] * 0.3
# y = rect['y'] + rect['height'] * 0.5

# # 点击
# tap(driver, x, y)

# # 档票
# rect = el[4].rect

# # # 计算点击位置
# x = rect['x'] + rect['width'] * 0.3
# y = rect['y'] + rect['height'] * 0.5

# # # 点击
# tap(driver, x, y)

driver.quit()
