from flask import Flask, request, jsonify
from flask_cors import CORS 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data4.db'
app.secret_key = "123"
db = SQLAlchemy(app)
CORS(app)

class Noticia(db.Model):
  title = db.Column(db.String())
  id = db.Column(db.String(), primary_key=True)
  content = db.Column(db.String())
  tag = db.Column(db.String()) # Informações da Notícia, Ex.: Desenvolvimento Web, Python, Ciência de Dados...

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=9090)