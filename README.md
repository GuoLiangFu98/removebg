# 批量消除照片背景并填充白色背景

# 介绍

removebg是依赖百度AI人像分割开发的批量消除照片背景并填充白色背景

# 运行环境
python3.7+

import os

import requests

import base64

import cv2

import numpy as np

from PIL import Image

from pathlib import Path


# 注意事项：
1、使用前需要将'client_id'和'client_secret'自行替换

2、使用需要将removebg.py移至待处理照片同级目录

# 使用

$ git clone https://github.com/GuoLiangFu98/removebg.git

$ cd removebg

$ python removebg.py

# 目前存在的BUG
1、对于一寸照片处理可能出现纯白照片

2、可能会漏掉一些没处理
