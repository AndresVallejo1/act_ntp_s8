import pandas as pd

def operaciones_series():
    
    # 1. Crear dos Series
    precios = pd.Series([100, 150, 200])
    descuentos = pd.Series([10, 20, 15])
    
    print("1. Series originales:")
    print(f"Precios: {precios.tolist()}")
    print(f"Descuentos: {descuentos.tolist()}")
    
    # 2. Resta entre Series (elemento por elemento)
    precios_finales = precios - descuentos
    print(f"\n2. Precios después de descuentos: {precios_finales.tolist()}")
    
    # 3. Multiplicación por escalar (IVA 16%)
    precios_con_iva = precios * 1.16
    print(f"\n3. Precios con IVA (16%): {precios_con_iva.tolist()}")
    
    # 4. Demostración elemento por elemento
    print("\n4. Operación elemento por elemento:")
    for i in range(len(precios)):
        resultado = precios[i] - descuentos[i]
        print(f"  {precios[i]} - {descuentos[i]} = {resultado}")

operaciones_series()