def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn import linear_model
    from sklearn.metrics import mean_squared_error
    import numpy as np
    import pickle
    df = pd.read_csv('data_lake/business/features/precios_diarios.csv')
    df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d')
    df['weekday'] = pd.to_numeric(df['weekday'])

    X = np.array(df['weekday']).reshape(-1, 1)
    y = np.array(df['precio']).reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=33
    )
    regr = linear_model.LinearRegression()
    model = regr.fit(X_train, y_train)
    pickle.dump(model, open("src/models/precios-diarios.pkl", "wb"))


if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
