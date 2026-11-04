---
title: "Full-Stack Expense Tracker (CLI & GUI)"
description: "A comprehensive personal finance application built with Python, featuring a Command Line Interface, a Graphical UI, and 100% test coverage using SQLite."
techStack: ["Python", "SQLite", "Tkinter", "Matplotlib"]
thumbnail: "/images/projects/expense/gui-dashboard.png"
repoUrl: "https://github.com/ArkanTsabit123"
category: "web-app"
featured: false
date: 2025-06-15
---

## Executive Summary

Managing personal finances is a universal challenge. While many apps exist, they often lack customizability, require expensive subscriptions, or compromise user privacy by syncing data to the cloud.

This project is a full-stack Python application that allows users to track their daily expenses completely offline. It was built to demonstrate advanced Python concepts, relational database management, GUI development, and rigorous software testing.

---

## The Problem: Cloud Dependency & Bad UX

Most budgeting apps force users to create an account, sync their data to a remote server, and pay a monthly fee. 

I wanted to build a lightweight, offline-first solution that gives the user 100% ownership of their financial data. The app needed to be fast, reliable, and capable of generating visual insights without needing an internet connection.

## The Solution: A Dual-Interface Application

I developed an application that runs entirely locally on the user's machine, backed by a robust SQLite database.

### 1. Dual Interface (CLI & GUI)
To cater to different types of users, I built two interfaces:
- **Command Line Interface (CLI):** With 12 distinct menus for power users who prefer typing commands.
- **Graphical User Interface (GUI):** Built with `Tkinter`, featuring 6 tabs for ease of use.

### 2. Relational Database (SQLite)
The application uses an optimized SQLite database. I designed the schema with 5 tables and 5 indexes to ensure that even after thousands of expense records, queries remain instantaneous.

### 3. Data Visualization
Using `Matplotlib`, the app automatically generates insightful charts (like monthly spending trends and category breakdowns) directly from the database.

![Expense Tracker Dashboard](/images/projects/expense/gui-dashboard.png)
*The Graphical User Interface showing analytics and charts.*

### 4. 100% Test Coverage (277 Unit Tests)
To ensure absolute reliability (because nobody wants to lose their financial data), I wrote **277 unit tests** using `unittest`. The application features a 100% test pass rate, ensuring that new features never break existing calculations.

![Test Results](/images/projects/expense/test-results.png)
*The test suite showing 277 successful test cases.*

---

## Technical Stack Breakdown

| Technology | Role in the Project |
| :--- | :--- |
| **Python** | Core application logic and data processing. |
| **SQLite** | Relational database storing user expenses securely offline. |
| **Tkinter** | Python's standard GUI library used for the desktop interface. |
| **Matplotlib** | Library used for generating visual charts and graphs. |

---

## The Results & Impact

- **Robust & Stable:** 277 unit tests ensure zero data corruption.
- **Fast Performance:** The SQLite database queries were optimized using indexes, ensuring instant load times.
- **User-Centric:** Gave the user complete ownership of their financial data with zero cloud dependency or subscription fees.