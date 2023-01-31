from flask import Flask
from flask import request

app = Flask(_name_)

@app.route("/operasBas",methods=["GET","POST"])
def operasBas():
    
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")

        if request.form.get("rbd") == "suma":
            return "<h2> La suma es: {}</h2>".format(str(int(num1)+int(num2)))
        elif request.form.get("rbd") =="resta":
            return "<h2> La resta es: {}</h2>".format(str(int(num1)-int(num2)))
        elif request.form.get("rbd") == "mult":
            return "<h2> La multiplicacion es: {}</h2>".format(str(int(num1)*int(num2)))
        elif request.form.get("rbd") == "div":
            return "<h2> La division es: {}</h2>".format(str(int(num1)/int(num2)))

    else:
        return"""
        <form action="/operasBas" method="POST">

            <label>N1: </label>
            <input type="text" name="num1"/><br><br>

            <label>N2: </label>
            <input type="text" name="num2"/><br><br>

            <input type="radio" name="rbd" id="rbd"  value="suma" checked/>
            <label for="rbd">Suma<label/><br>

            <input type="radio" name="rbd" id="rbd" value="resta" action="/"/>
            <label for="rbd">Resta<label/><br>

            <input type="radio" name="rbd" id="rbd" value="mult"/>
            <label for="rbd">Multiplicación<label/><br>

            <input type="radio" name="rbd" id="rbd" value="div"/>
            <label for="rbd">División<label/><br><br>

            <input type="submit" value="calcular"/>

        </form>
        """




if _name=="main_":
    app.run(debug=True,port=3000)