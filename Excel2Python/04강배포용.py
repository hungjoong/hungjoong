import pandas as pd

df1 = pd.read_excel("C:/Users/HJ.Kim/Documents/PythonWorkspace/Excel2Python/E04EXAMPLE.xlsx", sheet_name=1)
df2 = df1.fillna(0)
df3 = df1.dropna()
df2.to_clipboard(index=False)
df3.to_clipboard(index=False)