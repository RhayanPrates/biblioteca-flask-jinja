# 📚 Material de Apoio – Sistema de Biblioteca com Flask e Jinja2

## Apresentação

Este projeto foi desenvolvido durante aulas de *live coding* com o objetivo de introduzir conceitos fundamentais do desenvolvimento web utilizando Python e Flask.

Mais importante do que o resultado final, este repositório representa uma jornada de aprendizagem que começa com conceitos básicos da Web e evolui até a construção de uma aplicação dinâmica utilizando templates Jinja2.

Ao estudar este projeto, procure identificar não apenas o que cada trecho de código faz, mas também qual problema ele resolve.

---

# Arquitetura Cliente-Servidor

## Objetivo

Compreender como aplicações web funcionam.

Antes do Flask, é importante entender que uma aplicação web possui dois lados:

### Cliente

Normalmente um navegador:

* Chrome
* Firefox
* Edge
* Safari

Ou uma aplicação, em nossa aula utilizamos:
* Thunder Client - Extensão do VS Code

Mas podemos utilizar outros, como:
* Postman
* Httpie

O cliente faz solicitações ao servidor.

### Servidor

Responsável por:

* Receber requisições
* Processar dados
* Gerar respostas

No projeto, o servidor é criado pelo Flask.

```python
app = Flask(__name__)
```

---

## Fluxo Básico

```text
Navegador
    ↓
Requisição HTTP
    ↓
Servidor Flask
    ↓
Resposta HTTP
    ↓
Navegador
```

---

# Protocolo HTTP

## Objetivo

Entender como cliente e servidor se comunicam.

HTTP é o protocolo utilizado para transmitir informações na Web.

### Métodos HTTP

#### GET

Solicita informações.

Exemplo:

```text
GET /api/biblioteca
```

#### POST

Envia informações para o servidor.

Exemplo:

```text
POST /api/biblioteca
```

#### PUT

Atualiza informações.

Exemplo:

```text
PUT /api/biblioteca/123
```

#### DELETE

Remove informações.

Exemplo:

```text
DELETE /api/biblioteca/123
```

---

## Status Codes

### 200

Operação realizada com sucesso.

### 201

Recurso criado.

### 404

Recurso não encontrado.

### 503

Serviço indisponível.

---

# Introdução ao Flask

## Objetivo

Criar um servidor web utilizando Python.

### Criando a aplicação

```python
app = Flask(__name__)
```

### Criando uma rota

```python
@app.route('/')
def hello():
    return "Olá Mundo"
```

Quando o navegador acessa:

```text
http://localhost:5000/
```

o Flask executa a função correspondente.

---

## Rotas Dinâmicas

Também é possível capturar informações diretamente pela URL.

```python
@app.route('/<nome>')
def meu_nome(nome):
    return nome
```

Exemplo:

```text
http://localhost:5000/joao
```

Resultado:

```text
joao
```

---

# Construindo uma API

## Objetivo

Disponibilizar dados para outros sistemas.

Uma API retorna dados ao invés de páginas HTML.

### Exemplo

```python
return jsonify(biblioteca)
```

Resposta:

```json
[
  {
    "isbn": "123",
    "titulo": "Python"
  }
]
```

---

## Endpoints da API

### Listar livros

```text
GET /api/biblioteca
```

### Buscar livro

```text
GET /api/biblioteca/<isbn>
```

### Cadastrar livro

```text
POST /api/biblioteca
```

### Alterar livro

```text
PUT /api/biblioteca/<isbn>
```

### Excluir livro

```text
DELETE /api/biblioteca/<isbn>
```

---

# Trabalhando com Request

## Objetivo

Receber informações enviadas pelo cliente.

### Query String

URL:

```text
/biblioteca?isbn=123
```

Código:

```python
isbn = request.args.get('isbn')
```

---

### JSON

Recebendo dados enviados por uma API:

```python
novo_livro = request.get_json()
```

Exemplo:

```json
{
  "isbn": "123",
  "titulo": "Python para Web"
}
```

---

# Renderizando Templates

## Objetivo

Gerar páginas HTML dinamicamente.

Antes:

```python
return "<h1>Olá</h1>"
```

Depois:

```python
return render_template(
    'biblioteca.html',
    biblioteca=biblioteca
)
```

O Flask passa dados para o template.

---

## Fluxo

```text
Python
   ↓
render_template()
   ↓
Jinja2
   ↓
HTML Final
   ↓
Navegador
```

---

# Introdução ao Jinja2

## Objetivo

Inserir lógica dentro do HTML.

---

## Variáveis

```html
{{ livro.titulo }}
```

---

## Loops

```html
{% for livro in biblioteca %}
```

Permite percorrer listas.

---

## Condicionais

```html
{% if key[0] == 'isbn' %}
```

Permite tomar decisões.

---

## Filtros

Maiúsculas:

```html
{{ texto | upper }}
```

Capitalização:

```html
{{ texto | capitalize }}
```

Substituição:

```html
{{ texto | replace('_',' ') }}
```

---

## Herança de Templates

Template base:

```html
{% extends 'base.html' %}
```

Blocos reutilizáveis:

```html
{% block conteudo %}
```

Essa abordagem evita repetição de código HTML.

---

# Desafio para o Aluno

Após compreender o projeto, tente implementar:

### Nível 1

* Página de cadastro de livros.

### Nível 2

* Página de edição de livros.

### Nível 3

* Campo de busca por título.

### Nível 4

* Filtro por gênero.

### Nível 5

* Paginação da tabela.

---

# Conclusão

Ao final deste projeto você terá praticado:

✅ Arquitetura Cliente-Servidor

✅ HTTP

✅ Flask

✅ Rotas

✅ APIs REST

✅ Request

✅ Templates

✅ Jinja2

✅ Integração Backend e Frontend

# Próximos Passos

❌ Formulários html
❌ Implementação de banco de dados
❌ Uso de ORM
❌ Criação de Repositories
