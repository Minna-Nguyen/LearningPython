from flask import Flask, make_response, request, render_template
import random

# kaikki minnan työtä :))))

app = Flask(__name__)


# @app.route("/set_cookie", methods=['POST', 'GET'])
# def set_cookie():
#     response = make_response("<p>Set a cookie</p>")
#     response.set_cookie("money", "20")
#     return response


# @app.route("/read_cookie", methods=['POST', 'GET'])
# def read_cookie():
#     money = request.cookies.get("money")

#     return money


# @app.route("/delete_cookie", methods=['POST', 'GET'])
# def delete():
#     response = make_response("what's happening")
#     response.delete_cookie("money")
#     return response


@app.route("/slot_machine", methods=['POST', 'GET'])
def slot_machine():
    random_img = [random.randint(1, 3), random.randint(
        1, 3), random.randint(1, 3)]
    # read browser cookie (should display 20)
    money = request.cookies.get("money")
    win = "Jackpot!"
    lose = "You lose."
    response = make_response()

    if money == None:
        money = 20
    elif money == "1":
        response = make_response(render_template('index.html', lista=random_img, win=win, lose=lose, money="0")) #asettaa sinne html puolelle rahaksi 0€, mutta poistaa ton cookien 1 kohdalla
        response.delete_cookie("money")
        # response.set_cookie("money", "", expires=0)

        return response

    else:
        money = str(int(money) - 1)

    if random_img[0] == random_img[1]  and random_img[1] == random_img[2]:
        money = str(int(money) + 5)

    response = make_response(render_template('index.html', lista=random_img, win=win, lose=lose, money=money))
    response.set_cookie("money", f"{money}")

    return response


if __name__ == "__main__":
    app.run(debug=True)
