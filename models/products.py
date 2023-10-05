import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db
from models.products_categories_xref import products_categories_association_table


class Products(db.Model):
    __tablename__ = "Products"

    product_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_name = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String())
    price = db.Column(db.Float())
    active = db.Column(db.Boolean(), default=True)
    category_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Categories.category_id", ondelete="CASCADE"), nullable=False)

    categories = db.relationship("Categories", secondary=products_categories_association_table, back_populates='products')

    def __init__(self, product_name, description, price, active, category_id):
        self.product_name = product_name
        self.description = description
        self.price = price
        self.active = active
        self.category_id = category_id


class ProductsSchema(ma.Schema):
    class Meta:
        fields = ["product_id", "product_name", "description", "price", "active", "categories"]

    categories = ma.fields.Nested("CategoriesSchema", many=True, exclude=['products'])


product_schema = ProductsSchema()
products_schema = ProductsSchema(many=True)
