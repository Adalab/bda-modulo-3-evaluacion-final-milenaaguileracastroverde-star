# función de exploración
def exploracion(dataframe):
    """primera exploración del dataframe""" # esto es un docstring -> documentación de la función
    print(f"el tamaño de mi dataframe es: {dataframe.shape}")
    print("primeras filas")
    display(dataframe.head(2))
    display(dataframe.describe().T)