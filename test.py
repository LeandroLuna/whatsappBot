from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class Wb:
    def __init__(self):
        self.msg = "testando botttttttttttttttttttttt"
        self.contacts = ["Mikes - FROM ITAIM PTA 🇧🇷", "Mommy"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def Mensagem(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(15)
        for cont in self.contacts:
            contt = self.driver.find_element_by_xpath(
                f"//span[@title='{cont}']")
            time.sleep(3)
            contt.click()
            chat = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat.click()
            chat.send_keys(self.msg)
            butao = self.driver.find_element_by_xpath(
                '//span[@data-testid="send"]')
            butao.click()
            time.sleep(3)


bot = Wb()
bot.Mensagem()
