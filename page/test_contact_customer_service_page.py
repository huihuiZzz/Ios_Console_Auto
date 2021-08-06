from elment.contact_customer_service_element import ContactCustomerService
class ContactCustomerServiceAction(ContactCustomerService):  # 联系我们页操作
    def contact_customer_service_title_text(self):  # 联系我们页标题text
        return self.contact_customer_service_title().text
    def click_contact_customer_service_back(self): # 点击左上角返回 返回帮助中心页
        self.contact_customer_service_back().click()
        from page.test_help_center_page import HelpCenterAction
        return HelpCenterAction(self._driver)

