from datetime import datetime, date
from sqlalchemy import insert
from sqlalchemy.sql import select
from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String, DateTime, ForeignKey, Boolean, create_engine)


class banco():

    metadata = MetaData()

    bots = Table('bots', metadata,
        Column('bot_id', Integer(), primary_key=True),
        Column('bot_name', String(15), nullable=False, unique=True),
        Column('bot_email', String(100), nullable=False),
        Column('password', String(25), nullable=False),
        Column('birth_date', String(10), nullable=False),
        Column('created_on', DateTime(), default=datetime.now),
        Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
        
    )

    users = Table('users', metadata,
        Column('users_id', Integer(), primary_key=True),
        Column('users_name', String(15), nullable=False, unique=True),
        Column('bot_id', ForeignKey('bots.bot_id'))


    )

    engine = create_engine(f'sqlite:///base.db')
    metadata.create_all(engine)
    connection = engine.connect()

          

    
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
            'bot_name': f'{nome}',
            'bot_email': f'{email}',
            'password': f'{senha}',
            'birth_date': f'{nasc}'
        }]      



        Estrutura de users:

        :users_name : Nome do usuário
        :bot_id     : Id do bot que vai usar este users_name
        
        [{
            'users_name': f'{nome}',
                'bot_id' : idbot
        }]

        """


        if nome_tabela == "bots":
            ins = self.bots.insert()
        if nome_tabela == "users":
            ins = self.users.insert()

        result = self.connection.execute(ins, dados)

        return result

    
    def select_dados(self,param,option = None):

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
                ins = [self.bots.c.users_name]
            
        
        rp = self.connection.execute(select(ins))
        results = rp.fetchall()

        return results




        
        


