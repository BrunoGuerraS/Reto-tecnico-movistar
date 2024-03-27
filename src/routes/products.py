from flask import Blueprint, jsonify, render_template, request

from utils.scraper import products as scraped_products

products = Blueprint("products", __name__)


@products.route("/products")
def get_product():
    try:
        if scraped_products:
            return jsonify(scraped_products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# @products.route("/products")
# def get_product():
#     return render_template("products.html", name="products")


@products.route("/products/<int:id>")
def get_products(id):
    return f"Hello product {id}"


@products.route("/products/<int:id>", methods=["PUT"])
def put_product(id):
    return f"Product {id} updated"


@products.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    return f"Product {id} deleted"
