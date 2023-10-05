from flask import jsonify, Request, Response

from db import db
from models.products import Products, product_schema, products_schema
from models.categories import Categories
from util.reflection import populate_object


def product_add(req: Request) -> Response:
    post_data = req.form if req.form else req.json
    product_name = post_data.get("product_name")
    description = post_data.get("description")
    price = post_data.get("price")
    active = True
    category_id = post_data.get("category_id")

    new_record = Products(product_name, description, price, active, category_id)

    db.session.add(new_record)
    db.session.commit()

    product_query = db.session.query(Products).filter(Products.product_name == product_name).first()
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    product_query.categories.append(category_query)
    db.session.commit()

    return jsonify(product_schema.dump(product_query)), 201


def products_get_all(req: Request) -> Response:
    query = db.session.query(Products).all()

    return jsonify(products_schema.dump(query)), 200


def product_get_by_id(req: Request, product_id) -> Response:
    query = db.session.query(Products).filter(Products.product_id == product_id).first()

    return jsonify(product_schema.dump(query)), 200


def product_update_by_id(req: Request, product_id) -> Response:
    post_data = req.form if req.form else req.json
    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()

    if product_query:

        populate_object(product_query, post_data)

    try:

        db.session.commit()

    except:

        db.session.rollback()

        return jsonify("Error: unable to update record")

    return jsonify(product_schema.dump(product_query)), 200


def product_delete_by_id(req: Request, product_id) -> Response:
    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()

    db.session.delete(product_query)
    db.session.commit()

    return jsonify(f"product with id {product_id} has been deleted"), 200


def product_activity(req: Request, product_id) -> Response:
    product_query = db.sessions.query(Products).filter(Products.product_id == product_id).first()

    product_query.active = not product_query.active

    try:

        db.session.commit()

        if product_query.active:

            return jsonify("Product activated successfully"), 200

        else:

            return jsonify("Product deactivated successfully"), 200

    except:

        db.session.rollback()

        return jsonify("Error: unable to activate/deactive product"), 400


def product_add_category(req: Request) -> Response:
    post_data = req.form if req.form else req.json
    product_id = post_data.get("product_id")
    category_id = post_data.get("category_id")

    product_query = db.session.query(Products).filter(Products.product_id == product_id).first()
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    product_query.categories.append(category_query)

    db.session.commit()

    return jsonify({"message": "Category added", "product": product_schema.dump(product_query)}), 200
