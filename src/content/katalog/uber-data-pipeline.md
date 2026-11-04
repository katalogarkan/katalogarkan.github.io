---
title: "Uber Data Pipeline: Star Schema Data Warehouse"
description: "An in-depth data engineering project transforming raw Uber trip data into a highly optimized Star Schema Data Warehouse using Apache Airflow and DuckDB."
techStack: ["Python", "Apache Airflow", "DuckDB", "Streamlit", "Docker"]
thumbnail: "/images/projects/uber/dashboard.png"
repoUrl: "https://github.com/ArkanTsabit123"
category: "data-engineering"
featured: true
date: 2025-08-10
---

## Executive Summary

In the ride-sharing industry, data is generated at an astronomical rate. Every trip, every route, and every fare contributes to terabytes of raw data. However, raw CSV files are useless for business intelligence. 

This project demonstrates the end-to-end design and implementation of an automated data pipeline that ingests raw Uber trip data and models it into a **Star Schema Data Warehouse** using **DuckDB**, orchestrated by **Apache Airflow**.

---

## The Problem: The Cost of Unstructured Data

Imagine a business analyst trying to answer: *"What is the average fare per mile in Manhattan during rush hour?"* 

If the data is stored in a massive 10GB CSV file, running that query using traditional tools (like Excel or basic Pandas) would take minutes or even crash the computer. The business needed a **centralized, optimized, and structured database** that could answer complex analytical queries in milliseconds.

## The Solution: Dimensional Modeling

To solve this, I designed a data warehouse using **Dimensional Modeling** (Star Schema). Instead of one giant table, I split the data into:
1.  **Fact Table (`fact_trips`):** Contains the measurable metrics (trip distance, fare amount, timestamps).
2.  **Dimension Tables (`dim_passenger`, `dim_location`, `dim_time`):** Contains the contextual attributes.

This approach drastically reduces data redundancy and speeds up query performance.

### 1. Pipeline Architecture & Orchestration
The pipeline is fully automated. **Apache Airflow** manages the workflow, ensuring that new data is extracted, transformed, and loaded into the warehouse automatically.

![Uber Pipeline Flow](/images/projects/uber/pipeline-flow.png)
*The data flow from raw CSV to the final analytical dashboard.*

### 2. Technical Implementation
- **Extraction:** Python scripts fetch the raw Uber trip CSV files.
- **Transformation:** Pandas is used to clean the data, handle missing values, and engineer new features (like calculating trip duration).
- **Loading:** The transformed data is loaded into DuckDB (an in-process SQL OLAP database) for blazing-fast analytical queries.
- **Orchestration:** Airflow DAGs are created to schedule this process daily, with built-in retry logic if a step fails.

### 3. Data Model (Star Schema)
Here is the Entity Relationship Diagram (ERD) of the DuckDB warehouse:

![Uber Star Schema](/images/projects/uber/star-schema.png)
*The Star Schema design implemented in DuckDB.*

---

## The Dashboard

To provide value to the business, I built an interactive dashboard using **Streamlit**. It connects directly to DuckDB and allows stakeholders to filter data by date, location, and passenger count. 

![Uber Dashboard](/images/projects/uber/dashboard.png)
*Analytics dashboard built with Streamlit.*

---

## Technical Stack Breakdown

| Technology | Role in the Project | Why It Was Chosen |
| :--- | :--- | :--- |
| **Apache Airflow** | Orchestration & Scheduling | Manages the entire lifecycle, ensuring daily runs and handling failures automatically. |
| **DuckDB** | Data Warehouse | A high-performance, in-process analytical database that requires zero setup. |
| **Python & Pandas** | Data Transformation | The industry standard for robust data manipulation and feature engineering. |
| **Docker** | Containerization | Ensures the Airflow environment and Python dependencies run consistently. |

---

## The Results & Impact

- **Blazing Fast Queries:** The Star Schema allowed complex analytical queries to run in **milliseconds**, compared to minutes on raw files.
- **Zero Manual Effort:** The business saves hours of manual data processing every week.
- **Scalable Architecture:** The modular design allows the pipeline to easily handle 10x more data in the future.