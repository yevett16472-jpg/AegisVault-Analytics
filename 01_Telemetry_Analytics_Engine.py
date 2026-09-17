"""
AegisVault-Analytics: Telemetry & Performance Engine
Ecosystem Extension for AegisVault-MedCore
Architect: Axiom Veda
Framework: Pandora's Box Modular Architecture
"""

import os
import sqlite3
from datetime import datetime

class AegisAnalyticsEngine:
    """
    Core telemetry logging engine designed to capture, store,
    and index pipeline execution metrics in a secure local environment.
    """
    def __init__(self, db_name="aegis_analytics.db"):
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """Initializes local SQLite table for telemetry logs if not present."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pipeline_telemetry (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                module_name TEXT NOT NULL,
                execution_time_ms REAL NOT NULL,
                status TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def log_telemetry(self, module_name: str, execution_time_ms: float, status: str = "SUCCESS"):
        """Logs a single execution telemetry event into the database."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        timestamp = datetime.utcnow().isoformat()
        cursor.execute('''
            INSERT INTO pipeline_telemetry (module_name, execution_time_ms, status, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (module_name, execution_time_ms, status, timestamp))
        conn.commit()
        conn.close()
        print(f"[ANALYTICS] Logged {module_name} | Latency: {execution_time_ms:.2f}ms | Status: {status}")

    def fetch_all_telemetry(self):
        """Retrieves all stored telemetry records for analytical processing."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT module_name, execution_time_ms, status, timestamp FROM pipeline_telemetry')
        records = cursor.fetchall()
        conn.close()
        return records

if __name__ == "__main__":
    print("[+] Initializing AegisVault-Analytics Telemetry Engine...")
    engine = AegisAnalyticsEngine()
    
    # Ingest baseline simulation telemetry
    engine.log_telemetry("08_Local_Encryption_Enclave", 12.45)
    engine.log_telemetry("09_System_Integration_Validator", 8.12)
    engine.log_telemetry("04_System_Config_Loader", 4.31)
    
    print("[+] Telemetry Ingestion Complete. Total Records:", len(engine.fetch_all_telemetry()))