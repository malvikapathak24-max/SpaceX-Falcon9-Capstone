"""Interactive SpaceX Falcon 9 dashboard.
Run from a folder containing dataset_part_2.csv or spacex_launch_dash.csv:
    pip install dash pandas plotly
    python dashboard.py
"""
import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

DATA_FILE = "spacex_launch_dash.csv"
if not os.path.exists(DATA_FILE):
    DATA_FILE = "dataset_part_2.csv"
df = pd.read_csv(DATA_FILE)
required = {"FlightNumber", "LaunchSite", "PayloadMass", "Class"}
missing = required.difference(df.columns)
if missing:
    raise ValueError(f"Dataset is missing required columns: {sorted(missing)}")
df["PayloadMass"] = pd.to_numeric(df["PayloadMass"], errors="coerce")
df["Class"] = pd.to_numeric(df["Class"], errors="coerce")
df = df.dropna(subset=["LaunchSite", "PayloadMass", "Class"])
df["Class"] = df["Class"].astype(int)

app = Dash(__name__)
sites = sorted(df["LaunchSite"].dropna().unique())
min_payload = float(df["PayloadMass"].min())
max_payload = float(df["PayloadMass"].max())
app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Landing Outcome Dashboard"),
    html.Label("Select launch site"),
    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label": "All Sites", "value": "ALL"}] +
                [{"label": s, "value": s} for s in sites],
        value="ALL", clearable=False
    ),
    html.Label("Payload mass range (kg)"),
    dcc.RangeSlider(
        id="payload-slider", min=min_payload, max=max_payload,
        step=max((max_payload-min_payload)/100, 1),
        value=[min_payload, max_payload],
        tooltip={"placement": "bottom", "always_visible": False}
    ),
    dcc.Graph(id="success-pie"),
    dcc.Graph(id="flight-scatter")
], style={"maxWidth": "1100px", "margin": "auto", "padding": "20px"})

@app.callback(
    Output("success-pie", "figure"),
    Output("flight-scatter", "figure"),
    Input("site-dropdown", "value"),
    Input("payload-slider", "value")
)
def update_graphs(selected_site, payload_range):
    low, high = payload_range
    filtered = df[df["PayloadMass"].between(low, high)]
    if selected_site != "ALL":
        filtered = filtered[filtered["LaunchSite"] == selected_site]
    counts = filtered["Class"].value_counts().sort_index()
    pie = px.pie(
        names=[("Successful" if int(k) == 1 else "Unsuccessful") for k in counts.index],
        values=counts.values, title="Landing outcome distribution"
    )
    scatter = px.scatter(
        filtered, x="FlightNumber", y="PayloadMass", color="Class",
        hover_data=["LaunchSite"], title="Flight number vs payload mass by landing class",
        labels={"FlightNumber": "Flight number", "PayloadMass": "Payload mass (kg)", "Class": "Landing class"}
    )
    return pie, scatter

if __name__ == "__main__":
    app.run(debug=True)
