
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def graph_region(region_df, graph_type: str, month: str, dimension1: str, dimension2: str):
    """
    Parameters
    ----------
        region_df: (dataframe object) reshaped data frame object with mortage, delinquency and population data
        graph_type: (string) "box", "violin", "scatter", "line"
        dimension1: (str) one of 'Time' or 'Geography'
        dimension2: (str) one of 'AverageMortgageAmount', 'AverageMortgageAmount' or 'PopulationSize'
        
    Returns:
    --------
        None
    """
    
    #plot_dict = {'box': px.box,'violin': px.violin, 'scatter': px.scatter, 'line':px.line}
    plot_dict = px.scatter
    top_brands = ["Restaurants and Other Eating Places",
                  "Gasoline Stations",
                  "General Merchandise Stores, including Warehouses",
                  "Grocery Stores",
                  "Traveler Accommodation",
                  "Department Stores",
                  "Building Material and Supplies Dealers",
                  "Health and Personal Care Stores",
                  "Other Amusement and Recreation Industries",
                  "Sporting Goods, Hobby, and Musical Instruments",
                  "Automotive Parts, Accessories, and Tire Stores",
                  "Clothing Stores",
                  "Automobile Dealers"]

    try:
        # Initialize function
        fig = px.scatter(data_frame=region_df[region_df.Month == month], y=graph_type, x="Day")




        '''fig = plot_dict[graph_type](region_df, 
                                    x=dimension1, 
                                    y=dimension2, 
                                    color = "Geography",
                                   hover_name = "Time")
        # Format figure 
        title_string = f'Chart: {graph_type} plot of {dimension1} and {dimension2} by Geography'
        fig.update_layout(title = title_string)
        fig.update_xaxes(tickangle=-45)'''
        return fig
    
    except KeyError:
        print("Key not found. Make sure that 'graph_type' is in ['box','violin', 'scatter', 'line']")
    except ValueError:
        print("Dimension is not valid. dimension1 is one of 'Time' or 'Geography'")
        print("dimension2 is one of 'AverageMortgageAmount', 'DelinquencyRate', 'PopulationSize'")
        
# ----------------------------------------------------------------------------------#
# Read data

url = 'Top_Categories_6months_daily_visits.csv'
data_pop_del_mort_df = pd.read_csv(url)

# ----------------------------------------------------------------------------------#
# App section        
        

# Stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Intialize app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


# ----------------------------------------------------------------------------------#
# A dropdown menu and a chart

app.layout = html.Div([
             # This div contains a header H1, a dropdown to select the kind of plot and the plot
            html.H1("Changing daily-visit patterns for top brand categories"),
            dcc.Dropdown(
                        id='graph-type',
                        options=[{'label':"Restaurants and Other Eating Places",'value':"Restaurants and Other Eating Places"},
              {'label':"Grocery Stores",'value':"Grocery Stores"},
              {'label':"Traveler Accommodation",'value':"Traveler Accommodation"},
              {'label':"Department Stores",'value':"Department Stores"},
              {'label':"Building Material and Supplies Dealers",'value':"Building Material and Supplies Dealers"},
              {'label':"Health and Personal Care Stores",'value':"Health and Personal Care Stores"},
              {'label':"Other Amusement and Recreation Industries",'value':"Other Amusement and Recreation Industries"},
              {'label':"Automotive Parts, Accessories, and Tire Stores",'value':"Automotive Parts, Accessories, and Tire Stores"},
              {'label':"Clothing Stores",'value':"Clothing Stores"},
              {'label':"Automobile Dealers",'value':"Automobile Dealers"}],
                        value= 'Clothing Stores'),
dcc.Dropdown(
                        id='month',
                        options=[{'label':"Mar",'value':"Mar"},
              {'label':"Apr",'value':"Apr"},
              {'label':"May",'value':"May"},
              {'label':"Jun",'value':"Jun"},
              {'label':"Jul",'value':"Jul"},
              {'label':"Aug",'value':"Aug"}],
                        value= 'Mar'),
            dcc.Graph(id='graph-render')


])

@app.callback(
    Output('graph-render', 'figure'),
    Input('graph-type', 'value'),
    Input('month', 'value'))
def update_figure0(selected_graph, month):
    filtered_df = data_pop_del_mort_df
    fig0 = graph_region(filtered_df, selected_graph, month, "Gasoline Stations", "Clothing Stores")
    return fig0
