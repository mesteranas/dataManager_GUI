import json
import os
from settings import settings_handler
path=os.path.join(os.getenv('appdata'),settings_handler.appName,"data.json")
def getCatagory(catagoryName:str):
    with open(path,"r",encoding="utf-8")as data:
        data=json.load(data)
    return data[catagoryName]
def  saveCatagories(name:str,content:dict):
    with open(path,"r",encoding="utf-8") as data:
        data=json.load(data)
    data[name]=content
    with open(path,"w",encoding="utf-8")as file:
        file.write(str(data).replace("'",'"'))
def getCategoryContent(type:str,categoryName:str):
    with open(path,"r",encoding="utf-8")as data:
        data=json.load(data)
    return data[type][categoryName]
def  saveCatagoryContents(name:str,cname:str,content:dict):
    with open(path,"r",encoding="utf-8") as data:
        data=json.load(data)
    data[name][cname]=content
    with open(path,"w",encoding="utf-8")as file:
        file.write(str(data).replace("'",'"'))
