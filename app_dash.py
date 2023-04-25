# Utilizados para criar servidor Flask e auxiliar no Layout básico do Website com objetos da biblioteca Dash.
from flask import Flask, request
import dash
from dash import Dash, dcc, html, dash_table, State
from dash.dependencies import Input, Output
from dash.html import Div, Button
from dash.dcc import Upload, Dropdown,Graph, Store
# from dash import dcc, html, Input, Output, State
# Utilizado para verificar tipo de arquivo baixado e manipular tabelas
import numpy as np
import pandas as pd
# Utilizados para criar objetos / gráficos do Plotty 
from plotly.subplots import make_subplots
from plotly.graph_objs import *
import plotly.express as px
import plotly.graph_objects as go
from dash_svg import Svg, Path, Line

# Pacotes para leitura de arquivo enviado ao servidor.
import base64
import io
import json

# Auxiliar para armazenar arquivos.
import os

# Importando função auxiliar que retorna Layout.
from assets.dashCode import getLayoutFormated
from modelingFunc.functions1 import *

appServer= Flask(__name__)
# appServer.config['SECRET_KEY'] = str(int(np.floor(np.random.random() * np.random.random()* 10000)))
# appServer.config["SESSION_PERMANENT"] = False
# appServer.config["SESSION_TYPE"] = "filesystem"


app = dash.Dash(name =__name__,server = appServer, url_base_pathname='/')


app.layout = getLayoutFormated()

Graph_Layout = Layout(
    # paper_bgcolor= 'rgba(0,0,0,0)',
    plot_bgcolor= 'rgba(245, 245,245, 1)',
    paper_bgcolor ='rgba(245, 245,245, 1)',
    legend_bgcolor = 'rgba(245, 245,245, 1)',
    modebar_bgcolor = 'rgba(245, 245,245, 1)',
    hoverlabel_bgcolor = 'rgba(245, 245,245, 1)',

    font_color = 'rgba(0,0,0,1)',
    legend_font_color = 'rgba(0,0,0,1)',

    margin=go.layout.Margin(
        l=20, #left margin
        r=3, #right margin
        b=3, #bottom margin
        t=3,  #top margin
    )
    )

website_body_style= {
  "background": "#d9d9d9",
  "display": "flex",
  "flex-direction": "row",
  "gap": "0px",
  "align-items": "center",
  "justify-content": "flex-start",
  "align-self": "stretch",
  "flex": "1",
  "position": "relative",
}

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
        # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
        # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
        
    except Exception as e:
        return html.Div([
            'Erro ao processar arquivo.'
        ])
    return df


def verifyData(inputData):
    flagCleanData = True
    for tag in inputData: # Verifica para cada coluna se o dado contém apenas números.
        if(inputData[tag].dtype == np.float64 or inputData[tag].dtype == np.int64):
            pass
        else:
            flagCleanData = False
    # Se o dado for numérico, atualiza a página com dados importados.
    if(flagCleanData == True):
        return True
    else:
        print('Fail to Verify data')
        return False # html.Div('Sua tabela deve ser númerica')#index()
def getGraph(inputData):
    layout = Graph_Layout

    fig = make_subplots(rows=1,
                    cols=1,
                    subplot_titles=('Predição com modelo de Regressão GD'),
                    ) 
    fig.layout = layout
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='white' ,zeroline=True, zerolinewidth=2, zerolinecolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='white' , zeroline=True, zerolinewidth=2, zerolinecolor='grey')

    xName = inputData.columns[0] ; yName = inputData.columns[-1] ;data = inputData.sort_values(xName)
    # fig.add_scatter(x =inputData[xName],y=inputData[yName], mode='lines', color = 'black', name= 'Dados Importados')
    fig.add_trace( go.Scatter(x=data[xName], y=data[yName],
                        type = "scatter", 
                        mode = "markers+lines",
                        name='Dados importados'))
    
    return fig

