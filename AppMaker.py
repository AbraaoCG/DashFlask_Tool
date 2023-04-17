import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QUrl, QObject, pyqtSignal
from PyQt5.QtWebEngineWidgets import QWebEngineView
from flask import Flask, render_template
from assets.dashCode import getLayoutFormated
import dash
from dash import dcc, html, Input, Output, State

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from flask import Flask, render_template
from assets.dashCode import getLayoutFormated
import dash
from dash import dcc, html, Input, Output, State

def index():
    layout = getLayoutFormated()
    return render_template('index.html', layout=layout)

# Interface Gráfica
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.setWindowTitle('Aplicação com Flask e PyQt')
        self.setGeometry(100, 100, 800, 600)

        # Botão para iniciar o servidor Flask
        btn_start = QPushButton('Iniciar Servidor', self)
        btn_start.clicked.connect(self.start_server)
        btn_start.setStyleSheet('font-size: 20px; padding: 10px;')
        btn_start.setMaximumWidth(200)
        btn_start.setMinimumHeight(80)

        # Web View para exibir o preview da aplicação
        self.web_view = QWebEngineView(self)

        # Layout horizontal para o botão e a web view
        hbox = QHBoxLayout()
        hbox.addWidget(btn_start, alignment=Qt.AlignTop | Qt.AlignHCenter)
        hbox.addWidget(self.web_view)

        # Layout vertical para a janela principal
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        self.setLayout(vbox)


    def start_server(self):
        # Importa as bibliotecas necessárias
        from flask import Flask, render_template

        # Cria uma instância do Flask
        appServer= Flask(__name__)

        app = dash.Dash(name =__name__,server = appServer, url_base_pathname='/')


        app.layout = getLayoutFormated()

        # Inicia o servidor Flask em uma nova thread
        import threading
        thread = threading.Thread(target=app.run)
        thread.start()

        # Define a URL do servidor Flask como a página a ser renderizada no QWebEngineView
        self.web_view.setUrl(QUrl('http://127.0.0.1:8050/'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


