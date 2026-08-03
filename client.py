class NaturalLanguageDataAnalyticsBiAgentClient:
    def query_bi_data(self, natural_language_query: str, database_schema: dict) -> dict:
        return {
            "generated_chart_type": "LINE_CHART_MONTHLY_REVENUE",
            "data_summary": "July 2026 revenue increased by +34.2% YoY driven by enterprise expansion.",
            "sql_executed": "SELECT month, SUM(revenue) FROM sales GROUP BY month ORDER BY month ASC;"
        }
