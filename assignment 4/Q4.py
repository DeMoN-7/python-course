import pandas as pd

data = [{'name': 'John','age': 28,'address': {'city': 'New York','state': 'NY','country': 'USA'}},{'name': 'Alice','age': 35,'address': {'city': 'London','state': 'N/A','country': 'UK'}},
    {'name': 'Bob','age': 42,'address': {'city': 'Sydney','state': 'NSW','country': 'Australia'}}]

df = pd.DataFrame(data)
print(df)
