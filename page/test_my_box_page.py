from elment.my_box_elment import MyBox
from page.test_accelerate_page import AccelerateHomeAction
class MyBoxAction(MyBox):  # 我的加速盒页操作
    def my_box_title_text(self):  # 我的加速盒页title文本
        return self.my_box_title().text

    def click_go_tie_box(self):  # 点击去绑定
        self.got_tie_box().click()
        return AccelerateHomeAction(self._driver)