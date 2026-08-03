from client import NaturalLanguageDataAnalyticsBiAgentClient

def main():
    client = NaturalLanguageDataAnalyticsBiAgentClient()
    res = client.query_bi_data("Show me monthly revenue growth trend for 2026", {"tables": ["sales"]})
    print(f"Chart Type: {res['generated_chart_type']}")
    print(f"Summary: {res['data_summary']}")

if __name__ == "__main__":
    main()
