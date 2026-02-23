import dash 
from dash import dcc,html, Input, Output
import plotly.express as px
import plotly.data as pldata


#Load gapminder data
df = pldata.gapminder(return_type='pandas')

#Unique countries no duplicates
countries = df['country'].unique()


# Initialize Dash app
app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H1("GDP Per Capita by Country Over Time"), #Title
    
    dcc.Dropdown(
        id="country-dropdown", # id for the dropdown/callback
        options=[{"label": country, "value": country} for country in countries],
        value= "United States" # default value
    ),
    dcc.Graph(id="gdp-graph") #empty graph that will be updated by the callback
])

# Callback for when dropdown updates
@app.callback(
    Output("gdp-graph", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country_name):
    
    #Filtering the data only by the selected Country name 
    filtered_df = df[df['country'] == country_name]
    #Create linbe plot 
    fig = px.line(
        filtered_df, 
        x="year", 
        y="gdpPercap", 
        title=f"GDP Per Capita for {country_name}"
    )
    return fig
 
# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 