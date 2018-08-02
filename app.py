from flask import Flask, request

app = Flask(__name__)

count = 0

@app.route("/", methods=['GET', 'POST'])
def hello():
    """
    Método maneja comportamiento para las 
    entradas GET y POST del root

    POST Retorna un Hello World e incrementa contador
    GET  Retorna un Hello World
    """
    if request.method == 'POST':
       global count
       count += 1
    return 'Hello World %s!!!' % request.method

@app.route("/counter")
def counter():
    """
    Método maneja comportamiento para la entrada
    GET del endpoint counter

    GET  Retorna en numero de reques al endpoit root por POST
    """
    return 'Post requests: %s' % str(count)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
