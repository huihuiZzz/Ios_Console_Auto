from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import os
from appium.webdriver.common.touch_action import TouchAction
import time
import pytest


class BassPage:
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def open_Terminal(self):  # 打开电脑终端
        os.system("open -a Terminal ")

    def install_app(self):  # 重新安装APP
        Terminal_uninstall_app = "ideviceinstaller -U com.subao.GameConsoleMaster"
        os.system(Terminal_uninstall_app)
        Terminal_install_app = "ideviceinstaller -i /Users/mwdj/Desktop/XunyouConsoleBooster.ipa"
        os.system(Terminal_install_app)
        # time.sleep(4)
    def phone_wrapper(self):
        case = ["同意", "用手机加速 NS"]
        return case
    def box_wrapper(self):
        case = ["同意", "用盒子加速 PS4/PS5/NS/Xbox"]
        return case
    def start_accelerate(self):  # 进入手机加速首页
        desired_caps = {
            "platformName": "iOS",  # 被测手机是安卓
            "platformVersion": "14.2",  # ios版本
            "deviceName": "iPhone 6s Plus",  # 设备名
            "udid": "4ee15c15867a0d3973ca3b8b3b39d25f0e4eede9",  # 设备udid
            "automationName": "XCUiTest",
            "xcodeSigningId": "iPhone Developer",
            "xcodeOrgId": "AW87D25TB5",
            "bundleId": "com.subao.GameConsoleMaster",
            "updatedWDABundleId": "com.subao.guanghui.wda",
        }
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(5)
        for i in self.phone_wrapper():
            ikonw = self._driver.find_elements_by_name(i)
            if ikonw:
                ikonw[0].click()
        from page.test_accelerate_page import AccelerateHomeAction
        return AccelerateHomeAction(self._driver)

    def first_start(self):  # 初始化启动
        desired_caps = {
            "platformName": "iOS",  # 被测手机是安卓
            "platformVersion": "14.2",  # ios版本
            "deviceName": "iPhone 6s Plus",  # 设备名
            "udid": "4ee15c15867a0d3973ca3b8b3b39d25f0e4eede9",  # 设备udid
            "automationName": "XCUiTest",
            "xcodeSigningId": "iPhone Developer",
            "xcodeOrgId": "AW87D25TB5",
            "bundleId": "com.subao.GameConsoleMaster",
            "updatedWDABundleId": "com.subao.guanghui.wda",
            "autoAcceptAlerts": True  # 系统授权弹窗自动点击
        }
        self.open_Terminal()
        self.install_app()
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(20)
        from page.test_accelerate_page import AccelerateHomeAction
        return AccelerateHomeAction(self._driver)

    def start(self):  # 正常启动
        desired_caps = {
            "platformName": "iOS",  # 被测手机是安卓
            "platformVersion": "14.2",  # ios版本
            "deviceName": "iPhone 6s Plus",  # 设备名
            "udid": "4ee15c15867a0d3973ca3b8b3b39d25f0e4eede9",  # 设备udid
            "automationName": "XCUiTest",
            "xcodeSigningId": "iPhone Developer",
            "xcodeOrgId": "AW87D25TB5",
            "bundleId": "com.subao.GameConsoleMaster",
            "updatedWDABundleId": "com.subao.guanghui.wda",
        }
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(5)
        from page.test_accelerate_page import AccelerateHomeAction
        return AccelerateHomeAction(self._driver)

    def first_start_phone_accelerate(self):  # 初始化启动进入手机加速页
        desired_caps = {
            "platformName": "iOS",  # 被测手机是安卓
            "platformVersion": "14.2",  # ios版本
            "deviceName": "iPhone 6s Plus",  # 设备名
            "udid": "4ee15c15867a0d3973ca3b8b3b39d25f0e4eede9",  # 设备udid
            "automationName": "XCUiTest",
            "xcodeSigningId": "iPhone Developer",
            "xcodeOrgId": "AW87D25TB5",
            "bundleId": "com.subao.GameConsoleMaster",
            "updatedWDABundleId": "com.subao.guanghui.wda",
            "autoAcceptAlerts": True  # 系统授权弹窗自动点击
        }
        self.open_Terminal()
        self.install_app()
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(20)
        for i in self.phone_wrapper():
            ikonw = self._driver.find_elements_by_name(i)
            if ikonw:
                ikonw[0].click()
        from page.test_accelerate_page import AccelerateHomeAction
        return AccelerateHomeAction(self._driver)

    def first_start_box_accelerate(self):  # 初始化启动进入盒子加速页
        desired_caps = {
            "platformName": "iOS",  # 被测手机是安卓
            "platformVersion": "14.2",  # ios版本
            "deviceName": "iPhone 6s Plus",  # 设备名
            "udid": "4ee15c15867a0d3973ca3b8b3b39d25f0e4eede9",  # 设备udid
            "automationName": "XCUiTest",
            "xcodeSigningId": "iPhone Developer",
            "xcodeOrgId": "AW87D25TB5",
            "bundleId": "com.subao.GameConsoleMaster",
            "updatedWDABundleId": "com.subao.guanghui.wda",
            "autoAcceptAlerts": True  # 系统授权弹窗自动点击
        }
        self.open_Terminal()
        self.install_app()
        self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self._driver.implicitly_wait(20)
        for i in self.box_wrapper():
            ikonw = self._driver.find_elements_by_name(i)
            if ikonw:
                ikonw[0].click()
        from page.test_accelerate_page import AccelerateHomeAction
        return AccelerateHomeAction(self._driver)

    def close_app(self):  # 关闭APP
        self._driver.implicitly_wait(3)
        return self._driver.close_app()

    def skip_box_welcome_page(self):  # 跳过盒子欢迎页
        self.first_start_box_accelerate().click_have_accelerate_box()
        return self

    def public_logged_in_vip(self):  # 登录随机账号
        self.first_start_box_accelerate().click_have_accelerate_box().open_more().click_not_logged_in().\
            logged_in_random().click_verification_code().write_in_correct_verification_code()
        return self

    def public_logged_in_xunyou_vip(self):  # 登录vip账号
        self.first_start_box_accelerate().click_have_accelerate_box().open_more().click_not_logged_in().\
            logged_in_appoint().click_verification_code().write_in_correct_verification_code()
        from page.test_more_page import MoreHomeAction
        return MoreHomeAction(self._driver)

    def public_logged_in_random(self):  # 登录随机账号
        self.first_start_phone_accelerate().open_more().click_not_logged_in().logged_in_random().\
            click_verification_code().write_in_correct_verification_code()
        from page.test_more_page import MoreHomeAction
        return MoreHomeAction(self._driver)

    def public_logged_not_in_xunyou_vip(self):  # 登录非vip账号(包含跳过盒子页步骤)
        self.first_start_box_accelerate().click_have_accelerate_box().open_more().click_not_logged_in().\
            logged_in_not_vip_appoint().click_verification_code().write_in_correct_verification_code()
        from page.test_more_page import MoreHomeAction
        return MoreHomeAction(self._driver)

    def get_into_more(self):  # 进入更多页
        self.start().open_more()
        from page.test_more_page import MoreHomeAction
        return MoreHomeAction(self._driver)

    def lookup_toast(self,message):  # 查找toast方法
        toast_element = WebDriverWait(self._driver, 5).until(lambda x: x.find_element_by_xpath(message))
        print(toast_element.text)
        assert toast_element.text

    def judge_element_exist(self,massage):  # 判断元素是否存在,没有是flase
        if self._driver.find_elements_by_name(massage) == []:
            return False
        else:
            return True
    def slide(self):  # 会员页滑动
        self._driver.swipe(200, 576, 200, 145, 500)
        return self



    # def judge_in_element_exist(self,massage,i):  # 判断页面中某一元素是否包含某
    #     if self._driver.find_elements_by_name(massage):
