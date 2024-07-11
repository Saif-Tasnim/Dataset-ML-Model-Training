import numpy as np
import pandas as pd
# Example data
data = {
    'Age': [25, 30, 35, 40, 45],
    'Premium': [1.5, 2.0, 2.5, 3.0, 3.5],
    'Height': [170, 175, 180, 185, 190],  # Height in cm
    'Weight': [65, 70, 75, 80, 85]        # Weight in kg
}

# Create DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
# csv_file_path = 'extended_dataset.csv'
df.to_csv('C:/Users/ABCD/Desktop/Machine Learning/extend_data.csv', index=False)

# df = pd.DataFrame(data)
# df.to_csv('C:/Users/ABCD/Desktop/Machine Learning/data.csv', index=False)
