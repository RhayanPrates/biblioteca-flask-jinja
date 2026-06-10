from flask import Flask, render_template, request, redirect, url_for, jsonify
from database import db
from repositories import LivroRepository

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
db.init_app(app)

# Rota de exemplo unificada usando o Repositório
@app.route('/biblioteca', methods=['GET', 'POST'])
def interface_web():
    if request.method == 'POST':
        acao = request.form.get('acao')
        
        if acao == 'cadastrar':
            LivroRepository.salvar(
                isbn=request.form.get('isbn'),
                titulo=request.form.get('titulo'),
                autor=request.form.get('autor')
            )
        elif acao == 'deletar':
            LivroRepository.deletar(request.form.get('isbn'))
            
        return redirect(url_for('interface_web'))
        
    livros = LivroRepository.listar_todos()
    return render_template('biblioteca.html', biblioteca=[l.to_dict() for l in livros])

# A API também passa a consumir o MESMO repositório, matando a duplicação!
@app.route('/api/biblioteca/<isbn>', methods=['DELETE'])
def api_deletar_livro(isbn):
    sucesso = LivroRepository.deletar(isbn)
    if sucesso:
        return jsonify("mensagem: livro deletado com sucesso"), 200
    return jsonify("message: livro não localizado"), 404