from Modulos.banco import Banco
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests
import time
import json
import pickle
import random



class Bots():

    def __init__(self):
        
        fp = webdriver.FirefoxProfile("C:\\Users\\Vinicius\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\xxuk2da7.default-release")
        self.driver = webdriver.Firefox(fp)
        self.driver.implicitly_wait(5) 
        self.b = Banco("banco")   
          

        

    def __retorna_niks(self,qtdNiks):
        # Retorna uma lista de niks
        driver = self.driver        
       
        
        qtd = 300
        nomes = []
        lst_users_novos = []

        if qtdNiks < 300:
            qtd = qtdNiks
        

        driver.get("https://www.4devs.com.br/gerador_de_nicks")
        select = Select(driver.find_element_by_id("method"))
        select.select_by_value("noun")  

        
        while True:

            nomes = nomes + self.__busca_niks(qtd)
            nomes = list(set(nomes))
            
            lst_users_novos = []
            for n in nomes:
                if self.b.select_user(n) == []:
                    lst_users_novos.append(n)
                    print(n)
            
            nomes = lst_users_novos
           
            
            if qtdNiks - len(nomes) < 300:
                qtd = qtdNiks - len(nomes)

            if len(nomes) >= qtdNiks:
                break

        
        return nomes


    def __retorna_senhas(self,qtdSenha):

        driver = self.driver

        # Retorna uam lsita de senhas
        # Maximo aceito pelo site 3000
        qtd = 2000
        
        if qtdSenha < 2000:
            qtd = qtdSenha

        driver.get("https://www.4devs.com.br/gerador_de_senha")
        driver.find_element_by_id("txt_tamanho").clear()
        driver.find_element_by_id("txt_tamanho").send_keys("12")
        driver.find_element_by_class_name("block.pt-5").click()
        driver.find_element_by_id("txt_quantidade").clear()
        driver.find_element_by_id("txt_quantidade").send_keys(qtd)
        driver.find_element_by_id("bt_gerar_senha").click()
        psswd = driver.find_element_by_class_name("output-txt").get_attribute("value")
        psswd = psswd.split("\n")

        psswd = psswd[:-1]

        while len(psswd) < qtdSenha:        
            r = random.randint(2, len(psswd) - 1)
            psswd.append(psswd[r])

        return psswd


    def __busca_niks(self,qtd):

        driver = self.driver
        
        lnomes = []
        driver.find_element_by_id("quantity").clear()
        driver.find_element_by_id("quantity").send_keys(qtd)
        driver.find_element_by_id("bt_gerar_nick").click()
        
        nomes = driver.find_elements_by_class_name("generated-nick")

        for n in nomes:
            lnomes.append(n.text)

        return lnomes
    
    def __retorna_nascimento(self,qtd):

        data_nasc = []
        i = 0

        while i < qtd:
            data_nasc.append(f"{random.randint(1,27)}" + '/' + f"{random.randint(1,12)}" + '/' + f"{random.randint(1980, 2000)}")
            i +=1
        return data_nasc


    def __cadastra_emails(self,botcompleto):

        driver = self.driver

        driver.get("https://vinaszz.club/iredadmin")  


        with open('Logins_acesso\\email_admin.json', 'r') as j:
            json_data = json.load(j)


        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys(json_data["usuario"])
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(json_data["senha"])
        driver.find_element_by_name("login").click()

        
        for b in botcompleto:

            driver.get("https://vinaszz.club/iredadmin/create/user/mail.vinaszz.club")
            driver.find_element_by_class_name("text.fl-space").send_keys(b[0])    #nome do email
            driver.find_element_by_name("newpw").send_keys(b[1])  #senha
            driver.find_element_by_name("confirmpw").send_keys(b[1])  #confirmação de senha
            driver.find_element_by_name("cn").send_keys(b[0]) #Nome de exibição do email no painel de email
            driver.find_element_by_name("mailQuota").clear()    
            driver.find_element_by_name("mailQuota").send_keys(10)  #Quota de mb do email do bot
            driver.find_element_by_class_name("button.green").click()

            mensagem = None
            try:
                driver.implicitly_wait(2)
                driver.find_element_by_class_name("notification.note-success").text     
                driver.implicitly_wait(10)
            except:
                try:
                    driver.implicitly_wait(2)
                    if "O endereço de email já existe" in driver.find_element_by_class_name("notification.note-error").text:
                        mensagem = "Já existe"
                    driver.implicitly_wait(10)
                except Exception as msg2:
                    mensagem = msg2
        
        return mensagem
    


    def __registra_banco(self,BotsCompleto):


        lista = []
        for bt in BotsCompleto:
            lista.append({
                'bot_name': bt[0],
                'bot_email': bt[3],
                'password': bt[1],
                'birth_date': bt[2]
            })
        self.b.insere("bots",lista)

    
    def registra_na_twitch(self):
        
        driver = self.driver
        driver.get("https://www.twitch.tv/")

        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
                driver.add_cookie(cookie)

        driver.find_element_by_xpath("//*[@data-a-target='signup-button']").click()
        driver.find_element_by_id("signup-username").clear()
        driver.find_element_by_id("signup-username").send_keys("borbos3459j")
        driver.find_element_by_id("password-input").clear()
        driver.find_element_by_id("password-input").send_keys("SoTp01251213")
        driver.find_element_by_id("password-input-confirmation").clear()
        driver.find_element_by_id("password-input-confirmation").send_keys("SoTp01251213")
        driver.find_elements_by_xpath("//*[@aria-label='Insira seu dia de nascimento']")[0].send_keys("12")
        driver.find_elements_by_xpath("//*[@aria-label='Selecione seu mês de aniversário']")[0].send_keys("f")
        driver.find_element_by_xpath("//*[@aria-label='Insira seu ano de nascimento']").send_keys("1986")
        driver.find_element_by_id("email-input").send_keys("borbos3459j@gmail.com")
        driver.find_element_by_xpath("//*[@data-a-target='passport-signup-button']").click()
    
    
    

    def retorna_bot_completo(self,qtd):

        driver = self.driver

        BotsCompleto = []
        niks = self.__retorna_niks(qtd)
        senhas = self.__retorna_senhas(qtd)
        datanasc = self.__retorna_nascimento(qtd)        

        for x in range(qtd):

            BotsCompleto.append([niks[x], senhas[x], datanasc[x], niks[x] + "@mail.vinaszz.club"])
        
        
        self.__cadastra_emails(BotsCompleto)
        driver.close()
        self.__registra_banco(BotsCompleto)        
        
        
        return BotsCompleto
