import time

from elment.more_page_elment import MoreHomePage
from page.test_help_center_page import HelpCenterAction
from page.test_login_registration_page import LoginRegistrationAction
from page.test_my_box_page import MyBoxAction
class MoreHomeAction(MoreHomePage):  # 更多页操作
    def check_help_center(self):  # 检查帮助中心栏位
        return self.help_center().text

    def click_help_center(self):  # 进入帮助中心页
        self.help_center().click()
        return HelpCenterAction(self._driver)  # 进帮助中心操作页

    def not_logged_in_click_my_box(self):  # 未登录点击我的加速盒
        self.my_box().click()
        return LoginRegistrationAction(self._driver)

    def click_not_logged_in(self):  # 点击未登录栏 登录
        self.not_logged_in().click()
        return LoginRegistrationAction(self._driver)

    def check_not_logged_in(self):  # 检查未登录栏text
        return self.not_logged_in().text

    def logged_in_my_box(self):  # 已登录点击我的加速盒页
        self.my_box().click()
        return MyBoxAction(self._driver)

    def check_logged_in_title(self):  # 查看更多页已登录账号元素展示
        return self.logged_in_title().text

    def click_logged_in_title(self):  # 点击已登录账号title
        self.logged_in_title().click()
        return self

    def check_get_number_setting(self):  # 账号设置页顶部title
        return self.get_number_setting_title().text

    def click_exit_get_number_setting(self):  # 点击退出账号设置页
        self.exit_get_number_setting().click()
        return self

    def click_exit_sign_in(self):  # 账号设置页点击退出登录
        self.exit_sign_in().click()
        return self

    def check_exit_sign_in(self):  # 账号设置页退出登录文本
        return self.exit_sign_in().text

    def click_exit_sign_in_determine(self):  # 账号设置页退出登录弹窗点击确定
        self.exit_sign_in_determine().click()
        return self

    def click_exit_sign_in_cancel(self):  # 确定退出弹窗点击取消
        self.exit_sign_in_cancel().click()
        return self

    def check_confirm_exit_pop(self):  # 检查确定退出弹窗文案
        return self.confirm_exit_pop().text

    def click_understand_xunyou(self):  # 点击了解迅游
        self.understand_xunyou().click()
        return self

    def click_join_QQ_group(self):  # 点击加入QQ群
        self.join_QQ_group().click()
        return self

    def check_QQ_group(self):  # 检查迅游主机加速用户群名
        self._driver.implicitly_wait(30)
        return self.QQ_group().text

    def check_about_xunyou_title(self):  # 关于迅游顶部title
        return self.about_xunyou_title().text

    def click_understand_xunyou_wechat_pop(self):  # 点击微信公众号栏
        self.understand_xunyou_wechat_pop().click()
        return self

    def check_follow_xunyou_console_accelerate(self):  # 关注迅游主机加速text
        return self.follow_xunyou_console_accelerate().text

    def click_renew_now(self):  # 点击立即续费按钮
        self.renew_now().click()
        return self

    def check_renew_now(self):  # 立即续费text
        return self.renew_now().text

    def click_become_a_member(self):  # 点击成为会员按钮
        self.become_a_member().click()
        return self

    def check_become_a_member(self):  # 成为会员按钮text
        return self.become_a_member().text

    def click_buy_now(self):  # 点击立即购买按钮
        self.buy_now().click()
        return self

    def check_buy_now(self):  # 立即购买按钮text
        return self.buy_now().text

    def check_subscribe(self):  # 订阅按钮text
        return self.subscribe_button().text

    def click_vip_exchange_code(self):  # 点击会员兑换码入口
        self.vip_exchange_code().click()
        return self

    def check_vip_exchange_code(self):  # 查看会员页title
        return self.vip_exchange_code_title().text

    def click_exit_exchange_code(self):  # 点击退出兑换码页button
        self.exit_exchange_code().click()
        return self