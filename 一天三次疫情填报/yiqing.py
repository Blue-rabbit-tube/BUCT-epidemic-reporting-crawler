# coding=gbk
import requests
import re
import time
import mail

header={
    "User-Agent":""
    }
cookie={
"UUkey" : "",               #�Լ�ץ����cookie
"eai-sess" : "",              
"Hm_lvt_":"",
"Hm_lpvt_4":"",       

}

ti=int(time.time())

url_test="https://eai.buct.edu.cn/site/applicationSquare/index?sid=2&time="+str(ti)

r=requests.get("https://eai.buct.edu.cn/ncov/wap/default/index",headers=header,cookies=cookie,verify=False)

if '201802xxxx' in r.text:     #�ж�һ��cookie�Ƿ���Ч��
    print("Login success")


da=str(int("20"+time.strftime("%y%m%d"))-1)

print(da)

datas={
"sfzx":1,
"tw":1,
"area":"�����в�ƽ��",
"city":"������",
"province":"������",
"address":"�����в�ƽ���Ͽ��򱱾�������ѧ(��ƽУ��)УҽԺ����������ѧ��ƽУ��",
"geo_api_info":'''{}''',
"sfcyglq":0,
"sfyzz":0,
"qtqk":"",
"askforleave":0
}
print(datas)
r=requests.post("https://eai.buct.edu.cn/ncov/wap/default/save",headers=header,cookies=cookie,data=datas,verify=False)
result=eval(r.text)
print(result["m"])
mail.diy_mail(str(datas)+str(da)+result["m"])
