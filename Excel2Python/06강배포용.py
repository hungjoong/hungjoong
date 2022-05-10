#!/usr/bin/env python
# coding: utf-8

# # 엑셀 읽어오기 : read_excel()

# In[ ]:





# # 엑셀의 if기능 : mask

# In[ ]:





# # 엑셀의 다중if : 다중mask

# In[ ]:





# # 클립보드에 복사 : to_clipboard()

# In[ ]:





# # 전체코드

# In[25]:


import pandas as pd 

df1 = pd.read_excel("E06EXAMPLE.xlsx", sheet_name=1)
cond1 = df1["점수"].isnull()
df1["참석여부"] = df1["점수"].mask(cond1, "X").mask(~cond1, "O")
cond2 = df1["점수"] > 70
cond3 = df1["점수"] > 90
df1["성적"] = df1["점수"].mask(~cond2, "C").mask(cond2, "B").mask(cond3, "A")
df1.to_clipboard(index=False)

