import pytextnow
import auth

client = pytextnow.Client(username=auth.username, sid_cookie=auth.sid, csrf_cookie=auth.csrf)
#client.send_sms(auth.test_num, 'testing') 


def send(number, message):
    client.send_sms(number, message) 
    print (message + ' to ' + number)


    new_messages = client.get_unread_messages()
    for message in new_messages:
        message.mark_as_read()
        print(message) # message.content or message.number
        return(message)


