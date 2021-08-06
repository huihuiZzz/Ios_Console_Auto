from elment.help_center_elment import HelpCenterPage
from page.test_common_problem_page import CommonProblemAction
from page.test_contact_customer_service_page import ContactCustomerServiceAction
class HelpCenterAction(HelpCenterPage): #  帮助中心页操作
    def help_center_title(self):  # 帮助中心顶部title
        return self.help_center_title_text().text

    def click_common_problem(self):  # 点击常见问题栏进入常见问题页
        self.help_center_common_problem().click()
        return CommonProblemAction(self._driver)  # 返回进入常见问题页

    def click_contact_customer_service(self):  # 点击联系客服进入联系客服页
        self.help_center_contact_customer_service().click()
        return ContactCustomerServiceAction(self._driver)

