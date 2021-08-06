from App.App_start import BassPage
class AccelerateHomePage(BassPage):  #  更多页
    def more_page(self): # 更多icon
        return self._driver.find_element_by_xpath("//*[@name='更多']")

    def hide_pop_title(self):  # 隐私弹窗标题
        return self._driver.find_element_by_name("欢迎使用迅游主机加速APP")

    def hide_pop_agree(self):  # 隐私弹窗同意button
        return self._driver.find_element_by_name("同意")

    def hide_pop_refuse(self):  # 隐私弹窗不同意button
        return self._driver.find_element_by_name("不同意")

    def newusers_guide_title(self):  # 选择加速方式页title(新用户引导页)
        return self._driver.find_element_by_name('迅游为您提供两种主机加速方式')

    def hide_pop_promtpop(self):  # 隐私弹窗_提醒弹窗
        return self._driver.find_element_by_name('您需要同意迅游主机加速隐私协议，才能使用APP，否则我们无法为您提供服务。')

    def hide_pop_hidetreaty(self):  # 隐私弹窗内的《隐私协议》元素
        return self._driver.find_element_by_name('《隐私协议》')

    def hidetreaty_title(self):  # 隐私协议页标题
        case = self._driver.find_elements_by_name('隐私协议')
        return case[1]

    def hide_pop_sla(self):  # 隐私弹窗内的《服务协议》元素
        return self._driver.find_element_by_name('《服务协议》')

    def sla_title(self):  # 服务协议页标题
        case = self._driver.find_elements_by_name('服务协议')
        return case[1]

    def accelerate_box_title(self):  # 新用户引导页盒子加速区块标题
        return self._driver.find_element_by_name("用盒子加速 PS4/PS5/NS/Xbox")

    def accelerate_box_buy_now(self):  # 盒子加速页立即购买button
        return self._driver.find_element_by_name("立即购买")

    def have_accelerate_box(self):
        case = self._driver.find_elements_by_name("已有加速盒")
        return case[1]

    def accelerate_phone_title(self):  # 新用户引导页手机加速区块标题
        return self._driver.find_element_by_name("用手机加速 NS")

    def give_publicity_to_accelerate_box(self):  # 新用户引导页了解加速盒button
        return self._driver.find_element_by_name("了解加速盒")

    def accelerate_phone_game_on(self):  # 手机加速页选择游戏Button
        return self._driver.find_element_by_name('选择游戏')

    def safari_taobao_open(self):  # 加速盒淘宝页弹窗在"淘宝"中打开此页？弹窗的打开按钮
        return self._driver.find_element_by_name("打开")

    def taobao_store(self):  # 淘宝【加入购物车】button
        return self._driver.find_element_by_name("加入购物车")

    def connection_box_wifi(self):  # 盒子页请连接wifi
        return self._driver.find_element_by_name("连接加速盒WiFi")

    def phone_accelerate_icon(self):  # 手机加速icon
        case = self._driver.find_elements_by_class_name('XCUIElementTypeButton')
        return case[5]

    def phone_accelerate_regional(self):  # 加速区服
        return self._driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="迅游主机加速"]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeButton')

    def phone_accelerate_button(self):  # 手机加速页加速按钮
        case = self._driver.find_element_by_name('加速')
        return case[1]

    def phone_accelerate_list_search(self):  # 手机加速游戏列表搜索栏
        case = self._driver.find_elements_by_name('搜索')
        return case[0]

    def game_list_search(self):  # 游戏列表页搜索栏
        case = self._driver.find_elements_by_name('搜索')
        return case[0]

    def game_list_tank_world(self):  # 游戏列表页搜索坦克世界结果游戏图标
        case = self._driver.find_elements_by_name('坦克世界')
        return case[0]

    def game_list_test(self):  # 游戏列表页搜索测试结果游戏图标
        case = self._driver.find_elements_by_name('测试')
        return case[0]

    def accelerate_button(self):  # 游戏列表页搜索测试结果游戏图标
        case = self._driver.find_elements_by_name('加速')
        return case[1]

    def accelerate_WiFi_button(self):  # 手机加速页wifi
        return self._driver.find_element_by_name('WIFI')

    def accelerate_fame(self):  # 声明弹窗title
        return self._driver.find_element_by_name('声明')

    def fame_continue_to(self):  # 声明弹窗继续button
        case = self._driver.find_elements_by_name('继续')
        return case[0]

    def fame_cancel_to(self):  # 声明弹窗取消button
        case = self._driver.find_elements_by_name('取消')
        return case[0]

    def confirm_fame_continue_to(self):  # 确认声明弹窗继续button
        case = self._driver.find_elements_by_name('确定')
        return case[0]

    def confirm_fame_cancel_to(self):  # 确认声明弹窗继续button
        case = self._driver.find_elements_by_name('取消')
        return case[0]

    def vpn_pop(self):  # vpn弹窗title
        case = self._driver.find_elements_by_name('“XunyouConsoleBooster”想添加VPN配置')
        return case[1]

    def vpn_allow(self):  # vpn弹窗允许button
        return self._driver.find_element_by_name('允许')

    def vpn_close(self):  # vpn弹窗不允许button
        return self._driver.find_element_by_name('不允许')

    def add_vpn_configuration_determine(self):  # 添加vpn配置弹窗确定
        case = self._driver.find_elements_by_name('确定')
        return case[0]

    def the_connection_tutorial(self):  # 连接教程title
        case = self._driver.find_elements_by_name('连接教程')
        return case[0]

    def add_vpn_configuration_cancel(self):  # 添加vpn配置弹窗取消
        case = self._driver.find_elements_by_name('取消')
        return case[0]

    def connection_tutorial_cancel(self):  # 连接教程关闭
        return self._driver.find_element_by_name('crowss')

    def switch_accelerate_way(self):  # 切换加速方式text
        return self._driver.find_element_by_name('切换加速方式')

    def please_4g(self):  # 请开启移动网络text
        return self._driver.find_element_by_name('请开启移动网络')