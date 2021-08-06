from App.App_start import BassPage
import time

class MoreHomePage(BassPage):   # 更多页

    def help_center(self):  # 帮助中心栏
        return self._driver.find_element_by_name("帮助中心")
    def my_box(self):  # 我的加速盒栏
        return self._driver.find_element_by_name("我的加速盒")
    def not_logged_in(self):  # 未登录栏
        case = self._driver.find_elements_by_name("未登录")
        return case[1]

    def logged_in_title(self):  # 更多页已登录账号title
        case = self._driver.find_elements_by_class_name('XCUIElementTypeStaticText')
        return case[2]

    def open_number_setting(self):  # 打开183.。。账号设置页
        return self._driver.find_element_by_xpath('//XCUIElementTypeOther[@name="183****4444"]')

    def get_number_setting_title(self):  # 账号设置页title
        case = self._driver.find_elements_by_name("账号设置")
        return case[1]

    def exit_get_number_setting(self):  # 退出账号设置页按钮
        return self._driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="账号设置"]/XCUIElementTypeButton')

    def exit_sign_in(self):  # 账号设置页退出登录按钮
        return self._driver.find_element_by_name("退出登录")

    def exit_sign_in_determine(self):  # 账号设置 确定退出按钮
        return self._driver.find_element_by_name("确定退出")

    def exit_sign_in_cancel(self):  # 账号设置取消按钮
        return self._driver.find_element_by_name("取消")

    def confirm_exit_pop(self):  # 确定退出弹窗
        return self._driver.find_element_by_name('确定退出?')

    def understand_xunyou(self):  # 了解迅游栏
        return self._driver.find_element_by_name('了解迅游')

    def about_xunyou_title(self):  # 关于迅游顶部title
        case = self._driver.find_elements_by_name('关于迅游')
        return case[1]

    def join_QQ_group(self):  # 加入QQ群栏
        return self._driver.find_element_by_name('加入QQ群')

    def QQ_group(self):  # qq群名
        return self._driver.find_element_by_name('迅游主机加速用户群')

    def understand_xunyou_wechat_pop(self):  # 关于迅游微信公众号栏
        return self._driver.find_element_by_name('微信公众号：迅游主机加速')

    def follow_xunyou_console_accelerate(self):  # 关注迅游主机加速弹窗
        return self._driver.find_element_by_name('关注迅游主机加速')

    def renew_now(self):  # 立即续费按钮
        case = self._driver.find_elements_by_name("立即续费")
        return case[0]

    def become_a_member(self):  # 成为会员按钮
        case = self._driver.find_elements_by_name("成为会员")
        return case[0]

    def buy_now(self):  # 立即购买按钮
        case = self._driver.find_elements_by_name("立即购买")
        return case[0]

    def subscribe(self):  # 订阅按钮
        time.sleep(10)
        case = self._driver.find_elements_by_class_name('XCUIElementTypeButton')
        return case[2]

    def subscribe_button(self):  # 订阅按钮
        return self._driver.find_element_by_name('订阅')

    def vip_exchange_code(self):  # 会员兑换码入口
        return self._driver.find_element_by_name('使用会员兑换码')

    def vip_exchange_code_title(self):  # 会员兑换码页title
        case = self._driver.find_elements_by_name('兑换会员')
        return case[1]

    def exit_exchange_code(self):  # 退出兑换码页button
        case = self._driver.find_elements_by_class_name('XCUIElementTypeButton')
        return case[1]
