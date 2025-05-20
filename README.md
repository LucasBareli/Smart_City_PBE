PARA RODAR A APLICAÇÃO :

Comandos via CMD:

cd back

py -m venv env

env\scripts\activate

pip install -r requirements.txt

py manage.py runserver


TESTAR A APLICAÇÃO:

http://127.0.0.1:8000/admin/

para pegar o token e ter funções administrativas:
http://127.0.0.1:8000/api/token/
usuario = lin
senha = 123

GET:
http://127.0.0.1:8000/api/ambientes
http://127.0.0.1:8000/api/sensores
http://127.0.0.1:8000//api/historicos


Outros métodos (POST, PUT, DELETE):
http://127.0.0.1:8000//api/historicos/{id}
http://127.0.0.1:8000//api/sensores/{id}
http://127.0.0.1:8000//api/ambientes/{id}

PARA LER OS ARQUIVOS.XLSX
http://127.0.0.1:8000/api/leitura_arquivos


Ultimas 24hrs
http://127.0.0.1:8000/api/historicos/ultimas24h

Ex:http://127.0.0.1:8000/api/historicos/search?data_inicial=2025-05-19T00:00:00&data_final=2025-05-20T23:59:59


Para fazer filtragens:
http://127.0.0.1:8000/api/historicos/search
http://127.0.0.1:8000/api/ambientes/search
http://127.0.0.1:8000/api/sensores/search

Ex:http://127.0.0.1:8000/api/ambientes/search?search=CESAR AUGUSTO DA COSTA 
