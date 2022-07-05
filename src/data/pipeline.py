
"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""

import luigi 
from luigi import Task, LocalTarget
import os
import pandas as pd
from create_data_lake import create_data_lake
from ingest_data import ingest_data
from transform_data import transform_data
from clean_data import clean_data
from compute_monthly_prices import compute_monthly_prices
from compute_daily_prices import compute_daily_prices

class Ingest_Transform_Clean_Data(Task):
        def output(self):
            return LocalTarget("data_lake/cleansed/precios-horarios.csv")

        def run(self):
            #os.system("rm -rf data_lake")
            try:
                #create_data_lake()
                #print("-----------Create Date Lake---------------")
                ingest_data()
                print("-----------Data Ingest Finished---------------")
                transform_data()
                print("-----------Data Transform Finished------------")
                clean_data()
                print("-----------Data clean Finished----------------")
            except Exception as e:
                print(e)
                print("Data Lake already exist")


class ComputeDay(Task):
        def requires (self):
            return Ingest_Transform_Clean_Data()

        def output(self):
            return LocalTarget('data_lake/business/precios-diarios.csv')

        def run(self):
            try:
                compute_daily_prices()
                print("-----------Compute Daily Prices Finished-------")
            except Exception as e:
                print(e)


class ComputeMonth(Task):
        def requires(self):
            return Ingest_Transform_Clean_Data()

        def output(self):
            return LocalTarget('data_lake/business/precios-mensuales.csv')

        def run(self):
            try:
                compute_monthly_prices()
                print("-----------Compute Monthly Prices Finished------")
            except Exception as e:
                print(e)

class PipeComputePrices(Task):

        def requires(self):
            return [
                ComputeDay(),
                ComputeMonth(),
            ]

if __name__ == "__main__":
        import doctest
        luigi.run(["PipeComputePrices", "--local-scheduler"])
        doctest.testmod()
