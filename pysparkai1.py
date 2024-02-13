# ingest data
from pyspark_ai import SparkAI
from apikey import getOpenai

getOpenai()

spark_ai = SparkAI()
spark_ai.activate()
auto_df = spark_ai.create_df("https://www.carpro.com/blog/full-year-2022-national-auto-sales-by-brand")
print(auto_df.show(n=5))