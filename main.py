from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',resultado="")

@app.route('/resultado',methods=['POST'])
def resultado():
    numero = int(request.form['numero'])
    vez = 0
    num1 = 1
    num2 = 2

    while vez < numero:
        vez = vez + 1
        print(num1 * num2 // 2)
        v = (num1 * num2)//2 #Variável para guardar e usar na hora de retornar mais fácil
        a = num1 * num2
        num1 = num1 + 1
        num2 = a
    return render_template('index.html',resultado=f'O fatorial de {numero} é {v}')

if __name__ =='__main__':
    app.run(debug=True)