def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.datasets import make_regression
    import numpy as np
    import pickle

    #Cargar datos
    df = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df['weekday'] = pd.to_numeric(df['weekday'])

    #Datos de entrenamiento y de test
    X = np.array(df['weekday']).reshape(-1, 1)
    y = np.array(df['precio']).reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=500
    )

    #Modelo de regresión RandomForest
    X_train, y_train = make_regression(n_features=1)
    regr = RandomForestRegressor()
    modelo=regr.fit(X_train, y_train)
    pickle.dump(modelo, open("src/models/precios-diarios.pkl", "wb"))


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
