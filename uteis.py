def remove_duplicado():
    "Esta função cracha o arquivo json ainda não resolvido"
    lista = {}
    for l in dados:
        lista[l] = list(set(dados[l]))
    
    with open("redessocials3.json", "w") as outfile:  
        json.dump(lista, outfile)

def carrega_users():
    # Abre o banco
    with open('redessocials3.json') as f:
        data = json.load(f)   
    return data

def salva_users():

    for user in listaFaltante:
        dados[user[0]].append(user)

    with open("dbteste.json", "w") as outfile:  
        json.dump(dados, outfile)

def rt_users_faltantes():
    
    "Esta função retorna uma lista de usuários faltantes"
    lista_retorno = []
    for usr in lista_online:
        if usr in dados[usr[0]]:
            pass
        else:
            lista_retorno.append(usr)
    return lista_retorno