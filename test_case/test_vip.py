import allure

from App.App_start import BassPage
import pytest
@allure.feature('会员')
class TestVip:

    @allure.story('已登录会员账号【用户状态卡片】显示【立即续费】按钮')
    @pytest.mark.p0
    def test_vip_check_renew_now(self):
        succeed = BassPage().public_logged_in_xunyou_vip().check_renew_now()
        assert "立即续费" == succeed

    @allure.story('点击【成为会员】按钮跳转到【购买】页面')
    @pytest.mark.p0
    def test_click_become_a_member(self):
        succeed = BassPage().public_logged_not_in_xunyou_vip().click_become_a_member().check_buy_now()
        assert "立即购买" == succeed

    @allure.story('点击【立即购买】按钮进入购买流程')
    @pytest.mark.p0
    def test_click_buy_now(self):
        succeed = BassPage().public_logged_not_in_xunyou_vip().click_become_a_member().click_buy_now().check_subscribe()
        assert "订阅" == succeed

    @allure.story('点击【立即续费】按钮跳转到【购买】页面')
    @pytest.mark.p0
    def test_click_immediately_a_renewal(self):
        succeed = BassPage().public_logged_in_xunyou_vip().click_renew_now().check_buy_now()
        assert "立即购买" == succeed

    @allure.story('新用户登录APP，弹出【领取成功】弹窗')
    @pytest.mark.p0
    def test_check_get_the_success(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().click_not_logged_in().logged_in_random(). \
            click_verification_code().write_in_correct_verification_code().free_vip_pop_title()
        assert "会员已到账" == succeed

    @allure.story('【领取成功】弹窗点击【去加速】按钮进入【加速】页面')
    @pytest.mark.p0
    def test_click_go_to_accelerate(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().click_not_logged_in().logged_in_random(). \
            click_verification_code().write_in_correct_verification_code().click_go_accelerate().game_on_text()
        assert "选择游戏" == succeed

    @allure.story('用户已经领取过试用，无法领取试用时间')
    @pytest.mark.p0
    def test_not_new_vip_free_time(self):
        succeed = BassPage().first_start_phone_accelerate().open_more().click_not_logged_in().\
            logged_in_not_vip_appoint().click_verification_code().write_in_correct_verification_code().\
            judge_element_exist('会员已到账')
        assert False is succeed

    @allure.story('点击【使用会员兑换码】按钮，跳转至内部【兑换会员】页面')
    @pytest.mark.p0
    def test_click_buy_now(self):
        succeed = BassPage().public_logged_in_xunyou_vip().click_renew_now().slide().click_vip_exchange_code().\
            click_exit_exchange_code().check_buy_now()
        assert "立即购买" == succeed
