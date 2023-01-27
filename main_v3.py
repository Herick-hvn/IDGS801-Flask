from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hola Mundo cambios nuevos</h1>"

@app.route("/menu")
def menu():
    return "<h1>Hola desde menu</h1>"

@app.route("/user/<string:user>")
def user(user):
    return "Hola" + " " + user 

@app.route("/user/<int:n>")
def numero(n):
    return "Numero {}".format(n) 

@app.route("/user/<int:id>/<string:name>")
def func(id, name):
    return "ID: {} Numero: {} ".format(id, name) 

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es {} ".format(n1+n2) 

@app.route("/suma2", methods=["GET","POST"])
def sumar():
    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        resultado = int(num1) + int(num2)
        return  "<h1>La suma es: {}</h1>".format(str(resultado))
    else:
        return '''
        <form method="post">
            <input type="text" name="num1">
            <input type="text" name="num2">
            <input type="submit" value="Sumar">
        </form>
        '''

if __name__ == "__main__":
    app.run(debug = True, port=3000)