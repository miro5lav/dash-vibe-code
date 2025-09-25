import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server
# Define CSS styles for light and dark themes
LIGHT_THEME = {
    'backgroundColor': '#FFFFFF',
    'color': '#000000',
    'cardBackground': '#F8F9FA',
    'borderColor': '#E9ECEF'
}

DARK_THEME = {
    'backgroundColor': '#1E1E1E',
    'color': '#FFFFFF', 
    'cardBackground': '#2D2D2D',
    'borderColor': '#404040'
}

# Load the data
def load_data():
    try:
        # Try to load the actual CSV file
        df = pd.read_csv('animals_info.csv')
        return df
    except FileNotFoundError:
        # Create sample data if file doesn't exist (for demonstration)
        print("animals_info.csv not found. Creating sample data...")
        
        # Sample data structure based on typical animal datasets
        sample_data = {
            'name': ['Lion', 'Tiger', 'Eagle', 'Shark', 'Elephant', 'Penguin', 'Snake', 'Frog', 
                    'Butterfly', 'Whale', 'Bear', 'Deer', 'Owl', 'Turtle', 'Kangaroo', 'Dolphin',
                    'Wolf', 'Rabbit', 'Hawk', 'Octopus', 'Gorilla', 'Zebra', 'Flamingo', 'Crocodile'],
            'class': ['Mammalia', 'Mammalia', 'Aves', 'Chondrichthyes', 'Mammalia', 'Aves', 'Reptilia', 'Amphibia',
                     'Insecta', 'Mammalia', 'Mammalia', 'Mammalia', 'Aves', 'Reptilia', 'Mammalia', 'Mammalia',
                     'Mammalia', 'Mammalia', 'Aves', 'Mollusca', 'Mammalia', 'Mammalia', 'Aves', 'Reptilia'],
            'habitat': ['Grassland', 'Forest', 'Mountains', 'Ocean', 'Savanna', 'Arctic', 'Desert', 'Wetland',
                       'Garden', 'Ocean', 'Forest', 'Forest', 'Forest', 'Wetland', 'Grassland', 'Ocean',
                       'Forest', 'Grassland', 'Mountains', 'Ocean', 'Forest', 'Savanna', 'Wetland', 'Wetland'],
            'diet': ['Carnivore', 'Carnivore', 'Carnivore', 'Carnivore', 'Herbivore', 'Carnivore', 'Carnivore', 'Carnivore',
                    'Herbivore', 'Carnivore', 'Omnivore', 'Herbivore', 'Carnivore', 'Omnivore', 'Herbivore', 'Carnivore',
                    'Carnivore', 'Herbivore', 'Carnivore', 'Carnivore', 'Omnivore', 'Herbivore', 'Omnivore', 'Carnivore'],
            'order': ['Carnivora', 'Carnivora', 'Accipitriformes', 'Carcharhiniformes', 'Proboscidea', 'Sphenisciformes', 
                     'Squamata', 'Anura', 'Lepidoptera', 'Cetacea', 'Carnivora', 'Artiodactyla', 'Strigiformes', 
                     'Testudines', 'Diprotodontia', 'Cetacea', 'Carnivora', 'Lagomorpha', 'Accipitriformes', 
                     'Octopoda', 'Primates', 'Perissodactyla', 'Phoenicopteriformes', 'Crocodilia'],
            'population': [20000, 3900, 500000, 100000, 415000, 12000000, 3000000, 2000000,
                          200000000, 50000, 600000, 30000000, 4000000, 300000, 50000000, 600000,
                          300000, 40000000, 2000000, 300000000, 1000000, 750000, 3200000, 250000]
        }
        
        df = pd.DataFrame(sample_data)
        return df

# Load the data
df = load_data()

