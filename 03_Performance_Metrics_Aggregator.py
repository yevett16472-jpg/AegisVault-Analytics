"""
AegisVault-Analytics: Performance Metrics Aggregator
Ecosystem Extension for AegisVault-MedCore
Architect: Axiom Veda
Framework: Pandora's Box Modular Architecture
"""

import sqlite3

class AegisMetricsAggregator:
    """
    Analytics engine that processes raw telemetry data from SQLite
    and computes pipeline performance metrics.
    """
    def __init__(self, db_name="aegis_analytics.db"):
        self.db_name = db_name

    def compute_summary_metrics(self) -> dict:
        """Calculates total executions, average latency, and success rates."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*), AVG(execution_time_ms) FROM pipeline_telemetry')
        total_runs, avg_latency = cursor.fetchone()
        
        cursor.execute("SELECT COUNT(*) FROM pipeline_telemetry WHERE status = 'SUCCESS'")
        successful_runs = cursor.fetchone()[0]
        
        conn.close()
        
        success_rate = (successful_runs / total_runs * 100) if total_runs else 0.0
        avg_latency = avg_latency if avg_latency else 0.0
        
        return {
            "total_executions": total_runs,
            "average_latency_ms": round(avg_latency, 2),
            "success_rate_pct": round(success_rate, 2)
        }

    def display_report(self):
        """Displays aggregated performance report to console."""
        metrics = self.compute_summary_metrics()
        print("\n==================================================")
        print("       AEGISVAULT TELEMETRY PERFORMANCE REPORT     ")
        print("==================================================")
        print(f" Total Executions Monitored : {metrics['total_executions']}")
        print(f" Average Latency            : {metrics['average_latency_ms']} ms")
        print(f" System Success Rate        : {metrics['success_rate_pct']}%")
        print("==================================================\n")

if __name__ == "__main__":
    print("[+] Initializing AegisVault Metrics Aggregator...")
    aggregator = AegisMetricsAggregator()
    aggregator.display_report()
    