# ----------------------------------------------------------------------------------#

    
# ----------------------------------------------------------------------------------#
# Improving aesthetics, dropdown that changes three graphs

# app.layout = html.Div([
#     html.Div(
#         className="six columns",
#         children = [
#             html.H1("Housing graphs"),
#                 dcc.Dropdown(
#                     id='province',
#                     options=[{'label': i, 'value': i} for i in data_pop_del_mort_df['Geography'].unique()],
#                     value= 'Newfoundland'
#                 ),
            
#             html.Div([
#                    dcc.Graph(id='graph-time-mortgage')
#                     ], className="six columns"),
            
#             html.Div([
#                 dcc.Graph(id='graph-time-del')
#                 ], className="six columns"),
            
#             ]),
    
#     html.Div(
#         className="six columns",
#         children = [
#             html.Div([
#             dcc.Graph(id='scatter-mortgage-del')
#             ]),
#         ])
# ])


    
# @app.callback(
#     Output('graph-time-mortgage', 'figure'),
#     Input('province', 'value'))
# def update_figure1(selected_province):
#     df = data_pop_del_mort_df
#     filtered_df = df[df['Geography'] == selected_province]
#     fig1 = graph_region(filtered_df, 'line', "Time", "AverageMortgageAmount")
#     return fig1

# @app.callback(
#     Output('graph-time-del', 'figure'),
#     Input('province', 'value'))
# def update_figure2(selected_province):
#     df = data_pop_del_mort_df
#     filtered_df = df[df['Geography'] == selected_province]  
#     fig2 = graph_region(filtered_df, 'line', "Time", "DelinquencyRate")
#     return fig2

# @app.callback(
#     Output('scatter-mortgage-del', 'figure'),
#     Input('province', 'value'))
# def update_figure3(selected_province):
#     df = data_pop_del_mort_df
#     filtered_df = df[df['Geography'] == selected_province]  
#     fig3 = graph_region(filtered_df, 'scatter', "AverageMortgageAmount", "DelinquencyRate")
#     return fig3

# ----------------------------------------------------------------------------------#
# text_style = {
#     'textAlign' : 'center',
#     'color' : "black"
# }

# card_text_style = {
#     'textAlign' : 'center',
#     'color' : 'black'
# }
    
# app.layout = html.Div([
#     html.Div([
#         html.H2("Housing Market Trends in Vancouver (quarterly, 2012 - 2020)", style=card_text_style),
#         html.Div([
            
#             dcc.Dropdown(
#                 id='xaxis-column',
#                 options=[{'label': 'Geography', 'value': 'Geography'},
#                          {'label': 'Time', 'value': 'Time'},
#                         {'label': 'Population Size', 'value': 'PopulationSize'},
#                          {'label': 'Delinquency Rate', 'value': 'DelinquencyRate'},
#                         {'label': 'Average Mortgage Amount', 'value': 'AverageMortgageAmount'}],
#                 value='Geography'
#             ),
#             dcc.Dropdown(
#                 id='yaxis-column',
#                 options=[{'label': 'Population Size', 'value': 'PopulationSize'},
#                          {'label': 'Delinquency Rate', 'value': 'DelinquencyRate'},
#                         {'label': 'Average Mortgage Amount', 'value': 'AverageMortgageAmount'}],
#                 value='PopulationSize'
#             ),
            
#         ]),
        
#         html.Div([
#             dcc.Checklist(
#                 id='graph-type',
#                 options=[{'label': 'Violin plot', 'value': 'violin'},
#                          {'label': 'Box plot', 'value': 'box'},
#                         {'label': 'Scatter plot', 'value': 'scatter'},
#                         {'label': 'Line plot', 'value': 'line'}],
#                 value=['violin']
#             )
#         ])
#     ]),

#     dcc.Graph(id='indicator-graphic'),

    
# ])

# @app.callback(
#     Output('indicator-graphic', 'figure'),
#     Input('graph-type', 'value'),
#     Input('xaxis-column', 'value'),
#     Input('yaxis-column', 'value'))
# def update_figure3(selected_graph, xaxis, yaxis):
#     filtered_df = data_pop_del_mort_df
#     fig3 = graph_region(filtered_df, selected_graph[0], xaxis, yaxis)
#     return fig3

# ----------------------------------------------------------------------------------#

if __name__ == '__main__':  
    
    app.run_server(debug=True) 