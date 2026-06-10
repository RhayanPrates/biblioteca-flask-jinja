from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class LivroModel(db.Model):
    __tablename__ = 'livros'
    
    isbn = db.Column(db.String(20), primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Helper para facilitar o retorno das APIs JSON"""
        return {"isbn": self.isbn, "titulo": self.titulo, "autor": self.autor}