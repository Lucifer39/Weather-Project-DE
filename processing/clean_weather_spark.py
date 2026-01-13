from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    to_timestamp,
    current_timestamp,
    year,
    month,
    dayofmonth
)

spark = SparkSession.builder.appName("WeatherCleanTransformation").getOrCreate()

#Paths
RAW_PATH = "storage/raw/*.json"
CLEAN_PATH = "storage/clean/"

df_raw = spark.read.option("multiLine", True).json(RAW_PATH)

#Selecting Data Columns
df_clean = df_raw.select(
    col("location.name").alias("city"),
    col("location.country").alias("country"),
    col("current.temp_c").alias("temperature_c"),
    col("current.humidity").alias("humidity"),
    col("current.wind_kph").alias("wind_kph"),
    col("current.condition.text").alias("condition"),
    col("current.last_updated").alias("event_time"),
)

df_clean = df_clean.dropna(
    subset=["city", "country", "event_time"]
)

df_clean = df_clean.fillna({
    "humidity": -1,
    "wind_kph": 0.0,
    "condition": "unknown"
})

#add ingestion time
df_clean = df_clean.withColumn(
    "ingestion_time",
    current_timestamp()
)

#add partition columns
df_clean = df_clean.withColumn("year", year("event_time"))\
    .withColumn("month", month("event_time"))\
    .withColumn("day", dayofmonth("event_time"))

df_clean = df_clean.filter(
    (col("temperature_c").between(-60, 60)) &
    (col("humidity").between(-1, 100))
)

df_clean.select(
    col("humidity"),
    col("condition")
).groupby(
    "humidity", "condition"
).count().show(10, False)

df_clean.write.mode("append").partitionBy("year", "month", "day").parquet(CLEAN_PATH)

spark.stop()

