"""
BOT SELENIUM DRIVE

"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


global path
path = '//*[@id="LoginButton"]/span'
class HPDESK:

    def __init__(self, username, password):
        
        self.servico = Service(ChromeDriverManager().install())
        self.robo = webdriver.Chrome(service=self.servico)
        time.sleep(1)
        self.robo.get("https://helpdesk.grupokurujao.com.br/otrs/index.pl")
        time.sleep(1)
        #self.robo.fullscreen_window()
        self.robo.find_element('xpath','//*[@id="User"]').click() #clicar
        time.sleep(1)
        self.robo.find_element('xpath','//*[@id="User"]').send_keys(username)#digitar
        time.sleep(1)
        self.robo.find_element('xpath','//*[@id="Password"]').send_keys(password) #password
        time.sleep(1)
        self.robo.find_element('xpath',path).click()#login
        self.robo.fullscreen_window()
        time.sleep(1)
        self.robo.find_element('xpath','//*[@id="nav-Tickets"]/a')#abre menu
        time.sleep(1)
        self.robo.find_element('xpath','//*[@id="nav-Tickets"]/a').click()#seleciona chamados
        time.sleep(1)
        self.robo.find_element('xpath','//*[@id="nav-Tickets-Statusview"]/a').click() #seleciona o status view
        time.sleep(1)
        self.robo.find_element('xpath','//*[@id="TicketID_162015"]/td[7]/div').click() #clica no chamado
        time.sleep(2)
        self.robo.find_element('xpath','/html/body').click()#conteudo do chamado
        time.sleep(1)
        texto_copiado = '0'
        self.robo.find_element('xpath','/html/body').text(texto_copiado)

        #self.robo.find_element()
        self.robo.close()


username = 'joao.marinho'
password = 'a1h2q4v1'
HPDESK(username,password)

