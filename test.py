import requests

url = 'https://api-amcred.onrender.com'
secret = open('admin_pass','r').read()

req = requests.get(url,auth = ('deepen',secret),json = {})
print(req)
print(req.text)