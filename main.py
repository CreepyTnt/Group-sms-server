import os
import pytextnow
import auth
import time
import json


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

                try:#check if file already exsists
                    f = open(path, 'r')
                    f.close()
                    client.send_sms(msg_num, 'That chat already exsists')
                except:
                    f = open (path, 'w')
                    group = msg_num
                    f.write(json.dumps([group]))
                    f.close()
                    client.send_sms(msg_num, 'Group created')


            elif str.lower(msg_content) == 'help':
                client.send_sms(msg_num, 'current commands are !help, !create.') #more commands will include message, delete group, remove from group, leave group, setup(to change you display name in chats), and lookup by number.
            
            elif str.lower(msg_content) == '!add':
                path = auth.save_dir + ask(msg_num, 'Please enter a name of your group.') + '.txt'
                if os.path.exists(path):
                    f = open(path, 'r')
                    group = json.loads(f.read())
                    if msg_num in group or '+1' + msg_num in group:
                        f.close()

                        group.append(ask(msg_num, 'please enter the number(starting with +1) to add to group'))

                        f = open (path, 'w')
                        print ('file opened')
                        f.writelines(json.dumps(group))
                        
                        client.send_sms(msg_num, 'added to group')
                        
                    else:
                        client.send_sms(msg_num, 'You can only add people to groups you are in.')
                    f.close()

                else:
                    client.send_sms(msg_num, "Chat doesn't exsist")
                
                    

            elif str.lower(msg_content) == '!message':
                path = auth.save_dir + ask(msg_num, 'Please enter the name of your group.') + '.txt'
            
                if os.path.exists(path):
                    f = open(path, 'r')
                    chat = json.loads(f.read())
                    if msg_num in chat:
                        
                        text = ask(msg_num, 'type message')
                        for i in chat:
                            print ('sent ' + text + ' to ' + i)
                            client.send_sms(i, msg_num + ' said: ' + text)
                    else:
                        client.send_sms(msg_num, 'You are not in this group.')

                else:
                    client.send_sms(msg_num, 'Error. Check your spelling in the group chat name.')



            elif str.lower(msg_content) == '!remove':
                path = auth.save_dir + ask(msg_num, 'Please enter the name of the group you would like to leave.') + '.txt'

                if os.path.exists(path):
                    f = open(path, 'r')
                    chat = json.loads(f.read())
                    if msg_num in chat:
                        f.close()
        
                        f = open(path, 'w')
                        f.write(json.dumps(chat.remove(msg_num)))
                        f.close()
                        client.send_sms(msg_num, 'Removed from chat.')
                    else:
                        client.send_sms(msg_num, 'you are not in this chat.')
                else:
                    client.send_sms(msg_num, 'this group doesn not exist.')





            else:
                client.send_sms(msg_num, 'invalid command, please use !help for list of commands')  
                


        else:
            client.send_sms(msg_num, 'invalid command, please use !help for list of commands')  
        
        
        
        
    






