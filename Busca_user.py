from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import requests
import time
import json
import pickle
import random


class Start_Selenium():    
  
   
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)

        
    def dark_mode(self):

        driver = self.driver

        # Configura o browser para dark mode
        driver.get("about:config")
        driver.find_element_by_id("warningButton").click()
        driver.find_element_by_id("about-config-search").send_keys("devtools.theme")
        driver.find_element_by_class_name("button-edit").click()
        driver.find_elements_by_xpath("//input[@type='text']")[1].send_keys("dark")
        driver.find_element_by_class_name("primary.button-save").click()

    def retorna_streamers(self,qtdstramers=50):

        # Esta função retorna uma lista de streamers

        qtdant = 0
        streamers = []

        self.driver.get("https://www.twitch.tv/directory/all?sort=VIEWER_COUNT")

        try:
            self.driver.find_element_by_class_name("tw-interactive.tw-link.tw-link--button").click()
        except:
            pass


        while len(streamers) < qtdstramers:

            elements = self.driver.find_elements_by_xpath("//a[@data-a-target='preview-card-channel-link']")

            sizeelem = len(elements)
            
            for stream in elements[qtdant:sizeelem]:    
                streamers.append(stream.get_attribute("href").replace("https://www.twitch.tv/", ""))

            qtdant = sizeelem

            elements[-1].location_once_scrolled_into_view
        

        streamers = streamers[:qtdstramers]
        return streamers


    def retorna_users(self,streamers):
        #Retorna users
        lista_response = []
        for streamer in streamers:
            response = json.loads(requests.get(f"https://tmi.twitch.tv/group/user/{streamer}/chatters").text)
            lista_response = lista_response + response["chatters"]["viewers"]
        
        return lista_response


    def fecha(self):

        self.driver.close()
    