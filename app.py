from flask import Flask, request, jsonify
from flask_cors import CORS 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data1.db' # Caminho do arquivo do banco de dados
app.secret_key = "123"
db = SQLAlchemy(app)
CORS(app)

class Noticia(db.Model):
  title = db.Column(db.String()) # Titulo da Notícia
  id = db.Column(db.String(), primary_key=True) # ID da notícia
  content = db.Column(db.String()) # Conteudo da notícia.
  tag = db.Column(db.String()) # Informações da Notícia, Ex.: Desenvolvimento Web, Python, Ciência de Dados...

with app.app_context():
    db.create_all()

from routes import * 

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9090)