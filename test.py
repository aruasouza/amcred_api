import requests

# url = 'https://api-amcred.onrender.com'
url = 'http://127.0.0.1:5000'
secret = open('admin_pass','r').read()

req = requests.post(url,auth = ('deepen',secret),json = {'situacaodoimovelderesidencia':'Cedida',
                                                        'situacaoimoveldeatividade':'Alugada',
                                                        'tipodeponto':'Fixo',
                                                        'formacaoescolar':'Sem Instrução',
                                                        'constituicao':'M.E.I.'})
print(req)
print(req.json())