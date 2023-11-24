import pandas as pd
import matplotlib.pyplot as plt

# Replace 'file1.csv' and 'file2.csv' with the actual paths to your CSV files
file_path1 = '~/robohub/julie/talos_public_ws/src/joint_animation_tutorial/scripts/talos_pickplace_jointpos.csv'
file_path2 = '~/robohub/julie/talos_public_ws/src/joint_animation_tutorial/scripts/merged_data.csv'

# Load data from CSV files
data1 = pd.read_csv(file_path1)
data2 = pd.read_csv(file_path2)

# Extract the first columns
first_column1 = data1.iloc[:, 0]
first_column2 = data2.iloc[:, 0]

# Plot the first columns side by side
plt.figure(figsize=(10, 4))  # Adjust the figure size as needed
plt.subplot(1, 2, 1)
plt.plot(first_column1)
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Original')

plt.subplot(1, 2, 2)
plt.plot(first_column2)
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Interpolated')

plt.tight_layout()  # Adjust layout for better spacing
plt.show()


