from flask import Flask
import datetime
from htmlhelper import generate_html_page
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
    date = datetime.datetime.now()
    p_element = f"<p>{date}</p>"
    # apple = f'{apple.png}'
    html_page = generate_html_page("DATE", p_element)
    return html_page


# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)