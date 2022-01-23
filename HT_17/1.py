# Завдання: за допомогою браузера (Selenium) відкрити форму за наступним посиланням:
# https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link
# заповнити і відправити її.
# Зберегти два скріншоти: заповненої форми і повідомлення про відправлення форми.
# В репозиторії скріншоти зберегти.
# Корисні посилання:
# https://www.selenium.dev/documentation/
# https://chromedriver.chromium.org/downloads

import os

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SubmitForm(object):
		
	def form_manipulation(self):
		wd = Chrome()
		wait = WebDriverWait(wd, 30)
		form_page = wd.get("https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link")
		input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')))
		input_field.send_keys("Denys Shamov")
		wd.save_screenshot("filled_form.png")
		submit_btn = wd.find_element(By.CSS_SELECTOR, 'div[jsname="M2UYVd"]')
		submit_btn.click()
		wd.save_screenshot("submitted_form.png")
		wd.close()


form = SubmitForm().form_manipulation()