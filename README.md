# TFDi-MD11-NavData-Translation

2024/7/20
由于目前暂时没有适用于MSFS TFDi MD11的及时更新的导航数据，因此编写了几个脚本，从P3D上已有的TFDi通用导航数据出发转换到MSFS上的导航数据格式。
大部分脚本都是作者用ChatGPT实现的（）
具体使用方法为首先用Access打开P3D版本的TFDi导航数据库文件，将每个表都导出为xlsx，随后执行xlsxtojson.py,MergeAndSplit.py,NantoNull.py来完成转换。
注意导出后的目录格式要匹配TFDi MD11 MSFS版本自带的导航数据。
