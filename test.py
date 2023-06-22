import requests

url = 'http://127.0.0.1:8070'
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
                                                        'totaldasreceitas':None,
                                                        'rendafamiliarmensal':None,
                                                        'conceitospc':None
                                                        })
print(req)
print(req.json())