from flask import render_template, jsonify, redirect, request
from app import app 
from news import news
@app.route("/")
def homepage():
  news_all = news("sla").get_noticias_all()
  return render_template("index.html", news=news_all)

@app.route("/create")
def createNoticiaPage():
  return render_template("create-noticia.html")

@app.route("/api/create-noticia", methods=["POST"])
def createRoute():
  titulo = request.form["title"]
  conteudo = request.form["conteudo"]
  tag = request.form["tag"]
  
  # Criar a noticica
  news_response = news("sla").criar_noticia(titulo, conteudo, tag)
  print(news_response)
  if news_response["msg"] == "success":
    return redirect(f"/noticia/{news_response['id']}")
  else:
    return "Erro ao postar a notícia"

@app.route("/noticia/<id>")
def noticiaPage(id):
  noticia = news(id).get_noticia()
  return render_template("noticia.html", artigo=noticia)

@app.route("/search")
def searchPage():
  tags = news("sla").get_tags_all()
  return render_template("search.html", tags=tags)

@app.route("/tag/<tag>")
def tagsPage(tag):
  noticias = news("sla").get_noticias_tag(tag)
  return render_template("tag.html", news=noticias)