# Define the app layout
app.layout = html.Div([
    # Header with toggle button
    html.Div([
        html.H1("Animal Planet Dashboard", 
                id='main-title',
                style={'text-align': 'center', 'color': '#2E8B57', 'margin-bottom': '30px', 'flex': '1'}),
        
        # Theme toggle button in top right
        html.Div([
            html.Button(
                "🌙", 
                id='theme-toggle',
                style={
                    'background': 'none',
                    'border': '2px solid #2E8B57',
                    'border-radius': '50%',
                    'width': '50px',
                    'height': '50px',
                    'font-size': '20px',
                    'cursor': 'pointer',
                    'color': '#2E8B57'
                }
            )
        ], style={'position': 'absolute', 'top': '20px', 'right': '20px'})
    ], style={'position': 'relative', 'display': 'flex', 'align-items': 'center'}),
    
    html.Div([
        html.P(f"Total Animals in Dataset: {len(df)}", 
               id='total-count',
               style={'text-align': 'center', 'font-size': '18px', 'margin-bottom': '20px'})
    ]),
    
    # First row with bar charts
    html.Div([
        html.Div([
            dcc.Graph(id='class-bar-chart')
        ], className='six columns'),
        
        html.Div([
            dcc.Graph(id='habitat-bar-chart')
        ], className='six columns'),
    ], className='row', style={'margin-bottom': '20px'}),
    
    # Second row with diet chart and population chart
    html.Div([
        html.Div([
            dcc.Graph(id='diet-bar-chart')
        ], className='six columns'),
        
        html.Div([
            html.H3("Population by Order", style={'text-align': 'center'}),
            dcc.RadioItems(
                id='chart-type-selector',
                options=[
                    {'label': 'Pie Chart', 'value': 'pie'},
                    {'label': 'Line Chart', 'value': 'line'}
                ],
                value='pie',
                style={'text-align': 'center', 'margin-bottom': '10px'}
            ),
            dcc.Graph(id='population-chart')
        ], className='six columns'),
    ], className='row'),
    
], id='main-container', style={'margin': '20px', 'transition': 'all 0.3s ease'})

# Callback for theme toggle
@app.callback(
    [Output('main-container', 'style'),
     Output('main-title', 'style'),
     Output('total-count', 'style'),
     Output('theme-toggle', 'children'),
     Output('theme-toggle', 'style')],
    [Input('theme-toggle', 'n_clicks')],
    prevent_initial_call=False
)
def toggle_theme(n_clicks):
    if n_clicks is None:
        n_clicks = 0
    
    is_dark = n_clicks % 2 == 1
    
    if is_dark:
        theme = DARK_THEME
        toggle_icon = "☀️"
        container_style = {
            'margin': '20px', 
            'transition': 'all 0.3s ease',
            'backgroundColor': theme['backgroundColor'],
            'color': theme['color'],
            'min-height': '100vh',
            'padding': '10px'
        }
        title_style = {
            'text-align': 'center', 
            'color': '#4CAF50', 
            'margin-bottom': '30px', 
            'flex': '1'
        }
        count_style = {
            'text-align': 'center', 
            'font-size': '18px', 
            'margin-bottom': '20px',
            'color': theme['color']
        }
        button_style = {
            'background': 'none',
            'border': '2px solid #4CAF50',
            'border-radius': '50%',
            'width': '50px',
            'height': '50px',
            'font-size': '20px',
            'cursor': 'pointer',
            'color': '#4CAF50'
        }
    else:
        theme = LIGHT_THEME
        toggle_icon = "🌙"
        container_style = {
            'margin': '20px', 
            'transition': 'all 0.3s ease',
            'backgroundColor': theme['backgroundColor'],
            'color': theme['color']
        }
        title_style = {
            'text-align': 'center', 
            'color': '#2E8B57', 
            'margin-bottom': '30px', 
            'flex': '1'
        }
        count_style = {
            'text-align': 'center', 
            'font-size': '18px', 
            'margin-bottom': '20px',
            'color': theme['color']
        }
        button_style = {
            'background': 'none',
            'border': '2px solid #2E8B57',
            'border-radius': '50%',
            'width': '50px',
            'height': '50px',
            'font-size': '20px',
            'cursor': 'pointer',
            'color': '#2E8B57'
        }
    
    return container_style, title_style, count_style, toggle_icon, button_style

