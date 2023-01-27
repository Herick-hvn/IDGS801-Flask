from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo desde flask"

@app.route("/hola")
def about():
    return "Hola desde hola"

@app.route("/nueva")
def about():
    return "Hola desde nueva"   

if __name__ == "__main__":
    app.run(debug = True, port=3000)