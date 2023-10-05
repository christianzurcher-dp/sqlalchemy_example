from flask import jsonify, Request, Response

from db import db
from models.categories import Categories, category_schema, categories_schema
from util.reflection import populate_object


def category_add(req: Request) -> Response:
    post_data = req.form if req.form else req.json
    category_name = post_data.get("category_name")

    new_record = Categories(category_name)

    db.session.add(new_record)
    db.session.commit()

    query = db.session.query(Categories).filter(Categories.category_name == category_name).first()

    return jsonify(category_schema.dump(query)), 201


def categories_get_all(req: Request) -> Response:
    query = db.session.query(Categories).all()

    return jsonify(categories_schema.dump(query)), 200


def category_get_by_id(req: Request, category_id) -> Response:
    query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    return jsonify(category_schema.dump(query)), 200


def category_update_by_id(req: Request, category_id) -> Response:
    post_data = req.form if req.form else req.json
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    if category_query:

        populate_object(category_query, post_data)

    db.session.commit()

    return jsonify(category_schema.dump(category_query)), 200


def category_delete_by_id(req: Request, category_id) -> Response:
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    if category_query:

        db.session.delete(category_query)
        db.session.commit()

        return jsonify(f"category with id {category_id} has been deleted"), 200

    return jsonify(f"Error: category with id {category_id} could not be found"), 404


def product_activity(req: Request, category_id) -> Response:
    category_query = db.sessions.query(Categories).filter(Categories.category_id == category_id).first()

    category_query.active = not category_query.active

    try:

        db.session.commit()

        if category_query.active:

            return jsonify("Category activated successfully"), 200

        else:

            return jsonify("Category deactivated successfully"), 200

    except:

        db.session.rollback()

        return jsonify("Error: unable to activate/deactive Category"), 400


def category_activity(req: Request, category_id) -> Response:
    category_query = db.sessions.query(Categories).filter(Categories.category_id == category_id).first()

    category_query.active = not category_query.active

    try:

        db.session.commit()

        if category_query.active:

            return jsonify("Product activated successfully"), 200

        else:

            return jsonify("Product deactivated successfully"), 200

    except:

        db.session.rollback()

        return jsonify("Error: unable to activate/deactive product"), 400
