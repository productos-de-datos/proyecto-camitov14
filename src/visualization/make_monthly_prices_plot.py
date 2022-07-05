
def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.
    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
    """
    import pandas as pd
    df_m = pd.read_csv('data_lake/business/precios-mensuales.csv', index_col=0)
    ax =df_m['precio'].plot(figsize=(15,5), kind='line', grid=True, x_compat=False)
    fig = ax.get_figure()
    fig.savefig('data_lake/business/reports/figures/monthly_prices.png')
    print("Saved ---")

if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()
    doctest.testmod()