import pandas as pd
import glob
import os

def merge_excel_files(file_path, file_format, save_path, save_format, columns=None):
    merge_df = pd.DataFrame()
    file_list = file_list = [f"{file_path}/{file}" for file in os.listdir(file_path) if file_format in file]
    
    for file in file_list:
        if file_format == ".xls":
            file_df = pd.read_excel(file, skiprows = 4)
        else:
            file_df = pd.read_csv(file)
        
        if columns is None:
            columns = file_df.columns
            
        temp_df = pd.DataFrame(file_df, columns=columns)
        
        merge_df = merge_df.append(temp_df)
    
    merge_df = merge_df.drop(['Pos', 'Order no.'], axis = 1)
    # merge_df = merge_df.groupby(['Part no.', 'designation', 'Manufacturer']).sum().groupby(level=0).cumsum().reset_index()
    merge_df = merge_df.groupby(['designation', 'Part no.', 'Manufacturer']).sum().groupby(level=1).cumsum().reset_index()
        
    if save_format == ".xls":
        merge_df.to_excel(save_path, index=False)
    else:
        merge_df.to_csv(save_path, index=False)
        

if __name__ == "__main__":
    merge_excel_files(file_path="C:/Users/HJ.Kim/OneDrive/PythonWorkspace/Example Data", file_format=".xls", 
                      save_path="C:/Users/HJ.Kim/OneDrive/PythonWorkspace/ExcelMerge.xlsx", save_format=".xls")