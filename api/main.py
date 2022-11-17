from flask import Flask, render_template, request, url_for, redirect
import requests
import json



app = Flask(__name__)
app.config['SECRET_KEY']='UZUMYMW'

@app.route("/placa")
def index():
    return render_template("index.html")

@app.route("/placa/search", methods=['GET','POST'])
def consulta_placas():
    if request.method =='POST':
        placa = request.form['buscar_placas']
        dados = requests.get("http://186.208.132.129:8080/acap/API/parceiros/placa/"+str(placa))
        json_data = json.loads(dados.content)
    return render_template("index.html",result=json_data)
    


if __name__=='__main__':
    app.run(debug=True)