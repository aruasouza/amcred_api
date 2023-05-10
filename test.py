import requests

# url = 'https://api-amcred.onrender.com'
url = 'http://127.0.0.1:5000'
secret = open('admin_pass','r').read()

req = requests.get(url,auth = ('deepen',secret),json = {})
print(req)
print(req.json())