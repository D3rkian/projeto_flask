from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def render_base():
    return "<h2>Olá, mundo!</h2><a href='/bas'>Clique aqui</a>"

@app.route('/bas')
def render_bas():
    return render_template('basee.html')



# @app.route('/base')
# def render():
#    return render_template('base.html', email='alba@ifrn.edu.br', tel='(84) 99999-9999')

@app.route('/basee')
def render_basee():
    return render_template('baseef1.html')

@app.route('/baseee')
def render_baseee():
    return render_template('baseef2.html')


#@app.route('/<pessoa>')
#def exibir_contato_de_alguem(pessoa):

                        #   contato = {
                                        #      "alba": {"email": "alba@ifrn.edu.br", "tel": "(84) 99999-9999"},
                                        #     "joao": {"email": "joao.silva@email.com", "tel": "(84) 88888-8888"},
                                        #    "maria": {"email": "maria.santos@email.com", "tel": "(84) 77777-7777"}
    #}

    #dados_pessoa = contato.get(pessoa.lower(), {
     #                          "email": "não", "tel": "não", "nome": pessoa})

    #if 'nome' not in dados_pessoa:
     #   dados_pessoa['nome'] = pessoa.capitalize()

    #return render_template('htmlfilho1.html',
     #                      nome_exibido=dados_pessoa['nome'],
      #                     email_exibido=dados_pessoa['email'],
       #                    tel_exibido=dados_pessoa['tel'])


if __name__ == '__main__':
    app.run(debug=True)
