import random

from elment.login_registration_element import LoginRegistration
from page.test_verification_code_page import VerificationCodeAction
public_number_vip = ['17800000000','17800000001','17800000002','17800000003','17800000004','17800000005','17800000006',
                 '17800000007','17800000008','17800000009']

public_number_not_vip = ['18381939440', '18381939441', '18381939445', '18381939446']

class LoginRegistrationAction(LoginRegistration):  # 登录页操作

    def check_welcome_xunyou(self):  # 欢迎登陆迅游text
        return self.welcome_xunyou().text

    def click_welcome_xunyou(self):  # 点击欢迎登录迅游（可以将键盘降下去）
        self.welcome_xunyou().click()
        return self

    def logged_in_random(self):   # 点击号码栏输入随机账号
        self.phone_id().send_keys('1831111{}'.format(random.randint(1000,9999)))
        return self

    def logged_in_appoint(self):  # 登录随机vip
        self.phone_id().send_keys(str(random.sample(public_number_vip,1)))
        return self

    def logged_in_not_vip_appoint(self):  # 登录随机非会员账号
        self.phone_id().send_keys(str(random.sample(public_number_not_vip,1)))
        return self

    def logged_in_appoint_183(self):  # 登录18333334444
        self.phone_id().send_keys('18333334444')
        return self

    # def check_logged_in_title(self):  # 查看更多页已登录账号元素展示

    def click_verification_code(self):  # 点击获取验证码
        self.verification_code().click()
        return VerificationCodeAction(self._driver)

    def check_verification_code_enabled(self):  # 获取验证码按钮是否可点击
        return self.verification_code().is_enabled()

    def write_in_error_quantity(self):  # 输入多位手机号
        self.phone_id().send_keys('1399999219392s我！3')
        return self

    def number_quantity(self):  # 判断手机号位数
        return len(self.phone_id().text)

    def click_privacy_agreement(self):  # 点击登录页隐私协议入口
        self.privacy_agreement().click()
        return self

    def click_service_agreement(self):  # 点击登录页服务协议入口
        self.service_agreement().click()
        return self

    def click_exit_privacy_agreement(self):  # 点击隐私协议详情页左上角<
        self.exit_privacy_agreement().click()
        return self

    def click_exit_service_agreement(self):  # 点击服务协议详情页左上角<
        self.exit_service_agreement().click()
        return self

    def check_keyboard_Delete(self):  # 检查键盘Delete文本，可用来判断键盘是否存在
        return self.keyboard_Delete().text

    def logged_in_assert(self):  # 判断是否进入了登录页
        assert "欢迎登录迅游" in self.check_welcome_xunyou()
        return self

    def click_exit_logged_in(self):  # 点击登录页左上角<点击,在加速首页触发的登录，返回加速页
        self.exit_logged_in().click()
        from page.test_accelerate_page import AccelerateHomeAction
        return AccelerateHomeAction(self._driver)

    def click_default_area_code(self):  # 点击区号按钮
        self.default_area_code().click()
        return self

    def click_exit_area_code(self):  # 点击区号页左上角<，返回登录页
        self.exit_area_code().click()
        return self

    def click_switch_area_code(self):  # 点击区号页面阿富汗区号
        self.switch_area_code().click()
        return self

    def check_switch_area_code(self):  # 查看修改后的区号
        return self.switch_area_code().text

    def check_memory_logged_in_number(self):  # 查看账号记忆功能文本
        return self.memory_logged_in_number().text