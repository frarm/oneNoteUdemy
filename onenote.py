from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

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

course_title = driver.find_element(
    By.CSS_SELECTOR, '#udemy > div.ud-main-content-wrapper > div.ud-main-content > div > div > div.paid-course-landing-page__container > div.top-container.dark-background > div > div > div:nth-child(3) > div > h1')

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
pyautogui.click(404, 1054, interval=0.5)
pyautogui.doubleClick(130, 1015, interval=0.5)
pyautogui.write(course_title.text)
is_first_page = True

for idx, title_element in enumerate(title_elements):
    if is_first_page == True:
        pyautogui.doubleClick(468, 132, interval=0.5)
        pyautogui.write(title_element.text)
        is_first_page = False
    else:
        pyautogui.click(325, 1008, interval=0.5)
        pyautogui.write(title_element.text)

    pyautogui.press('enter')
    for subtitle_element in subtitle_elements[temp:temp+array[idx]]:
        pyautogui.write(subtitle_element.text)
        pyautogui.press('enter')

    temp = temp+array[idx]

driver.close()
