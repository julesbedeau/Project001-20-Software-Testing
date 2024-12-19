import pandas as pd

# Creating a sample performance test result dataset for Excel export
performance_metrics = {
    "Metric": ["Average Response Time (ms)", "Throughput (req/sec)", "Error Rate (%)"],
    "Login API": [250, 50, 0.5],
    "Trade Execution (XRP)": [300, 40, 1.0],
    "Trade Execution (NVDA)": [320, 38, 1.5]
}

performance_results = pd.DataFrame(performance_metrics)

# Save the performance metrics to an Excel file
file_path = "./Performance_Test_Results.xlsx"

with pd.ExcelWriter(file_path) as writer:
    performance_results.to_excel(writer, index=False, sheet_name="Performance Metrics")

