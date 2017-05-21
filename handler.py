#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#from models import UserModel
import requests
import json

from structs import typing_message, text_message
    
def recived_message(event, token):#obtener datos o atributos necesarios del mensaje para darle posterior mente un tratamiento
    sender_id = event['sender']['id']
    recipient_id = event['recipient']['id']
    time_message = event['timestamp']
    message = event['message']
    text = message['text']

    typing = typing_message(sender_id)
    call_send_API(typing, token)

    user = call_user_API(sender_id, token)
    first_name = user['first_name']
    message = 'Hi {}, How are you?'.format( first_name )

#    user = { 'first_name' : first_name}
#    UserModel.save( user )

    message = text_message(sender_id, message)
    call_send_API(message, token)

def call_send_API(data, token):#enviando estructura
    res = requests.post('https://graph.facebook.com/v2.6/me/messages',
        params = {'access_token': token },
        data = json.dumps(data),#convierto la data e formato json
        headers = {'Content-type': 'application/json'}
        )
    if res.status_code == 200:
        print ("Message Successfully")




def call_user_API(user_id, token):
    res = requests.get('https://graph.facebook.com/v2.6/' + user_id ,
        params = {'access_token': token } )

    data = json.loads(res.text) 
    return data

#https://graph.facebook.com/v2.6/1452654684795263?access_token=EAADGMZBRFMwEBAJq52oEJOYNaDFQLzApplIP9J01Rl41w29ADwxxnFSk4OKj30IG0EVJOoGwCM31Yonb7wfyaZBXvlGAwDPQsZA7ke5vXm7Qm0sidzZCaQq2Uc2LDV1SxknY2g1GIPQ5TisJGcZCAZB60ZAGhjBYukgm07wgbYZAMgZDZD