from flask import Flask, make_response, jsonify, request


app = Flask("AtvBD")
app.config['JSON_SORT_KEYS'] = False

Usuarios = [
    {
        'nome': 'Joao',
        'cpf': 1111,
        'data_nasc': '16/02/2000'
    },
    {
        'nome': 'Jose',
        'cpf': 2222,
        'data_nasc': '13/02/2004'
    },
    {
        'nome': 'Pedro',
        'cpf': 3333,
        'data_nasc': '26/02/2020'
    }

]

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return make_response(jsonify('Lista de usuários', Usuarios))
    
@app.route('/cadastro', methods=['POST'])
def post_usuario():
    usuario = request.json
    Usuarios.append(usuario)
    return make_response(jsonify('Usuario cadastrado', usuario))

@app.route('/usuario', methods=['GET'])
def get_usuario_cpf():
    cpf = request.json
    for x in Usuarios:
        if x.get('cpf') == cpf:
            return jsonify(x)


app.run()