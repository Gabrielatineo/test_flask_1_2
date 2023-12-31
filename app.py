from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return {"payload":"welcome to my project"}

@app.route("/read", methods=["GET"])
def read():
    leer=request.args.get("content")
    if leer == "foo":
        return {"payload":foo}
    else:
        return "Usuario No Existe"


@app.route("/create", methods=["POST"])
def create():
    leer=request.args.get("content")
    if create == "bar":
        return {"payload":bar}
    else:
        return "Usuario No Existe"

@app.route("/init")
def init():
    un_usuario = request.args.get("content")

    if un_usuario == "alfa":
        return {"payload":un_usuario}
    else:  return "no esta"
        
if __name__ == "main":
    app.run(debug=True)

