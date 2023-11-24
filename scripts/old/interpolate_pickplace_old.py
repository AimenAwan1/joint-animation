import numpy as np
from scipy.interpolate import CubicSpline
import pandas as pd
import os

# Example function to load data from CSV
def load_data_from_csv(file_path):
    data = pd.read_csv(file_path)
    return data

# Example: Assuming you have one CSV file named 'talos_pickplace_jointpos.csv'
file_path = '~/robohub/julie/talos_public_ws/src/joint_animation_tutorial/scripts/talos_pickplace_jointpos.csv'
expanded_file_path = os.path.expanduser(file_path)  # Expand tilde in file path
data = load_data_from_csv(expanded_file_path)

# Create 'x' values array from 1 to 4608
x = np.arange(1, 4608)

# Create a new DataFrame for the interpolated values
interpolated_data = pd.DataFrame()

# Interpolate each of the first 32 columns separately
for i, column in enumerate(data.columns[:32]):
    # Convert 'y' values to numeric, replacing non-numeric values with NaN
    y = pd.to_numeric(data[column], errors='coerce')
    cs = CubicSpline(x, y)
    interpolated_data[f'interpolated_{i+1}'] = cs(x)

# Save the interpolated values without column titles and 'x' column to a new CSV file
interpolated_data.to_csv('interpolated_data.csv', header=False, index=False)

# Create a new file interleaving rows from 'data.csv' and 'interpolated_data.csv'
merged_file_path = 'merged_data.csv'
with open(expanded_file_path, 'r') as original_file, open('interpolated_data.csv', 'r') as interpolated_file, open(merged_file_path, 'w') as merged_file:
    for line_original, line_interpolated in zip(original_file, interpolated_file):
        merged_file.write(line_original.strip() + ',' + line_interpolated)

# Append the remaining rows from 'data.csv' to 'merged_data.csv'
with open(expanded_file_path, 'r') as original_file, open(merged_file_path, 'a') as merged_file:
    for line_original in original_file:
        merged_file.write(line_original.strip() + ',' + ','.join(['NaN']*32) + '\n')
