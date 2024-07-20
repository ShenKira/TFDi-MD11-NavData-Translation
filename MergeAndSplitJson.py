# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 21:16:08 2024

@author: shenz
"""

import pandas as pd
import json
import os
import numpy as np

def merge_json_files(file1, file2):
    # 读取JSON文件并转换为DataFrame
    df1 = pd.read_json(file1)
    df2 = pd.read_json(file2)
    
    # 合并两个DataFrame，按照"ID"字段
    merged_df = pd.merge(df1, df2, on="ID", how="outer")
    
    # 将NaN替换为None
    merged_df = merged_df.replace({np.nan: None})
    
    return merged_df

def replace_null_turn_dir(df):
    # 检测TurnDir的值，若为None则替换为空字符串
    df['TurnDir'] = df['TurnDir'].apply(lambda x: "" if x is None else x)
    return df

def save_by_terminal_id(merged_df, output_directory):
    # 根据"TerminalID"字段进行分组并保存为不同的JSON文件
    grouped = merged_df.groupby("TerminalID")
    
    for terminal_id, group in grouped:
        output_file = os.path.join(output_directory, f"TermID_{terminal_id}.json")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(group.to_dict(orient='records'), f, indent=4, ensure_ascii=False)
        print(f"Saved {output_file}")

if __name__ == "__main__":
    file1 = "TerminalLegs.json"
    file2 = "TerminalLegsEx.json"
    output_directory = "output"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    merged_df = merge_json_files(file1, file2)
    merged_df = replace_null_turn_dir(merged_df)
    save_by_terminal_id(merged_df, output_directory)