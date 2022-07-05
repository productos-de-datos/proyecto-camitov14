"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    import urllib.request
    for i in range(1995, 2022):
        try:
            url = 'https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/' + str(i) + '.xlsx'
            file_ = 'data_lake/landing/' + str(i) + '.xlsx'
            print(url, file_)
            urllib.request.urlretrieve(url, file_)
        except:
            url = 'https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/' + str(i) + '.xls'
            file_ = 'data_lake/landing/' + str(i) + '.xls'
            print(url, file_)
            urllib.request.urlretrieve(url, file_)
            print("An exception occurred")


if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
