from dash.html import Div, Button, Img
from dash.dcc import Tabs, Tab, Input, Upload, Store, Dropdown


def getLayoutFormated():
    return Div(
        [
            Div(
                children=[
                    Div(
                        children=[
                            Div(
                                children=[
                                    Div(
                                        children=[
                                            Div(
                                                children=["Tipo de Média Móvel"],
                                                id="numepochs_text_test",
                                                className="numepochs_text_test",
                                            ),
                                            Dropdown(
                                                options=[
                                                    {
                                                        "label": "Opção 1",
                                                        "value": "valor0",
                                                    },
                                                    {
                                                        "label": "Edite as opções no código.",
                                                        "value": "valor1",
                                                    },
                                                ],
                                                value="valor0",
                                                className="numepochs_box_test_dropdown_dash",
                                                id="numepochs_box_test_dropdown_dash_INPUT",
                                            ),
                                        ],
                                        id="arg6_test",
                                        className="arg6_test",
                                    ),
                                    Div(
                                        children=[
                                            Div(
                                                children=["Janela da Media móvel"],
                                                id="learningrate_test_text",
                                                className="learningrate_test_text",
                                            ),
                                            Input(
                                                type="number",
                                                placeholder="",
                                                className="learningrate_test_input_dash",
                                                id="learningrate_test_input_dash_INPUT",
                                            ),
                                        ],
                                        id="arg1_test",
                                        className="arg1_test",
                                    ),
                                    Div(
                                        children=[
                                            Button(
                                                children=[
                                                    Div(
                                                        children=["Executar"],
                                                        id="exec_button_text",
                                                        className="exec_button_text",
                                                    )
                                                ],
                                                id="exec_alg_test_button_dash_BUTTON",
                                                className="exec_alg_test_button_dash",
                                            )
                                        ],
                                        id="arg3_test",
                                        className="arg3_test",
                                    ),
                                ],
                                id="frame-9_test",
                                className="frame-9_test",
                            )
                        ],
                        id="args_content_test",
                        className="args_content_test",
                    )
                ],
                id="topleft",
                className="topleft",
            )
        ]
    )
