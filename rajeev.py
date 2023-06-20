import pandas as pd

data={"name":['rajeev','khatri','jonti','jheengur'],
    "marks":[22,22,67,10],
    "class":[9,9,9,9]
}
df=pd.DataFrame(data,columns=['name','marks','class'])
print(df)


s=pd.Series([5,6,7,8])
print(s)
