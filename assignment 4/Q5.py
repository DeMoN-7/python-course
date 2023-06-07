import pandas as pd
data = {'Name': ['John', 'Mike', 'Sarah', 'Mike', 'Emma'],'Age': [25, 30, 28, 30, 27]}
df = pd.DataFrame(data)
name_counts = df['Name'].value_counts()

print(name_counts)
