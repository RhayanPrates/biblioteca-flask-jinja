from flask import Flask, render_template, request, redirect, url_for
import dados

app = Flask(__name__)
biblioteca = dados.carregar_do_arquivo()

# --- FUNÇÕES AUXILIARES DE MANIPULAÇÃO DE DADOS ---
def adicionar_livro_lista(novo_livro):
    for l in biblioteca:
        if l['isbn'] == novo_livro['isbn']:
            return False
    biblioteca.append(novo_livro)
    dados.salvar_no_arquivo(biblioteca)
    return True

def deletar_livro_lista(isbn):
    for l in biblioteca:
        if l['isbn'] == isbn:
            biblioteca.remove(l)
            dados.salvar_no_arquivo(biblioteca)
            return True
    return False

# --- ROTAS ---
@app.route('/biblioteca', methods=['GET', 'POST'])
def interface_web():
    if request.method == 'POST':
        # Identifica qual ação o formulário enviou (cadastrar ou deletar)
        acao = request.form.get('acao')
        
        if acao == 'cadastrar':
            novo_livro = {
                'isbn': request.form.get('isbn'),
                'titulo': request.form.get('titulo'),
                'autor': request.form.get('autor')
            }
            adicionar_livro_lista(novo_livro)
            
        elif acao == 'deletar':
            isbn = request.form.get('isbn')
            deletar_livro_lista(isbn)
            
        return redirect(url_for('interface_web'))
        
    return render_template('biblioteca.html', biblioteca=biblioteca)