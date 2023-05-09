from flask import Blueprint, request, jsonify
import json
import numbers
from key import admin_pass
from api_model import atributos,calculate

main = Blueprint('main', __name__)

permited = json.load(open('permited_values.json','r',encoding = 'utf-8'))
numeric = json.load(open('numeric.json','r'))
numeric = set(numeric)

@main.route('/')
def index():
    return 'hello, world'
    auth = request.authorization
    if not auth:
        return jsonify({'message':'Permissão negada.'}),401
    if (auth.username != 'deepen') or (auth.password != admin_pass):
        return jsonify({'message':'Permissão negada.'}),401
    
    dados = request.json
    if not dados:
        jsonify({'message':'Nenhuma informação recebida'}),400
    data_dict = {}
    valores_negados = {}
    for atributo in atributos:
        if atributo in dados:
            if (atributo in numeric) and isinstance(dados[atributo],numbers.Number):
                data_dict[atributo] = dados.pop(atributo)
            elif dados[atributo] in permited[atributo]:
                data_dict[atributo] = dados.pop(atributo)
            else:
                valores_negados[atributo] = dados.pop(atributo)
    if valores_negados or dados:
        return jsonify({'message':'Alguns atributos e/ou valores não foram reconhecidos',
                        'errors':{'atributos negados':dados,'valores negados':valores_negados}}),400
    return jsonify({'probabilidade':calculate(data_dict)}),200