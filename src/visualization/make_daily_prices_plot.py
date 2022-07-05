def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """

    import pandas as pd
    df_m = pd.read_csv('data_lake/business/precios-diarios.csv', index_col=0)
    ax_plot =df_m['precio'].plot(figsize=(15,5), kind='line', grid=True, x_compat=False)
    fig = ax_plot.get_figure()
    fig.savefig('data_lake/business/reports/figures/daily_prices.png')
    print("Saved ---")

if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()
    doctest.testmod()
