# AegisVault-Analytics

[![Integration Suite](https://github.com/AxiomVeda/AegisVault-Analytics/actions/workflows/integration_tests.yml/badge.svg)](https://github.com/AxiomVeda/AegisVault-Analytics/actions)
![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

## System Overview
**AegisVault-Analytics** is a sovereign telemetry logging, schema visualization, and performance aggregation pipeline designed as an ecosystem extension for local decision support architecture. Built under the Pandora's Box compartmental matrix framework, it provides immutable local SQLite telemetry indexing, automated Markdown/ASCII schema rendering, and zero-dependency integration regression testing.

---

## Architectural Matrix

```text
+-----------------------------------------------------------------------+
|                    AEGISVAULT ANALYTICS MATRIX                        |
+-----------------------------------------------------------------------+
                                  |
                                  v
         +-------------------------------------------------+
         | 01_Telemetry_Analytics_Engine.py               |
         | - Ingests Execution Latencies                   |
         | - Writes to aegis_analytics.db (SQLite)        |
         +-------------------------------------------------+
                                  |
                                  v
         +-------------------------------------------------+
         | 02_Schema_Visualizer_Generator.py               |
         | - Generates Dynamic System Schemas             |
         | - Renders ASCII & Markdown System Maps          |
         +-------------------------------------------------+
                                  |
                                  v
         +-------------------------------------------------+
         | 03_Performance_Metrics_Aggregator.py            |
         | - Computes Latency Averages & Error Rates       |
         | - Evaluates Pipeline Uptime Percentages         |
         +-------------------------------------------------+
                                  |
                                  v
         +-------------------------------------------------+
         | 04_Analytics_Integration_Validator.py           |
         | - Executes End-to-End Regression Tests          |
         | - Asserts Pipeline Operational Stability       |
         +-------------------------------------------------+
         