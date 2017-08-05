import requests, json, time, random
####
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
            if get_token['error_msg']=="Invalid username or password (401)":
                print("incorrect password/id\nplease re-enter")
                gettoken()
            else:
                print('Please try again after verifying on Facebook to have token generated\n Or enter a proper id')
                gettoken()
####

####
def auto_comment():
    payload ={'method': 'get', 'access_token':token}
    t = requests.get('https://graph.facebook.com/v2.10/'+idfb+'/feed', params=payload).json()
    #link: https://graph.facebook.com/v2.10/(idfb)/feed?method=get&access_token=token
    comment_list= open("Compliment list.txt").read().splitlines()
    for item in t['data']:
        message= random.choice(comment_list)
        payload1={'method':'post', 'message':message, 'access_token':token }
        comment=requests.post('https://graph.facebook.com/v2.10/'+item['id']+'/comments', params=payload1).json()
        t=requests.get(t["paging"]["next"]).json()
        print (message + ' ' + item['id'] )
        time.sleep(2)
####

####            
def auto_react():
    payload ={'method': 'get', 'access_token':token}
    t = requests.get('https://graph.facebook.com/v2.10/'+idfb+'/feed', params=payload).json()
    reaction_list =  ['LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY']
    for item in t['data']:
        reaction = random.choice(reaction_list)
        payload1={'type':reaction, 'method': 'POST' ,'access_token':token}
        reactions=requests.post('https://graph.facebook.com/v2.8/'+item['id']+'/reactions', params=payload1).json()
        t=requests.get(t["paging"]["next"]).json()
        print (reaction + ' ' + item['id'] )
        time.sleep(2)
####
def auto_react_and_comment():
    payload ={'method': 'get', 'access_token':token}
    t = requests.get('https://graph.facebook.com/v2.10/'+idfb+'/feed', params=payload).json()
    reaction_list =  ['LIKE', 'LOVE', 'WOW', 'HAHA', 'SAD', 'ANGRY']
    comment_list= open("Compliment list.txt").read().splitlines()
    for item in t['data']:
        reaction = random.choice(reaction_list)
        payload1={'type':reaction, 'method': 'POST' ,'access_token':token}
        reactions=requests.post('https://graph.facebook.com/v2.8/'+item['id']+'/reactions', params=payload1).json()
        print (reaction + ' ' + item['id'] )

        message= random.choice(comment_list)
        payload1={'method':'post', 'message':message, 'access_token':token }
        comment=requests.post('https://graph.facebook.com/v2.10/'+item['id']+'/comments', params=payload1).json()

        t=requests.get(t["paging"]["next"]).json()
        print (message + ' ' + item['id'] )
        time.sleep(2)
    
                
####
ques=input("Do you have token? (Y/ N)")

if ques.upper()=="Y":
    token=input("token: ")
else:
    token=gettoken()
    print(token) 

idfb=input('Facebook ID you want to spam: ')
    
while True:
    ques1=input("Do you want to spam comments (c), reactions(r), or both (b)?")

    if ques1=='c':
        auto_comment()
    if ques1=='r':
        auto_react()
    if ques1=='b':
        auto_react_and_comment()
    else:
        ques1=input("Do you want to spam comments (c), reactions(r), or both (b)?")


"""
I actually have no idea what payload is. My friend, @minhkhoa2000, used it so I just picked it up from him. Huehue.
@minhkhoa2000 actually coded most of this as well.
"""
