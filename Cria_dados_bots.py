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


class dados_bots():

    def __init__(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)      

        

    def retorna_niks(self,qtdNiks):
        # Retorna uma lista de niks
        driver = self.driver
        
        qtd = 300
        nomes = []

        if qtdNiks < 300:
            qtd = qtdNiks
        

        driver.get("https://www.4devs.com.br/gerador_de_nicks")
        select = Select(driver.find_element_by_id("method"))
        select.select_by_value("noun")  

        
        while True:

            nomes = nomes + self.__busca_niks(qtd)
            nomes = list(set(nomes))

            
            if qtdNiks - len(nomes) < 300:
                qtd = qtdNiks - len(nomes)

            if len(nomes) >= qtdNiks:
                break

        
        return nomes


    def retorna_senhas(self,qtdSenha):

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
    
    def retorna_nascimento(self,qtd):

        data_nasc = []
        i = 0

        while i < qtd:
            data_nasc.append([random.randint(1,27), random.randint(1,12), random.randint(1980, 2000)])
            i +=1
        return data_nasc


    def retorna_bot_compelto(self,qtd):

        BotCompleto = {}
        niks = self.retorna_niks(qtd)
        senhas = self.retorna_senhas(qtd)
        datanasc = self.retorna_nascimento(qtd)

        for x in range(qtd):

            BotCompleto[x] = [niks[x], senhas[x], datanasc[x]]
        
        return BotCompleto
