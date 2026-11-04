---
title: "Building a Production-Ready ETL Pipeline with Airflow & BigQuery"
date: 2025-09-15
description: "A deep dive into how I designed and built an automated ETL pipeline processing 2.96M+ rows of data with 100% data quality using Python, Airflow, and PostgreSQL."
category: "tutorial"
tags: ["airflow", "python", "etl", "data-engineering"]
draft: false
coverImage: "/images/projects/batchetl/dashboard.png"
---

In the modern data-driven era, businesses are drowning in data but starving for insights. The difference between a successful company and a failing one often comes down to how efficiently they can move and transform data.

In this article, I want to break down one of my proudest technical achievements: the **BatchETL Pipeline**. This wasn't just a school project; it was an end-to-end, production-ready system designed to process millions of rows of data automatically with 100% data quality.

## The Architecture

![BatchETL Pipeline Architecture](/images/projects/batchetl/architecture.png)
*Figure 1: The architecture of the BatchETL Pipeline, showing the flow from raw data extraction to the final Streamlit dashboard.*

## The Problem: Manual Data is a Business Killer

Imagine a business where an employee has to manually download CSV files every morning, clean the data in Excel, and copy-paste it into a reporting dashboard. 

This process is:
1. **Time-consuming:** Taking hours of manual labor every week.
2. **Error-prone:** Human mistakes lead to bad data, which leads to bad business decisions.
3. **Not scalable:** What happens when the data grows from 10,000 rows to 3 million rows? Excel will crash.

## The Solution: An Automated ETL Pipeline

To solve this, I designed an automated ETL (Extract, Transform, Load) pipeline using industry-standard tools. The goal was simple: *Data should flow from the source to the dashboard without a human touching it.*

### The Tech Stack
- **Orchestration:** Apache Airflow (to schedule and monitor the pipeline).
- **Processing:** Python & Pandas (for heavy data transformation).
- **Storage/Data Warehouse:** PostgreSQL (for structured, fast querying).
- **Containerization:** Docker Compose (to ensure the environment runs identically everywhere).

### 1. Extraction
Every day at 2:00 AM, Airflow triggers a Python script. This script automatically fetches raw data (New York City Taxi trip data) and stores it in a staging area.

### 2. Transformation (The Heavy Lifting)
This is where Pandas shines. The raw data was messy. I wrote Python scripts to:
- Handle missing values (NaN).
- Remove duplicate records.
- Filter out outliers (e.g., trips with negative distances or impossible speeds).
- Convert timestamp strings into proper datetime objects.

### 3. Loading
Once the data is sparkling clean, it is loaded into a PostgreSQL data warehouse. I designed the database using a **Star Schema** (Fact and Dimension tables) to optimize it for analytical queries and dashboard performance.

![Star Schema ERD](/images/projects/batchetl/erd.png)
*Figure 2: The Star Schema database design used in PostgreSQL.*

## The Results: Numbers Don't Lie

The impact of this pipeline was immediate and measurable:
- **2.96 Million+ Rows** processed efficiently.
- **100% Data Quality** verified through automated testing scripts.
- **Execution time under 30 seconds** for the transformation phase.
- The business saved over 20 hours of manual data entry per week.

![Streamlit Dashboard](/images/projects/batchetl/dashboard.png)
*Figure 3: The final Streamlit dashboard used by the client to view analytics.*

## Why This Matters for Your Business

If your company is still relying on manual spreadsheets to understand your business metrics, you are losing money. 

A custom ETL pipeline built by a Data Engineer gives you:
1. **Real-time (or scheduled) insights** without human intervention.
2. **Trust in your data** because the transformations are coded and tested.
3. **Scalability** to handle millions of records as your business grows.

If you need a robust data pipeline to automate your business processes, let's discuss how I can build a similar solution for you.