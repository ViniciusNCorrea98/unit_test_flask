from flask import Blueprint, current_app, request, jsonify
from model import Book
from serealizer import BookSchema

bp_books = Blueprint('books', __name__)

@bp_books.route('/mostrar', methos=['GET'])
def listar_livros():
    bs= BookSchema(many=True)
    result = Book.query.all()
    return bs.jsonify(result), 200

@bp_books.route('/deletar/<id>', methods=['DELETE'])
def deletar_livro(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
    return jsonify('Livro deletado com sucesso!!')

@bp_books.route('/atualizar/<id>', methods=['PUT'])
def atualizar_livro(id):
    bs = BookSchema()
    query = Book.query.filter(Book.id == id)
    query.update(request.json)
    current_app.db.session.commit()
    return bs.jsonify(query.first())

@bp_books.route('/cadastrar', methods=['POST'])
def cadastrar_livro():
    bs = BookSchema()
    book, error = bs.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    return bs.jsonify(book), 200