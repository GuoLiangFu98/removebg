# encoding:utf-8
import os
import requests
import base64
import cv2
import numpy as np
from PIL import Image
from pathlib import Path

path = os.getcwd()
paths = list(Path(path).glob('*'))
#人像分割

# 百度AI开放平台鉴权函数
def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    data = {
        'grant_type': 'client_credentials',  # 固定值
        'client_id': '',  # 在开放平台注册后所建应用的API Key
        'client_secret': ''  # 所建应用的Secret Key
    }
    res = requests.post(url, data=data)
    res = res.json()
    access_token = res['access_token']
    return access_token
def png_jpg(png_name):
    im = Image.open(png_name)
    bg=Image.new('RGB',im.size,(255,255,255))
    bg.paste(im)
    jpg_name = png_name.split('.')[0]+".jpg"
    #quality 代表图片质量，值越低越模糊
    bg.save(jpg_name,quality=70)
    im.close()

    
def fullwhite(png_name):
    im = Image.open(png_name)
    x,y = im.size
    try:
        # 使用白色来填充背景
        # (alpha band as paste mask).
        p = Image.new('RGBA', im.size, (255,255,255))
        p.paste(im, (0, 0, x, y), im)
        p.save(png_name)
    except:
        pass

def removebg():
    try:
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg"
        # 二进制方式打开图片文件
        f = open(name, 'rb')
        print(name+"\t开始处理白底")
        img = base64.b64encode(f.read())
        params = {"image":img}
        access_token = get_access_token()
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            res = response.json()["foreground"]
            png_name=name.split('.')[0]+".png"
            with open(png_name,"wb") as f:
                data = base64.b64decode(res)
                f.write(data)
            fullwhite(png_name)
            png_jpg(png_name)
            os.remove(png_name)
            print(name+"\t处理成功！")
    except Exception as e:
        pass

if __name__ == '__main__':
    for i in paths:
        name = os.path.basename(i.name)
        if(name==os.path.basename(__file__)):
            continue
        removebg()
