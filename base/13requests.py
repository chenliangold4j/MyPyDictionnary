import requests
r = requests.get('https://www.163.com/')
print(r.status_code)
print(r.text)

