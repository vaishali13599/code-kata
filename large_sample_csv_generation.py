import pandas as pd
import numpy as np

# Function to generate a large CSV file
def generate_large_csv(filename, num_records):
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
    df.to_csv(filename, index=False)

# With this number, file size of the generated CSV is approx. 2.69GB. If we reduce this by half, the file size gets 1.34GB
rows_approx = 50000000

generate_large_csv('large_sample_data.csv', rows_approx)
