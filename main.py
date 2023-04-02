import chat_dir
import pytextnow
import auth
import time


client = pytextnow.Client(auth.username, auth.sid, auth.csrf)
#client.send_sms(auth.test_num, 'testing') 


def send(number, text):
    client.send_sms(number, text) 
    print (text + ' to ' + number)




send(auth.test_num, 'group sms server started')

test = chat_dir.test_group


while True:
    time.sleep(5)
    new_messages = client.get_unread_messages()
    for message in new_messages:
        time.sleep(5)
        message.mark_as_read()
        print(message) # message.content or message.number
        msg_num = message.number; msg_content = message.content

        for i in test[:test.index(msg_num)] + test[test.index(msg_num)+1:]:   #finds others in group chat
            
            time.sleep(5)
            print (i)
            send(i, str(msg_num) + ' said ' + str(msg_content))






