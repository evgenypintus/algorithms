from pyspark.sql import SparkSession

spark=SparkSession.builder.appName('appname').getOrCreate()

data = [(1, "Alice", 29), (2, "Bob", 35), (3, "Cathy", 27)]
columns = ["ID", "Name", "Age"]

df = spark.createDataFrame(data, columns)
df.show()