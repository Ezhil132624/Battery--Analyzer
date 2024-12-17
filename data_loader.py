import numpy as np
import pandas as pd
import os

def load_battery_data(file_path=None, generate_synthetic=True):
    """
    Load battery data from CSV or generate synthetic data.
    
    Parameters:
    - file_path (str, optional): Path to CSV file
    - generate_synthetic (bool): Whether to generate synthetic data if file not found
    
    Returns:
    - pandas.DataFrame: Battery data
    """
    # If file path is provided, try to load
    if file_path and os.path.exists(file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Error loading CSV: {e}")
    
    # Generate synthetic data
    if generate_synthetic:
        np.random.seed(42)  # for reproducibility
        cycles = np.arange(1, 101)
        
        # Synthetic data generation with some realistic aging characteristics
        data = {
            'cycle_number': cycles,
            'Battery_impedance': [0.015 + 0.001 * np.log(x) + np.random.random() * 0.002 for x in cycles],
            'Rct': [0.02 + 0.002 * np.log(x) + np.random.random() * 0.003 for x in cycles],
            'Temperature': [25 + np.random.random() * 5 for _ in cycles],
            'Capacity_Fade': [100 * (1 - 0.005 * np.log(x)) for x in cycles]
        }
        
        df = pd.DataFrame(data)
        
        # Optionally save the synthetic data
        if not os.path.exists('data'):
            os.makedirs('data')
        df.to_csv('data/battery_synthetic_data.csv', index=False)
        
        return df
    
    raise ValueError("No data source found. Please provide a valid CSV or set generate_synthetic=True")

# Optional: If you want to test the data loader
if __name__ == "__main__":
    df = load_battery_data()
    print(df.head())
    print(df.describe())