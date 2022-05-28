from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class python:
    def __init__(self):
        self.mensagem = "testando bot"
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def Mensagem(self):
        self.driver.get('https://www.python.org/downloads/')
        time.sleep(15)
        chat = self.driver.find_element_by_id('id-search-field')
        time.sleep(10)
        chat.click()
        chat.send_keys(self.mensagem)
        butao = self.driver.find_element_by_id('submit')
        time.sleep(10)
        butao.click()


bot = python()
bot.Mensagem()
