import requests
import re
import time
import mail

header={
    "User-Agent":""     #自己整一个ua
    }
cookie={
"UUkey" : "",               #自己抓取   
"eai-sess" : "",              
"Hm_lvt_":"",
"Hm_lpvt_":"",       

}

r=requests.get("https://eai.buct.edu.cn/ncov/wap/default/index",headers=header,cookies=cookie)

if '201802xxxx' in r.text:     #猜猜我是哪个学院的
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
"szgj":"",
"szcs":"",
"zgfxdq":"0",
"mjry":"0",
"csmjry":"0",
"tw":"2",
"sfcxtz":"0",
"sfjcbh":"0",
"sfcxzysx":"0",
"qksm":"",
"sfyyjc":"0",
"jcjgqr":"0",
"remark":"",

"address" :"",    #随便填
"geo_api_info":'{}',  #不用管
"area" :"",  #xx省 xx市 xx县/区  中间有空格
"province":"",   #xx省
"city":"",       #xx市

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
"xjzd":"",
"jcwhryfs":"",
"jchbryfs":"",
"szsqsfybl":"0",
"sfygtjzzfj":"",
"gtjzzfjsj":"",
"gtjzzchdfh":"",
"fjqszgjdq":"",
"jcjg":"",
}

r=requests.post("https://eai.buct.edu.cn/ncov/wap/default/save",headers=header,cookies=cookie,data=datas)
result=eval(r.text)
print(result["m"])
mail.diy_mail(result["m"])


