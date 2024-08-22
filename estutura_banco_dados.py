from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '123123'
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blog.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


db = SQLAlchemy(app)
db:SQLAlchemy

class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))

class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')

def incializar_banco_de_dados():
    with app.app_context():
        db.drop_all()
        db.create_all()

        autor = Autor(nome = 'Ricardo', email = 'ricardo@reis.com.br', senha = '123456', admin = True)
        db.session.add(autor)
        db.session.commit()

if __name__ == '__main__':
    print(app.url_map)
    incializar_banco_de_dados()