# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 15:55:35 2024

@author: shenz
"""

import pandas as pd
import os
import json

def xlsx_to_json(xlsx_file_path):
    # 获取文件名（不包括扩展名）
    base_name = os.path.splitext(os.path.basename(xlsx_file_path))[0]
    # 构建JSON文件路径
    json_file_path = os.path.join(os.path.dirname(xlsx_file_path), base_name + '.json')
    
    # 读取Excel文件并将其转换为DataFrame
    df = pd.read_excel(xlsx_file_path, engine='openpyxl')
    
    # 将DataFrame转换为JSON格式
    data = df.to_dict(orient='records')
    
    # 将JSON数据写入文件
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    
    print(f"Excel file {xlsx_file_path} has been converted to JSON file {json_file_path}")

if __name__ == "__main__":
    xlsx_directory = input("Please enter the directory containing the Excel files: ")

    if not os.path.isdir(xlsx_directory):
        print(f"The directory {xlsx_directory} does not exist.")
    else:
        # 遍历目录中的所有Excel文件并进行转换
        for file_name in os.listdir(xlsx_directory):
            if file_name.endswith('.xlsx'):
                xlsx_file_path = os.path.join(xlsx_directory, file_name)
                xlsx_to_json(xlsx_file_path)
