import pandas as pd
import numpy as np
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Ruta al archivo Excel
VolumeA = BASE_DIR / "excels/2014.xls"

# Nombre de la hoja
excel = "QD4"

# Leer la fila 5 del Excel para obtener el título del gráfico
titulo_row_value = pd.read_excel(VolumeA, sheet_name=excel, skiprows=2, usecols="K", nrows=1, header=None).iloc[0, 0]

# Convert the extracted value to string
titulo_row = str(titulo_row_value).strip()

# Resto del código para procesar el archivo Excel
raw_data = pd.read_excel(VolumeA, sheet_name=excel, skiprows=8, usecols="B:AF")

trans = raw_data.transpose()
trans.columns = trans.iloc[0]
trans = trans[1:]

# Agregar el nombre del país como una columna
trans['PAIS'] = trans.index

# Resetting index to ensure proper indexing
trans.reset_index(drop=True, inplace=True)

# Crear un diccionario con el título del gráfico y los datos
data_with_title = {"title": titulo_row, "data": trans.to_dict(orient='records')}

# Guardar los datos procesados en un archivo JSON
with open("C:/Users/pablo/Desktop/Uni/TFG/Web/myproject/static/jsons/2014/" + excel + ".json", "w") as json_file:
    json.dump(data_with_title, json_file)

print(titulo_row)
