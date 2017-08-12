import requests, json, time, random
from SpamBot import gettoken
def spam():
    while True:
        try:
            payload={'method':'post', 'message':random.choice(open("Compliment list.txt").read().splitlines()), 'access_token':token }		
            comment=requests.post('https://graph.facebook.com/v2.10/'+post_id+'/comments', params=payload).json()
            print(payload['message'])
            time.sleep(2)
        except KeyboardInterrupt:
            while True:
                ques=input("Do you want to quit (q) or continue (c)?")
                if ques=='q':
                    exit()
                if ques=='c':
                    spam()
                else:
                    print("invalid response")
                    ques
                   
if __name__ == "__main__":
    ques=input("Do you have token? (Y/ N)")
    if ques.upper()=="Y":
        global token
        token=input("token: ")
        while True:
            if token=='':
                token=input("please re-enter, or get new token (g)")
                if token=='g':
                    token=gettoken()
                    print(token) 
                else:
                    print('invalid response')
                    token=input("please re-enter, or get new token (g)")
            else:
                break
    else:   
        token=gettoken()
    post_id=input("ID of the post you want to spam in: ")
    spam()
