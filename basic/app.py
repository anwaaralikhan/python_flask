from datetime import datetime,timedelta,date
from flask import Flask,jsonify
from quotes import funny_quotes

import random


app = Flask(__name__)
print(datetime.now().date())


@app.route("/api/v1/funny")
def server_funny_quotes():
    quotes = funny_quotes()
    nr_of_quotes = len(quotes)
    selected_quote = quotes[random.randint(0, nr_of_quotes -1)]
    return jsonify(selected_quote)


@app.route("/api/v1/datetime")
def getDateTime():
    return jsonify(str(datetime.now().date()) + " - " + str(datetime.now().time()))


if __name__ == "__main__":
    app.run(debug=True)
