from ast import Return
from flask import Flask
from htmlhelper import generate_html_page
import random

# create Flask object, give module name
# where to look for resources, like templates or static files
app = Flask(__name__)

# if url is in root
@app.route("/slot-machine")
def slot_machine():
    apple = '"static/omena.jpg" width="256" height="256" alt="apple"'
    banana = '"static/banana.jpg" width="256" height="256" alt="banana"'
    mansikka = '"static/mansikka.jpg" width="256" height="256" alt="strawberry"'
    fruits = [apple, banana, mansikka]
    for fruit in fruits:
        # return f"<p>{random.randint(fruit, len(fruits))}</p>"
        return f"<p>{random.randint(fruit,len(fruits))}</p>"
    helper1  = generate_html_page("testing",banana)
    helper2  = generate_html_page("testing",apple)
    helper3  = generate_html_page("testing",mansikka)
    # return fruits

# start the app if using python3 app.py
if __name__ == "__main__":
    app.run(debug=True)