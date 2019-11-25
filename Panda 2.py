import pandas as pd
df=pd.DataFrame(carscsv)
a=df.iloc[1:10:2]
b=df.iloc[0]
c=df.loc[[23],['Model','cyl']]
d=df.loc[[1,28,18],['Model','cyl','gear']]