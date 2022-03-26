
import requests
url = 'http://127.0.0.1:5000/blogs'
myobj = {'title': 'jackiee'}

# x = requests.post(url, json = myobj)
# print(x.text)

r = requests.get('http://127.0.0.1:5000/blogs')
print(r.text)

# d = requests.delete("http://127.0.0.1:5000/blogs/1")
# print(d.status_code)