# Callback for class bar chart
@app.callback(
    Output('class-bar-chart', 'figure'),
    [Input('class-bar-chart', 'id'),
     Input('theme-toggle', 'n_clicks')]
)
def update_class_chart(_, n_clicks):
    if n_clicks is None:
        n_clicks = 0
    
    is_dark = n_clicks % 2 == 1
    theme = DARK_THEME if is_dark else LIGHT_THEME
    
    class_counts = df['class'].value_counts()
    
    fig = px.bar(
        x=class_counts.index,
        y=class_counts.values,
        title='Animals by Class',
        labels={'x': 'Class', 'y': 'Count'},
        color=class_counts.values,
        color_continuous_scale='Viridis'
    )
    
    fig.update_layout(
        title_x=0.5,
        xaxis_tickangle=-45,
        height=400,
        paper_bgcolor=theme['backgroundColor'],
        plot_bgcolor=theme['cardBackground'],
        font={'color': theme['color']},
        title_font={'color': theme['color']}
    )
    
    return fig

# Callback for habitat bar chart
@app.callback(
    Output('habitat-bar-chart', 'figure'),
    [Input('habitat-bar-chart', 'id'),
     Input('theme-toggle', 'n_clicks')]
)
def update_habitat_chart(_, n_clicks):
    if n_clicks is None:
        n_clicks = 0
    
    is_dark = n_clicks % 2 == 1
    theme = DARK_THEME if is_dark else LIGHT_THEME
    
    habitat_counts = df['habitat'].value_counts()
    
    fig = px.bar(
        x=habitat_counts.index,
        y=habitat_counts.values,
        title='Animals by Habitat',
        labels={'x': 'Habitat', 'y': 'Count'},
        color=habitat_counts.values,
        color_continuous_scale='Plasma'
    )
    
    fig.update_layout(
        title_x=0.5,
        xaxis_tickangle=-45,
        height=400,
        paper_bgcolor=theme['backgroundColor'],
        plot_bgcolor=theme['cardBackground'],
        font={'color': theme['color']},
        title_font={'color': theme['color']}
    )
    
    return fig

# Callback for diet bar chart
@app.callback(
    Output('diet-bar-chart', 'figure'),
    [Input('diet-bar-chart', 'id'),
     Input('theme-toggle', 'n_clicks')]
)
def update_diet_chart(_, n_clicks):
    if n_clicks is None:
        n_clicks = 0
    
    is_dark = n_clicks % 2 == 1
    theme = DARK_THEME if is_dark else LIGHT_THEME
    
    diet_counts = df['diet'].value_counts()
    
    fig = px.bar(
        x=diet_counts.index,
        y=diet_counts.values,
        title='Animals by Diet',
        labels={'x': 'Diet', 'y': 'Count'},
        color=diet_counts.values,
        color_continuous_scale='Cividis'
    )
    
    fig.update_layout(
        title_x=0.5,
        height=400,
        paper_bgcolor=theme['backgroundColor'],
        plot_bgcolor=theme['cardBackground'],
        font={'color': theme['color']},
        title_font={'color': theme['color']}
    )
    
    return fig

# Callback for population chart (pie or line)
@app.callback(
    Output('population-chart', 'figure'),
    [Input('chart-type-selector', 'value'),
     Input('theme-toggle', 'n_clicks')]
)
def update_population_chart(chart_type, n_clicks):
    if n_clicks is None:
        n_clicks = 0
    
    is_dark = n_clicks % 2 == 1
    theme = DARK_THEME if is_dark else LIGHT_THEME
    
    # Group by order and sum population
    order_population = df.groupby('order')['population'].sum().sort_values(ascending=False)
    
    if chart_type == 'pie':
        fig = px.pie(
            values=order_population.values,
            names=order_population.index,
            title='Population Distribution by Order'
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        
    else:  # line chart
        fig = px.line(
            x=range(len(order_population)),
            y=order_population.values,
            title='Population by Order (Line Chart)',
            markers=True
        )
        fig.update_xaxes(
            tickmode='array',
            tickvals=list(range(len(order_population))),
            ticktext=order_population.index,
            tickangle=-45
        )
        fig.update_traces(mode='lines+markers')
        fig.update_layout(
            xaxis_title='Order',
            yaxis_title='Population'
        )
    
    fig.update_layout(
        title_x=0.5,
        height=400,
        paper_bgcolor=theme['backgroundColor'],
        plot_bgcolor=theme['cardBackground'],
        font={'color': theme['color']},
        title_font={'color': theme['color']}
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
