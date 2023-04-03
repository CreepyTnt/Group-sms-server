import chat_dir
import pytextnow
import auth
import time


client = pytextnow.Client(auth.username, auth.sid, auth.csrf)
#client.send_sms(auth.test_num, 'testing') 


def send(number, text):
    client.send_sms(number, text) 
    print (text + ' to ' + number)







def ask(number, question, timeout=60, default="error.txt", advanced=False):

    timer_timeout = time.perf_counter()
    client.send_sms(number, question)

    while time.perf_counter() - timer_timeout <= timeout:
        time.sleep(1)
        new_messages = client.get_unread_messages()

        for message in new_messages:

            if message.number == message.number:
                message.mark_as_read()
                if advanced:
                    return message
                else:
                    return message.content

    # timeout error messages

    time.sleep(1)
    if default != "":
        client.send_sms(number, f'ERROR:TIMEOUT. User took too long to respond. Default response: {default}.')
    else:
        client.send_sms(number, "ERROR:TIMEOUT. User took too long to respond. Please use command again to retry.")

    return default






    


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

        if str.lower(msg_content)[0] == '!':
            if str.lower(msg_content) == '!create':

                path = auth.save_dir + ask(msg_num, 'Please enter a name for your group.') + '.txt'

                f = open (path, 'w')
                f.writelines(msg_num)
                client.send_sms(msg_num, 'Group created')
            elif str.lower(msg_content) == 'help':
                client.send_sms(msg_num, 'current commands are !help, !create.') #more commands will include message, delete group, remove from group, leave group, setup(to change you display name in chats), and lookup by number.
            
            elif str.lower(msg_content) == '!add':
                path = auth.save_dir + ask(msg_num, 'Please enter a name of your group.') + '.txt'

                f = open(path, 'r')
                if msg_num in f or '+1' + msg_num in f:
                    f.close()

                    f = open (path, 'w')
                    f.writelines('\n')
                    f.writelines(ask(msg_num, 'please enter the phone number of the person you would like to add.'))
                    client.send_sms(msg_num, 'added to group')
                    f.close()
                else:
                    client.send_sms(msg_num, 'You can only add people to groups you are in.')




        else:
            client.send_sms(msg_num, 'invalid command, please use !help for list of commands')    
        
        
        
        
        
        
        
        #for i in test[:test.index(msg_num)] + test[test.index(msg_num)+1:]:   #finds others in group chat
            
            #time.sleep(5)
            #print (i)
            #send(i, str(msg_num) + ' said ' + str(msg_content))






