📐 Architecture Overview

Project Name: <Project Name>
Environment: Dev
Last Updated: <Date>
Owner: <Your Name>

1. Purpose

This document describes the architecture for the <Project Name> data pipeline.
The pipeline ingests data from <API Name>, applies transformations in Azure Databricks, and stores curated datasets in Delta Lake for downstream consumption.

Primary objectives:

- Reliable API ingestion

- Structured transformation workflow

- Scalable and cost-efficient processing

- Data quality enforcement

- Clear separation of data layers

Architecture Diagram: 

          +-------------------+
          |   External API    |
          +-------------------+
                    |
                    v
          +-------------------+
          | Ingestion Layer   |
          | (Databricks Job)  |
          +-------------------+
                    |
                    v
          +-------------------+
          | Bronze Layer      |
          | Raw Delta Tables  |
          +-------------------+
                    |
                    v
          +-------------------+
          | Silver Layer      |
          | Cleaned / Normal  |
          +-------------------+
                    |
                    v
          +-------------------+
          | Gold Layer        |
          | Business Curated  |
          +-------------------+
                    |
                    v
          +-------------------+
          | Downstream BI     |
          | Reporting Systems |
          +-------------------+
