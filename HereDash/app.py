import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

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
            'Class': ['Mammalia', 'Mammalia', 'Aves', 'Chondrichthyes', 'Mammalia', 'Aves', 'Reptilia', 'Amphibia',
                     'Insecta', 'Mammalia', 'Mammalia', 'Mammalia', 'Aves', 'Reptilia', 'Mammalia', 'Mammalia',
                     'Mammalia', 'Mammalia', 'Aves', 'Mollusca', 'Mammalia', 'Mammalia', 'Aves', 'Reptilia'],
            'Habits': ['Grassland', 'Forest', 'Mountains', 'Ocean', 'Savanna', 'Arctic', 'Desert', 'Wetland',
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
    html.H1("Animal Planet Dashboard", 
            style={'text-align': 'center', 'color': '#2E8B57', 'margin-bottom': '30px'}),
    
    html.Div([
        html.P(f"Total Animals in Dataset: {len(df)}", 
               style={'text-align': 'center', 'font-size': '18px', 'margin-bottom': '20px'})
    ]),
    
    # First row with bar charts
    html.Div([
        html.Div([
            dcc.Graph(id='class-bar-chart')
        ], className='six columns'),
        
        html.Div([
            dcc.Graph(id='Habits-bar-chart')
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
    
], style={'margin': '20px'})

# Callback for class bar chart
@app.callback(
    Output('class-bar-chart', 'figure'),
    Input('class-bar-chart', 'id')
)
def update_class_chart(_):
    class_counts = df['Class'].value_counts()
    
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
        height=400
    )
    
    return fig

# Callback for Habits bar chart
@app.callback(
    Output('Habits-bar-chart', 'figure'),
    Input('Habits-bar-chart', 'id')
)
def update_Habits_chart(_):
    Habits_counts = df['Habits'].value_counts()
    
    fig = px.bar(
        x=Habits_counts.index,
        y=Habits_counts.values,
        title='Animals by Habits',
        labels={'x': 'Habits', 'y': 'Count'},
        color=Habits_counts.values,
        color_continuous_scale='Plasma'
    )
    
    fig.update_layout(
        title_x=0.5,
        xaxis_tickangle=-45,
        height=400
    )
    
    return fig

# Callback for diet bar chart
@app.callback(
    Output('diet-bar-chart', 'figure'),
    Input('diet-bar-chart', 'id')
)
def update_diet_chart(_):
    diet_counts = df['Diet'].value_counts()
    
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
        height=400
    )
    
    return fig

# Callback for population chart (pie or line)
@app.callback(
    Output('population-chart', 'figure'),
    Input('chart-type-selector', 'value')
)
def update_population_chart(chart_type):
    # Group by order and sum population
    order_population = df.groupby('Order')['Population'].sum().sort_values(ascending=False)
    
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
        height=400
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
