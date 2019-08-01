from selenium import webdriver
import time
import unittest


class webUiTest(unittest.TestCase):
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('测试结束')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('开始进行测试')

    def test_a_run(self):
        browser = webdriver.Chrome()
        browser.get("http://oppotester.myoppo.com/PhenixSign/login.php")
        time.sleep(10)
        login_empid = browser.find_element_by_id("login_empid")
        login_empid.clear()
        time.sleep(1)
        login_empid.send_keys("80243057")
        time.sleep(3)
        login_password = browser.find_element_by_id("login_password")
        time.sleep(1)
        login_password.clear()
        time.sleep(3)
        login_password.send_keys("123456")
        time.sleep(1)
        logging_btn = browser.find_element_by_id("login_ok")
        logging_btn.click()
        time.sleep(5)
        every_day = browser.find_element_by_id("bjui-hnav-tree1_2_span")
        every_day.click()
        time.sleep(5)
        sign_in = browser.find_element_by_xpath("//*[@id='j_custom_form']/div[2]/ul/li[2]/button")
        sign_in.click()
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()
