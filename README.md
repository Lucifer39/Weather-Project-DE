# Weather Data Engineering Pipeline

An end-to-end data engineering project that ingests weather data from a public API, processes it using Apache Spark, and produces analytics-ready datasets at multiple aggregation levels.

## Architecture Overview

API → Raw JSON → Clean Parquet → Daily City Aggregates → Daily Country Aggregates

## Data Pipeline Stages

### 1. Ingestion
- Periodic ingestion using WeatherAPI
- Environment-based secret management
- Progress-aware logging (console + file)
- Immutable raw JSON storage

### 2. Clean Layer (Spark)
- Multi-line JSON parsing
- Schema flattening and type enforcement
- Event time vs ingestion time separation
- Null handling and sanity validation
- Partitioned Parquet output (year/month/day)

### 3. Aggregations
- Daily city-level metrics (avg/min/max temperature, humidity)
- Hierarchical roll-up to country-level aggregates
- Partitioned analytics datasets

## Tech Stack
- Python
- Apache Spark
- Linux (cron for scheduling)
- GitHub

## Key Engineering Decisions
- Immutable raw data for replayability
- Hierarchical aggregations to avoid recomputation
- Partitioning by date for query efficiency
- Lightweight validation instead of hard failures

## Sample Use Cases
- Daily temperature trends by city or country
- Weather pattern comparisons across regions
- Data volume and ingestion monitoring

## Future Enhancements
- Orchestration with Airflow
- Data quality metrics
- Cloud deployment
- Streaming ingestion

