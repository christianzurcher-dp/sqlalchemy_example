from flask import request, Response, Blueprint

import controllers

categories = Blueprint('categories', __name__)


@categories.route('/category', methods=['POST'])
def category_add() -> Response:
    return controllers.category_add(request)


@categories.route('/categories', methods=['GET'])
def categories_get_all() -> Response:
    return controllers.categories_get_all(request)


@categories.route('/category/<category_id>', methods=['GET'])
def category_get_by_id(category_id) -> Response:
    return controllers.category_get_by_id(request, category_id)


@categories.route('/category/<category_id>', methods=['PUT'])
def category_update_by_id(category_id) -> Response:
    return controllers.category_update_by_id(request, category_id)


@categories.route('/category/<category_id>', methods=['DELETE'])
def category_delete_by_id(category_id) -> Response:
    return controllers.category_delete_by_id(request, category_id)


@categories.route('/category/<category_id>', methods=['PATCH'])
def category_activity(category_id) -> Response:
    return controllers.category_activity(request, category_id)
