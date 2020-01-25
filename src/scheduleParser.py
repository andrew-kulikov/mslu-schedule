from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from schedule import Schedule
import time


class ScheduleParser:
    def __init__(self, schedule_url: str, root_dir: str):
        self.root_dir = root_dir
        self.url = schedule_url
        self.started = False

    def start(self):
        if self.started:
            return
    
        # configure driver options
        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': self.root_dir}
        options.add_experimental_option('prefs', prefs)

        # start webdriver
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get(self.url)

        self.started = True

    def stop(self):
        self.driver.close()

    def __select_option(self, select_name: str, text: str, wait: bool = False):
        if wait:
            time.sleep(2)

        element = self.driver.find_element_by_xpath(
            "//select[contains(@name,'{0}')]".format(select_name))
        all_options = element.find_elements_by_tag_name('option')

        for option in all_options:
            print('{0}'.format(option.text))

        Select(element).select_by_visible_text(text)

    def get_schedule(self, schedule: Schedule):
        self.__select_option('faculty', schedule.faculty)
        self.__select_option('course', schedule.course)
        self.__select_option('studyYears', schedule.years)
        # wait because of strange element behavior
        self.__select_option('studyGroups', schedule.group, wait=True)
        self.__select_option('studyWeeks', schedule.week)

        # wait for download link to appear
        print_link = WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element_by_id('printReport'))

        print_link.click()
    
    def __enter__(self):
        self.start()
    
    def __exit__(self, type, value, traceback):
        self.stop()
