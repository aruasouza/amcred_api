import requests

# url = 'https://api-amcred.onrender.com'
url = 'http://127.0.0.1:5000'
secret = open('admin_pass','r').read()

req = requests.post(url,auth = ('deepen',secret),json = {'situacaodoimovelderesidencia':'Cedida',
                                                        'situacaoimoveldeatividade':'Alugada',
                                                        'tipodeponto':'Fixo',
                                                        'formacaoescolar':'Sem Instrução',
                                                        'constituicao':'M.E.I.',
                                                        'finalidadeemprestimo':'Giro',
                                                        'taxaaomes':0.15,
                                                        'valoremprestado':10000000,
                                                        'quantidadeparcelas':10,
                                                        'totaldasreceitas':0,
                                                        'rendafamiliarmensal':0
                                                        })
print(req)
print(req.json())