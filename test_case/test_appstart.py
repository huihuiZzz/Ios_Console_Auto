import allure

from App.App_start import BassPage
import pytest

@allure.feature('App启动')
class TestAppStart:

    @allure.story('首次启动APP，出现【隐私提醒】弹窗')
    @pytest.mark.p0
    def test_hide_pop(self):
        succeed = BassPage().first_start().hide_pop_title_text()
        assert "欢迎使用迅游主机加速APP" == succeed

    @allure.story('【隐私提醒】弹窗点击【隐私协议】按钮进入到【隐私协议】页面')
    @pytest.mark.p0
    def test_hide_pop_hide_treaty(self):
        succeed = BassPage().first_start().click_hide_pop_hidetreaty().check_hidetreaty()
        assert "隐私协议" == succeed

    @allure.story('【隐私提醒】弹窗点击【服务协议】按钮进入到【服务协议】页面')
    @pytest.mark.p0
    def test_hide_pop_sla(self):
        succeed = BassPage().first_start().click_hide_pop_sla().check_sla_text()
        assert "服务协议" == succeed

    @allure.story('【隐私提醒】弹窗点击【同意】按钮，之后启动APP不再显示此弹窗')
    @pytest.mark.p0
    def test_check_hide_pop(self):
        succeed = BassPage().first_start().click_hide_pop_agree().start().newusers_guide_title_text()
        assert "迅游为您提供两种主机加速方式" == succeed

    @allure.story('【隐私提醒】弹窗点击【不同意】按钮，出现【提示】弹窗')
    @pytest.mark.p0
    def test_hide_pop_prompt_pop(self):
        succeed = BassPage().first_start().hide_pop_refuse_button().promt_pop_text()
        assert '您需要同意迅游主机加速隐私协议，才能使用APP，否则我们无法为您提供服务。' == succeed

    @allure.story('【点击【隐私协议】弹窗的【同意】按钮，进入【新用户引导】页')
    @pytest.mark.p0
    def test_new_users_guide(self):
        succeed = BassPage().first_start().click_hide_pop_agree().newusers_guide_title_text()
        assert "迅游为您提供两种主机加速方式" == succeed

    @allure.story('点击【盒子加速区块】进入【盒子加速】页')
    @pytest.mark.p0
    def test_accelerate_box_page(self):
        succeed = BassPage().first_start().click_hide_pop_agree().click_accelerate_box_title().buy_now_text()
        assert "立即购买" == succeed

    @allure.story('点击【手机加速区块】进入【手机加速】页')
    @pytest.mark.p0
    def test_accelerate_phone_page(self):
        succeed = BassPage().first_start().click_hide_pop_agree().click_accelerate_phone_title().game_on_text()
        assert "选择游戏" == succeed

    @allure.story('已安装淘宝，点击【宣传语】吊起淘宝APP，打开宝贝详情页')
    @pytest.mark.p0
    def test_click_box_give_publicity_to(self):
        succeed = BassPage().first_start().click_hide_pop_agree().click_give_publicity_to_accelerate_box(). \
            click_safari_taobao_open().check_taobao_store()
        assert "加入购物车" == succeed

    # 冷启动APP获取ABtest配置

