import pandas as pd


data = {
    "propietario": ["Carlos", "Ana", "Pedro", "ana", "LUIS", None, "María", "PEDRO", "Carlos"],
    "metros": [120, 85, 150, 85, None, 200, "180", 150, 120],
    "propiedad_ocupada": ["Sí", "No", "Sí", "sí", "NO", None, "No", "Sí", "Sí"],
    "num_cuartos": [3, 2, 4, 2, 3, 5, None, 4, 3],
    "tipo_prop": ["Casa", "Departamento", "Casa", "departamento", "casa", "Depto", None, "Casa", "Casa"],
    "ubicacion": ["Santiago", "Valparaíso", "Santiago", "valparaiso", "Rancagua", "Rancagua", "Concepción", None, "Santiago"],
    "año_construccion": [2005, 2010, 1995, 2010, 2022, 1980, 2000, "dos mil cinco", 2005],
    "valor_prop": [85000000, 55000000, 97000000, 55000000, 120000000, None, 73000000, 97000000, 85000000],
    "num_baños": [2, 1, 3, 1, 2, 3, 2, None, 2],
    "estado_prop": ["Buena", "Regular", "Buena", "regular", "Excelente", None, "Buena", "Buena", "Buena"],
    "tipo_construccion": ["Hormigón", "Madera", "Hormigon", "madera", None, "Hormigón armado", "Madera", "Hormigon", "Hormigón"],
    "servicios_disp": ["Agua, Luz", "Agua", "Agua, Luz, Gas", "agua,luz", "Agua, Gas", "Agua, Luz", None, "Agua, Luz, Gas", "Agua, Luz"],
    "comodidades": ["Patio, Piscina", "Estacionamiento", None, "Patio", "Piscina", "Patio,Estacionamiento", "Ninguna", "Patio, Piscina", "Patio, Piscina"],
    "num_garajes": [1, 0, 2, 1, 2, None, None, 2, 1]
}

df = pd.DataFrame(data)
tipo_prop = pd.DataFrame(["Casa", "Departamento"], columns=["tipo_prop"]) #Solo deben ser de este tipo
valores_inconsistentes = set(df['tipo_prop']).difference(tipo_prop['tipo_prop'])
print("Valores Inconsistentes en 'tipo_prop':", valores_inconsistentes)
#Identificar cuales son los valores inconsistentes:
inconsistentes = df[df['tipo_prop'].isin(valores_inconsistentes)]
print(f"Filas con valores inconsistentes en 'tipo_prop': {inconsistentes}")