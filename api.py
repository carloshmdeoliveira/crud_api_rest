from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from models import Cliente
from database import db_session
from database import Base
import mysql.connector
import json

app = Flask(__name__)
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo
    if(mensagem):
        body[""] = mensagem
    return Response(json.dumps(body, indent=4, sort_keys=True, default=str), status = status, mimetype="")

# @app.after_request
# def add_header(r):
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     return r

@app.route("/clientes", methods=["GET"])
def seleciona_clientes():
    clientes_objetos = Cliente.query.all()
    clientes_json = [cliente.to_json() for cliente in clientes_objetos]  
    return gera_response(200, "clientes", clientes_json, "Clientes listados.")

@app.route("/cliente/<codigo>", methods=["GET"])
def seleciona_cliente(codigo):
     cliente_objeto = Cliente.query.filter_by(codigo=int(codigo)).first()
     cliente_json = cliente_objeto.to_json()
     return gera_response(200, "cliente", cliente_json, "Cliente selecionado.")

# @app.route("/cliente", methods=["POST"])
# def cria_cliente():
#     body = request.get_json()
#     try:
#         cliente_objeto = Cliente(nome=body["nome"], razao_social=body["razao_social"], cnpj=body["cnpj"], data_inclusao=body["data_inclusao"])
#         db_session.add(cliente_objeto)
#         db_session.commit()
#         return gera_response(201, "cliente", cliente_objeto.to_json(), "Criado com sucesso!")
#     except Exception as e:
#         print(e)
#         return gera_response(400, "usuario", {}, "Erro ao cadastrar.")

# @app.route("/cliente/<codigo>", methods=["PUT"])
# def atualiza_cliente(codigo):
#     cliente_objeto = Cliente.query.filter_by(codigo=codigo).first()
#     body = request.get_json()

#     try:
#         if('nome' in body):
#             cliente_objeto.nome = body['nome']
#         if('razao_social' in body):
#             cliente_objeto.razao_social = body['razao_social']
#         if('cnpj' in body):
#             cliente_objeto.cnpj = body['cnpj']
#         if('data_inclusao' in body):
#             cliente_objeto.data_inclusao = body['data_inclusao']

#         db_session.add(cliente_objeto)
#         db_session.commit()
#         return gera_response(200, "cliente", cliente_objeto.to_json(), "Atualizado com sucesso!")
#     except Exception as e:
#         print('Erro', e)
#         return gera_response(400, "usuario", {}, "Erro ao atualizar.")

# @app.route("/cliente/<codigo>", methods=["DELETE"])
# def deleta_cliente(codigo):
#     cliente_objeto = Cliente.query.filter_by(codigo=codigo).first()

#     try:
#         db_session.delete(cliente_objeto)
#         db_session.commit()
#         return gera_response(200, "cliente", cliente_objeto.to_json(), "Deletado com sucesso!")
#     except Exception as e:
#         print('Erro', e)
#         return gera_response(400, "usuario", {}, "Erro ao Deletar.")

# if __name__== '__main__':
app.run()