import pandas as pd
data = {'Name': ['John', 'Mike', 'Sarah', 'Emma', 'Tom'],
        'Age': [25, 30, 28, 27, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Boston', 'San Francisco'],
        'Salary': [50000, 60000, 55000, 52000, 65000]}
df = pd.DataFrame(data)

sliced_df = df.loc[1:3, ['Name', 'City']]
print("Sliced DataFrame:")
print(sliced_df)

name = df.at[0, 'Name']
print("\nName at index 0:", name)

salary_series = df['Salary']
print("\nSalary Series:")
print(salary_series)

df['Bonus'] = [5000, 6000, 5500, 5200, 6500]
print("\nDataFrame with Bonus column:")
print(df)

df.dropna(inplace=True)
print("\nDataFrame after dropping null values:")
print(df)
