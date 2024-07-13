import pandas as pd
import numpy as np

# Sample data generation
num_records = 10000  # Adjust this number as needed

first_names = ['John', 'Jane', 'Alice', 'Bob']
last_names = ['Doe', 'Smith', 'Johnson', 'Williams']
addresses = ['123 Main St', '456 Oak St', '789 Pine St', '101 Maple St']
date_of_births = pd.date_range(start='1950-01-01', end='2000-12-31', periods=num_records)

data = {
    'first_name': np.random.choice(first_names, num_records),
    'last_name': np.random.choice(last_names, num_records),
    'address': np.random.choice(addresses, num_records),
    'date_of_birth': np.random.choice(date_of_births, num_records),
}

df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)