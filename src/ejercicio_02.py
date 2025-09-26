import pandas as pd

def series_indices_personalizados():

        #Indices personalizados
    calificaciones = pd.Series([85, 92, 78], 
    index=['Matemáticas', 'Ciencias', 'Historia'])

    print("1. Serie de calificaciones:")
    print(calificaciones)
    
    # 2.Acceder a valor especifico
    calificacion_ciencias = calificaciones['Ciencias']
    print(f"\n 2. Calificación en Ciencias: {calificacion_ciencias}")
    
    # 3.Información básica de la Serie
    print("\n 3. Información básica:")
    print(f"Tamaño: {calificaciones.size}")
    print(f"Índices: {calificaciones.index.tolist()}")
    
    # 4. Estadísticas básicas
    print("\n 4. Estadísticas:")
    print(f"Suma: {calificaciones.sum()}")
    print(f"Promedio: {calificaciones.mean():.2f}")

series_indices_personalizados()