import requests
from main import delete_id
from main import update_certain_blog

ADD = "Add"
DELETE = "Delete with id"
UPDATE = "Update with id"
FETCH = "Fetch all"

choices = [ADD, DELETE, UPDATE, FETCH]

for i in range(0, len(choices)):
    print(f'{i}) {choices[i]}')


user_input = int(input("\nWhat do you want to do? Choose number.\n"))
# user_input = f'{user + 1}'


if choices[user_input] == ADD:
    url = 'http://127.0.0.1:5000/blogs/add-new'
    title = input("Your title name?\n")
    text = input("\nWrite your text\n")
    myobj = {"title": title, "body": text}

    add_blog = requests.post(url, json = myobj)
    print(add_blog.text)

if choices[user_input] == DELETE:
    which_id = int(input("Which blog do you want to delete? Give id of that blog.\n"))
    id_blog = delete_id(which_id)
    d = requests.delete('http://127.0.0.1:5000//blogs/delete/<int:the_id>')
    print(d.status_code)


if choices[user_input] == FETCH:
    get_all = requests.get('http://127.0.0.1:5000/blogs')
    print(get_all.text)


# d = requests.delete("http://127.0.0.1:5000/customers/1")
# print(d.status_code)