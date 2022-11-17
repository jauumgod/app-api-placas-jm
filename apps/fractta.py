from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class FracttalBOT:

    def __init__(self, username, password):

        self.servico = Service(ChromeDriverManager().install())
        self.bot = webdriver.Chrome(service=self.servico)
        time.sleep(1)
        self.bot.get("https://app.fracttal.com/signin")
        time.sleep(10)
        self.bot.find_element(By.NAME, 'email').click()
        self.bot.find_element(By.NAME, 'email').send_keys(username) #usuario
        self.bot.fullscreen_window()
        time.sleep(1)
        self.bot.find_element(By.CLASS_NAME,"MuiTouchRipple-root css-w0pj6f").click() #avançar
        self.bot.find_element().click()
        self.bot.find_element().send_keys(password)
        self.bot.find_element().click()
        self.bot.close()



username = 'joao.marinho@grupokurujao.com.br'
password = 'A1h2q4v1@1'
FracttalBOT(username, password)
