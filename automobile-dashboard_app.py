"""Module 05 Final Lab 02: automobile sales reports."""

from pathlib import Path
import argparse

import dash
from dash import Input, Output, dcc, html
import pandas as pd
import plotly.express as px

SOURCE = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
parser = argparse.ArgumentParser()
parser.add_argument("--data", help="Optional local course CSV; otherwise use local default or IBM URL")
parser.add_argument("--port", type=int, default=8050)
args = parser.parse_args()
DATA = Path(__file__).with_name("historical_automobile_sales.csv")
data = pd.read_csv(args.data or (DATA if DATA.is_file() else SOURCE))
years = sorted(int(year) for year in data["Year"].dropna().unique())
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

app = dash.Dash(__name__)
app.title = "Automobile Sales Statistics Dashboard"
app.layout = html.Div(
    [
        html.H1("Automobile Sales Statistics Dashboard", style={"textAlign": "center"}),
        html.Div(
            [
                html.Label("Select report"),
                dcc.Dropdown(
                    id="report-type",
                    options=[
                        {"label": "Recession Period Statistics", "value": "recession"},
                        {"label": "Yearly Statistics", "value": "yearly"},
                    ],
                    value="recession",
                    clearable=False,
                ),
                html.Label("Select year"),
                dcc.Dropdown(id="year", options=[{"label": str(year), "value": year} for year in years], value=years[-1], clearable=False),
            ],
            style={"maxWidth": 700, "margin": "auto"},
        ),
        html.Div(id="report-output", className="chart-grid", style={"display": "grid", "gridTemplateColumns": "repeat(auto-fit, minmax(450px, 1fr))"}),
    ]
)


@app.callback(Output("year", "disabled"), Input("report-type", "value"))
def disable_year(report_type):
    return report_type == "recession"


@app.callback(Output("report-output", "children"), Input("report-type", "value"), Input("year", "value"))
def update_report(report_type, year):
    if report_type == "recession":
        subset = data[data["Recession"] == 1]
        annual = subset.groupby("Year", as_index=False)["Automobile_Sales"].mean()
        by_type = subset.groupby("Vehicle_Type", as_index=False)["Automobile_Sales"].mean()
        advertising = subset.groupby("Vehicle_Type", as_index=False)["Advertising_Expenditure"].sum()
        unemployment = subset.groupby(["unemployment_rate", "Vehicle_Type"], as_index=False)["Automobile_Sales"].mean()
        figures = [
            px.line(annual, x="Year", y="Automobile_Sales", title="Average automobile sales during recessions", markers=True),
            px.bar(by_type, x="Vehicle_Type", y="Automobile_Sales", title="Average sales by vehicle type during recessions"),
            px.pie(advertising, values="Advertising_Expenditure", names="Vehicle_Type", title="Advertising expenditure by vehicle type during recessions"),
            px.bar(unemployment, x="unemployment_rate", y="Automobile_Sales", color="Vehicle_Type", title="Unemployment rate and average sales during recessions"),
        ]
    else:
        subset = data[data["Year"] == year]
        annual = data.groupby("Year", as_index=False)["Automobile_Sales"].mean()
        monthly = subset.groupby("Month", as_index=False)["Automobile_Sales"].sum()
        monthly["Month"] = pd.Categorical(monthly["Month"], categories=month_order, ordered=True)
        monthly = monthly.sort_values("Month")
        by_type = subset.groupby("Vehicle_Type", as_index=False)["Automobile_Sales"].mean()
        advertising = subset.groupby("Vehicle_Type", as_index=False)["Advertising_Expenditure"].sum()
        figures = [
            px.line(annual, x="Year", y="Automobile_Sales", title="Average automobile sales by year", markers=True),
            px.line(monthly, x="Month", y="Automobile_Sales", title=f"Monthly automobile sales in {year}", markers=True),
            px.bar(by_type, x="Vehicle_Type", y="Automobile_Sales", title=f"Average sales by vehicle type in {year}"),
            px.pie(advertising, values="Advertising_Expenditure", names="Vehicle_Type", title=f"Advertising expenditure by vehicle type in {year}"),
        ]
    return [dcc.Graph(figure=figure) for figure in figures]


if __name__ == "__main__":
    app.run(debug=False, port=args.port)
