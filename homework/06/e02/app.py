from flask import Flask
import datetime
# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)

# if url is in root
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/myname")
def myname():
    return "<p>Minna<p/>"

@app.route("/date")
def date():
    x = datetime.datetime.now()
    return f"<p>{x}</p>"

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)