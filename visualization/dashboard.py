import dash
from dash import dcc, html, Input, Output
import dash_table
import plotly.express as px
import pandas as pd
import sqlite3
from analysis.trend_analysis import analyze_trend, generate_comment

def create_dashboard():
    app = dash.Dash(__name__)

    # Fetch data from SQLite
    conn = sqlite3.connect('db/economy_data.db')
    df = pd.read_sql('SELECT * FROM economic_indicators', conn)
    df['DateTime'] = pd.to_datetime(df['DateTime'], errors='coerce')  # Convert to datetime
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')  # Ensure 'Value' is numeric
    indicator = df.Category[0]
    country = df.Country[0]
    df.drop(columns=["Country", "Category", "Frequency", "HistoricalDataSymbol", "LastUpdate"], inplace=True)

    def create_scatter_plot(data):
        fig = px.scatter(
            data,
            x='DateTime',
            y='Value',
            title=f'{country} Economic Indicator Over Time : {indicator}',
            labels={'DateTime': 'Date', 'Value': 'Indicator Value'}
        )
        fig.update_layout(
            xaxis_title='Date',
            yaxis_title='Indicator Value',
            xaxis=dict(
                tickformat='%Y-%m-%d',
                nticks=20
            )
        )
        return fig

    def create_data_table(data):
        return dash_table.DataTable(
            id='data-table',  # Correct ID here
            columns=[{"name": i, "id": i} for i in data.columns],
            data=data.to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'left'},
            page_size=10
        )

    initial_style = {'textAlign': 'center', 'marginBottom': '20px'}
    app.layout = html.Div(children=[
        html.H1(children=f'{country} Economic Dashboard'),
        html.Div(
            id='trend-comment',
            style=initial_style
        ),
        html.Div(children=[
            dcc.Graph(id='economic-indicator-scatter', figure=create_scatter_plot(df),
                      style={'width': '66.66%', 'display': 'inline-block'}),
            html.Div(children=[
                html.H2('Data Table'),
                create_data_table(df),

            ], style={'width': '33.33%', 'display': 'inline-block'})
        ], style={'display': 'flex'})
    ])

    @app.callback(
        [Output('data-table', 'data'),
         Output('trend-comment', 'children'),
         Output('trend-comment', 'style')],
        [Input('economic-indicator-scatter', 'relayoutData')]
    )
    def update_table_and_comment(relayout_data):
        if relayout_data:
            # Extract x-axis range values
            xaxis_range_start = relayout_data.get('xaxis.range[0]')
            xaxis_range_end = relayout_data.get('xaxis.range[1]')

            if xaxis_range_start and xaxis_range_end:
                # Convert string to datetime
                xaxis_range_start = pd.to_datetime(xaxis_range_start, errors='coerce')
                xaxis_range_end = pd.to_datetime(xaxis_range_end, errors='coerce')

                # Filter data based on x-axis range
                filtered_df = df[(df['DateTime'] >= xaxis_range_start) & (df['DateTime'] <= xaxis_range_end)]
            else:
                filtered_df = df
        else:
            filtered_df = df

        # Drop rows with NaN values in 'Value' or 'DateTime'
        filtered_df = filtered_df.dropna(subset=['Value', 'DateTime'])

        if filtered_df.empty:
            return filtered_df.to_dict('records'), "Not enough data to analyze.", {'color': 'black'}

        # Perform trend analysis and generate comment
        trend_description = analyze_trend(filtered_df)
        comment = generate_comment(trend_description)

        # Determine color based on trend
        if 'negative' == trend_description:
            color = 'green'
        elif 'positive' == trend_description:
            color = 'red'
        else:
            color = 'black'
        style = {**initial_style, 'color': color}

        return filtered_df.to_dict('records'), comment, style

    app.run_server(debug=True)
