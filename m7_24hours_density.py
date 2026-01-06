import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 1) READ THE DATA
# =========================
df = pd.read_csv("m7_24hours_density.csv")

# Keep only M7 line (safety check)
df = df[df["route"] == "M7"]

# =========================
# 2) BASIC ANALYSIS
# =========================
print("Average passenger count:", df["passenger_count"].mean())
print("Peak hour:", df.loc[df["passenger_count"].idxmax(), "hour"])
print("Maximum passenger count:", df["passenger_count"].max())

print("\nStatistical Summary:")
print(df["passenger_count"].describe())

# =========================
# 3) ANOMALY DETECTION (DATA SCIENCE)
# =========================
q1 = df["passenger_count"].quantile(0.25)
q3 = df["passenger_count"].quantile(0.75)
iqr = q3 - q1

anomalies = df[
    (df["passenger_count"] < q1 - 1.5 * iqr) |
    (df["passenger_count"] > q3 + 1.5 * iqr)
]

print("\nDetected anomaly hours:")
if anomalies.empty:
    print("No anomalies detected.")
else:
    print(anomalies)

# =========================
# 4) VISUALIZATION
# =========================

# Passenger density by hour
plt.figure()
plt.bar(df["hour"], df["passenger_count"])
plt.title("M7 Metro Line – 24-Hour Passenger Density")
plt.xlabel("Hour")
plt.ylabel("Passenger Count")
plt.xticks(range(0, 24))
plt.show()

# Boxplot (supports anomaly logic)
plt.figure()
sns.boxplot(y=df["passenger_count"])
plt.title("M7 Metro Line Passenger Density Distribution")
plt.show()
