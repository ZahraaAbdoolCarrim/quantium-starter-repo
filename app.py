from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv('data/daily_sales_data_improved.csv')
fig = px.line(df, x='date', y='sales')
dcc.Graph(figure=fig)

app.layout = html.Div(children=[
    html.H1(children='Daily Sales Data for Pink Morsels'),
    dcc.Graph(
        id='sales-scatter',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run(debug=True)
