from db import db

products_categories_association_table = db.Table(
    "ProductCategoryAssociation",
    db.Model.metadata,
    db.Column('product_id', db.ForeignKey("Products.product_id"), primary_key=True),
    db.Column('Category_id', db.ForeignKey("Categories.category_id"), primary_key=True)
)
