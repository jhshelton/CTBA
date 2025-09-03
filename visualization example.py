import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "data/livedata-weekly-job-changes-2025-07-23.csv"
df = pd.read_csv(file_path)

df['current_job.started_at'] = pd.to_datetime(df['current_job.started_at'], errors = 'coerce')
df['previous_job.ended_at'] = pd.to_datetime(df['previous_job.ended_at'], errors = 'coerce')

df['month'] = df.apply(
    lambda row: row['current_job.started_at']
    if row['arrival/departure'] == 'arrival' else row['previous_job.ended_at'],
   axis = 1
).dt.tz_localize(None).dt.to_period('M').dt.start_time

df_2025 = df[df['month'].dt.year == 2025].copy()

monthly_counts = (df_2025.groupby(['month', 'arrival/departure']).size().reset_index(name = 'count'))

pivot_monthly = monthly_counts.pivot(index = 'month', columns = 'arrival/departure', values = 'count').fillna(0)


pivot_monthly.plot(kind = 'bar', stacked = False, color = ['#382261', '#D4A421'])

plt.title('Monthly Job Arrivals vs. Departures (2025)')
plt.ylabel('Number of Changes')
plt.xlabel('Month')
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()
plt.show()

departures = df[df['arrival/departure'] == 'departure']
top_departure_companies = departures['previous_job.company.name'].value_counts().nlargest(10)

sns.barplot(x= top_departure_companies.values, y = top_departure_companies.index, hue = top_departure_companies.index, dodge = False, legend = False, palette = 'coolwarm')

plt.title('Top Companies by Number of Departures')
plt.xlabel('Number of Departures')
plt.ylabel('Company')
plt.grid(axis = 'x', linestyle = '--', alpha = 0.5)
plt.show()

departures_by_function = (
    departures['previous_job.function']
    .value_counts()
    .nlargest(10)
    .reset_index()
)

departures_by_function.columns = ['previous_job.function', 'count']

sns.barplot(
    data = departures_by_function,
    x = 'count',
    y = 'previous_job.function',
    hue = 'previous_job.function',
    palette = 'Reds_r',
    legend = False
)

plt.title("Top 10 Job Functions by Number of Departures")
plt.xlabel('Number of Departures')
plt.ylabel("Job Function")
plt.grid(axis = 'x', linestyle = '--', alpha = 0.5)
plt.show()