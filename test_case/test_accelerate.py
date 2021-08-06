import allure

from App.App_start import BassPage
import pytest


@allure.feature('加速相关')
class TestAccelerate:

    @allure.story('搜索有结果显示')
    @pytest.mark.p0
    def test_search_results(self):
        succeed = BassPage().public_logged_in_random().start().logged_in_click_icon().\
            click_phone_accelerate_search_tank().judge_element_exist('坦克世界')
        assert True is succeed

    @allure.story('搜索无结果显示')
    @pytest.mark.p0
    def test_search_not_results(self):
        succeed = BassPage().public_logged_in_random().start().logged_in_click_icon(). \
            click_phone_accelerate_search_error_tank().judge_element_exist('ceoeeeeee')
        assert False is succeed

    @allure.story('加速成功弹出【连接教程】弹窗')
    @pytest.mark.p0
    def test_check_connect_the_tutorial(self):
        succeed = BassPage().public_logged_in_random().start().logged_in_click_icon().click_game_list_test().\
            click_game_list_test().click_accelerate_WiFi_button().click_accelerate_button().click_fame_continue_to(). \
            click_vpn_allow().check_the_connection_tutorial()
        assert "连接教程" == succeed

    @allure.story('未选择游戏【加速方式】可以切换')
    @pytest.mark.skip
    def test_check_connect_the_tutorial(self):
        succeed = BassPage().public_logged_in_random().start().logged_in_click_icon().click_game_list_test(). \
            click_accelerate_WiFi_button().click_accelerate_button().click_fame_continue_to(). \
            click_vpn_allow().check_the_connection_tutorial()
        assert "连接教程" == succeed

    @allure.story('非数据状态下，加速热点游戏弹出【请开启移动网络】弹窗')
    @pytest.mark.p0
    def test_check_accelerate_way(self):
        succeed = BassPage().public_logged_in_random().start().logged_in_click_icon().click_game_list_test(). \
            click_game_list_test().click_accelerate_button().check_please_4g()
        assert "请开启移动网络" == succeed

    @allure.story('未授权VPN，点击【加速】按钮，出现【声明】弹窗')
    @pytest.mark.p0
    def test_check_statement(self):
        succeed = BassPage().public_logged_in_random().start().logged_in_click_icon().click_game_list_test(). \
                    click_accelerate_WiFi_button().click_accelerate_button().check_accelerate_fame()
        assert "声明" == succeed

    @allure.story('点击【允许】按钮弹出添加VPN成功返回【手机加速】页，开始加速')
    @pytest.mark.p0
    def test_vpn_allow_auto_accelerate(self):
        succeed = BassPage().public_logged_in_xunyou_vip().start().logged_in_click_icon().click_game_list_test(). \
            click_accelerate_WiFi_button().click_accelerate_button().click_fame_cancel_to().\
            click_confirm_fame_continue_to().click_fame_continue_to().click_vpn_allow().check_the_connection_tutorial()
        assert "连接教程" == succeed

    @allure.story('点击【确定】按钮弹出【添加VPN配置】弹窗')
    @pytest.mark.p0
    def test_vpn_allow_auto_accelerate(self):
        succeed = BassPage().public_logged_in_xunyou_vip().start().logged_in_click_icon().click_game_list_test(). \
            click_accelerate_WiFi_button().click_accelerate_button().click_fame_cancel_to(). \
            click_confirm_fame_continue_to().click_fame_continue_to().click_vpn_close().\
            click_add_vpn_configuration_determine().check_vpn_pop_title()
        assert '“XunyouConsoleBooster”想添加VPN配置' == succeed