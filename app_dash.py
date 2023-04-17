# Utilizados para criar servidor Flask e auxiliar no Layout básico do Website com objetos da biblioteca Dash.
from flask import Flask, request
import dash
from dash import dcc, html, Input, Output, State
# Utilizado para verificar tipo de arquivo baixado e manipular tabelas
import numpy as np
import pandas as pd
# Utilizados para criar objetos / gráficos do Plotty 
from plotly.subplots import make_subplots
from plotly.graph_objs import *
import plotly.express as px
import plotly.graph_objects as go

# Utilizados para decodificar Arquivo enviado via browser
import base64
import io
# Utilizado para chamar programas no terminal.
import subprocess 
# Utilizado para identificar Windows ou Linux
import platform
import os
# Importando função auxiliar que retorna Layout.
from assets.dashCode import getLayoutFormated

appServer= Flask(__name__)
# appServer.config['SECRET_KEY'] = str(int(np.floor(np.random.random() * np.random.random()* 10000)))
# appServer.config["SESSION_PERMANENT"] = False
# appServer.config["SESSION_TYPE"] = "filesystem"


app = dash.Dash(name =__name__,server = appServer, url_base_pathname='/')


app.layout = getLayoutFormated()

