from dash.html import Div, Button, Img
from dash.dcc import Tabs, Tab, Input, Upload, Store, Dropdown
from dash_svg import Svg, Path, Line


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
                                                children=[],
                                                id="rectangle-4",
                                                className="rectangle-4",
                                            ),
                                            Div(
                                                children=[],
                                                id="rectangle-5",
                                                className="rectangle-5",
                                            ),
                                        ],
                                        id="retangles-logo",
                                        className="retangles-logo",
                                    ),
                                    Div(
                                        children=[
                                            Div(
                                                children=["D2P"],
                                                id="d-2-p",
                                                className="d-2-p",
                                            ),
                                            Div(
                                                children=["Data to Modeling"],
                                                id="data-to-modeling",
                                                className="data-to-modeling",
                                            ),
                                        ],
                                        id="frame-2",
                                        className="frame-2",
                                    ),
                                ],
                                id="logo-box",
                                className="logo-box",
                            )
                        ],
                        id="upper-header",
                        className="upper-header",
                    ),
                    Div(
                        children=[
                            Div(
                                children=[
                                    Svg(
                                        children=[
                                            Path(
                                                d="M0 0H119H244V502.588V570.59V712H0V0Z",
                                                fill="#3A2EC8",
                                            )
                                        ],
                                        id="rectangle-16_SVG",
                                        className="rectangle-16",
                                        fill="none",
                                        height="712",
                                        width="244",
                                        xmlns="http://www.w3.org/2000/svg",
                                    ),
                                    Div(
                                        children=[
                                            Svg(
                                                children=[
                                                    Line(
                                                        stroke="#8B2F2F",
                                                        strokeWidth="2",
                                                        transform="matrix(0.757602 -0.652716 0.72495 0.688801 9 12.7849)",
                                                        x2="11.5971",
                                                        y1="-1",
                                                        y2="-1",
                                                    ),
                                                    Path(
                                                        d="M16.5508 4.71436L19.7087 7.36947",
                                                        stroke="#8B2F2F",
                                                        strokeWidth="2",
                                                    ),
                                                    Line(
                                                        stroke="#8B2F2F",
                                                        strokeWidth="2",
                                                        transform="matrix(0.810068 -0.586335 0.662404 0.749147 19.7087 7.57153)",
                                                        x2="7.79661",
                                                        y1="-1",
                                                        y2="-1",
                                                    ),
                                                    Line(
                                                        stroke="#FEBA08",
                                                        strokeWidth="2",
                                                        x1="4.78955",
                                                        x2="4.78955",
                                                        y2="20",
                                                    ),
                                                    Line(
                                                        stroke="#FEBA08",
                                                        strokeWidth="2",
                                                        x2="24",
                                                        y1="16.1428",
                                                        y2="16.1428",
                                                    ),
                                                ],
                                                id="icon-time-series_SVG",
                                                className="icon-time-series",
                                                fill="none",
                                                height="20",
                                                width="27",
                                                xmlns="http://www.w3.org/2000/svg",
                                            ),
                                            Div(
                                                children=["Time Series"],
                                                id="time-series",
                                                className="time-series",
                                            ),
                                        ],
                                        id="time-series-tab-dash",
                                        className="time-series-tab-dash",
                                    ),
                                    Div(
                                        children=[
                                            Svg(
                                                children=[
                                                    Path(
                                                        d="M6.27376 9.60737H11.7506M13.5763 13.2586H4.44813C3.47976 13.2586 2.55105 12.8739 1.8663 12.1892C1.18156 11.5045 0.796875 10.5757 0.796875 9.60737V3.86395C0.796862 3.23613 0.958732 2.61891 1.26685 2.0719C1.57498 1.5249 2.01894 1.06658 2.55587 0.741211L4.44813 2.0719C5.01874 1.72613 8.12967 4.94679 8.79688 4.94679C9.46408 4.94679 13.0057 1.72613 13.5763 2.07191L15.4685 0.741211C16.0053 1.0665 16.4492 1.52467 16.7573 2.07151C17.0654 2.61834 17.2274 3.23537 17.2275 3.86303V9.60737C17.2275 10.5757 16.8428 11.5045 16.1581 12.1892C15.4734 12.8739 14.5446 13.2586 13.5763 13.2586Z",
                                                        stroke="white",
                                                        strokeLinecap="round",
                                                        strokeLinejoin="round",
                                                        strokeWidth="1.36922",
                                                    )
                                                ],
                                                id="icon-data-reg_SVG",
                                                className="icon-data-reg",
                                                fill="none",
                                                height="14",
                                                width="18",
                                                xmlns="http://www.w3.org/2000/svg",
                                            ),
                                            Div(
                                                children=[
                                                    "Data",
                                                    Div([]),
                                                    "Regression",
                                                ],
                                                id="data-regression",
                                                className="data-regression",
                                            ),
                                        ],
                                        id="data-reg-tab-dash",
                                        className="data-reg-tab-dash",
                                    ),
                                    Div(
                                        children=[
                                            Div(
                                                children=[
                                                    Div(
                                                        children=[],
                                                        id="yeloow",
                                                        className="yeloow",
                                                    ),
                                                    Div(
                                                        children=[],
                                                        id="blue",
                                                        className="blue",
                                                    ),
                                                    Div(
                                                        children=[],
                                                        id="green",
                                                        className="green",
                                                    ),
                                                    Div(
                                                        children=[],
                                                        id="red",
                                                        className="red",
                                                    ),
                                                ],
                                                id="icon-clustering",
                                                className="icon-clustering",
                                            ),
                                            Div(
                                                children=["Clustering"],
                                                id="clustering",
                                                className="clustering",
                                            ),
                                        ],
                                        id="clustering-tab-dash",
                                        className="clustering-tab-dash",
                                    ),
                                    Div(
                                        children=[
                                            Svg(
                                                children=[
                                                    Path(
                                                        d="M12.4566 14.9167C12.4566 15.3769 12.7054 15.75 13.0122 15.75C13.319 15.75 13.5677 15.3769 13.5677 14.9167V9.08325H17.4566C17.7635 9.08325 18.0122 8.71017 18.0122 8.24992C18.0122 7.78967 17.7635 7.41658 17.4566 7.41658H13.5677V1.58333C13.5677 1.1231 13.319 0.75 13.0122 0.75C12.7054 0.75 12.4566 1.1231 12.4566 1.58333V7.41658H8.56776C8.26094 7.41658 8.01221 7.78967 8.01221 8.24992C8.01221 8.71017 8.26094 9.08325 8.56776 9.08325H12.4566V14.9167Z",
                                                        fill="#FEBA08",
                                                    ),
                                                    Path(
                                                        d="M12.4566 26.3611C12.4566 26.852 12.7054 27.25 13.0122 27.25C13.319 27.25 13.5677 26.852 13.5677 26.3611V20.1388H17.4566C17.7635 20.1388 18.0122 19.7408 18.0122 19.2499C18.0122 18.759 17.7635 18.361 17.4566 18.361H13.5677V12.1389C13.5677 11.648 13.319 11.25 13.0122 11.25C12.7054 11.25 12.4566 11.648 12.4566 12.1389V18.361H8.56776C8.26094 18.361 8.01221 18.759 8.01221 19.2499C8.01221 19.7408 8.26094 20.1388 8.56776 20.1388H12.4566V26.3611Z",
                                                        fill="#FEBA08",
                                                    ),
                                                    Path(
                                                        d="M4.45664 26.3611C4.45664 26.852 4.70541 27.25 5.01219 27.25C5.31903 27.25 5.56775 26.852 5.56775 26.3611V20.1388H9.45665C9.76348 20.1388 10.0122 19.7408 10.0122 19.2499C10.0122 18.759 9.76348 18.361 9.45665 18.361H5.56775V12.1389C5.56775 11.648 5.31903 11.25 5.01219 11.25C4.70541 11.25 4.45664 11.648 4.45664 12.1389V18.361H0.567764C0.260941 18.361 0.012207 18.759 0.012207 19.2499C0.012207 19.7408 0.260941 20.1388 0.567764 20.1388H4.45664V26.3611Z",
                                                        fill="#FEBA08",
                                                    ),
                                                    Path(
                                                        d="M21.4566 26.3611C21.4566 26.852 21.7054 27.25 22.0122 27.25C22.319 27.25 22.5677 26.852 22.5677 26.3611V20.1388H26.4566C26.7635 20.1388 27.0122 19.7408 27.0122 19.2499C27.0122 18.759 26.7635 18.361 26.4566 18.361H22.5677V12.1389C22.5677 11.648 22.319 11.25 22.0122 11.25C21.7054 11.25 21.4566 11.648 21.4566 12.1389V18.361H17.5678C17.2609 18.361 17.0122 18.759 17.0122 19.2499C17.0122 19.7408 17.2609 20.1388 17.5678 20.1388H21.4566V26.3611Z",
                                                        fill="#FEBA08",
                                                    ),
                                                    Path(
                                                        d="M12.4566 37.4167C12.4566 37.8769 12.7054 38.25 13.0122 38.25C13.319 38.25 13.5677 37.8769 13.5677 37.4167V31.5833H17.4566C17.7635 31.5833 18.0122 31.2102 18.0122 30.7499C18.0122 30.2897 17.7635 29.9166 17.4566 29.9166H13.5677V24.0833C13.5677 23.6231 13.319 23.25 13.0122 23.25C12.7054 23.25 12.4566 23.6231 12.4566 24.0833V29.9166H8.56776C8.26094 29.9166 8.01221 30.2897 8.01221 30.7499C8.01221 31.2102 8.26094 31.5833 8.56776 31.5833H12.4566V37.4167Z",
                                                        fill="#FEBA08",
                                                    ),
                                                ],
                                                id="icon-neural-network_SVG",
                                                className="icon-neural-network",
                                                fill="none",
                                                height="39",
                                                width="28",
                                                xmlns="http://www.w3.org/2000/svg",
                                            ),
                                            Div(
                                                children=["Neural Network"],
                                                id="neural-network",
                                                className="neural-network",
                                            ),
                                        ],
                                        id="neural-net-tab-dash",
                                        className="neural-net-tab-dash",
                                    ),
                                    Div(
                                        children=[
                                            Div(
                                                children=[
                                                    Div(
                                                        children=[],
                                                        id="yeloow2",
                                                        className="yeloow2",
                                                    ),
                                                    Div(
                                                        children=[],
                                                        id="blue2",
                                                        className="blue2",
                                                    ),
                                                    Div(
                                                        children=[],
                                                        id="green2",
                                                        className="green2",
                                                    ),
                                                    Div(
                                                        children=[],
                                                        id="red2",
                                                        className="red2",
                                                    ),
                                                ],
                                                id="icon-img-recognition",
                                                className="icon-img-recognition",
                                            ),
                                            Div(
                                                children=["Image recognition"],
                                                id="image-recognition",
                                                className="image-recognition",
                                            ),
                                        ],
                                        id="img-recogn-tab-dash",
                                        className="img-recogn-tab-dash",
                                    ),
                                ],
                                id="side-menu-tabs-dash",
                                className="side-menu-tabs-dash",
                            ),
                            Div(
                                children=[],
                                id="side-tabs-result",
                                className="side-tabs-result",
                            ),
                        ],
                        id="website-body",
                        className="website-body",
                    ),
                ],
                id="main-aplication",
                className="main-aplication",
            )
        ]
    )
