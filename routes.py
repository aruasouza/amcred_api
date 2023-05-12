from flask import Blueprint, request, json, Response
import json
import numbers
from key import admin_pass
from api_model import atributos,calculate

main = Blueprint('main', __name__)

permited = json.load(open('permited_values.json','r',encoding = 'utf-8'))
numeric = set(json.load(open('numeric.json','r',encoding = 'utf-8')))
mandatory = set(json.load(open('mandatory.json','r',encoding = 'utf-8')))
atributos = atributos.copy()
atributos.remove('valorparcela')
atributos.remove('pesoparcela')

def jsonify(data):
    json_str = json.dumps(data,ensure_ascii = False)
    return Response(json_str,content_type="application/json; charset=utf-8" )

@main.route('/')
def index():
    auth = request.authorization
    if not auth:
        return jsonify({'message':'Permissão negada.'}),401
    if (auth.username != 'deepen') or (auth.password != admin_pass):
        return jsonify({'message':'Permissão negada.'}),401
    if not request.data:
        return jsonify({'message':'Nenhum dado recebido.'}),400
    dados = request.json
    data_dict = {}
    valores_negados = {}
    valores_faltantes = []
    for atributo in atributos:
        if atributo in dados:
            if (atributo in numeric) and isinstance(dados[atributo],numbers.Number):
                data_dict[atributo] = dados.pop(atributo)
            elif dados[atributo] in permited[atributo]:
                data_dict[atributo] = dados.pop(atributo)
            else:
                valores_negados[atributo] = dados.pop(atributo)
        else:
            if atributo in mandatory:
                valores_faltantes.append(atributo)
    if valores_negados or dados or valores_faltantes:
        return jsonify({'message':'Há erros no envio das informações.',
                        'errors':{'atributos negados':list(dados.keys()),'valores negados':valores_negados,'atributos obrigatórios ausentes':valores_faltantes}}),400
    return jsonify({'probabilidade':calculate(data_dict)}),200