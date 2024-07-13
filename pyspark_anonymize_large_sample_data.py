from pyspark.sql import SparkSession
from pyspark.sql.functions import sha2, col

spark = SparkSession.builder.appName("AnonymizeData").getOrCreate()

def anonymize_csv_spark(input_file, output_file):
    df = spark.read.csv(input_file, header=True, inferSchema=True)
    
    # Anonymize specified columns
    df = df.withColumn('first_name', sha2(col('first_name'), 256))
    df = df.withColumn('last_name', sha2(col('last_name'), 256))
    df = df.withColumn('address', sha2(col('address'), 256))
    
    df.write.csv(output_file, header=True, mode='overwrite')

# Anonymize the sample data using PySpark
anonymize_csv_spark('large_sample_data.csv', 'anonymized_large_data.csv')
