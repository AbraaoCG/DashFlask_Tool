# Utilizados para criar servidor Flask e auxiliar no Layout básico do Website com objetos da biblioteca Dash.
from flask import Flask, request
import dash
from dash import Dash, dcc, html, dash_table, Input, Output, State
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


# CallBack com função de Alterar Output de acordo com os dados enviados ao servidor.
@app.callback(Output('div_com_nome_arquivo_uploaded','children'),
              Output('store_input_data','data'),
              Input('input_data_UPLOAD','contents'),
              State('input_data_UPLOAD','filename'),
              State('input_data_UPLOAD','last_modified')
              )
def update_output(content, filename, date):
    if content is not None:
        df = parse_contents(content, filename, date).to_dict('records')
        
        # Definindo caminho viável para armazenar tabelas.
        user_IP = request.remote_addr.replace('.','_')
        userPath = os.path.join(app.server.instance_path, user_IP)
        nameDiv = html.Div(f'Tabela Enviada: '+ filename ,className='datauploaded_name') # DEFINIR NOME DO ESTILO ???
 
        return nameDiv,df
    else:
        return html.Div('Nenhum arquivo selecionado', className= 'datauploaded_name'),{}


# CallBack com função de Alterar Output de acordo com função principal, definida em ??Dropdown??
@app.callback(Output('store_ML_Data','data'),
              Input('main_function_DROPDOWN','value'),
              Input('store_input_data','data')
              )

def changeOutput_ML(mlFunction,inputDF):
    df = pd.DataFrame.from_dict(inputDF) # DataFrame com arquivo enviado ao servidor
    mlFunc = mlFunction # Variável com opção selecionada pelo usuário

    # Desenvolver Criação de Tabelas com resultados em função do Layout desejado.
