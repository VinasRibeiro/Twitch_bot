from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import time
import json
import pickle



class Divulgador():

   
    def __init__(self):

        fp = webdriver.FirefoxProfile("C:\\Users\\Vinicius\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\xxuk2da7.default-release")
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.twitch.tv/")



    def login(self,lgUser, passUser):

        driver = self.driver

        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
                driver.add_cookie(cookie)
    
        driver.find_element_by_xpath("//*[@data-a-target='login-button']").click()
        driver.find_element_by_xpath("//input[@id='login-username']").clear()
        driver.find_element_by_xpath("//input[@id='login-username']").send_keys(lgUser)

        driver.find_element_by_xpath("//input[@id='password-input']").clear()
        driver.find_element_by_xpath("//input[@id='password-input']").send_keys(passUser)
        driver.find_element_by_xpath("//*[@data-a-target='passport-login-button']").click()

        time.sleep(1)
        




    def envia_mensagem(self,mensagem, Listausers):

        driver = self.driver

        for user in Listausers:

            try:

                # Abre aba sussurro
                driver.find_elements_by_xpath("//*[@data-a-target='whisper-box-button']")[0].click()
                
                # Limpa o campo que busca usuário
                driver.find_elements_by_id("threads-box-filter")[0].clear()

                # Envia o nome da pessoa no campo de busca
                driver.find_elements_by_id("threads-box-filter")[0].send_keys(user)

                time.sleep(1)
                
                # Clica no usuário buscado
                driver.find_element_by_class_name("tw-align-items-center.tw-border-b.tw-flex.tw-flex-nowrap.tw-flex-row.tw-full-width.tw-pd-1.whispers-list-item").click()
                time.sleep(1)

                #Limpa o campo sussurro
                driver.find_element_by_class_name("tw-block.tw-border-bottom-left-radius-medium.tw-border-bottom-right-radius-medium.tw-border-top-left-radius-medium.tw-border-top-right-radius-medium.tw-font-size-6.tw-full-width.tw-input.tw-pd-l-1.tw-pd-r-3.tw-pd-y-05").clear()

                # Envia uma mensagem no campo do sussurro
                driver.find_element_by_class_name("tw-block.tw-border-bottom-left-radius-medium.tw-border-bottom-right-radius-medium.tw-border-top-left-radius-medium.tw-border-top-right-radius-medium.tw-font-size-6.tw-full-width.tw-input.tw-pd-l-1.tw-pd-r-3.tw-pd-y-05").send_keys(mensagem)

                
                # Envia a mensagem do sussurro
                driver.find_element_by_class_name("tw-block.tw-border-bottom-left-radius-medium.tw-border-bottom-right-radius-medium.tw-border-top-left-radius-medium.tw-border-top-right-radius-medium.tw-font-size-6.tw-full-width.tw-input.tw-pd-l-1.tw-pd-r-3.tw-pd-y-05").send_keys(Keys.ENTER)

                time.sleep(2)            

                # Fecha o sussurro atual
                driver.find_element_by_xpath("//*[@aria-label='Fechar']").click()
                
            except:
                try:
                    # Fecha o sussurro atual
                    driver.find_element_by_xpath("//*[@aria-label='Fechar']").click()
                except:
                    driver.find_element_by_xpath("//*[@aria-label='Minimizar']").click()



    