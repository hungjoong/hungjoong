import pandas as pd

df1 = pd.read_excel("E05EXAMPLE.xlsx", sheet_name=1)
df1["승점"] = df1["승"] * 3 + df1["무"]
df1["득실차"] = df1["득점"] - df1["실점"]
df2 = df1.drop(["득점", "실점"], axis=1)
df2.to_clipboard(index=False)