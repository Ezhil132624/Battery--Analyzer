import pandas as pd
from data_loader import load_battery_data
from plot_utils import create_impedance_plot, save_impedance_plot
from analysis import generate_detailed_report

def main():
    # Load battery data
    data = load_battery_data()
    
    # Create impedance plot
    fig = create_impedance_plot(data)
    
    # Save the plot
    save_impedance_plot(fig, 'data/battery_impedance_plot.html')
    
    # Generate detailed report
    report = generate_detailed_report(data)
    
    # Print the report
    print("Battery Aging Analysis Report:")
    print("\nImpedance Trends:")
    for key, value in report['Impedance Trends'].items():
        print(f"{key}: {value}")
    
    print("\nAging Metrics:")
    for key, value in report['Aging Metrics'].items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()