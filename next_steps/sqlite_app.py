from flask import Flask, render_template, request, redirect, url_for
from database import db, LivroModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Cria as tabelas na primeira execução
with app.app_context():
    db.create_all()

# --- REGRAS USANDO ORM SUBISTITUINDO O SQL PURO ---
@app.route('/biblioteca', methods=['GET', 'POST'])
def interface_web():
    if request.method == 'POST':
        acao = request.form.get('acao')
        
        if acao == 'cadastrar':
            novo = LivroModel(
                isbn=request.form.get('isbn'),
                titulo=request.form.get('titulo'),
                autor=request.form.get('autor')
            )
            db.session.add(novo)
            db.session.commit()
            
        elif acao == 'deletar':
            isbn = request.form.get('isbn')
            livro = LivroModel.query.get(isbn)
            if livro:
                db.session.delete(livro)
                db.session.commit()
                
        return redirect(url_for('interface_web'))
        
    livros = LivroModel.query.all()
    return render_template('biblioteca.html', biblioteca=[l.to_dict() for l in livros])