import os
import django
import pandas as pd
from api.models import Sensores  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')
django.setup()

planilhas = {
    'Contador.xlsx':        ('Contador de Pessoas', 'Un'),
    'luminosidade.xlsx':    ('Luminosidade', 'Lux'),
    'temperatura.xlsx':     ('Temperatura', '°C'),
    'umidade.xlsx':         ('Umidade', '%'),
}

BASE_PATH = os.path.dirname(__file__)
inseridos = 0

for nome_arquivo, (tipo_sensor, unidade) in planilhas.items():
    caminho = os.path.join(BASE_PATH, nome_arquivo)
    print(f"\nRead {nome_arquivo}...")

    try:
        df = pd.read_excel(caminho)
    except Exception as e:
        print(f"ERROR to open {nome_arquivo}: {e}")
        continue

    print(f"Columns: {df.columns.tolist()}")

    for index, row in df.iterrows():
        try:
            obj = Sensores.objects.create(
                sensor=tipo_sensor,
                mac_address=str(row['mac_address']),
                unidade_med=unidade,
                valor=str(row['valor']),
                latitude=float(row['latitude']),
                longitude=float(row['longitude'])
            )
            inseridos += 1
        except Exception as e:
            print(f"ERROR at {index + 2} inside {nome_arquivo}: {e}")