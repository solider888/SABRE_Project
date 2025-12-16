import dash
import numpy as np
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash import Input, Output, dcc, html, callback
import plotly.graph_objects as go

from lib.sabr import SABR_market_vol


input_component = dmc.Stack(
    [
        dmc.Text("f", size="sm"),
        dmc.Slider(
            value=0.018,
            min=0.00001,
            max=0.04,
            step=0.00001,
            labelAlwaysOn=True,
            id="sabr-f",
        ),
        dmc.Text("t_exp", size="sm"),
        dmc.Slider(
            value=5, min=0.00001, max=30, step=0.00001, labelAlwaysOn=True, id="sabr-t"
        ),
        dmc.Text("alpha", size="sm"),
        dmc.Slider( 
            value=0.04,
            min=0.01,
            max=0.1,
            step=0.00001,
            labelAlwaysOn=True,
            id="sabr-alpha",
        ),
        dmc.Text("beta", size="sm"),
        dmc.Slider(
            value=0.5, min=0, max=1, step=0.5, labelAlwaysOn=True, id="sabr-beta"
        ),
        dmc.Text("vov", size="sm"),
        dmc.Slider(
            value=0.101,
            min=0.01,
            max=0.5,
            step=0.00001,
            labelAlwaysOn=True,
            id="sabr-vov",
        ),
        dmc.Text("rho", size="sm"),
        dmc.Slider(
            value=0.64, min=-1, max=1, step=0.00001, labelAlwaysOn=True, id="sabr-rho"
        ),
    ],
    id="smile-input-stack",
)

smile_page_layout = html.Div(
    [
        input_component,
        html.Div(
            dcc.Graph(id="sabr-vol-output"),
            id="smile-graph-div",
            style={"display": "none"},
        ),
    ]
)


@callback(
    Output("sabr-vol-output", "figure"),
    Output("smile-graph-div", "style"),
    Input("sabr-f", "value"),
    Input("sabr-t", "value"),
    Input("sabr-alpha", "value"),
    Input("sabr-beta", "value"),
    Input("sabr-vov", "value"),
    Input("sabr-rho", "value"),
    prevent_initial_call=True,
)
def get_sabr_vol(f, t_exp, alpha, beta, vov, rho):
    """Simple handler that displays the current SABR inputs.

    This function currently echoes the inputs back to the page. Later we
    can replace it with a proper SABR vol calculation and formatting.
    """
    strikes_in_bps = np.arange(-150, 175, 25)
    strikes = f + strikes_in_bps * 0.0001
    vols = SABR_market_vol(
        K=strikes, f=f, t_exp=t_exp, alpha=alpha, beta=beta, nu=vov, rho=rho
    )

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=strikes_in_bps,
            y=vols,
            name="SABR Smile",
            line=dict(color="firebrick", width=4),
        )
    )
    fig.update_layout(
        height=600,
        width=800,
        title=dict(text="SABR Volatility Smile"),
        xaxis=dict(title=dict(text="Strike (bps)")),
        yaxis=dict(title=dict(text="Volatility")),
    )
    return fig, {"display": "block"}