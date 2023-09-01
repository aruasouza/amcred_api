import requests

url = 'http://192.168.100.3:8070'
secret = open('app_simples/admin_pass','r').read()

req = requests.post(url,auth = ('deepen',secret),json = {'situacaodoimovelderesidencia':'Cedida',
                                                        'situacaoimoveldeatividade':'Alugada',
                                                        'tipodeponto':'Fixo',
                                                        'formacaoescolar':'Sem Instrução',
                                                        'constituicao':'M.E.I.',
                                                        'finalidadeemprestimo':'Giro',
                                                        'taxaaomes':0.1,
                                                        'valoremprestado':1000000,
                                                        'quantidadeparcelas':10,
                                                        'totaldasreceitas':100,
                                                        'rendafamiliarmensal':20000,
                                                        'conceitospc':'A'
                                                        })
print(req)
print(req.json())