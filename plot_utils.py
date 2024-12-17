import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd

def create_impedance_plot(df):
    """
    Create an interactive Plotly plot for battery impedance parameters
    
    Parameters:
    df (pandas.DataFrame): DataFrame containing battery aging data
    
    Returns:
    plotly.graph_objs.Figure: Interactive impedance plot
    """
    # Create a figure with multiple traces
    fig = go.Figure()

    # Battery Impedance Plot
    fig.add_trace(go.Scatter(
        x=df['cycle_number'], 
        y=df['Battery_impedance'], 
        mode='lines+markers',
        name='Electrolyte Resistance',
        line=dict(color='blue'),
        hovertemplate='Cycle: %{x}<br>Impedance: %{y:.4f} Ω<extra></extra>'
    ))

    # Charge Transfer Resistance Plot
    fig.add_trace(go.Scatter(
        x=df['cycle_number'], 
        y=df['Rct'], 
        mode='lines+markers',
        name='Charge Transfer Resistance',
        line=dict(color='red'),
        yaxis='y2',
        hovertemplate='Cycle: %{x}<br>Rct: %{y:.4f} Ω<extra></extra>'
    ))

    # Update layout for dual y-axis
    fig.update_layout(
        title='Battery Impedance Parameters Over Charge/Discharge Cycles',
        height=600,
        width=1000,
        xaxis_title='Cycle Number',
        yaxis_title='Electrolyte Resistance (Ω)',
        yaxis2=dict(
            title='Charge Transfer Resistance (Ω)',
            overlaying='y',
            side='right'
        ),
        hovermode='closest',
        legend=dict(x=0, y=1.1, orientation='h')
    )

    return fig

def save_impedance_plot(fig, filename='battery_impedance_plot.html'):
    """
    Save the impedance plot as an interactive HTML file
    
    Parameters:
    fig (plotly.graph_objs.Figure): Plotly figure to save
    filename (str): Output filename
    """
    pio.write_html(fig, file=filename, auto_open=True)