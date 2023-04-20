# Utilizados para criar servidor Flask e auxiliar no Layout básico do Website com objetos da biblioteca Dash.
from flask import Flask, request
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State
from dash.html import Div, Button
from dash.dcc import Upload, Dropdown, Input
# from dash import dcc, html, Input, Output, State
# Utilizado para verificar tipo de arquivo baixado e manipular tabelas
import numpy as np
import pandas as pd
# Utilizados para criar objetos / gráficos do Plotty 
from plotly.subplots import make_subplots
from plotly.graph_objs import *
import plotly.express as px
import plotly.graph_objects as go

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
        print(e)
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
        return False # html.Div('Sua tabela deve ser númerica')#index()


# # # CallBack com função de Alterar Output de acordo com os dados enviados ao servidor.
# # @app.callback(Output( 'datauploaded_name_box','children'),
# #               Output('store_input_data','data'),
# #               Input('senddata_upload_dash_UPLOAD', 'contents' ),
# #               State('senddata_upload_dash_UPLOAD', 'filename'),
# #               State('senddata_upload_dash_UPLOAD', 'last_modified')
# #             )

# # def x():
# #     pass
#             Output('store_input_data','data'),
# def update_output(contents, filenames, dates):
    
#     if contents is not None:
#         dfList = [
#             parse_contents(c, n, d) for c, n, d in
#             zip(contents, filenames, dates)]
    
#         df = dfList[0]
#         filename = filenames[0]
        
#         # Definindo caminho viável para armazenar tabelas.
#         user_IP = request.remote_addr.replace('.','_')
#         userPath = os.path.join(app.server.instance_path, user_IP)
#         nameDiv = html.Div(f'Tabela Enviada: '+ filename ,className='datauploaded_name') # DEFINIR NOME DO ESTILO ???
 
#         return nameDiv,df
#     else:
#         return html.Div('Nenhum arquivo selecionado', className= 'datauploaded_name'),{}



# # CallBack com função de Alterar o SubMenu de opções
# @app.callback(Output('Sub_Menu_Options','children'),
#               Input('select_main_function_DROPDOWN','value'),
#               # Input('store_input_data','data')
#               )

# def changeOutput_ML(mlFunction,inputDF):
#     df = pd.DataFrame.from_dict(inputDF) # DataFrame com arquivo enviado ao servidor
    
#     if (mlFunction == 0):
#         children = html.Div()# Preencher com código de menu oriundo 
#         return children
        
#     elif(mlFunction == 1):
#         children = subMenu_mediaMov()# Preencher com código de menu oriundo 
#         return children

# # Função Para retornar Layout de um menu com argumentos de média móvel.
# def subMenu_mediaMov():
#     return Div(
#         [
#             Div(
#                 children=[
#                     Div(
#                         children=[
#                             Div(
#                                 children=[
#                                     Div(
#                                         children=[
#                                             Div(
#                                                 children=["Tipo de Média Móvel"],
#                                                 id="numepochs_text_test",
#                                                 className="numepochs_text_test",
#                                             ),
#                                             Dropdown(
#                                                 options=[
#                                                     {
#                                                         "label": "Tendências",
#                                                         "value": 0,
#                                                     },
#                                                     {
#                                                         "label": "Médias Móveis",
#                                                         "value": 1,
#                                                     },
#                                                 ],
#                                                 value=0, 
#                                                 className="numepochs_box_test_dropdown_dash",
#                                                 id="numepochs_box_test_dropdown_dash_INPUT",
#                                             ),
#                                         ],
#                                         id="arg6_test",
#                                         className="arg6_test",
#                                     ),
#                                     Div(
#                                         children=[
#                                             Div(
#                                                 children=["Janela da Media móvel"],
#                                                 id="learningrate_test_text",
#                                                 className="learningrate_test_text",
#                                             ),
#                                             Input(
#                                                 type="number",
#                                                 placeholder="",
#                                                 className="learningrate_test_input_dash",
#                                                 id="learningrate_test_input_dash_INPUT",
#                                             ),
#                                         ],
#                                         id="arg1_test",
#                                         className="arg1_test",
#                                     ),
#                                     Div(
#                                         children=[
#                                             Button(
#                                                 children=[
#                                                     Div(
#                                                         children=["Executar"],
#                                                         id="exec_button_text",
#                                                         className="exec_button_text",
#                                                     )
#                                                 ],
#                                                 id="exec_alg_test_button_dash_BUTTON",
#                                                 className="exec_alg_test_button_dash",
#                                             )
#                                         ],
#                                         id="arg3_test",
#                                         className="arg3_test",
#                                     ),
#                                 ],
#                                 id="frame-9_test",
#                                 className="frame-9_test",
#                             )
#                         ],
#                         id="args_content_test",
#                         className="args_content_test",
#                     )
#                 ],
#                 id="topleft",
#                 className="topleft",
#             )
#         ]
#     )


