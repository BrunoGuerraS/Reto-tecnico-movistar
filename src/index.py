from flask import Flask, jsonify, request

from routes.products import products

app = Flask(__name__, template_folder="layout")

app.register_blueprint(products)


if __name__ == "__main__":
    app.run(debug=True)
