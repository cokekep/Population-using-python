import pandas as pd
df = pd.read_csv('nga_pop_sendist_2016.csv')
pop = dict(df.groupby(['admin1Name_en'])['Population2016'].sum())
def popSum(data):
    result = {}
    for key, value in pop.items():
        if value >= 5000000:
            result[key] = value
    return result
print(popSum(pop))