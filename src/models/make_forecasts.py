def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    import pandas as pd
    import pickle
    import numpy as np
    from sklearn.model_selection import train_test_split

    df = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df['weekday'] = pd.to_numeric(df['weekday'])

    X = np.array(df['weekday']).reshape(-1, 1)
    #y = np.array(df['precio']).reshape(-1, 1)

    with open('src/models/precios-diarios.pkl', 'rb') as f:
        estimator = pickle.load(f)

    pred_precio = estimator.predict(X)
    df['pred_precio'] = pred_precio
    answer = df[['fecha', 'precio', 'pred_precio']]
    answer.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=False)


if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()
