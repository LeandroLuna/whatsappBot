import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Wb:
    def __init__(self):
        self.msg = "Hi humans! I am A robot (aka bot), and ur brazilian boy forgot to notify his contacts that he changed his whatsapp number. Yeah, i know, i know, fucking dumb, i think the same. Well, he SLAVED me to say this, so add him or you are going to make a man SAD, DEPRESSED, and all the bad things"
        self.contacts = ["Manonnn Sbbh", "Nikola Wis!"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=en-US')
        self.driver = webdriver.Chrome(
            executable_path=r'C:\Users\leand\Desktop\BOT WHATSAPP/chromedriver.exe', chrome_options=options)

    def Mensagem(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for cont in self.contacts:
            contat = self.driver.find_element_by_xpath(
                f"//span[@title='{cont}']")
            time.sleep(3)
            contat.click()
            chat = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat.click()
            chat.send_keys(self.msg)
            button = self.driver.find_element_by_xpath(
                '//span[@data-icon="send"]')
            time.sleep(3)
            button.click()
            time.sleep(5)


bot = Wb()
bot.Mensagem()
