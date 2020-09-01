# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome
from WebClass.ChromeClass.ReuseChrome import ReuseChrome
from WebClass.ChromeClass.MyChrome import MyChrome
from time import sleep

# driver1 = Chrome()
# executor_url = driver1.command_executor._url
# session_id = driver1.session_id
# print(session_id)
# print(executor_url)
# driver1.get("https://www.baidu.com/")

# del driver1
# sleep(3)
# # 通过session id 打开获取浏览器
# driver2 = ReuseChrome(command_executor=executor_url, session_id=session_id)
# # driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
# driver2.session_id = session_id
# print(driver2.current_url)
# print(driver2.title)


# ********************测试方法judge_open_web_page_by_title********************
# driver1 = MyChrome()
# driver1.create("www.baidu.com")
# print(driver1.title)
# res = driver1.judge_open_web_page_by_title("百度一下，你就知道")
# res = driver1.judge_open_web_page_by_title("百度一下，你就知")
# res = driver1.judge_open_web_page_by_title("百度一下，你就知",regex=False)
# res = driver1.judge_open_web_page_by_title("一下，你就知",regex=False)
# print(res)
# driver1.quit()
# ********************测试方法judge_open_web_page_by_title********************

# ********************测试方法********************
driver1 = MyChrome()
driver1.create("www.baidu.com")
test_element = driver1.add_element_attribute(xpath=['//*[@id="kws"]','//*[@id="kw"]'])
# test_element = driver1.add_element_attribute(id="kw")

test_element.send_keys("123")
sleep(2)
print(test_element)
print(type(test_element))
driver1.quit()
# ********************测试方法********************



