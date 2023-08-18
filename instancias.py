import pyreadstat
import pandas as pd
import csv
data, metadata= pyreadstat.read_sav('Trabajo - Instancia 15.sav')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.DataFrame(data)

print(df)

data_list = df.values.tolist()

with open('instancia15.txt', 'w') as file:
    for row in data_list:
        line = ' '.join(str(int(element)) for element in row)
        file.write(line + '\n')