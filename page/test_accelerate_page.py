from elment.home_page_elment import AccelerateHomePage
from appium.webdriver.common.touch_action import TouchAction


class AccelerateHomeAction(AccelerateHomePage):  # 加速首页操作
    def open_more(self):  # 进入更多页
        self.more_page().click()
        from page.test_more_page import MoreHomeAction
        return MoreHomeAction(self._driver)

    def hide_pop_title_text(self):  # 隐私弹窗标题文本断言
        return self.hide_pop_title().text

    def click_hide_pop_agree(self):  # 隐私弹窗点击同意(进入新用户引导页)
        self.hide_pop_agree().click()
        return self

    def newusers_guide_title_text(self):  # 新用户引导页title元素
        return self.newusers_guide_title().text

    def hide_pop_refuse_button(self):  # 隐私弹窗点击不同意
        self.hide_pop_refuse().click()
        return self

    def promt_pop_text(self):  # 隐私弹窗_提醒弹窗断言
        return self.hide_pop_promtpop().text

    def click_hide_pop_hidetreaty(self):  # 点击隐私弹窗上的隐私协议
        self.hide_pop_hidetreaty().click()
        return self

    def check_hidetreaty(self):  # 隐私协议顶部title断言
        return self.hidetreaty_title().text

    def click_hide_pop_sla(self):  # 点击隐私弹窗上的服务协议
        self.hide_pop_sla().click()
        return self

    def check_sla_text(self):  # 服务协议页顶部title
        return self.sla_title().text

    def click_accelerate_box_title(self):  # 点击盒子加速区块标题
        self.accelerate_box_title().click()
        return self

    def buy_now_text(self):  # 盒子加速页立即购买text
        return self.accelerate_box_buy_now().text

    def click_have_accelerate_box(self):  # 点击盒子加速页已有加速盒
        self.have_accelerate_box().click()
        return self
    def click_accelerate_phone_title(self):  # 新用户引导页点击手机加速区块标题
        self.accelerate_phone_title().click()
        return self

    def game_on_text(self):  # 手机加速页选择游戏button
        return self.accelerate_phone_game_on().text

    def click_accelerate_box_buy_now(self):  # 盒子加速页立即购买点击
        self.accelerate_box_buy_now().click()
        return self

    def click_safari_taobao_open(self):  # 点击浏览器加速盒淘宝页弹窗在"淘宝"中打开此页？弹窗的打开按钮
        self._driver.implicitly_wait(100)
        self.safari_taobao_open().click()
        return self

    def check_taobao_store(self):  # 检查【加入购物车】是否存在
        self._driver.implicitly_wait(100)
        return self.taobao_store().text

    def click_give_publicity_to_accelerate_box(self): # 点击了解加速盒
        self.give_publicity_to_accelerate_box().click()
        return self

    def connection_box_wifi_text(self):  # 请连接加速盒wifi文本
        return self.connection_box_wifi().text

    def logged_in_click_icon(self):  # 已登录点击icon
        self.phone_accelerate_icon().click()
        return self

    def click_phone_accelerate_list_search(self):  # 点击手机加速游戏搜索栏
        self.phone_accelerate_list_search().click()
        return self

    def click_phone_accelerate_search_tank(self):  # 点击手机加速游戏搜索栏输入tank
        self.phone_accelerate_list_search().send_keys('tank')
        return self

    def click_phone_accelerate_search_error_tank(self):  # 点击手机加速游戏搜索栏输入错误坦克
        self.phone_accelerate_list_search().send_keys('ceoeeeeee')
        return self

    def click_game_list_write_tank(self):  # 点击游戏列表页搜索输入tank
        self.game_list_search().send_keys('tank')
        return self

    def click_game_list_test(self):  # 点击游戏列表页'测试'游戏
        self.game_list_test().click()
        return self

    def click_accelerate_WiFi_button(self):  # 点击游戏列表页'WiFI'
        TouchAction(self._driver).tap(x=344,y=534).perform()
        return self

    def click_accelerate_button(self):  # 点击加速
        self.accelerate_button().click()
        return self

    def check_accelerate_fame(self):  # 声明弹窗title
        return self.accelerate_fame().text

    def click_fame_continue_to(self):  # 点击声明弹窗继续
        self.fame_continue_to().click()
        return self

    def click_fame_cancel_to(self):  # 点击声明弹窗取消
        self.fame_cancel_to().click()
        return self

    def click_confirm_fame_continue_to(self):  # 点击确认声明弹窗确定
        self.confirm_fame_continue_to().click()
        return self

    def click_cancel_fame_continue_to(self):  # 点击确认声明弹窗取消
        self.confirm_fame_cancel_to().click()
        return self

    def click_vpn_allow(self):  # 点击vpn弹窗允许
        self.vpn_allow().click()
        return self

    def click_vpn_close(self):  # 点击vpn弹窗不允许
        self.vpn_close().click()
        return self

    def check_vpn_pop_title(self):  # 添加vpn配置text
        return self.vpn_pop().text

    def click_add_vpn_configuration_determine(self):  # 配置vpn弹窗点击确定
        self.add_vpn_configuration_determine().click()
        return self

    def check_the_connection_tutorial(self):  # 查看连接教程title
        self._driver.implicitly_wait(5)
        return self.the_connection_tutorial().text

    def click_connection_tutorial_cancel(self):  # 点击连接教程关闭按钮
        self.connection_tutorial_cancel().click()
        return self

    def check_switch_accelerate_way(self):  # 查看切换加速方式text
        return self.switch_accelerate_way().text

    def check_please_4g(self):  # 查看请开启移动网络弹窗text
        return self.please_4g().text

    def not_logged_click_phone_accelerate_icon(self):  # 未登录点击手机加速页icon
        self.phone_accelerate_icon().click()
        from page.test_login_registration_page import LoginRegistrationAction
        return LoginRegistrationAction(self._driver)

    def not_logged_click_phone_accelerate_regional(self):  # 未登录点击首页切换游戏区服
        self.phone_accelerate_regional().click()
        from page.test_login_registration_page import LoginRegistrationAction
        return LoginRegistrationAction(self._driver)
