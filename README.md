# 📚 Sistema de Biblioteca - Flask & Jinja2

Este é um projeto pedagógico desenvolvido em sala de aula para a turma de Python. O objetivo principal é compreender na prática o funcionamento do protocolo **HTTP**, a criação de rotas e servidores web com o microframework **Flask**, e a renderização dinâmica de páginas HTML utilizando o motor de templates **Jinja2**.

---

## 🛠️ Objetivos de Aprendizado

Com este código, praticamos e aprendemos:
1. **Conceitos de HTTP:** Como funcionam requisições (`Requests`) e respostas (`Responses`), além dos métodos HTTP (foco inicial em `GET` e `POST`).
2. **Rotas com Flask:** Como mapear uma URL do navegador para uma função específica no Python usando `@app.route()`.
3. **Templates Dinâmicos (Jinja2):** Como parar de servir arquivos HTML estáticos e passar variáveis do backend (Python) para o frontend (HTML).
4. **Estruturas de Controle no HTML:** Como utilizar loops (`{% for %}`) e condicionais (`{% if %}`) diretamente nas páginas web.

---

## 📂 Estrutura do Projeto

Abaixo está a estrutura padrão adotada no projeto (crucial para o Flask localizar os arquivos corretamente):

```text
biblioteca-flask-jinja/
│
├── app.py                # Arquivo principal contendo o servidor e as rotas Flask
├── README.md             # Documentação do projeto
│
├── templates/            # PASTA OBRIGATÓRIA: Onde o Flask busca os arquivos HTML
│   ├── base.html         # Template base (herança de layout do Jinja2)
│   ├── index.html        # Página inicial (listagem de livros)
│   └── cadastrar.html    # Formulário de cadastro de livros
│
└── static/               # PASTA OBRIGATÓRIA: Para arquivos estáticos (CSS, imagens, JS)
    └── css/
        └── style.css     # Estilização visual da biblioteca