import requests
from main import delete_id
from main import update_certain_blog



# from flask import Flask, jsonify, request, make_response
# import json


# app = Flask(__name__)

# id = 3
# blogs = [{"id": 1, "title": "titleone", "body": "bunch of texts"}, {"id": 2, "title": "title two", "body": "bunch of texts"}, {
#     "id": 3, "title": "sunt aut facere repellat provident - optio reprehenderit", "body": "quia et suscipit\nsuscipit recusa... "}]

# @app.route('/blogs/update/<int:update_id>', methods=['POST', 'GET'])
# def update_certain_blog(update_id):
#     # with app.app_context():
#         for i in range(0, len(blogs)):
#             # go through all the elements, take certain blog by 'id' and update
#             if  blogs[i]["id"] == update_id:
#                 blogs[i].update({"title":"Mayday", "body":"Mayday is when..."})
#                 return jsonify(blogs[i])


# @app.route('/blogs/delete/<int:the_id>', methods=['DELETE'])
# def delete_id(the_id):
#     index_to_be_deleted = -1
#     for i in range(0, len(blogs)):
#         if(blogs[i]["id"] == the_id):
#             index_to_be_deleted = i
#     if(index_to_be_deleted != -1):
#         blogs.pop(index_to_be_deleted)
#         return make_response("", 204)
#     else:
#         return make_response("", 404)

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

# if choices[user_input] == DELETE:
#     which_id = int(input("Which blog do you want to delete? Give id of that blog.\n"))

#     id_blog = delete_id(which_id)
#     d = requests.delete('http://127.0.0.1:5000//blogs/delete/which_id')
#     print(d.status_code)

if choices[user_input] == UPDATE:
    # def create_app():
        # input = int(input("What blog do you want to update? Give id.\n"))
        get_all = requests.get('http://127.0.0.1:5000/blogs')
        print(get_all.text)
        x = int(input("Give id of the blog.\n"))
        title = input("Title fo the blog\n")
        text = input("\nPost your text\n")
        update_id = update_certain_blog(x, new_post)


        update_blog = requests.post('http://127.0.0.1:5000/blogs/update/<update_id>')
        print(update_blog.text)


if choices[user_input] == FETCH:
    get_all = requests.get('http://127.0.0.1:5000/blogs')
    print(get_all.text)

# d = requests.delete("http://127.0.0.1:5000/customers/1")
# print(d.status_code)