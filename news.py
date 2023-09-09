from app import Noticia, db
import uuid
import markdown


class news():
  def __init__(self, id):
    self.id = id 


  def gerar_id(self):
    id = uuid.uuid4()
    return str(id)

  @staticmethod
  def transform_markdown(text):
    html = markdown.markdown(text)
    return str(html)

  def criar_noticia(self, titulo, conteudo, tag):
    idGerado = self.gerar_id()
    # Validações
    if tag == "" or tag == " ":
      return "digite uma tag"

    novaNoticia = Noticia(title=titulo, content=self.transform_markdown(conteudo), tag=tag, id=idGerado)
    db.session.add(novaNoticia)
    db.session.commit()

    return {
      "msg": "success",
      "id": novaNoticia.id 
    }

  def deletar_noticia(self):
    noticia = Noticia.query.filter_by(id=self.id).first()
    if not noticia:
      return "notícia não existe."
    else:
      db.session.delete(noticia)
      db.session.commit()
      return "noticia excluida com sucesso"

  def get_noticia(self):
    noticia = Noticia.query.filter_by(id=self.id).first()
    if noticia:
      return noticia
    else:
      return "noticia nao existe"

  def get_noticias_tag(self, tag):
    tag = tag.lower() 
    noticias = []

    noticias_db = Noticia.query.filter_by(tag=tag).all()
    if len(noticias_db) <= 0:
      return "nao existe noticias com essa tag."
    for ntc in noticias_db:
      noticias.append({
        "title": ntc.title,
        "id": ntc.id,
        "tag": ntc.tag
      })

    return noticias

  def get_noticias_all(self):
    noticias = Noticia.query.all()
    return noticias

  def get_tags_all(self):
    unique_tags = db.session.query(Noticia.tag).distinct().all()
    tags = [tag[0] for tag in unique_tags]
    return tags