import allure, pytest
class Test_allure:
    def setup(self):
        pass
    def teardown(self):
        pass
    @allure.step('我是测试步骤001')
    def test_al(self, a):
        assert a !=2