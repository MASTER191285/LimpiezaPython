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
    "valor_prop": [85000000, 55000000, 97000000, 55000000, 120000000, None, 73000000, 97000000],
    "num_baños": [2, 1, 3, 1, 2, 3, 2, None],
    "estado_prop": ["Buena", "Regular", "Buena", "regular", "Excelente", None, "Buena", "Buena"],
    "tipo_construccion": ["Hormigón", "Madera", "Hormigon", "madera", None, "Hormigón armado", "Madera", "Hormigon"],
    "servicios_disp": ["Agua, Luz", "Agua", "Agua, Luz, Gas", "agua,luz", "Agua, Gas", "Agua, Luz", None, "Agua, Luz, Gas"],
    "comodidades": ["Patio, Piscina", "Estacionamiento", None, "Patio", "Piscina", "Patio,Estacionamiento", "Ninguna", "Patio, Piscina"],
    "num_garajes": [1, 0, 2, 1, 2, None, None, 2]
}

df = pd.DataFrame(data)

print(f"Valores Faltantes por Columna: {df.isnull().sum()}") #Muestra la cantidad de valores nulos por columna

columnas_numericas = {
    "metros": 0,
    "num_cuartos": 0,
    "año_construccion": 0,
    "valor_prop": 0,
    "num_baños": 0,
    "num_garajes": 0
}

df.fillna(value=columnas_numericas, inplace=True) #Reemplaza los valores nulos en las columnas numericas con 0

print(f"Valores Faltantes por Columna: {df.isnull().sum()}") #Muestra la cantidad de valores nulos por columna