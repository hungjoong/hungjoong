#!/usr/bin/env python
# coding: utf-8

# # 엑셀 읽어오기 : read_excel()

# In[ ]:





# # 표 재구조화 : pivot_table()

# In[ ]:





# # 엑셀의 if : mask()

# In[ ]:





# # 클립보드에 복사 : to_clipboard()

# In[ ]:





# # 전체코드

# In[10]:


import pandas as pd

df1 = pd.read_excel("E07EXAMPLE.xlsx", sheet_name=1)
pdf1 = df1.pivot_table("점수", index="이름", columns="과목", aggfunc="count")
cond1 = pdf1 == 1 
pdf1 = pdf1.mask(cond1, "O").fillna("X")
pdf1.to_clipboard()

