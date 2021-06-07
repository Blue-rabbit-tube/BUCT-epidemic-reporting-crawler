import requests
import re
import time

header={
    "User-Agent":"自己搞一个ua"
    }
cookie={
"UUkey" : "",                #填入cookie
"eai-sess" : "",              #填入cookie
"Hm_lvt_":"",       #填入cookie   自己抓包
"Hm_lpvt_":"",       #填入cookie
}

r=requests.get("https://eai.buct.edu.cn/ncov/wap/default/index",headers=header,cookies=cookie)

if '填学号' in r.text:
    print("Login success")

ti=int(time.time())
da=str(int("20"+time.strftime("%y%m%d"))-1)

datas={
"ismoved":"0",
"jhfjrq":"",
"jhfjjtgj":"",
"jhfjhbcc":"",
"sfxk":"0",
"xkqq":"",
"tw":"2",
"sfcxtz":"0",
"sfjcbh":"0",
"sfcxzysx":"0", 
"sfyyjc":"0",
"jcjgqr":"0",
"remark":"",

"address" :"",                  #填地点
"geo_api_info":'',              #填定位
"area" :"xx省 xx市 xx县",    #填地点
"province":"xx省",            #填地点
"city":"xx市",                #填地点

"sfzx":"0",
"sfjcwhry":"0", 
"sfjchbry":"0", 
"sfcyglq":"0", 
"gllx":"",
"glksrq":"",
"jcbhlx":"", 
"jcbhrq":"", 
"bztcyy":"", 
"sftjhb":"0", 
"sftjwh":"0", 
"sfsfbh":"0", 
"xjzd":"",                   #填地点
"jcwhryfs":"",
"jchbryfs":"",
"szgj":"",
"jcjg":"",
"uid":"19191",    #不知道什么东西 自己抓包叭
"created":ti,
"date":da,
"jcqzrq":"",
"sfjcqz":"",
"szsqsfybl":"0",
"sfsqhzjkk":"",
"sqhzjkkys":"", 
"sfygtjzzfj":"", 
"gtjzzfjsj":"",
"id":"804143",        #不知道什么东西 自己抓包叭
"gwszdd":"",
"sfyqjzgc":"",
"jrsfqzys":"",
"jrsfqzfy":"",
"qksm":"",
}
r=requests.post("https://eai.buct.edu.cn/ncov/wap/default/save",headers=header,cookies=cookie,data=datas)
result=print(r.text)
#print(result["m"])
