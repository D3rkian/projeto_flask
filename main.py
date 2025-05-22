from flask import Flask, render_template


app = Flask(__name__)




@app.route('/')
def index():


    return 'Olá Mundo!'




@app.route('/render')
def render():
    return render_template('index.html', email='alba@ifrn.edu.br', tel='(84) 99999-9999')




if __name__ == '__main__':
    app.run(debug=True)