from flask_marshmallow import Marshmallow

from app.model import Book

marsh = Marshmallow()

def configure(app):
    marsh.init_app(app)

class BookSchema(marsh.ModelSchema):
    class Meta:
        model = Book