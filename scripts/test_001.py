import allure
import pytest
class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="例子")
    def test_001_1(self):
        # allure.attach("用户名","花花")
        # allure.attach("密码","123456")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="例子")
    def test_001_2(self):
        # allure.attach("用户名","花花")
        # allure.attach("密码","123456")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="例子")
    def test_001_3(self):
        # allure.attach("用户名","花花")
        # allure.attach("密码","123456")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="例子")
    def test_001_4(self):
        # allure.attach("用户名","花花")
        # allure.attach("密码","123456")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="例子")
    def test_001_5(self):
        # allure.attach("用户名","花花")
        # allure.attach("密码","123456")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="例子")
    def test_001_6(self):
        # allure.attach("用户名","花花")
        # allure.attach("密码","123456")
        assert False