from traceback import print_tb
from flask import Flask
from flask import render_template
from flask import request
from repository import save_to_database
from repository import read_database
from validation import is_name
from string_helper import csv_to_list

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        #['first_name'] tulee tuolta html puolelta name='first_name'
        fname = request.form['first_name']
        lname = request.form['last_name']
        #validate the user input names
        ok_name = is_name(f"{fname} {lname}")
        if ok_name:
            #if name is valid, then save the gotten 
            # values from the browser to database.txt
            data = save_to_database(fname, lname)
            read = read_database()
            r_list = csv_to_list(read)
            print(r_list)
        else:
            print("Name must be contain 2 characters that are not numbers")
        
        # show_list = csv_to_list(read)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)