import requests, json, time, random
####
def gettoken(): #an trom cua Khoa hjhj
    flag = True
    while flag:
        username= input('nhap username fb: ')
        password= input('nhap password fb: ')
        payload= {'u': username, 'p': password}
        get_token= requests.get('http://gymtranhuynh-winazure.rhcloud.com/token.php', params=payload).json()
        try:
            if get_token['error_msg']:
                print ("Error:" + get_token['error_msg'])
        except KeyError:
                token= get_token['access_token']
                flag= False      
    return token;
####
def getfeed():
    payload ={'method': 'get', 'access_token':token}
    t = requests.get('https://graph.facebook.com/v2.10/'+idfb+'/feed', params=payload).json()
    return t
def auto(t, key ):
    while True:
        try:
            for item in t['data']:
                payload1={
                    'type':random.choice(['LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY']),
                    'message':random.choice(open("Compliment list.txt").read().splitlines()) , 
                    'method': 'POST' ,
                    'access_token':token
                    }
                for i in key:
                    request_api=requests.post('https://graph.facebook.com/v2.8/'+item['id']+'/'+i, params=payload1).json()
                if key==['reactions']:
                    print (payload1['type'] +' | '+item['id'] )
                if key==['comments']:
                    print (payload1['message'] +' | '+item['id'] )
                if key==['comments', 'reactions']:
                    print (payload1['message'] +' | '+payload1['type'] +' | '+item['id'])
                    time.sleep(2)
            t=requests.get(t["paging"]["next"]).json()
        except KeyError:
            break
        except KeyboardInterrupt:
            while True:
                ques2=input("Do you want to quit (q) or want to change the spamming method (c)?")
                if ques2=='q':
                       break
                if ques2=='c':
                       choices()
                else:
                       print('invalid response')
                       ques2

                       
ques=input("Do you have token? (Y/ N)")

if ques.upper()=="Y":
    token=input("token: ")
else:
    token=gettoken()
    print(token) 
def idfb():
    global idfb
    idfb=input('Facebook ID you want to spam: ')

def choices():
    global ques1, key, t
    ques1=input("Do you want to spam comments (c), reactions(r), or both (b)?")
    t = getfeed()
    if ques1=='c':
        key= ['comments']
        auto(t, key)
        
    if ques1=='r':
        key= ['reactions']
        getfeed()
        auto(t, key)
        
    if ques1=='b':
        key= ['comments', 'reactions']
        auto(t, key )
if __name__ == "__main__":
    idfb()
    choices()
    

"""
I actually have no idea what payload is. My friend, @minhkhoa2000, used it so I just picked it up from him. Huehue.
@minhkhoa2000 actually coded most of this as well.
"""
