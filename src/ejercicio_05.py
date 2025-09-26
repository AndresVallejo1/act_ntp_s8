import pandas as pd

def dataframe_desde_lista_diccionarios():

    # 1. Lista de diccionarios
    empleados = [
        {'empleado': 'Ana García', 'salario': 50000, 'departamento': 'Ventas'},
        {'empleado': 'Carlos López', 'salario': 60000, 'departamento': 'TI'},
        {'empleado': 'María Rodríguez', 'salario': 55000, 'departamento': 'RH'},
    ]
    
    # 2. Convertir a DataFrame y mostrarlo
    df = pd.DataFrame(empleados)
    print("1. DataFrame completo:")
    print(df)
    
    # 3. Acceder a filas específicas por indice numerico
    print("\n2. Primera fila:")
    print(df.iloc[0])  
    
    print("\n3. Primeras 2 filas:")
    print(df.head(2))

dataframe_desde_lista_diccionarios()

