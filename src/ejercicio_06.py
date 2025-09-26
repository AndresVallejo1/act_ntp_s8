import pandas as pd

def dataframe_desde_lista_listas():

    # 1. Datos en lista de listas
    datos_libros = [
        ['Cien años de soledad', 'Gabriel García Márquez', 1967],
        ['1984', 'George Orwell', 1949],
        ['El Quijote', 'Miguel de Cervantes', 1605],
    ]
    
    # 2. Nombres de columnas
    columnas = ['Titulo', 'Autor', 'Año']
    
    # 3. Crear DataFrame y mostrarlo con sus dimensiones
    df = pd.DataFrame(datos_libros, columns=columnas)
    print("1. DataFrame de libros:")
    print(df)
    print(f"\n2. Dimensiones: {df.shape}")
    print(f"   Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    
dataframe_desde_lista_listas()
