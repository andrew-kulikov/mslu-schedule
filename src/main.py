from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import os


SCHEDULE_URL = 'http://raspisanie.mslu.by/schedule/reports/publicreports/schedulelistforgroupreport'
FACULTY = 'Переводческий'
COURSE = '3'
YEARS = '2019/2020'
GROUP = '303/2 ан-нем'
G1 = '308/1 ан-араб'
WEEK = '1 сентября - 8 сентября'


def select_option(driver, select_name, text, wait=False):
    if wait:
        time.sleep(3)
    # element = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(
    #    (By.XPATH, "//select[contains(@name,'{0}')]".format(select_name))))
    element = driver.find_element_by_xpath(
        "//select[contains(@name,'{0}')]".format(select_name))
    print(element.text)
    all_options = element.find_elements_by_tag_name("option")

    print('-' * 30)
    for option in all_options:
        try:
            print('{0}; value : {1}'.format(
                option.text, option.get_attribute('value')))
        except Exception as e:
            print(e)

    faculty_select = Select(element)
    faculty_select.select_by_visible_text(text)


def main():
    driver = webdriver.Chrome()
    driver.get(SCHEDULE_URL)

    options = webdriver.ChromeOptions()
    options.add_argument('download.default_directory={0}'.format(os.getcwd()))

    select_option(driver, 'faculty', FACULTY)
    select_option(driver, 'course', COURSE)
    select_option(driver, 'studyYears', YEARS)
    select_option(driver, 'studyGroups', G1, wait=True)
    select_option(driver, 'studyWeeks', WEEK)

    
    print_link = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_id('printReport'))

    print(print_link.get_attribute("innerHTML"))

    time.sleep(3)

    driver.close()


if __name__ == "__main__":
    main()
