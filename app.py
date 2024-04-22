from flask import Flask, render_template, request, redirect, url_for
import galaxias_BD

app = Flask(__name__)

@app.route('/')
def inicio():
    galaxias = galaxias_BD.listar_galaxias()
    return render_template('index.html', dados=galaxias)

@app.route('/cadastrar')
def criar():
    return render_template("cadastrar.html")

@app.route('/criar', methods=['POST'])
def criar_galaxia():
    nome = request.form['nome']
    estrelaPrincipal = request.form['estrela']
    distancia = request.form['distancia']
    imagem = request.form['imagem']

    galaxias_BD.inserir_galaxia(nome, estrelaPrincipal, distancia, imagem)
    return redirect(url_for('inicio'))

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_galaxia_route(id):
    galaxias_BD.deletar_galaxia(id)
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    galaxia = galaxias_BD.retornar_galaxia(id)
    if galaxia:
        return render_template('editar.html', id=id, galaxia=galaxia)
    return redirect(url_for('inicio'))

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        estrelaPrincipal = request.form['estrela']
        distancia = request.form['distancia']
        imagem = request.form['imagem']
        
        if galaxias_BD.retornar_galaxia(id):
            galaxias_BD.atualizar_galaxia(id, nome, estrelaPrincipal, distancia, imagem)
            return redirect(url_for('inicio'))
        else:
            return 'Galáxia não encontrada!', 404

if __name__ == '__main__':
    galaxias_BD.criar_tabela()
    app.run(debug=True)
