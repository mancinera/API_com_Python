from flask import Flask, jsonify, request#

app = Flask(__name__)# Aqui estamos iniciando o app com o flask definindo seu nome como o nome do nosso arquivo em python.

livros = [#Aqui estamos criando uma lista para armazenar nossos livros que teremos na nossa API.
    {
        'id': 1,
        'título': 'Ó Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J. K Howling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atomicos',
        'autor': 'James Clear'
    }
]


#Criar
@app.route('/livros', methods=['POST'])#Aqui estamos criando uma funcao que nos permite criar/incluir novos livros dentro da nossa lista.

#Nesse caso, criamos a funcao com nome incluir_novo_livro sem parametros. Criamos uma variavel com nome novo_livro para obter/salvar o livro que o usuario digitar. Apos isso, usamos a funcionalidade append para incluir o livro na nossa lista. Usamos o metodo HTTP POST.
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)
#Consultar (Todos)
@app.route('/livros', methods=['GET'])#Aqui estamos criando uma funcao nos permite consultar todos nossos livros dentro da lista. Criamos uma funcao que nos retorna em jsonify utilizando o metodo HTTP GET. 
def obter_livros():
    return jsonify(livros)
# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])#Aqui estamos criando uma funcao onde nos permite consultar nossos livros de nossa lista por id. É feito um loop nomeado livro que passa pelos nossa lista de livros e que caso o id deles seja igual ao id cadastrado em nossa lista, ele trará o mesmo para visualizacao usando o metodo HTTP GET.
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@app.route('/livros/<int:id>', methods=['PUT'])#Aqui criamos estamos criando uma variavel que carrega a funcionalocade request.get_json para guardar o valor que o usuario passar. Criamos o looping indice/livro para pegar o indice dos nossos livros e inumerar os mesmo para realizar a estrutura de condicao onde se o id passado no parameto for igual o id o livro na lista entao sera atualizado a informacao descritao no mesmo.
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])#Aqui estamos criando uma funcao onde tambem pegando pelo indice dos livros e seu id, enumeramos ele e caso o livro com id passado seja igual o id do livro na lista entao o livro do id/indice sera excluido da lista.
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)#Aqui estamos iniciando nosso servidor local na porta 5000 onde poderemos visualizar toda nossa operacao.