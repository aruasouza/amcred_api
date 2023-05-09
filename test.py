import requests

url = 'http://192.168.100.6'
secret = open('admin_pass','r').read()

req3 = requests.get(url)
print(req3)
print(req3.json())