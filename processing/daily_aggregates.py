from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    avg,
    max,
    min,
    count,
    to_date
)

spark = SparkSession.builder.appName("DailyWeatherAggregates").getOrCreate()

CLEAN_PATH = "storage/clean/"
AGG_PATH = "storage/aggreagates/daily_city_weather"

df_clean = spark.read.parquet(CLEAN_PATH)

df_clean = df_clean.withColumn(
    "date",
    to_date(col("event_time"))
)

df_daily = df_clean.groupBy(
    "city",
    "country",
    "date"
).agg(
    avg("temperature_c").alias("avg_temp_c"),
    max("temperature_c").alias("max_temp_c"),
    min("temperature_c").alias("min_temp_c"),
    avg("humidity").alias("avg_humidity"),
    count("*").alias("records_count")
)


df_daily.write.mode("append").partitionBy("date").parquet(AGG_PATH)

spark.stop()