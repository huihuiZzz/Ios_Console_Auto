from App.App_start import BassPage
class ContactCustomerService(BassPage):
    def contact_customer_service_title(self):  # 联系我们页
        case = self._driver.find_elements_by_name("联系我们")
        return case[1]
    def contact_customer_service_back(self):  # 左上角  <
        return self._driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="联系我们"]/XCUIElementTypeButton[1]')