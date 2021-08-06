from App.App_start import BassPage
class HelpCenterPage(BassPage):  # 帮助中心页
    def help_center_title_text(self):  # 标题文本
        case=self._driver.find_elements_by_name('帮助中心')
        return case[1]
    def help_center_common_problem(self):
        return self._driver.find_element_by_name("常见问题")
    def help_center_contact_customer_service(self):
        return self._driver.find_element_by_name("联系客服")