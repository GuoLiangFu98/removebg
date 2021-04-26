# removebg-批量消除照片背景并填充白色背景

# 介绍

removebg是依赖百度AI人像分割开发的批量消除照片背景并填充白色背景

# 运行环境
•python3.7+

•import os

•import requests

•import base64

•import cv2

•import numpy as np

•from PIL import Image

•from pathlib import Path


# 注意事项：
1、使用前需要注册百度AI并创建人像分割项目，将removebg.py中的'client_id'和'client_secret'替换，详情请见百度AI官网：https://ai.baidu.com/

2、使用需要将removebg.py移至待处理照片同级目录

# 使用

$ git clone https://github.com/GuoLiangFu98/removebg.git

$ cd removebg

$ python removebg.py

# 目前存在的BUG
1、对于一寸照片处理可能出现纯白照片

2、可能会漏掉一些没处理

# 待优化
1、API处理照片后返回的是png格式的照片，这里是先存储png,将png转jpg,再删除png，比较耗时
2、暂时不支持不同级目录处理，会报错
