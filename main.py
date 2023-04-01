import sms
import chat_dir
import pytextnow
import auth
import time


client = pytextnow.Client(username=auth.username, sid_cookie=auth.sid, csrf_cookie=auth.csrf)
#client.send_sms(auth.test_num, 'testing') 

def send(number, message):
    client.send_sms(number, message) 
    print (message + ' to ' + number)





sms.send(auth.test_num, 'group sms server started')

test = chat_dir.test_group


while True:
    time.sleep(5)
    new_messages = client.get_unread_messages()
    for message in new_messages:
        time.sleep(5)
        message.mark_as_read()
        print(message) # message.content or message.number


        for i in test[:test.index(message.number)] + test[test.index(message.number)+1:]:   #finds others in group chat
            time.sleep(5)
            sms.send(i, message.number + 'said' + '"' + message.content + '"')
            



