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

class SubmitForm(object):
		
	def form_manipulation(self):
		wd = Chrome()
		form_page = wd.get("https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform?usp=sf_link")
		input_field = wd.find_element(By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')
		print(input_field.text)
		input_field.send_keys("Denys Shamov")
		wd.save_screenshot("filled_form.png")
		submit_btn = wd.find_element(By.CSS_SELECTOR, 'div[jsname="M2UYVd"]')
		submit_btn.click()
		wd.save_screenshot("submitted_form.png")
		wd.close()


form = SubmitForm().form_manipulation()