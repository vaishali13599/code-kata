import hashlib
import pandas as pd

def anonymize_column(column):
    return column.apply(lambda x: hashlib.sha256(x.encode()).hexdigest())

def anonymize_csv(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Anonymize specified columns
    df['first_name'] = anonymize_column(df['first_name'])
    df['last_name'] = anonymize_column(df['last_name'])
    df['address'] = anonymize_column(df['address'])
    
    df.to_csv(output_file, index=False)

# Anonymize the sample data
anonymize_csv('sample_data.csv', 'anonymized_data.csv')
