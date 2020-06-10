import pandas as pd
result = {}
df = pd.read_csv('nga_pop_sendist_2016.csv')
pop = dict(df.groupby(['admin1Name_en'])['Population2016'].sum())
for key, value in pop.items():
    if value >= 5000000:
        result[key] = value
print(result)
    #break
#for key, value in pop.items():
 #   if value > 5000000:
  #      result.append(pop)
   #     print (result)
    #    break
    #else:
     #   break
#print(df[["SenDist_en", "Population2016"]].head())
#print(df.head())