def create_time_series():
    x = np.arange(0)
    y = x * 1
    example_fig = getGraph(pd.DataFrame({'x': x , 'y' : y}))
    page_layout = Div(
        [
            Div(
                children=[
                    Upload(
                        children=[
                            Div(
                                children=[
                                    Div(
                                        children=[],
                                        id="rectangle-31",
                                        className="rectangle-31",
                                    ),
                                    Div(
                                        children=[],
                                        id="rectangle-32",
                                        className="rectangle-32",
                                    ),
                                ],
                                id="group-43",
                                className="group-43",
                            ),
                            Div(
                                children=["Import Data"],
                                id="import-data",
                                className="import-data",
                            ),
                        ],
                        id="import-data-upload-dash_UPLOAD",
                        className="import-data-upload-dash",
                        multiple=True,
                    ),
                    Div(
                        children=[
                            Div(
                                children=[
                                    Div(
                                        children=[
                                            Div(
                                                children=[
                                                    Div(
                                                        children=["Time History"],
                                                        id="time-history",
                                                        className="time-history",
                                                    )
                                                ],
                                                id="time-history-title",
                                                className="time-history-title",
                                            ),
                                            Graph(
                                                id="time-history-graph-dash_GRAPH",
                                                className="time-history-graph-dash",
                                                figure=example_fig,
                                            ),
                                        ],
                                        id="time-history-frame",
                                        className="time-history-frame",
                                    ),
                                    Div(
                                        children=[
                                            Div(
                                                children=[
                                                    Div(
                                                        children=["Data Decomposition"],
                                                        id="data-decomposition",
                                                        className="data-decomposition",
                                                    )
                                                ],
                                                id="data-decomposition-title",
                                                className="data-decomposition-title",
                                            ),
                                            Graph(
                                                id="data-decomposition-graph-dash_GRAPH",
                                                className="data-decomposition-graph-dash",
                                                figure=example_fig,
                                            ),
                                        ],
                                        id="data-decomposition-frame",
                                        className="data-decomposition-frame",
                                    ),
                                ],
                                id="graphs",
                                className="graphs",
                            ),
                            Div(
                                children=[
                                    Div(
                                        children=[
                                            Div(
                                                children=["Data Report"],
                                                id="data-report",
                                                className="data-report",
                                            )
                                        ],
                                        id="data-report-title",
                                        className="data-report-title",
                                    ),
                                    Div(
                                        children=[
                                            Div(
                                                children=["AAAAAAAAAAAAAAAAAAAAAAAAAA"],
                                                id="aaaaaaaaaaaaaaaaaaaaaaaaaa",
                                                className="aaaaaaaaaaaaaaaaaaaaaaaaaa",
                                            )
                                        ],
                                        id="data-report-info-box",
                                        className="data-report-info-box",
                                    ),
                                ],
                                id="data-report-frame",
                                className="data-report-frame",
                            ),
                        ],
                        id="data-input-frame",
                        className="data-input-frame",
                    ),
                ],
                id="box-input-data-test",
                className="box-input-data-test",
            )
        ]
    )

    return page_layout

# Callback para descrever funcionamento do menu lateral.
@app.callback(
    Output('time-series-button-dash_BUTTON','n_clicks'), # ---- Botões do sideMenu
    Output('data-reg-button-dash_BUTTON','n_clicks'),
    Output('clustering-button-dash_BUTTON','n_clicks'),
    Output('neural-net-button-dash_BUTTON','n_clicks'),
    Output('img-recogn-button-dash_BUTTON','n_clicks'), # ----


    Output('website-body','style'),
    Output('side-tabs-result','children'), # 'Resultado' que corresponde ao frame à direita para cada seleção no menu lateral
    Output('frame-svg-selected-tab_SVG','children'), # Elemento SVG que é responsável pelo efeito de trocar de seleção

    Input('time-series-button-dash_BUTTON','n_clicks'),
    Input('data-reg-button-dash_BUTTON','n_clicks'),
    Input('clustering-button-dash_BUTTON','n_clicks'),
    Input('neural-net-button-dash_BUTTON','n_clicks'),
    Input('img-recogn-button-dash_BUTTON','n_clicks')
)

