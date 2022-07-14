from sqlalchemy import Column, DateTime, Integer, String
from database import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(50))
    razao_social = Column(String(50))
    cnpj = Column(String(50))
    data_inclusao = Column(DateTime)

    def __init__(self, codigo=None, nome=None, razao_social=None, cnpj=None, data_inclusao=None):
         self.codigo = codigo
         self.nome = nome
         self.razao_social = razao_social
         self.cnpj = cnpj
         self.data_inclusao = data_inclusao

    def to_json(self):
        return {
         "codigo": self.codigo,
         "nome": self.nome,
         "razao_social": self.razao_social,
         "cnpj": self.cnpj,
         "data_inclusao": self.data_inclusao
        }

# from sqlalchemy import Column, Integer, String
# from yourapplication.database import Base

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), unique=True)
#     email = Column(String(120), unique=True)

#     def __init__(self, name=None, email=None):
#         self.name = name
#         self.email = email

#     def __repr__(self):
#         return f'<User {self.name!r}>'