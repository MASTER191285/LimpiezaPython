import pandas as pd
import numpy as np

data = {
    "propietario": ["Carlos", "Ana", "Pedro", "ana", "LUIS", None, "María", "PEDRO"],
    "metros": [120, 85, 150, 85, None, 200, "180", 150],
    "propiedad_ocupada": ["Sí", "No", "Sí", "sí", "NO", None, "No", "Sí"],
    "num_cuartos": [3, 2, 4, 2, 3, 5, None, 4],
    "tipo_prop": ["Casa", "Departamento", "Casa", "departamento", "casa", "Depto", None, "Casa"],
    "ubicacion": ["Santiago", "Valparaíso", "Santiago", "valparaiso", "Rancagua", "Rancagua", "Concepción", None],
    "año_construccion": [2005, 2010, 1995, 2010, 2022, 1980, 2000, "dos mil cinco"],
    "valor_prop": ["$85.000.000", "$55.000.000", "$97.000.000", "$55.000.000", "$120.000.000", None, "$73.000.000", "$97.000.000"],
    "num_baños": [2, 1, 3, 1, 2, 3, 2, None],
    "estado_prop": ["Buena", "Regular", "Buena", "regular", "Excelente", None, "Buena", "Buena"],
    "tipo_construccion": ["Hormigón", "Madera", "Hormigon", "madera", None, "Hormigón armado", "Madera", "Hormigon"],
    "servicios_disp": ["Agua, Luz", "Agua", "Agua, Luz, Gas", "agua,luz", "Agua, Gas", "Agua, Luz", None, "Agua, Luz, Gas"],
    "comodidades": ["Patio, Piscina", "Estacionamiento", None, "Patio", "Piscina", "Patio,Estacionamiento", "Ninguna", "Patio, Piscina"],
    "num_garajes": [1, 0, 2, 1, 2, None, None, 2],
    "fecha_publicacion": ["26.08.2023", "20.11.2022", "8/11/22", "5-Mar-24", "24.09.25", "7/11/2023", "20/06/23", "7/11/2023"],
}

df = pd.DataFrame(data)
print(df.dtypes) #Tipos de Datos de las columnas
print("*" * 50)
df["valor_prop"] = df["valor_prop"].str.replace("$", "", regex=False)
df["valor_prop"] = df["valor_prop"].str.replace(".", "", regex=False)
df["valor_prop"] = df["valor_prop"].str.replace(",", "", regex=False)
df["valor_prop"] = df["valor_prop"].astype(float)
print(df.dtypes) #Tipos de Datos Actualizados de las columnas

#Manejo de Fechas
#Estandarizar el formato de fecha
df['fecha_publicacion'] = pd.to_datetime(df['fecha_publicacion'], dayfirst=True)
print(df['fecha_publicacion'])