import pandas as pd
import numpy as np

def dataframe_desde_numpy():
   
    # 1. Crear array NumPy 2D
    ventas_trimestrales = np.array([
        [15000, 18000, 22000],  # Empresa A
        [12000, 15000, 19000],  # Empresa B
        [20000, 23000, 25000],  # Empresa C
        [18000, 21000, 24000]   # Empresa D
    ])
    
    print("1. Array NumPy original:")
    print(ventas_trimestrales)
    print(f"Dimensiones: {ventas_trimestrales.shape}")
    
    # 2. Crear DataFrame
    df = pd.DataFrame(ventas_trimestrales, 
                     columns=['Q1', 'Q2', 'Q3'],
                     index=['Empresa A', 'Empresa B', 'Empresa C', 'Empresa D'])
    
    print("\n2. DataFrame desde NumPy:")
    print(df)
    
    # 3. Verificar tipos de datos
    print("\n3. Tipos de datos:")
    print(df.dtypes)

dataframe_desde_numpy()

