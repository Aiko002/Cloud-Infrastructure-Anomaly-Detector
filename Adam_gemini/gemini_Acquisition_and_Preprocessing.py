import pandas as pd
from google.cloud import monitoring_v3
from google.cloud import bigquery

# Replace with your GCP project ID and metric type
project_id = "your-project-id"
metric_type = "metric.googleapis.com/resource/cpu_utilization"

# Retrieve metric data using Stackdriver Monitoring API
client = monitoring_v3.MetricServiceClient()
time_series = client.list_time_series(
    request={
        "filter": f'resource.type="gce_instance" AND metric.type="{metric_type}"',
        "interval.start_time": "2024-01-01T00:00:00Z",
        "interval.end_time": "2024-10-18T12:03:55Z",
    }
)

# Extract timestamp and metric values
timestamps = []
values = []
for series in time_series.time_series:
    for point in series.points:
        timestamps.append(point.interval.start_time)
        values.append(point.value.double_value)

# Create a Pandas DataFrame
df = pd.DataFrame({"timestamp": timestamps, "value": values})
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

# Preprocess the data (e.g., handle missing values, outliers, normalization)
df = df.fillna(method="ffill")  # Forward fill missing values
df = df[(df["value"] > 0) & (df["value"] < 100)]  # Remove outliers
df["value"] = (df["value"] - df["value"].min()) / (df["value"].max() - df["value"].min())  # Normalize

# Create additional features (e.g., time-based features, differences)
df["hour"] = df.index.hour
df["day_of_week"] = df.index.dayofweek
df["day_of_month"] = df.index.day
df["month"] = df.index.month
df["year"] = df.index.year
df["diff"] = df["value"].diff()

# Split into training and testing sets
train_size = int(len(df) * 0.8)
train_data = df[:train_size]
test_data = df[train_size:]