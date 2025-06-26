# Spotify Listening Habits Analyzer

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar

# Load sample or user streaming history CSV
df = pd.read_csv("fake_spotify_streaming.csv")

# Convert endTime to datetime
df['endTime'] = pd.to_datetime(df['endTime'])
df['Date'] = df['endTime'].dt.date

# Add additional time-based columns
df['Hour'] = df['endTime'].dt.hour
df['Day'] = df['endTime'].dt.day_name()
df['Month'] = df['endTime'].dt.month

df['Duration_min'] = df['msPlayed'] / (1000 * 60)

# Display basic stats
print("\nTop 5 Most Played Artists:")
print(df['artistName'].value_counts().head())

print("\nTop 5 Most Played Tracks:")
print(df['trackName'].value_counts().head())

print("\nTotal Listening Time (in Hours):")
print(round(df['Duration_min'].sum() / 60, 2))

# Plotting Section
plt.style.use("seaborn-v0_8-darkgrid")

# 1. Top Artists
plt.figure(figsize=(10, 6))
df['artistName'].value_counts().head(10).plot(kind='barh', color='skyblue')
plt.title("Top 10 Most Played Artists")
plt.xlabel("Play Count")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 2. Top Tracks
plt.figure(figsize=(10, 6))
df['trackName'].value_counts().head(10).plot(kind='barh', color='lightgreen')
plt.title("Top 10 Most Played Tracks")
plt.xlabel("Play Count")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# 3. Listening by Hour
plt.figure(figsize=(10, 5))
sns.histplot(df['Hour'], bins=24, kde=False, color='coral')
plt.title("Distribution of Listening by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Count")
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

# 4. Listening by Day of Week
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Day', order=list(calendar.day_name))
plt.title("Listening by Day of Week")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Heatmap: Day vs Hour
heatmap_data = df.groupby(['Day', 'Hour']).size().unstack().fillna(0)
plt.figure(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap="YlGnBu")
plt.title("Listening Heatmap: Day vs Hour")
plt.tight_layout()
plt.show()

# 6. Monthly Listening Trend
monthly = df.groupby(['Month'])['Duration_min'].sum()
plt.figure(figsize=(10, 5))
monthly.plot(kind='line', marker='o', color='purple')
plt.title("Monthly Listening Trend (Minutes)")
plt.xlabel("Month")
plt.ylabel("Minutes Played")
plt.xticks(ticks=range(1,13), labels=[calendar.month_name[i] for i in range(1,13)], rotation=45)
plt.tight_layout()
plt.show()

# Export cleaned data if needed
df.to_csv("cleaned_spotify_history.csv", index=False)
