import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
# from pages.landing_option_dash import landing_page
# from pages.pricer_option_dash import pricer_page
# from pages.graph_option_dash import graph_page

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True
)

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "backgroundColor": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "marginLeft": "18rem",
    "marginRight": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("SABR Webapp", className="display-4"),
        html.Hr(),
        html.P("A Webapp provides SABR intelligence", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Pricer", href="/pricer", active="exact"),
                dbc.NavLink("Graphs", href="/graphs", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return "This is home page"
    elif pathname == "/pricer":
        return "This is pricer page"
    elif pathname == "/graphs":
        return "This is graphs page"
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


if __name__ == "__main__":
    app.run(debug=True, port=8050)