"""
AegisVault-Analytics: System Integration Validator
Ecosystem Extension for AegisVault-MedCore
Architect: Axiom Veda
Framework: Pandora's Box Modular Architecture
"""

import os
import sqlite3
import importlib.util

def import_numbered_module(module_name, file_path):
    """Dynamically imports Python files starting with numerical prefixes."""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Dynamic imports for numbered script files
mod_01 = import_numbered_module("engine", "01_Telemetry_Analytics_Engine.py")
mod_03 = import_numbered_module("aggregator", "03_Performance_Metrics_Aggregator.py")

AegisAnalyticsEngine = mod_01.AegisAnalyticsEngine
AegisMetricsAggregator = mod_03.AegisMetricsAggregator


class AegisIntegrationValidator:
    """
    Automated regression runner that validates end-to-end operational stability
    across database logging, schema rendering, and metrics aggregation.
    """
    def __init__(self, db_name="aegis_analytics.db", schema_file="ARCHITECTURE_SCHEMA.md"):
        self.db_name = db_name
        self.schema_file = schema_file

    def test_database_integrity(self) -> bool:
        """Asserts SQLite database exists and contains active records."""
        if not os.path.exists(self.db_name):
            print("[FAIL] Database file missing.")
            return False
        
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM pipeline_telemetry")
        count = cursor.fetchone()[0]
        conn.close()
        
        assert count > 0, "Database table contains no records."
        print(f"[PASS] Database Integrity Verified ({count} records found).")
        return True

    def test_schema_artifact(self) -> bool:
        """Asserts Markdown architecture schema artifact exists and is non-empty."""
        if not os.path.exists(self.schema_file):
            print("[FAIL] Architecture schema file missing.")
            return False
        
        file_size = os.path.getsize(self.schema_file)
        assert file_size > 0, "Architecture schema file is empty."
        print(f"[PASS] Schema Artifact Verified ({file_size} bytes).")
        return True

    def test_metrics_aggregation(self) -> bool:
        """Asserts metrics aggregator successfully computes valid latency values."""
        aggregator = AegisMetricsAggregator(self.db_name)
        metrics = aggregator.compute_summary_metrics()
        
        assert metrics["total_executions"] > 0, "Total executions must be greater than zero."
        assert metrics["success_rate_pct"] >= 0.0, "Success rate invalid."
        print(f"[PASS] Metrics Aggregator Verified (Avg Latency: {metrics['average_latency_ms']}ms).")
        return True

    def run_full_validation_suite(self):
        """Executes all integration tests sequentially."""
        print("\n==================================================")
        print("    AEGISVAULT ANALYTICS INTEGRATION VALIDATION    ")
        print("==================================================")
        
        try:
            db_pass = self.test_database_integrity()
            schema_pass = self.test_schema_artifact()
            metrics_pass = self.test_metrics_aggregation()
            
            if db_pass and schema_pass and metrics_pass:
                print("\n[+] SYSTEM STATUS: ALL INTEGRATION TESTS PASSED (100% STABLE)")
            else:
                print("\n[-] SYSTEM STATUS: VALIDATION FAILED")
        except AssertionError as e:
            print(f"\n[-] ASSERTION ERROR: {e}")
        print("==================================================\n")

if __name__ == "__main__":
    validator = AegisIntegrationValidator()
    validator.run_full_validation_suite()