from my_tools import lettergrade
import pandas as pd
data = pd.read_csv('scores.csv')
result = data
result['grade'] = data['score'].apply(lettergrade)
result.to_csv('grades.csv', index=False)