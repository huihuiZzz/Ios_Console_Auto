from App.App_start import BassPage
class MyBox(BassPage):  # 我的加速盒页
    def my_box_title(self):  #页面标题
        case = self._driver.find_elements_by_name("我的加速盒")
        return case[1]

    def got_tie_box(self):
        return self._driver.find_element_by_name("去绑定")