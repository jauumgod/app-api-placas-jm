
import requests
import json



def placa_data():
    dados = requests.get("http://186.208.132.129:8080/acap/API/parceiros/placa/")
    receive = "DAO2044"
    res = ("http://186.208.132.129:8080/acap/API/parceiros/placa/" + str(receive))
    json_data = json.loads(dados.content)
    print(json_data['data'])
placa_data()