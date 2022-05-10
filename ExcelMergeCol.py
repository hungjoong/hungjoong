# 액셀파일 합치기 
# Eplan BOM Export File을 하나의 Excel 파일로 컬럼으로 구분하여 저장

import pandas as pd
import glob
import os
from pathlib import Path

file_path="C:/Users/HJ.Kim/OneDrive/PythonWorkspace/Example Data"
file_format=".xls"
save_path="C:/Users/HJ.Kim/OneDrive/PythonWorkspace/ExcelMerge.xlsx"
save_format=".xls"

merge_df = pd.DataFrame(columns=['designation', 'Part no.', 'Manufacturer'])

file_list = file_list = [f"{file_path}/{file}" for file in os.listdir(file_path) if file_format in file]

for file in file_list:
    file_df = pd.read_excel(file, skiprows = 4)
    file_df = file_df.drop(['Pos', 'Order no.'], axis = 1)
    file_df = file_df[['designation', 'Part no.', 'Manufacturer', 'Quantity']]
    file_name = Path(file).stem
    file_df = file_df.rename(columns={'Quantity':file_name})
    merge_df = merge_df.merge(file_df, how="outer")

merge_df.insert(3, 'Total', 0)
merge_df['Total'] = merge_df.iloc[:,4:].sum(axis=1)
merge_df = merge_df.sort_values(by=['Manufacturer', 'Part no.'] ,ascending=True)
merge_df.to_excel(save_path, index=False)
merge_df.reset_index(drop=True)