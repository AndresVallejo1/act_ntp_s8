import pandas as pd

def analisis_ventas_diarias():
    #Serie de ventas
    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165])

    #Valor inicie 3
    print("Venta en el tercer dia:", ventas[3])

    #Promedio de ventas
    print("Promedio de ventas:", ventas.mean())

    #Valores ordenados
    print("Ventas ordenadas:")
    print(ventas.sort_values())

analisis_ventas_diarias()

