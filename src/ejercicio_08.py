import pandas as pd
import json
import os

def dataframe_desde_json():

    # 1. Datos en formato JSON
    datos_vehiculos = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2022},
        {"marca": "Honda", "modelo": "Civic", "año": 2021},
        {"marca": "Ford", "modelo": "Focus", "año": 2023},
        {"marca": "Volkswagen", "modelo": "Golf", "año": 2020}
    ]
    
    archivo_json = 'vehiculos.json'
    
    try:
        # 2. Guardar como JSON
        with open(archivo_json, 'w', encoding='utf-8') as file:
            json.dump(datos_vehiculos, file, ensure_ascii=False, indent=2)
        
        print("1. Archivo JSON creado exitosamente")
        
        # 3. Leer con pandas y mostrarlo con tipos de datos
        df = pd.read_json(archivo_json)
        print("\n2. DataFrame desde JSON:")
        print(df)
        print("\n3. Tipos de datos:")
        print(df.dtypes)
        
    except Exception as e:
        print(f"Error: {e}")
    
dataframe_desde_json()