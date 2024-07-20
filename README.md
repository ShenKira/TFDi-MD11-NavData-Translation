# TFDi-MD11-NavData-Translation


由于目前暂时没有适用于MSFS TFDi MD11的及时更新的导航数据，因此在分析了P3D上和MSFS上的TFDi导航数据格式后编写了几个脚本，从P3D上已有的TFDi通用导航数据出发转换到MSFS上的导航数据格式。  
大部分脚本都是作者用ChatGPT实现的（）  
具体使用方法为首先用Access打开P3D版本的TFDi导航数据库文件，将每个表都导出为xlsx，随后执行xlsxtojson.py,MergeAndSplit.py,NantoNull.py来完成转换。  
注意导出后的目录格式要匹配TFDi MD11 MSFS版本自带的导航数据(目录为Community\tfdidesign-aircraft-md11\Data\Primary)。  

TFDi MD11 is a newly released aircraft that currently there is no suitable updated NavData for it, so after analyzing the NavData format for TFDi on P3D and MSFS I wrote several scripts to transform the NavData.  
Most of the scripts are wrote using ChatGPT()  
To use these scripts, you have to open the P3D version TFDi NavData Database using Access and extract all tables as xlsx format, the run xlsxtojson.py,MergeAndSplit.py,NantoNull.py to complete the transform.  
Be careful about the directory format, the translated Navdata should match the original directory format of TFDi MD11 MSFS version(NavData directory is Community\tfdidesign-aircraft-md11\Data\Primary)

2024/7/21
