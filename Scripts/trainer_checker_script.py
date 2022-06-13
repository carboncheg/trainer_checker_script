import os
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep
from logger import Logger

caps = DesiredCapabilities.CHROME
# caps["pageLoadStrategy"] = "normal"    # complete
caps["pageLoadStrategy"] = "eager"       # interactive
# caps["pageLoadStrategy"] = "none"      # none

link = 'https://lc.rt.ru/auth'
path_to_driver = 'C:\\tools\\chromedriver.exe'
browser = webdriver.Chrome(path_to_driver, desired_capabilities=caps)

browser.maximize_window()
browser.get(f'{link}')

# AUTHORIZATION

login_field = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/form/div[1]/div[1]/input')
login_field.send_keys('')  # Ты знаешь чей номер телефона тут указан

password_visible = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/form/div[3]/div[3]')
password_visible.click()

password_field = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/form/div[3]/div[1]/input')
password_field.send_keys('')  # Тут самый частый пароль, который ты использовал на Лицее

submit_button = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/form/button')
submit_button.submit()
sleep(1)

# GET FILE WITH IDS

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'src\exam_items_imported_lesson_ids.txt')

with open(file_path, 'r', encoding='utf-8') as file:

    # CHECK TRAINERS IN LESSONS

    count = 0
    for lesson_id in file:

        count += 1
        Logger.add_action('----------')
        Logger.add_action(f'Test {count} started! Lesson {lesson_id.strip()}')

        browser.get(f'https://lc.rt.ru/lessons/{lesson_id.strip()}')

        try:
            select_trainer_tab = WebDriverWait(browser, 2).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="root"]/div/div[4]/div[2]/div/div/div[2]/div[1]/div[2]'))).click()
            Logger.add_action(' - checking Trainer tab passed successfully')
        except TimeoutException:
            try:
                error_404 = browser.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/div/div/div[2]')
                assert 'такой страницы не существует' in error_404.text
                Logger.add_nonexistent_lesson(f'{lesson_id.strip()}')
                Logger.add_action(' - screenshot saved')
                Logger.add_action(f'Test {count} FAILED on error 404! Lesson {lesson_id.strip()}')
                continue
            except AssertionError:
                browser.save_screenshot(
                    f'src/screenshots/lesson_{lesson_id.strip()}__{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.png')
                Logger.add_error_lesson(f'{lesson_id.strip()}')
                Logger.add_action(' - screenshot saved')
                Logger.add_action(f'Test {count} FAILED on Trainer tab checking! Lesson {lesson_id.strip()}')
                continue

        try:
            question_wrapper = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="root"]/div/div[4]/div[2]/div/div/div[2]/div[2]/div/div')))
            Logger.add_action(' - checking Question wrapper passed successfully')
        except TimeoutException:
            browser.save_screenshot(
                f'src/screenshots/lesson_{lesson_id.strip()}__{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.png')
            Logger.add_error_lesson(f'{lesson_id.strip()}')
            Logger.add_action(' - screenshot saved')
            Logger.add_action(f'Test {count} FAILED on Question wrapper checking! Lesson {lesson_id.strip()}')
            continue

        try:
            question_title = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="root"]/div/div[4]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]')))
            Logger.add_action(' - checking Question title passed successfully')
            sleep(0.5)
        except TimeoutException:
            browser.save_screenshot(
                f'src/screenshots/lesson_{lesson_id.strip()}__{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.png')
            Logger.add_error_lesson(f'{lesson_id.strip()}')
            Logger.add_action(' - screenshot saved')
            Logger.add_action(f'Test {count} FAILED on Question title checking! Lesson {lesson_id.strip()}')
            continue

        try:
            answer_option_1 = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="root"]/div/div[4]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div')))
            Logger.add_action(' - checking Answer option 1 passed successfully')
        except TimeoutException:
            browser.save_screenshot(
                f'src/screenshots/lesson_{lesson_id.strip()}__{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.png')
            Logger.add_error_lesson(f'{lesson_id.strip()}')
            Logger.add_action(' - screenshot saved')
            Logger.add_action(f'Test {count} FAILED on Answer option 1 checking! Lesson {lesson_id.strip()}')
            continue

        try:
            answer_option_2 = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="root"]/div/div[4]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div/div')))
            Logger.add_action(' - checking Answer option 2 passed successfully')
        except TimeoutException:
            browser.save_screenshot(
                f'src/screenshots/lesson_{lesson_id.strip()}__{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.png')
            Logger.add_error_lesson(f'{lesson_id.strip()}')
            Logger.add_action(' - screenshot saved')
            Logger.add_action(f'Test {count} FAILED on Answer option 2 checking! Lesson {lesson_id.strip()}')
            continue

        try:
            answer_option_3 = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="root"]/div/div[4]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div')))
            Logger.add_action(' - checking Answer option 3 passed successfully')
        except TimeoutException:
            browser.save_screenshot(
                f'src/screenshots/lesson_{lesson_id.strip()}__{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.png')
            Logger.add_error_lesson(f'{lesson_id.strip()}')
            Logger.add_action(' - screenshot saved')
            Logger.add_action(f'Test {count} FAILED on Answer option 3 checking! Lesson {lesson_id.strip()}')
            continue

        try:
            answer_option_4 = WebDriverWait(browser, 2).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="root"]/div/div[4]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/div/div')))
            Logger.add_action(' - checking Answer option 4 passed successfully')
        except TimeoutException:
            browser.save_screenshot(
                f'src/screenshots/lesson_{lesson_id.strip()}__{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.png')
            Logger.add_error_lesson(f'{lesson_id.strip()}')
            Logger.add_action(' - screenshot saved')
            Logger.add_action(f'Test {count} FAILED on Answer option 4 checking! Lesson {lesson_id.strip()}')
            continue

        browser.save_screenshot(
            f'src/screenshots/lesson_{lesson_id.strip()}__{str(datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S--%f"))}.png')
        Logger.add_action(' - screenshot saved')
        Logger.add_action(f'Test {count} PASSED! Lesson {lesson_id.strip()} checked!')


browser.quit()
