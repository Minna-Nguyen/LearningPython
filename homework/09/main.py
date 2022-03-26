from flask import Flask, jsonify, request, make_response
import json


app = Flask(__name__)

id = 3
blogs = [{"id": 1, "title": "titleone", "body": "bunch of texts"}, {"id": 2, "title": "title two", "body": "bunch of texts"}, {
    "id": 3, "title": "sunt aut facere repellat provident - optio reprehenderit", "body": "quia et suscipit\nsuscipit recusa... "}]

# listaa kaikki blogit
@app.route('/blogs')
def get_blogs():
    return jsonify(blogs)

# lisää uusi blogi 
@app.route('/blogs', methods=['POST'])
def add_blog():
    blog = json.loads(request.data)
    # https://www.programiz.com/python-programming/global-keyword
    # global id
    # id = id + 1
    # blog["id"] = id
    # blogs.append(blog)

    global id
    id = id + 1
    blog["id"] = id
    blogs.append(blog)
    return make_response(jsonify(blog), 201)


# tarkista tietty blogi
@app.route('/blogs/<int:id>', methods=['GET'])
def get_certain_blog(id):
    for i in range(0, len(blogs)):
        if  blogs[i]["id"] == id:
            result = jsonify(blogs[i])
            return result

#päivitä tietty blogi
@app.route('/blogs/update/<int:update_id>', methods=['GET'])
def update_certain_blog(update_id):
    for i in range(0, len(blogs)):
        # go through all the elements, take certain blog by 'id' and update
        if  blogs[i]["id"] == update_id:
            blogs[i].update({"title":"Mayday", "body":"Mayday is when..."})
            return jsonify(blogs[i])

# poista tietty blogi
@app.route('/blogs/<int:the_id>', methods=['DELETE'])
def delete_id(the_id):
    index_to_be_deleted = -1
    for i in range(0, len(blogs)):
        if(blogs[i]["id"] == the_id):
            index_to_be_deleted = i
    if(index_to_be_deleted != -1):
        blogs.pop(index_to_be_deleted)
        return make_response("", 204)
    else:
        return make_response("", 404)

# poista kaikki blogit
@app.route('/blogs/delete_all', methods=['DELETE'])
def delete_blog():
    for i in range(0, len(blogs)):
        if blogs[i] != None:
            blogs.clear()
            if blogs == []:
                return make_response("", 204)
            else:
                return make_response("", 404)

        if request.method == "POST":
            return "hello"


if __name__ == "__main__":
    app.run(debug=True)
