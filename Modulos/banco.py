from Modulos.busca_user import Busca_users
from datetime import datetime, date
from sqlalchemy import insert, update
from sqlalchemy.sql import select
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, ForeignKey, Boolean, create_engine)



class Banco:
           

    def __init__(self,nome_banco):

        metadata = MetaData()
        

        self.bots = Table('bots', metadata,
            Column('bot_id', Integer(), primary_key=True),
            Column('bot_name', String(15), index=True, nullable=False, unique=True),
            Column('bot_email', String(100), nullable=False),
            Column('password', String(25), nullable=False),
            Column('birth_date', String(10), nullable=False),
            Column('reg_twitch', Boolean(), default=False),
            Column('created_on', DateTime(), default=datetime.now),
            Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
            
        )

        self.users = Table('users', metadata,
            Column('user_id', Integer(), primary_key=True),
            Column('user_name', String(15), index=True, nullable=False, unique=True),
            Column('usado', Boolean(), default=False),
            Column('created_on', DateTime(), default=datetime.now),
            Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
        )

        engine = create_engine(f'sqlite:///Dados\\{nome_banco}.db')
        metadata.create_all(engine)
        self.connection = engine.connect()
      
    

    
    def select_dados(self,param,option = None):

        lista_retorno = []

        """
        Esta função retorna dados de acordo com os parâmetros

        :param  :bots ou users: É a tabela especificada
        :option :opcional 

        """
        
        if param == "bots":
            ins = [self.bots]
            if option == "nome":
                ins = [self.bots.c.bot_name]
           
        
        if param == "users":
            ins = [self.users]
            if option == "nome":
                ins = [self.users.c.user_name]
            
        
        rp = self.connection.execute(select(ins))
        results = rp.fetchall()

        if option == "nome":
            for r in results:
                lista_retorno.append(r[0])
            return lista_retorno


        return results

    
    def select_user(self,nome):

        users = self.users
        s = select([users]).where(users.c.user_name == nome)
        rp = self.connection.execute(s)
        results = rp.fetchall()

        return results


    def insere(self,nome_tabela,dados):

        """
        :Esta função insere dados de acordo com os parâmetros:
        :Formato de dados:
        
        
        Estrutura de bots:        
        
        :bot_name  : Nome do usuario da twitch
        :bot_email : Id do bot no banco de dados 
        :password  : Retorna informações do usuario criado ou retorna mensagem de erro
        :birth_date: Data de nascimento

        [{
            'bot_name': nome,
            'bot_email': email,
            'password': senha,
            'birth_date': nasc
        }]      


        Estrutura de user:
        :user: Nome do usuário

        [{
            'user_name' : nome
        }]

        """

            

        if nome_tabela == "bots":
            ins = self.bots.insert()
        if nome_tabela == "users":
            ins = self.users.insert()
        
        result = self.connection.execute(ins, dados)        

        return result



    def atualiza_stats(self,nome_tabela,nome_user,valor):

        """
        Esta função altera o valor bool do usuário para marcar se ele já foi usado ou não
        Assim a data de update é atualizada automáticamente.    
        """
        
        u = update(self.users).where(self.users.c.user_name == nome_user)
        u = u.values(usado=valor)
        result = self.connection.execute(u)
        
        return result
    

    def insere_novos_users_no_banco(self):

        # Esta função busca usuários baseado nos streamers
        # Ele primeiro busca streamers baseado no numero total_streamers
        # Depois insere no banco de dados usuários que não existem até o momento.
            
        Busers = Busca_users()
        streamer = Busers.retorna_streamers(1)
        Busers.fecha()
        users = Busers.retorna_users(streamer)    

        lista_nova = []
        lista = []

        for u in users:
            if self.select_user(u) == []:
                lista_nova.append(u)

        for u in lista_nova:
            lista.append({'user_name': u })

        self.insere("users",lista)

        return lista

