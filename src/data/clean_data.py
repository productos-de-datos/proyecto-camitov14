def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """

    import pandas as pd
    df_1 = pd.DataFrame(columns=['Fecha', 'hora', 'precio'])
    for i in range(1997, 2022):
        file_ = 'data_lake/raw/' + str(i) + '.csv'
        df_2 = pd.read_csv(file_)
        df_3 = pd.melt(df_2, id_vars=['Fecha'], value_vars=df_2.columns[2:], var_name='hora', value_name='precio')
        df_1 = pd.concat([df_1, df_3], axis=0)
        print("clean and concat", file_)
    df_1.columns = ['fecha', 'hora', 'precio']
    df_1.to_csv('data_lake/cleansed/precios-horarios.csv', sep=',', encoding='utf-8', index=False)

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
