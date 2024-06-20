import pandas as pd
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Ruta al archivo Excel
VolumeA = BASE_DIR / "excels/2023.xlsx"

# Nombre de la hoja
excel = "Q16"

# Leer la fila 5 del Excel para obtener el título del gráfico
titulo_row_value = pd.read_excel(VolumeA, sheet_name=excel, skiprows=6, usecols="A", nrows=1, header=None).iloc[0, 0]

# Convertir el valor extraído a cadena de texto
titulo_row = str(titulo_row_value).strip()

# Resto del código para procesar el archivo Excel
raw_data = pd.read_excel(VolumeA, sheet_name=excel, skiprows=11, usecols="A:AC")

# Reemplazar valores NaN con ceros (0)
raw_data = raw_data.fillna(0)

trans = raw_data.transpose()
trans.columns = trans.iloc[0]
trans = trans[1:]

# Agregar el nombre del país como una columna
trans['PAIS'] = trans.index

# Resetear el índice para asegurar un índice adecuado
trans.reset_index(drop=True, inplace=True)

# Crear un diccionario con el título del gráfico y los datos
data_with_title = {"title": titulo_row, "data": trans.to_dict(orient='records')}

# Guardar los datos procesados en un archivo JSON
with open("C:/Users/pablo/Desktop/Uni/TFG/Web/myproject/static/jsons/2023/" + excel + ".json", "w") as json_file:
    json.dump(data_with_title, json_file)

print(titulo_row)
