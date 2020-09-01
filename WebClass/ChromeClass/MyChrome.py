# -*- coding:utf-8 -*-
from selenium.webdriver import Chrome as WebDriver
import warnings


class MyChrome(WebDriver):
    def __init__(self):
        WebDriver.__init__(self)

    def create(self, url):
        """
        打开指定url
        :param url:网址
        :return:
        """
        if url.startswith('www'): url = "https://" + url
        self.get(url)

    def judge_open_web_page_by_title(self, title, regex=True, times=1) -> bool:
        """
        根据title判断网页是否打开
        :param title:
        :param regex:是否完全匹配
        :param sleep:默认延迟1s
        :return:
        """
        import re
        from time import sleep
        if not isinstance(title, str):
            title = str(title)
        sleep(times)
        current_title = self.title
        if regex:
            result = re.fullmatch(title, current_title, re.M | re.I)
        else:
            result = re.search(title, current_title, re.M | re.I)
        return True if result else False

    def add_element_attribute(self, id=None, xpath=None):
        if xpath:
            if isinstance(xpath, list):
                ErrorMessage = None
                for index, xpath_obj in enumerate(xpath):
                    try:
                        return self.find_element_by_xpath(xpath_obj)
                    except Exception as e:
                        ErrorMessage = e
                        continue
                raise ErrorMessage
            elif isinstance(xpath, str):
                return self.find_element_by_xpath(xpath)
        elif id:
            if not isinstance(id, str):
                id = str(id)
            return self.find_element_by_id(id)

    def add_elements_attribute(self, id=None, xpath=None):
        pass
