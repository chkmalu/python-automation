import pandas as pd

d = {
    'A':[1,2,3,4,5,6],
    'B':[2,3,4,5,6,7],
    'C':[3,4,5,6,7,8],
    'D':[4,5,6,7,8,9],
    'E':[5,6,7,8,9,10]
}


df = pd.DataFrame(d)
df.to_csv('myfils.csv')