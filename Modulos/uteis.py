import json


def retorna_users_faltantes(users_db,users_atual):
    
    "Esta função retorna uma lista de usuários faltantes"
    lista_retorno = []
    for usr in users_db:
        if usr in users_atual[usr[0]]:
            pass
        else:
            lista_retorno.append(usr)
    return lista_retorno