import allure

from App.App_start import BassPage
import pytest

@allure.feature('更多')
class TestMore:

    @allure.story('点击【更多】可以进入【更多】页面')
    @pytest.mark.p0
    def test_click_help_center(self):
        succeed = BassPage().start_accelerate().open_more().check_help_center()
        assert "帮助中心" == succeed

    @allure.story('点击【常见问题】可以进入【常见问题】页面')
    @pytest.mark.p0
    def test_click_faq(self):
        succeed = BassPage().start_accelerate().open_more().click_help_center().click_common_problem(). \
            click_common_problem_back().help_center_title()
        assert "帮助中心" == succeed

    @allure.story('点击【联系客服 】按钮可以进入【联系我们】页面')
    @pytest.mark.p0
    def test_click_contact_customer_service(self):
        succeed = BassPage().start_accelerate().open_more().click_help_center().click_contact_customer_service(). \
            click_contact_customer_service_back().help_center_title()
        assert "帮助中心" == succeed

    @allure.story('点击【帮助中心】按钮，进入【帮助中心】页面')
    @pytest.mark.p0
    def test_open_click_help_center(self):
        succeed = BassPage().start_accelerate().open_more().click_help_center().help_center_title()
        assert "帮助中心" == succeed

    @allure.story('用户未登陆点击【我的加速盒】跳转到登陆页面')
    @pytest.mark.p0
    def test_not_logged_click_my_box(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().not_logged_in_click_my_box().\
            check_welcome_xunyou()
        assert "欢迎登录迅游" == succeed

    @allure.story('用户已登录点击【我的加速盒】进入【我的加速盒】页面')
    @pytest.mark.p0
    def test_logged_in_click_my_box(self):
        succeed = BassPage().public_logged_in_vip().get_into_more().logged_in_my_box().my_box_title_text()
        assert "我的加速盒" == succeed

    @allure.story('用户未绑定加速盒，点击【我的加速盒】页面【去绑定】按钮跳转到【连接加速盒WiFi】页面')
    @pytest.mark.p0
    def test_not_tie_box_logged_in_click_my_box(self):
        succeed = BassPage().public_logged_in_vip().get_into_more().logged_in_my_box().click_go_tie_box().\
            connection_box_wifi_text()
        assert "连接加速盒WiFi" == succeed

        # 点击【我的加速盒】的【上报日志】按钮toast【上报成功】
        #
        # 30s内再次点击【上报日志】提示【请勿重复上报】
        #
        # 加速盒联网，点击【固件版本】按钮弹出【发现新版本】弹窗
        #
        # 点击【立即升级】按钮升级成功弹出【升级成功】弹窗
        #
        # 加速盒不需要升级，点击【固件版本】按钮toast【当前已是最新版本】
        #
        # 非会员点击【开始加速】跳转到会员页面
        #
        # 会员点击【开始加速】弹出【加速盒有新版本】弹窗
        #
        # 点击【去升级】按钮跳转到【我的加速盒】页面自动点击【固件版本】按钮
        #
        # 点击【WiFi设置】按钮进入【WiFi设置】页面
        #
        # 输入内容合规点击【保存】按钮弹出【确定保存】弹窗
        #
        # 用户已绑定加速盒，点击【加速盒解绑】按钮弹出【确定解绑加速盒】弹框
        #
        # 点击【确定】按钮可以关闭弹框返回【更多】页面

    @allure.story('输入有效手机号，点击【获取验证码】可以收到验证码（获取验证码后按钮不可点击）')
    @pytest.mark.p0
    def test_obtain_verification_code(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().click_not_logged_in().logged_in_random() \
            .click_verification_code().judge_verification_code_time()
        assert False is succeed

    @allure.story('手机号最多可输入11位数字')
    @pytest.mark.p0
    def test_number_quantity(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().click_not_logged_in()\
            .write_in_error_quantity().number_quantity()
        assert 11 == succeed

    @allure.story('输入正确格式的手机号，点击【获取验证码】按钮')
    @pytest.mark.p0
    def test_click_obtain_verification_code(self):
        succeed = BassPage().start().open_more().click_not_logged_in().logged_in_random()\
            .click_verification_code().check_please_enter_the_verification_code()
        assert '请输入验证码' == succeed

    @allure.story('【输入验证码】页面输入正确的验证码，自动登录成功')
    @pytest.mark.p0
    def test_sign_in_success(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().click_not_logged_in(). \
            logged_in_random().click_verification_code().write_in_correct_verification_code(). \
            if_new_user_pop_close().check_logged_in_title()
        assert '183' in succeed

    @allure.story('【登录页面】点击【服务协议】按钮可以跳转到服务协议页面')
    @pytest.mark.p0
    def test_click_logged_service_agreement(self):
        succeed = BassPage().first_start_box_accelerate().open_more().click_not_logged_in().click_welcome_xunyou().\
            click_service_agreement().click_exit_service_agreement().check_keyboard_Delete()
        assert "Delete" == succeed

    @allure.story('【登录页面】点击【隐私协议】按钮可以跳转到隐私协议页面')
    @pytest.mark.p0
    def test_click_logged_privacy_agreement(self):
        succeed = BassPage().start().open_more().click_not_logged_in().click_welcome_xunyou().\
            click_privacy_agreement().click_exit_privacy_agreement().check_keyboard_Delete()
        assert "Delete" == succeed

    @allure.story('点击【未登录】状态卡片可以跳转到【登录】页面')
    @pytest.mark.p0
    def test_click_not_logged_in(self):
        succeed = BassPage().start().open_more().click_not_logged_in().check_keyboard_Delete()
        assert "Delete" == succeed

    @allure.story('触发【输入手机号】页面的时机')
    @pytest.mark.p0
    def test_check_enter_phone_number(self):
        BassPage().start().not_logged_click_phone_accelerate_icon().logged_in_assert().click_exit_logged_in().\
            not_logged_click_phone_accelerate_icon().logged_in_assert()

    @allure.story('【输入手机号】页面点击【服务协议】按钮进入【服务协议】页面')
    @pytest.mark.p0
    def test_service_agreement_back(self):
        succeed = BassPage().start().open_more().click_not_logged_in().click_welcome_xunyou(). \
                    click_service_agreement().click_exit_service_agreement().check_welcome_xunyou()
        assert "欢迎登录迅游" == succeed

    @allure.story('【输入手机号】页面点击【隐私协议】按钮进入【隐私协议】页面')
    @pytest.mark.p0
    def test_privacy_agreement_back(self):
        succeed = BassPage().start().open_more().click_not_logged_in().click_welcome_xunyou(). \
                    click_privacy_agreement().click_exit_privacy_agreement().check_welcome_xunyou()
        assert "欢迎登录迅游" == succeed

    @allure.story('点击【区号】，进入【区号设置】页面')
    @pytest.mark.p0
    def test_privacy_agreement_back_button(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().click_not_logged_in().\
            click_default_area_code().click_exit_area_code().check_welcome_xunyou()
        assert "欢迎登录迅游" == succeed

    @allure.story('选择区号后返回【输入手机号】页面，区号变更为选择的区号')
    @pytest.mark.p0
    def test_click_area_code(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().click_not_logged_in().click_default_area_code().\
            click_switch_area_code().check_switch_area_code()
        assert "+93" == succeed

    @allure.story('已登录点击用户卡片可以进入【账号设置】页面')
    @pytest.mark.p0
    def test_get_number_setting(self):
        succeed = BassPage().public_logged_in_vip().start().open_more().click_logged_in_title().\
            click_exit_get_number_setting().check_logged_in_title()
        assert "183" in succeed

    @allure.story('点击【确定退出】按钮可以退出账号并回到【更多】页面')
    @pytest.mark.p0
    def test_quit_number_setting(self):
        succeed = BassPage().public_logged_in_vip().start().open_more().click_logged_in_title().click_exit_sign_in().\
            click_exit_sign_in_determine().check_not_logged_in()
        assert "未登录" == succeed

    @allure.story('点击用户卡片进入账号设置页面')
    @pytest.mark.p0
    def test_get_into_setting(self):
        succeed = BassPage().public_logged_in_vip().start().open_more().click_logged_in_title().\
            check_get_number_setting()
        assert "账号设置" == succeed

    @allure.story('退出登录后本地记录此次登录手机号')
    @pytest.mark.skip
    def test_log_out_memory(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().click_not_logged_in() \
            .logged_in_appoint_183().click_verification_code().write_in_correct_verification_code()\
            .click_logged_in_title().click_exit_sign_in().click_exit_sign_in_determine().click_not_logged_in()\
            .check_memory_logged_in_number()
        assert '18333334444' == succeed

    @allure.story('点击退出登录弹出确认退出弹窗')
    @pytest.mark.p0
    def test_click_log_out(self):
        succeed = BassPage().public_logged_in_vip().start().open_more(). \
            click_logged_in_title().click_exit_sign_in().check_confirm_exit_pop()
        assert '确定退出?' == succeed

    @allure.story('点击取消关闭确认退出弹窗')
    @pytest.mark.p0
    def test_click_log_out_cancel(self):
        succeed = BassPage().public_logged_in_vip().start().open_more(). \
            click_logged_in_title().click_exit_sign_in().click_exit_sign_in_cancel().check_exit_sign_in()
        assert '退出登录' == succeed

    @allure.story('点击【了解迅游】进入了解迅游页面')
    @pytest.mark.p0
    def test_click_understand_xunyou(self):
        succeed = BassPage().start().open_more().click_understand_xunyou().check_about_xunyou_title()
        assert '关于迅游' == succeed
    #
    @allure.story('点击【了解迅游】页面【微信公众号】按钮，出现【微信公众号】弹窗')
    @pytest.mark.p0
    def test_understand_xunyou_wechat(self):
        succeed = BassPage().start().open_more().click_understand_xunyou().click_understand_xunyou_wechat_pop().\
            check_follow_xunyou_console_accelerate()
        assert '关注迅游主机加速' == succeed

    @allure.story('服务端已配置QQ群，点击【加入QQ群】按钮跳转到手机QQ客户端')
    @pytest.mark.p0
    def test_jump_QQ_group(self):
        succeed = BassPage().start().open_more().click_understand_xunyou().click_join_QQ_group(). \
            check_QQ_group()
        assert '迅游主机加速用户群' == succeed