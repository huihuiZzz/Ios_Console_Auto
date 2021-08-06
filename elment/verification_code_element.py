from App.App_start import BassPage

class VerificationCodePage(BassPage):  # 验证码页

    def verificationcode_one(self):  # 验证码页第一个
        return self._driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="迅游主机加速"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText')

    def verificationcode_two(self):  # 验证码页第二个
        return self._driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="迅游主机加速"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText')


    def verificationcode_thirty(self):  # 验证码页第三个
        return self._driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="迅游主机加速"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText')


    def verificationcode_four(self):  # 验证码页第四个
        return self._driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="迅游主机加速"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText')


    def please_enter_the_verification_code(self):  # 请输入验证码
        return self._driver.find_element_by_name("请输入验证码")

    def count_down(self):  # 倒计时
        case = self._driver.find_elements_by_class_name('XCUIElementTypeButton')
        return case[-1]

    def new_user_pop_close(self):  # 新用户会员弹窗右上角'x'按钮
        case = self._driver.find_elements_by_name('alert x close')
        return case

    def free_vip_pop(self):  # 会员已到账title
        return self._driver.find_element_by_name('会员已到账')

    def go_accelerate(self):  # 去加速button
        case = self._driver.find_elements_by_name('去加速')
        return case[0]

#//XCUIElementTypeApplication[@name="迅游主机加速"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText')
