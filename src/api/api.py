class Database:
    def __init__(self) -> None:
        with open("MOCK_DATA.json", "r") as file:
            self.data = json.load(file)

    def get_data(self):
        print("fetching data...")
        return self.data


database = Database()


def process_data(data):
    return sum(1 if product["available"] else 0 for product in data["products"])


def get_stock(data):
    return {"available": len(data["products"])}


import flask
import json

app = flask.Flask(__name__)


@app.route("/list")
def get_list():
    data = database.get_data()
    return flask.jsonify(data), 200


@app.route("/available")
def get_available():
    data = database.get_data()
    available = process_data(data)

    response = {"available": available}
    return flask.jsonify(response), 200


@app.route("/number")
def get_number():
    data = database.get_data()
    response = process_data(data)
    return flask.jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)

import requests
import json

res = requests.get("192.168.100.2/list")
