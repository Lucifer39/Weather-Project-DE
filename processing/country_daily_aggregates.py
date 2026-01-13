from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    avg,
    max,
    min,
    sum
)


spark = SparkSession.builder.appName("CountryDailyAggregates").getOrCreate()

CITY_AGG_PATH = "storage/aggreagates/daily_city_weather"
COUNTRY_AGG_PATH = "storage/aggreagates/daily_country_weather"

df_city = spark.read.parquet(CITY_AGG_PATH)

df_country = df_city.groupBy(
    "country",
    "date"
).agg(
    avg("avg_temp_c").alias("avg_temp_c"),
    max("max_temp_c").alias("max_temp_c"),
    min("min_temp_c").alias("min_temp_c"),
    avg("avg_humidity").alias("avg_humidity"),
    sum("records_count").alias("records_count")
)

df_country.write.mode("append").partitionBy("date").parquet(COUNTRY_AGG_PATH)

spark.stop()