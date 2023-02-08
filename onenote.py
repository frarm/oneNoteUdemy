import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_argument("start-maximized")
driver = webdriver.Edge(options=options)
driver.implicitly_wait(20)
driver.get(
    'https://www.udemy.com/course/angular-10-fundamentos-8-app/')


element = driver.find_element(By.CSS_SELECTOR,
                              '#udemy > div.ud-main-content-wrapper > div.ud-main-content > div > div > div.paid-course-landing-page__container > div.paid-course-landing-page__body > div > div:nth-child(3) > div > button')
element.click()

elements = driver.find_elements(By.CSS_SELECTOR,
                                'div.accordion-panel--panel--24beS > span')
for element in elements:
    driver.execute_script(
        "arguments[0].setAttribute('data-checked', 'checked')", element)
title_elements = driver.find_elements(By.CSS_SELECTOR,
                                      '.section--section-title--wcp90')

subtitle_elements = driver.find_elements(By.CSS_SELECTOR,
                                         'div.section--row--3sLRB span')

ul_elements = driver.find_elements(By.CSS_SELECTOR,
                                   'div.accordion-panel--content-wrapper--1GE5R > div > ul')

array = []
for ul_element in ul_elements:
    count = len(ul_element.find_elements(By.TAG_NAME,
                                         'li'))
    array.append(count)

temp = 0
for idx, title_element in enumerate(title_elements):
    print(title_element.text)
    for subtitle_element in subtitle_elements[temp:temp+array[idx]]:
        print("\t"+subtitle_element.text)
    temp = temp+array[idx]

driver.close()
