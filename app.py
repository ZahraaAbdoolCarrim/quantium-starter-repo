from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()
df = pd.read_csv('data/daily_sales_data_improved.csv')
fig = px.line(df, x='date', y='sales')

fig.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='#7FDBFF'
)
dcc.Graph(figure=fig)

app.layout = html.Div(
    style={
        'fontFamily': 'verdana',
        'backgroundColor': 'black',
        'color': 'white',
    },
    children=[
    html.H1(
        children='Daily Sales Data for Pink Morsels',
        style={
            'fontFamily': 'verdana',
            'color': '#7FDBFF',
        }
        ),
    dcc.Graph(
        id='sales-line',
        figure=fig,
        style={
            'backgroundColor': 'black',
            'color': 'white',
            'fontFamily': 'verdana',
        }
    ),
    "Filter by: ",
    dcc.RadioItems(
        ['North', 'South', 'East', 'West', 'All'],
        'North',
        id='region',
    )
])

@callback (
        Output('sales-line', 'figure'),
        Input('region', 'value')
)
def update_graph(region):
    if (region == "All"):
        filtered_df = df
    else:
        filtered_df = df[df['region'] == region.lower()]

    fig = px.line(filtered_df, x='date', y='sales')

    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='#7FDBFF'
    )


    return fig


if __name__ == '__main__':
    app.run(debug=True)
