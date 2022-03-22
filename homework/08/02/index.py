from flask import Flask, redirect, request, render_template, session, url_for


app = Flask(__name__)

app.secret_key = "itsasecret"

@app.route("/")
@app.route("/page1")
def index():
    #jos ei ole 'session' niin vie käyttäjä kirjautusmissivustolle
    if session.get("username") == None:
        return render_template("login.html")
        # näytä kirjauduttu sivusto
    else:
        return render_template("page1.html", username=session['username'])

@app.route("/login", methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        #käyttäjän syöte
        name = request.form['username']
        password = request.form['password']
        #tallenna käyttäjän syötteet tänne session
        session['username'] = name
        session['password'] = password

        if session['username'] == "Minna" and session['password'] == "apua123":
            return render_template("page1.html", username=session['username'])
        else:
            return render_template("error.html")
    return render_template("login.html")

@app.route("/page2")
def page2():
    if session.get("username"):
        return render_template("page2.html", username=session['username'])
        # jos ei löydy username session, vie takaisin kirjautumissivustolle
    else:
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('password', None)

    return redirect('login')

if __name__ == "__main__":
    app.run(debug=True)