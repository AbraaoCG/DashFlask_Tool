from flask import Flask, render_template,request,session
import numpy as np
from werkzeug.utils import secure_filename
from plotly.subplots import make_subplots
from plotly.graph_objs import *
from dash import dcc, html
import plotly.express as px
from bs4 import BeautifulSoup
from bs4.element import Tag
from dash.html import Div , Button
from dash_svg import Svg,Path,Line

def parse_html(tag):
    if ( not tag.name):
        return html.Div()
    children = []
    tag_name = tag.name.lower()
    tag_class = tag.get('class', [])
    #if (tag_class == 'select_but_upload'): print(tag_class)
    flag = False
    id_value = tag_class[0] if tag_class else None
    class_value = tag_class[0] if tag_class else None

    print(class_value)
    if(tag.children):
        for child in tag.children:
            
            if ( isinstance(child, str )  and child.strip() != ''):
                children.append(child.strip())
            elif isinstance(child, Tag):
                children.append(parse_html(child))

    if ((tag_name == 'path') or (tag_name == 'line')):
        return solve_svg_subComps(tag,tag_name)
    
    if(len(tag_class) > 0):
        if tag_name == 'img':        
            tag_src = tag.get('src', [])
            component =html.Img(className=class_value, src=f'./assets/imgs/{tag_src}')
            return component
        
        elif 'button-dash' in class_value:
            component = html.Button(className = class_value,id = f'{id_value}_BUTTON', children = children,n_clicks=0)
            return component
        elif 'tabs-dash' in class_value:
            component = dcc.Tabs(className = class_value ,id = f'{id_value}_TABS' ,value='YOUR_DEFAULT_TAB_VALUE',children = children)
            return component
        elif 'tab-dash' in class_value:
            component = dcc.Tab(className = class_value,label=tag_class[0], value = f'{id_value}_TAB' , children = children)
            return component
        elif 'upload-dash' in class_value:
            component = dcc.Upload(className = class_value, id = f'{id_value}_UPLOAD' ,multiple=True, children = children)
            return component
        elif 'input-dash' in class_value:
            component = dcc.Input(className = class_value, id = f'{id_value}_INPUT' , type = "number", placeholder = "")
            return component
        elif 'dropdown-dash' in class_value:
            component = dcc.Dropdown(options = [{'label': 'Opção 1', 'value': 'valor0'},{'label': 'Edite as opções no código.', 'value': 'valor1'}], value = "valor0", className = class_value,id = f'{id_value}_INPUT' )
            return component
        elif 'graph-dash' in class_value:
            component = dcc.Graph(figure ={},id = f'{id_value}_GRAPH', className= class_value)
            return component
        elif tag_name == 'svg':  # Adicionando a condição para elementos HTML SVG
            # Cria o componente Dash SVG passando o HTML SVG como string
            svg_properties = {
            'width': tag.get('width'),
            'height': tag.get('height'),
            'viewBox': tag.get('viewBox'),
            'fill': tag.get('fill'),
            'xmlns': tag.get('xmlns')
            }
            component = Svg(className = class_value, id = f'{id_value}_SVG', **svg_properties, children = children)
            return component
        
    if class_value:
        return html.Div(children=children, id=id_value, className=class_value)
    else:
        return html.Div(children=children)

def solve_svg_subComps(tag,tag_name):
    if tag_name == 'path':  
        svg_properties = {
            'd': tag.get('d'),
            'fill': tag.get('fill'),
            'stroke': tag.get('stroke'),
            'strokeWidth': tag.get('stroke-width'),
            'strokeLinecap': tag.get('stroke-linecap'),
            'strokeLinejoin': tag.get('stroke-linejoin'),
            'strokeMiterlimit': tag.get('stroke-miterlimit'),
            'strokeDasharray': tag.get('stroke-dasharray'),
            'strokeDashoffset': tag.get('stroke-dashoffset'),
            'fillOpacity': tag.get('fill-opacity'),
            'strokeOpacity': tag.get('stroke-opacity'),
            'opacity': tag.get('opacity'),
            'transform': tag.get('transform'),
        }
        component = Path(**svg_properties)
        return component
    elif tag_name == 'line':  
        svg_properties = {
            'x1': tag.get('x1'),
            'y1': tag.get('y1'),
            'x2': tag.get('x2'),
            'y2': tag.get('y2'),
            'transform': tag.get('transform'),
            'stroke': tag.get('stroke'),
            'strokeWidth': tag.get('stroke-width')
        }
        component = Line(**svg_properties)
        return component

def parse_html_file(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')  
    initialTag = soup.find('body')
    return parse_html(initialTag)


def writeLayout(InputFilename, OutPutFilename):
    # Ler Arquivo HTML
    with open(InputFilename, "r", encoding='utf-8') as f:
        html_str= f.read()
    
    # Transformar HTML em Dash
    dash_code = parse_html_file(html_str)

    # Preparação para arquivo de saida
    importStr = """from dash.html import Div , Button, Img \nfrom dash.dcc import Tabs,Tab,Input,Upload,Store,Dropdown,Graph\nfrom dash_svg import Svg,Path,Line\n\n"""
    # Escrever python de saída com função para retornar estrutura.
    with open(OutPutFilename, "w", encoding='utf-8') as f:
        f.write(importStr)
        f.write('def getLayoutFormated():\n    return ')
        f.write(str(dash_code))

def getLayoutRaw(InputFilename):
    # Ler Arquivo HTML
    with open(InputFilename, "r", encoding='utf-8') as f:
        html_str= f.read()

    # Retornar código Dash não formatado.
    return parse_html_file(html_str)


# ------------------------------------------------------------------------



# writeLayout(InputFilename = 'index.html', OutPutFilename = 'dashCode.py')

# getLayoutRaw( InputFilename = 'index.html' )

# -------------------------------------------------------------------------
