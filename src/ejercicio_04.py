import pandas as pd

def dataframe_desde_diccionario():
        
    # 1. Crear diccionario con datos
    datos_productos = {
        'Producto': ['Laptop', 'Smartphone', 'Tablet', 'Monitor'],
        'Precio': [1200, 800, 400, 300],
        'Categoria': ['Electrónicos', 'Electrónicos', 'Electrónicos', 'Periféricos']
    }
    
    # 2. Convertir a DataFrame y mostrarlo
    df = pd.DataFrame(datos_productos)
    print("1. DataFrame completo:")
    print(df)
    
    # 3. Acceder a columna específica
    print("\n2. Columna 'Precio':")
    print(df['Precio'])
    
    # 4. Información básica
    print("\n3. Información del DataFrame:")
    df.info()

dataframe_desde_diccionario()