def side_menu_functional(b1,b2,b3,b4,b5):
    website_body_style_new = website_body_style.copy()
    website_body_style_new['background'] = "#92878B"
    if (b1 != 0):
        svg_comp = Path(
            d="M0 0H117H244V22C244 35.8071 232.807 47 219 47L47.1327 47C33.3256 47 22.1327 58.1929 22.1327 72V82C22.1327 95.8071 33.3256 107 47.1327 107H219C232.807 107 244 118.193 244 132V712H0V0Z",
            fill="#3A2EC8"
        )
        return 0,0,0,0,0,website_body_style_new,create_time_series(),svg_comp
    if (b2 != 0):
        svg_comp = Path(
            d="M0 0H119H244L245.292 156.737C245.406 170.647 234.146 181.975 220.237 181.943L47.1419 181.555C33.4755 181.525 22.3171 192.474 22.0894 206.139L21.9227 216.14C21.6902 230.087 32.915 241.526 46.8631 241.557L219.529 241.944C233.325 241.975 244.488 253.175 244.473 266.971L244 712H0V0Z",
            fill="#3A2EC8"
        )
        return 0,0,0,0,0,website_body_style_new,html.Div(),svg_comp
    if (b3 != 0):
        svg_comp = Path(
            d="M0 0H119H244L244.921 291.921C244.965 305.759 233.759 317 219.921 317H47.9253C34.1995 317 23.0405 328.066 22.9262 341.792L22.8429 351.792C22.7271 365.68 33.9535 377 47.842 377H219.463C233.284 377 244.483 388.216 244.463 402.037L244 712H0V0Z",
            fill="#3A2EC8"
        )
        return 0,0,0,0,0,website_body_style_new,html.Div(),svg_comp
    if (b4 != 0):
        svg_comp = Path(
            d="M0 0H119H244V427C244 440.807 232.807 452 219 452H47.1327C33.3256 452 22.1327 463.193 22.1327 477V487C22.1327 500.807 33.3256 512 47.1327 512H219C232.807 512 244 523.193 244 537V712H0V0Z",
            fill="#3A2EC8"
        )
        return 0,0,0,0,0,website_body_style_new,html.Div(),svg_comp
    if (b5 != 0):
        svg_comp = Path(
            d="M0 0H119H244V562C244 575.807 232.807 587 219 587H47.1327C33.3256 587 22.1327 598.193 22.1327 612V622C22.1327 635.807 33.3256 647 47.1327 647H219C232.807 647 244 658.193 244 672V712H0V0Z",
            fill="#3A2EC8"
        )
        return 0,0,0,0,0,website_body_style_new,html.Div(),svg_comp
    svg_comp = Path(
           d="M0 0H119H244V502.588V570.59V712H0V0Z",
           fill="#3A2EC8"
        )
    return 0,0,0,0,0,website_body_style,html.Div(),svg_comp
    
# CallBack com função de Alterar Output de acordo com os dados enviados ao servidor.
@app.callback(
              Output('store_input_data_filePath','data'),
              Input('import-data-upload-dash_UPLOAD', 'contents' ),
              State('import-data-upload-dash_UPLOAD', 'filename'),
              State('import-data-upload-dash_UPLOAD', 'last_modified')
              )
          
def update_output(contents, filenames, dates):
    if contents is not None:
        dfList = [
            parse_contents(c, n, d) for c, n, d in
            zip(contents, filenames, dates)]
        print(dfList[0])
        df = dfList[0]
        filename = filenames[0]
        print(type(df))
        # Definindo caminho viável para armazenar tabelas.
        user_IP = request.remote_addr.replace('.','_')
        userPath = os.path.join(app.server.instance_path, user_IP)
        if not (os.path.exists(userPath)):
            os.makedirs(userPath)
        filePath = os.path.join(userPath,filename)
        print(filePath)
        
        df.to_csv(filePath,index=False)
        print(filePath,'DONE')
        return filePath
    else:
        return None

# CallBack para alterar exibição de resultados em função do Upload de arquivos ( time series. )
@app.callback(
    Output('time-history-graph-dash_GRAPH','figure'),
    Output('data-decomposition-graph-dash_GRAPH','figure'),
    Input('store_input_data_filePath','data'),
)

def generateGraphs(filePath):
    print('aaaa')
    df = pd.read_csv(filePath,index_col=False)
    input_fig = getGraph(df)
    decomp_graph = getGraph_DataDecomposition(df)
    return input_fig,decomp_graph

def getGraph_DataDecomposition(inputData):
    layout = Graph_Layout
    fig = make_subplots(rows=1,
                    cols=1,
                    subplot_titles=('Decomposição Linear.'),
                    ) 
    fig.layout = layout
    fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='white' ,zeroline=True, zerolinewidth=2, zerolinecolor='grey')
    fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='white' , zeroline=True, zerolinewidth=2, zerolinecolor='grey')

    xName = inputData.columns[0] ; yName = inputData.columns[-1] ;data = inputData.sort_values(xName)
    x = data[xName].to_numpy()
    y = data[yName].to_numpy()
    linear_trend = polynomial_regression(x,y,1) # calculo de tendência linear.

    trend_decomp = y - linear_trend

    # fig.add_scatter(x =inputData[xName],y=inputData[yName], mode='lines', color = 'black', name= 'Dados Importados')
    fig.add_trace( go.Scatter(x=x, y=linear_trend,
                        type = "scatter", 
                        mode = "markers+lines",
                        #name='Tendência Linear.'
                        ))
    fig.add_trace( go.Scatter(x=x, y=trend_decomp,
                        type = "scatter", 
                        mode = "markers+lines",
                        #name='Dados importados sem tendência Linar.'
                        )
                        )
    
    
    # Retirando tendência Linear.
    

    return fig

if __name__ == "__main__":

    app.run(debug=True)

