import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px
from pathlib import Path

# Загрузка данных
DATA_PROCESSED = Path('../data/processed')
deals = pd.read_parquet(DATA_PROCESSED / 'deals_clean.parquet')

# Подготовка: тренд создания сделок по дням
deals_per_day = (
    deals.groupby(deals['Created Time'].dt.date)
    .size()
    .reset_index(name='count')
    .rename(columns={'Created Time': 'date'})
)

# Создаём приложение
app = dash.Dash(__name__)

# Описываем layout — что показать на странице
app.layout = html.Div([
    html.H1('CRM Analytics Dashboard'),
    html.H3('Online IT School'),
    html.Hr(),
    
    html.H2('Тренд создания сделок'),
    dcc.Graph(
        figure=px.line(
            deals_per_day,
            x='date',
            y='count',
            title='Количество сделок, созданных по дням'
        )
    ),
])

# Запуск
if __name__ == '__main__':
    app.run(debug=True)