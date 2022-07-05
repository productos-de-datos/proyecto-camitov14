
import pytest
import pandas as pd


def import_data():
    df_test = pd.read_csv('data_lake/business/precios-diarios.csv')
    df_test2 = pd.read_csv('data_lake/business/precios-mensuales.csv')
    df_test3 = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    return df_test, df_test2, df_test3

def test_data_():
    df_test, df_test2, df_test3 = import_data()
    expect1 = (8886, 3)
    expect2 = (292, 3)
    expect3 = (214968, 3)
    expect = [expect1,expect2,expect3]
    assert1 = df_test.shape
    assert2 = df_test2.shape
    assert3 = df_test3.shape
    assert_t = [assert1,assert2,assert3]
    print(assert_t, expect)
    assert expect == assert_t