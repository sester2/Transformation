🔄 Transformations Documentation

Project Name: <Project Name>
Environment: Dev
Last Updated: <Date>
Owner: <Your Name>

1. Purpose

This document outlines all transformation logic applied to data after ingestion from <API Name>.

The goal of the transformation layer is to:

Clean and normalize raw API data

Enforce schema standards

Remove duplicates

Apply business logic

Prepare curated datasets for downstream analytics


2. Source Data (Bronze Layer)

Source Table: <catalog>.<schema>.bronze_<entity>
Storage Path: /mnt/<env>/bronze/<entity>/
Data Format: Delta

2.1 Bronze Characteristics

Raw JSON preserved

Minimal transformations

Includes ingestion metadata:

ingestion_timestamp

ingestion_date

source_endpoint

run_id


3. Bronze → Silver Transformations
3.1 Objective

Convert raw API payload into structured, validated dataset.

3.2 Schema Standardization
Rules Applied

Convert camelCase to snake_case

Explicit type casting

Normalize timestamp formats to UTC

Trim whitespace

Example: 

from pyspark.sql.functions import col, trim

silver_df = bronze_df.select(
    col("id").cast("string").alias("record_id"),
    trim(col("userName")).alias("user_name"),
    col("createdAt").cast("timestamp").alias("created_timestamp")
)


3.4 Deduplication Strategy
Business Key(s)

<primary_key_column>

Logic

Keep most recent record based on <updated_at>

Drop duplicates using window function

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, desc

window_spec = Window.partitionBy("record_id").orderBy(desc("updated_timestamp"))

dedup_df = silver_df \
    .withColumn("row_num", row_number().over(window_spec)) \
    .filter("row_num = 1") \
    .drop("row_num")
