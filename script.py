from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard

class MonkeyTypeBot:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.browser = None

    def start_browser(self):
        service = ChromeService(executable_path=self.driver_path)
        self.browser = webdriver.Chrome(service=service)

    def open_website(self, url):
        self.browser.get(url)

    def wait_for_element(self, xpath, timeout=2):
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def get_active_words(self, xpath):
        word_list = self.browser.find_elements(By.XPATH, xpath)
        active_index = next((i for i, word in enumerate(word_list) if 'active' in word.get_attribute('class')), None)
        return word_list[active_index:] if active_index is not None else []

    def type_words(self, words):
        full_text = ""
        for word in words:
            letters = "".join([char.text for char in word.find_elements(By.XPATH, './letter') if char.text]) + " "
            if letters.strip():
                full_text += letters
        if full_text:
            ActionChains(self.browser).send_keys(full_text).perform()

    def run(self, url, words_xpath):
        self.start_browser()
        self.open_website(url)
        self.wait_for_element(words_xpath)

        try:
            while True:
                if keyboard.is_pressed('esc'):
                    print("ESC pressed, exiting...")
                    break

                active_words = self.get_active_words(words_xpath)
                self.type_words(active_words)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.browser.quit()

if __name__ == "__main__":
    DRIVER_PATH = './webdriver/chromedriver/chromedriver.exe'
    WORDS_XPATH = '/html/body/div[11]/main/div/div[3]/div[7]/div[4]/div'
    URL = 'https://monkeytype.com/'

    bot = MonkeyTypeBot(DRIVER_PATH)
    bot.run(URL, WORDS_XPATH)
