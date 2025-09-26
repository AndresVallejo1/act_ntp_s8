import pandas as pd
import csv
import os

def lectura_archivo_csv():
   
    # 1. Crear y escribir archivo CSV
    archivo_csv = 'cursos.csv'
    
    try:
        with open(archivo_csv, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Encabezados
            writer.writerow(['curso', 'instructor', 'duracion'])
            # Datos
            writer.writerow(['Python Básico', 'Ana López', 40])
            writer.writerow(['Pandas Avanzado', 'Carlos Ruiz', 30])
            writer.writerow(['Machine Learning', 'María García', 60])
        
        print("1. Archivo CSV creado exitosamente")
        
        # 2. Leer archivo CSV con pandas y mostrar dataframe con manejo de errores
        try:
            df = pd.read_csv(archivo_csv)
            print("\n2. DataFrame desde CSV:")
            print(df)
            
        except FileNotFoundError:
            print(f"\nError: El archivo '{archivo_csv}' no existe.")
        except pd.errors.EmptyDataError:
            print(f"\nError: El archivo '{archivo_csv}' está vacío.")
        except Exception as e:
            print(f"\nError inesperado al leer el archivo: {e}")

    except Exception as e:
        print(f"Error al crear el archivo: {e}")

lectura_archivo_csv()