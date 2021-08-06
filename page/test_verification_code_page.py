from elment.verification_code_element import VerificationCodePage

class VerificationCodeAction(VerificationCodePage):  # 验证码页操作
    def write_in_correct_verification_code(self):  # 输入1234正确验证码
        self.verificationcode_one().send_keys(1)
        self.verificationcode_two().send_keys(2)
        self.verificationcode_thirty().send_keys(3)
        self.verificationcode_four().send_keys(4)
        return self
    def write_in_error_verification_code(self):  # 输入2345验证码
        self.verificationcode_one().send_keys(2)
        self.verificationcode_two().send_keys(3)
        self.verificationcode_thirty().send_keys(4)
        self.verificationcode_four().send_keys(5)
        from page.test_more_page import MoreHomeAction
        return MoreHomeAction(self._driver)

    def check_please_enter_the_verification_code(self):  # 检查请输入验证码text
        return self.please_enter_the_verification_code().text

    def judge_verification_code_time(self):  # 判断验证码页倒计时内是否可点击
        return self.count_down().is_enabled()

    def if_new_user_pop_close(self):  # 有新用户弹窗的话就关闭
        self._driver.implicitly_wait(5)
        if self.new_user_pop_close():
            self.new_user_pop_close()[0].click()
        from page.test_more_page import MoreHomeAction
        return MoreHomeAction(self._driver)

    def free_vip_pop_title(self):  # 检查会员3天弹窗的文案
        return self.free_vip_pop().text

    def click_go_accelerate(self):  # 点击去加速
        self.go_accelerate().click()
        from page.test_accelerate_page import AccelerateHomeAction
        return AccelerateHomeAction(self._driver)