# Data Engineering Coding Challenge Solution

### Problem 2 Solution:

- I approached the problem step-by-step with the asks of the problem.
- I started with writing a python code to generate a sample csv file. sample_csv_generation.py does this. Since there were no restrictions on libraries to be used in this problem, I used numpy and pandas to generate the sample data.
- On running 'python sample_csv_generation.py' on local, it created sample_data.csv for me.
- The next step was to anonymize the data. To anonymize the data, I used hashlib and pandas library to encode the data and wrote the code in anonymize_sample_data.py.
- On running 'python anonymize_sample_data.py' on local, it create anonymized_data.csv for me.
- The next part of the problem was to do this for 2GB file and demonstrate that it can work for an even larger dataset.
- I recalled that we use PySpark for working with large data sets. So, the first task was to create a large dataset.
- Using numpy and pandas, I coded large_sample_csv_generation.py to generate a large file. Initially I tried with smaller number of rows and then had to adjust it to finally get a file greater than 2GB (2.69GB).
- Then, I wrote the code in pyspark_anonymize_large_sample_data.py to use PySpark library to anonymize data.
- After running 'python pyspark_anonymize_large_sample_data.py' on terminal, a folder of size 11.54GB was generated with anonymized data and '_SUCCESS' file was generated demonstrating that it worked for large data set.
- PySpark is used to work with large data sets.


### Note:

- I have not uploaded large files to Github since it was taking a lot of time to upload (~13-14GB).
- Feel free to run the code on your local as described above in the solution.
- Also, please check the screenshots for the proof that it was running successfully on my local.
- Thanks!