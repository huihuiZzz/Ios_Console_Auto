from App.App_start import BassPage
class LoginRegistration(BassPage):  # 登陆/注册页
    def welcome_xunyou(self):  # 欢迎登陆迅游文本
        return self._driver.find_element_by_name("欢迎登录迅游")
    def phone_id(self):  # 手机号码栏
        return self._driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="迅游主机加速"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField')
    def verification_code(self):  # 获取验证码button
        return self._driver.find_element_by_name("获取验证码")

    def privacy_agreement(self):  # 登录页隐私协议按钮
        case = self._driver.find_elements_by_name("隐私协议")
        return case[1]

    def service_agreement(self):  # 登录页服务协议按钮
        case = self._driver.find_elements_by_name("服务协议")
        return case[1]

    def logged_privacy_agreement(self):  # 登录页隐私协议详情页标题
        case = self._driver.find_elements_by_name("隐私协议")
        return case[1]

    def logged_service_agreement(self):  # 登录页服务协议详情页标题
        case = self._driver.find_elements_by_name("服务协议")
        return case[1]

    def exit_privacy_agreement(self):  # 隐私协议详情页左上角"<"
        return self._driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="隐私协议"]/XCUIElementTypeButton[1]')

    def exit_service_agreement(self):  # 服务协议详情页左上角"<"
        return self._driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="服务协议"]/XCUIElementTypeButton[1]')

    def keyboard_Delete(self):  # 键盘的Delete键 ，可以用来判断键盘是否弹出
        return self._driver.find_element_by_name('Delete')

    def exit_logged_in(self):  # 登录页左上角<键
        return self._driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="XunyouConsoleBooster.GCMLoginVC"]/XCUIElementTypeButton')

    def default_area_code(self):  # 区号按钮
        case = self._driver.find_elements_by_class_name('XCUIElementTypeButton')
        return case[6]

    def exit_area_code(self):  # ,区号页左上角<
        return self._driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="选择国家和地区"]/XCUIElementTypeButton')

    def switch_area_code(self):  # 登录页选择93后的区号栏
        return self._driver.find_element_by_name('+93')

    def memory_logged_in_number(self):  # 记录登录过的手机号
        return self._driver.find_element_by_ios_predicate('value == "18333334444"')