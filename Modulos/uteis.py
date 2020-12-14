import json
import pickle


def retorna_users_faltantes(users_db,users_atual):
    
    "Esta função retorna uma lista de usuários faltantes"
    lista_retorno = []
    for usr in users_db:
        if usr in users_atual[usr[0]]:
            pass
        else:
            lista_retorno.append(usr)
    return lista_retorno

def dark_mode(self):

        driver = self.driver

        # Configura o browser para dark mode
        driver.get("about:config")
        driver.find_element_by_id("warningButton").click()
        driver.find_element_by_id("about-config-search").send_keys("devtools.theme")
        driver.find_element_by_class_name("button-edit").click()
        driver.find_elements_by_xpath("//input[@type='text']")[1].send_keys("dark")
        driver.find_element_by_class_name("primary.button-save").click()
    

def cookies(self,RW):

        if RW == "abrir":
            driver = self.driver
            # Carrega ou salva cookies
            cookies = pickle.load(open("cookies.pkl", "rb"))
            for cookie in cookies:
                driver.add_cookie(cookie)

        if RW == "gravar":
            pickle.dump(driver.get_cookies() , open("cookies.pkl","wb"))