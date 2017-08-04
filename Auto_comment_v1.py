#python 3
import requests, json, time, random
def gettoken(): #an trom cua Khoa hjhj
    id=input("id: ")
    pw=input("password: ")
    pl={'u': id, 'p': pw}
    get_token=requests.get('http://gymtranhuynh-winazure.rhcloud.com/token.php', params=pl).json()
    while True:
        try:
            token=get_token['access_token']
            return token
        except KeyError:
            print("incorrect password/id")
            break

ques=input("Do you have token? (Y/ N)")

if ques.upper()=="Y":
    token=input("token: ")
else:
    token=gettoken()
    print(token) #print for what tho?

idfb=input('Facebook ID you want to spam: ')
payload={'method': 'get', 'access_token':token}
t = requests.get('https://graph.facebook.com/v2.10/'+idfb+'/feed', params=payload).json()
#link: https://graph.facebook.com/v2.10/(idfb)/feed?method=get&access_token=token

while True:
    for item in t['data']:
        payload1={'method':'post', 'message':'clgt', 'access_token':token }
        comment=requests.post('https://graph.facebook.com/v2.10/'+item['id']+'/comments', params=payload1).json()
        t=requests.get(t["paging"]["next"]).json()

#I actually have no idea what payload is. My friend, @minhkhoa2000, used it so I just picked it up from him. Huehue.
#@minhkhoa2000 actually coded most of this. Huehue.
