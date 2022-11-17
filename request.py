
import requests
import json



def placa_data():
    dados = requests.get("http://186.208.132.129:8080/acap/API/parceiros/placa/")
    receive = str("DAO2044")
    json_string = str(dados)
    res = "http://186.208.132.129:8080/acap/API/parceiros/placa/" + receive
    json_data = json.loads(dados.content)
    print(json_data)
placa_data()