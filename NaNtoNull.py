# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:10:27 2024

@author: shenz
"""

import os
import pandas as pd
import numpy as np
import json

def replace_nan_with_null(json_file_path):
    # 读取JSON文件并转换为DataFrame
    df = pd.read_json(json_file_path)
    
    # 将NaN替换为None
    df = df.replace({np.nan: None})
    
    # 将DataFrame转换回JSON格式
    data = df.to_dict(orient='records')
    
    # 将JSON数据写回文件
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    directory = input("Please enter the directory containing the JSON files: ")

    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
    else:
        # 遍历目录中的所有JSON文件并进行处理
        for file_name in os.listdir(directory):
            if file_name.endswith('.json'):
                json_file_path = os.path.join(directory, file_name)
                replace_nan_with_null(json_file_path)
                print(f"Processed {json_file_path}")
