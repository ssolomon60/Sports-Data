import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'sports_data.csv'  # <-- Change this line to the actual file path of your CSV
df = pd.read_csv(file_path)

# Inspect column names to verify the correct column names
print("Column names in the dataset:")
print(df.columns)

# Explore the data to understand its structure
print("First 5 rows of the dataset:")
print(df.head())

# Answer Question 1: Analyze Team Performance (Win-Loss Percentage)
team_performance = df.groupby('team')['win_loss_perc'].mean()
team_performance = team_performance.sort_values(ascending=False)

# Plot Top Teams by Win-Loss Percentage
plt.figure(figsize=(10, 6))
team_performance.head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Teams by Win-Loss Percentage")
plt.xlabel("Teams")
plt.ylabel("Win-Loss Percentage")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Answer Question 2: Analyze Points Scored per Team
team_points = df.groupby('team')['points'].sum()
team_points = team_points.sort_values(ascending=False)

# Plot Top Teams by Total Points Scored
plt.figure(figsize=(10, 6))
team_points.head(10).plot(kind='bar', color='salmon')
plt.title("Top 10 Teams by Total Points Scored")
plt.xlabel("Teams")
plt.ylabel("Total Points")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Answer Question 3: Identify Teams with the Highest Turnover Percentage
team_turnovers = df.groupby('team')['turnover_pct'].mean()
team_turnovers = team_turnovers.sort_values(ascending=False)

# Plot Top Teams by Turnover Percentage
plt.figure(figsize=(10, 6))
team_turnovers.head(10).plot(kind='bar', color='lightgreen')
plt.title("Top 10 Teams by Turnover Percentage")
plt.xlabel("Teams")
plt.ylabel("Turnover Percentage")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Print out the top teams for each category for reference
print("\nTop Teams by Win-Loss Percentage:")
print(team_performance.head(10))

print("\nTop Teams by Total Points Scored:")
print(team_points.head(10))

print("\nTop Teams by Turnover Percentage:")
print(team_turnovers.head(10))
