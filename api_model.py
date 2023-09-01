from xgboost import XGBClassifier
import numpy as np
import json
from keras.models import load_model

catdict = json.load(open('categories.json','r',encoding = 'utf-8'))
normalize_dict = json.load(open('normalization.json','r',encoding = 'utf-8'))
popt = json.load(open('coef.json','r'))
atributos = json.load(open('ordem_atributos.json','r',encoding = 'utf-8'))
nafill = json.load(open('nafill.json','r',encoding = 'utf-8'))
model_xgb = XGBClassifier()
model_xgb.load_model('model_load.json')
model_deep = load_model('model_DeepV2.h5')
with open('anti_bs','r') as f:
    anti_bs = f.read().split()
    a,b = float(anti_bs[0]),float(anti_bs[1])
ppindice = atributos.index('pesoparcela')

def pol3(x):
    return ((x + b) ** 3) * a

def calc_renda(x,y):
    if x == None:
        if y == None:
            return 0
        return y
    if y == None:
        return x
    return max(x,y)

def valor_da_parcela(row):
    taxa = row['taxaaomes']
    vp = row['valoremprestado']
    n = max(row['quantidadeparcelas'],1)
    if taxa == 0:
        return vp / n
    return vp * (taxa * ((1 + taxa) ** n)) / (((1 + taxa) ** n) - 1)

def square(x,a,b,c):
    return ((x ** 2) * a) + (x * b) + c

corrector = lambda x: square(x,*popt)

def calculate(data_dict):
    weight = .87
    vector = []
    rendafamiliarmensal = data_dict['rendafamiliarmensal'] if 'rendafamiliarmensal' in data_dict else None
    totaldasreceitas = data_dict['totaldasreceitas'] if 'totaldasreceitas' in data_dict else None
    data_dict['valorparcela'] = valor_da_parcela(data_dict)
    renda = calc_renda(rendafamiliarmensal,totaldasreceitas)
    data_dict['pesoparcela'] = data_dict['valorparcela'] / renda if renda > 0 else 1
    data_dict['pesoparcela'] = data_dict['pesoparcela'] if data_dict['pesoparcela'] <= 1 else 1
    for atributo in atributos:
        if data_dict[atributo] is None:
            value = nafill[atributo]
        else:
            value = data_dict[atributo]
        if atributo in catdict:
            value = catdict[atributo][value]
        value = (value - normalize_dict[atributo]['mean']) / normalize_dict[atributo]['std']
        vector.append(value)
    vector = np.array([vector])
    pred_xgb = corrector(model_xgb.predict_proba(vector)[0,1])
    pred_deep = model_deep(vector).numpy()[0][0]
    return min((pred_deep * weight) + (pred_xgb * (1 - weight)) + pol3(vector[0,ppindice]),0.99)