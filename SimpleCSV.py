import pandas as pd

final_dict = {}
data = pd.read_csv('data.csv')
for country in data['country'].unique():
    people = data.loc[data['country'].eq(country), 'person'].tolist()
    final_dict[country] = {
        'people': people,
        'count': len(people),
    }
print(final_dict)
