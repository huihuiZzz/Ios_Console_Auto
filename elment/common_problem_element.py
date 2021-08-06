from App.App_start import BassPage
class CommonProblemPage(BassPage): # 常见问题页
    def common_problem_title(self):  # 页面标题
        case=self._driver.find_elements_by_name("常见问题")
        return case[1]
    def common_problem_back(self):  # 页面左上角 <
        return self._driver.find_element_by_xpath('//XCUIElementTypeNavigationBar[@name="常见问题"]/XCUIElementTypeButton[1]')