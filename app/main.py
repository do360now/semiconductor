from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import random
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Initialize the FastAPI app
app = FastAPI()

# Mount static files (optional if you have static assets like images, CSS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Simulated ASML TWINSCAN NXT:870 Lithography System data generator
def generate_lithography_data():
    return {
        "time": pd.Timestamp.now(),
        "wafer_throughput": random.randint(325, 335),  # wafers/hour, slightly fluctuating
        "reticle_temperature": round(random.uniform(22.5, 24.5), 2),  # Celsius
        "laser_power": round(random.uniform(40, 60), 2),  # Watts (KrF laser)
        "exposure_dose": round(random.uniform(150, 180), 2),  # mJ/cm²
        "overlay_accuracy": round(random.uniform(0.5, 7.5), 3)  # ≤ 7.5 nm
    }

# Create the Dash app with proper pathname prefixes
dash_app = Dash(
    __name__,
    requests_pathname_prefix="/",  # Ensure the trailing slash here
    routes_pathname_prefix="/"
)

# Initialize an empty DataFrame to store simulated data
df = pd.DataFrame(columns=["time", "wafer_throughput", "reticle_temperature", "laser_power", "exposure_dose", "overlay_accuracy"])

# Dash app layout with separate graphs for each parameter
dash_app.layout = html.Div([
    html.H1("TWINSCAN NXT:870 Lithography System Dashboard"),
    
    dcc.Graph(id='wafer-throughput-graph', animate=True),
    dcc.Graph(id='reticle-temperature-graph', animate=True),
    dcc.Graph(id='laser-power-graph', animate=True),
    dcc.Graph(id='exposure-dose-graph', animate=True),
    dcc.Graph(id='overlay-accuracy-graph', animate=True),
    
    # Interval component to update the graphs every second
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,  # Update every 1 second
        n_intervals=0
    ),
    
    # Display the last updated stats
    html.Div(id="live-update-text"),
])

import datetime

@dash_app.callback(
    [
        Output('wafer-throughput-graph', 'figure'),
        Output('reticle-temperature-graph', 'figure'),
        Output('laser-power-graph', 'figure'),
        Output('exposure-dose-graph', 'figure'),
        Output('overlay-accuracy-graph', 'figure'),
        Output('live-update-text', 'children')
    ],
    [Input('interval-component', 'n_intervals')]
)
def update_graphs_live(n):
    global df
    
    # Simulate new data
    new_data = generate_lithography_data()
    
    # Append the new data to the DataFrame
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    
    # Limit the size of the DataFrame for visualization purposes
    if len(df) > 50:
        df = df.iloc[1:]

    # Define the sliding window (e.g., the last 60 seconds)
    now = pd.Timestamp.now()
    window_start_time = now - pd.Timedelta(seconds=60)

    # Create a separate trace and layout for each parameter
    throughput_trace = go.Scatter(x=df['time'], y=df['wafer_throughput'], mode='lines+markers', name='Wafer Throughput (Wafers/hour)')
    throughput_layout = go.Layout(
        title='Wafer Throughput', 
        xaxis=dict(title='Time', range=[window_start_time, now]), 
        yaxis=dict(title='Throughput (Wafers/hour)')
    )

    temperature_trace = go.Scatter(x=df['time'], y=df['reticle_temperature'], mode='lines+markers', name='Reticle Temperature (°C)')
    temperature_layout = go.Layout(
        title='Reticle Temperature', 
        xaxis=dict(title='Time', range=[window_start_time, now]), 
        yaxis=dict(title='Temperature (°C)')
    )

    laser_power_trace = go.Scatter(x=df['time'], y=df['laser_power'], mode='lines+markers', name='Laser Power (W)')
    laser_power_layout = go.Layout(
        title='Laser Power', 
        xaxis=dict(title='Time', range=[window_start_time, now]), 
        yaxis=dict(title='Power (W)')
    )

    exposure_dose_trace = go.Scatter(x=df['time'], y=df['exposure_dose'], mode='lines+markers', name='Exposure Dose (mJ/cm²)')
    exposure_dose_layout = go.Layout(
        title='Exposure Dose', 
        xaxis=dict(title='Time', range=[window_start_time, now]), 
        yaxis=dict(title='Dose (mJ/cm²)')
    )

    overlay_accuracy_trace = go.Scatter(x=df['time'], y=df['overlay_accuracy'], mode='lines+markers', name='Overlay Accuracy (nm)')
    overlay_accuracy_layout = go.Layout(
        title='Overlay Accuracy', 
        xaxis=dict(title='Time', range=[window_start_time, now]), 
        yaxis=dict(title='Accuracy (nm)')
    )

    # Create the figure objects for each graph
    throughput_figure = {'data': [throughput_trace], 'layout': throughput_layout}
    temperature_figure = {'data': [temperature_trace], 'layout': temperature_layout}
    laser_power_figure = {'data': [laser_power_trace], 'layout': laser_power_layout}
    exposure_dose_figure = {'data': [exposure_dose_trace], 'layout': exposure_dose_layout}
    overlay_accuracy_figure = {'data': [overlay_accuracy_trace], 'layout': overlay_accuracy_layout}
    
    # Text display for the last updated data point
    last_data_text = (
        f"Latest Data - Time: {new_data['time']}, "
        f"Wafer Throughput: {new_data['wafer_throughput']} wafers/hour, "
        f"Reticle Temperature: {new_data['reticle_temperature']} °C, "
        f"Laser Power: {new_data['laser_power']} W, "
        f"Exposure Dose: {new_data['exposure_dose']} mJ/cm², "
        f"Overlay Accuracy: {new_data['overlay_accuracy']} nm"
    )
    
    return throughput_figure, temperature_figure, laser_power_figure, exposure_dose_figure, overlay_accuracy_figure, last_data_text


# Mount the Dash app on the `/dashboard` route
app.mount("/", WSGIMiddleware(dash_app.server))

# Main entry point
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
