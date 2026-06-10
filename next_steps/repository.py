from database import db, LivroModel

class LivroRepository:
    
    @staticmethod
    def listar_todos():
        return LivroModel.query.all()
    
    @staticmethod
    def buscar_por_isbn(isbn):
        return LivroModel.query.get(isbn)
    
    @staticmethod
    def salvar(isbn, titulo, autor):
        # Verifica se já existe para evitar crash
        existe = LivroModel.query.get(isbn)
        if existe:
            return False
            
        novo_livro = LivroModel(isbn=isbn, titulo=titulo, autor=autor)
        db.session.add(novo_livro)
        db.session.commit()
        return True
        
    @staticmethod
    def deletar(isbn):
        livro = LivroModel.query.get(isbn)
        if livro:
            db.session.delete(livro)
            db.session.commit()
            return True
        return False

    @staticmethod
    def atualizar(isbn, dados_alterados):
        livro = LivroModel.query.get(isbn)
        if livro:
            for chave, valor in dados_alterados.items():
                if hasattr(livro, chave):
                    setattr(livro, chave, valor)
            db.session.commit()
            return True
        return False