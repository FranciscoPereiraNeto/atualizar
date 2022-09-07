from crypt import methods
from flask import Flask, render_template, request
from model import model
import this

this.nome = ""
this.telefone = ""
this.endereco = ""
this.data = ""
this.dados = ""
this.modelo = model()
this.codigo = 0
this.msg = ""


pessoa = Flask(__name__)

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nome       =request.form['tNovoNome']
        this.telefone   =request.form['tNovoTelefone']
        this.endereco   =request.form['tNovoEndereco']
        this.data       =request.form['tNovoData']
        this.dados      =this.modelo.inserir(this.nome, this.telefone, this.endereco, this.data)
    return render_template('index.html', titulo="Página Principal", resultado=this.dados)
@pessoa.route('/consultar.html', methods=['GET','POSt'])
def consultarTudo():
    if request.method == 'POST':
        this.msg = this.modelo.consultar()
        return render_template('consultar.html', titulo="Consultar", dados=this.msg)



if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)
    
    


