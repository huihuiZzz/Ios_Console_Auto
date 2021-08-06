from elment.common_problem_element import CommonProblemPage

class CommonProblemAction(CommonProblemPage):  #  常见问题页操作
    def common_problem_title_text(self):  # 常见问题页标题问题
        return self.common_problem_title().text

    def click_common_problem_back(self):  # 常见问题页左上角 <，执行后返回至帮助中心页
        self.common_problem_back().click()
        from page.test_help_center_page import HelpCenterAction
        return HelpCenterAction(self._driver)