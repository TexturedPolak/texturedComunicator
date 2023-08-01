import eel
import redis
from cryptography.fernet import Fernet
global messages #tu przechowujemy wiadomości
messages="<br>"
#komunikacja z bazą danych
redisHost="tc.inf1b.tk"
redisUsername="beta"
redisPassword="betatesterna100"
redisClient = redis.Redis(host=redisHost,port=40434,db=0,decode_responses=True,username=redisUsername,password=redisPassword)
key="TfiyXJmNXNiZ-nTlyHBb62AHs4VMA7mNddyayIBMV80="
#uruchomienie modulu eel  
eel.init("web")  
#Zinterpretowanie funkcji używanych przez js
#Funkcja wysyłająca wiadomość
#funkcja wyswietlajaca ostanio wyslane wiadomosci
@eel.expose
def getLastMessages():
    global messages
    global lastMessage
    global key
    lastMessage = int(redisClient.get('lastKey'))
    showedMessage=1
    while showedMessage <= lastMessage:
        #decrypt
        messages+=Fernet(key).decrypt(redisClient.get(str(showedMessage)).encode()).decode()+"<br>"
        showedMessage+=1
    return messages
@eel.expose
def getNewMessages():
    global messages
    global lastMessage
    global key
    lastDatabaseMessage=int(redisClient.get('lastKey'))
    if lastDatabaseMessage!=lastMessage:
        lastMessage+=1
        while lastMessage <=lastDatabaseMessage:
            #decrypt
            messages+=Fernet(key).decrypt(redisClient.get(str(lastMessage)).encode()).decode()+"<br>"
            lastMessage+=1
        lastMessage=lastDatabaseMessage
        eel.getNewMessages(messages)
        return 0
    else:
        return 0
@eel.expose
def sendMessage(message):
    global key
    lastDatabaseMessage=int(redisClient.get('lastKey'))
    #encrypt
    redisClient.set(name=str(lastDatabaseMessage+1),value=Fernet(key).encrypt(message.encode()).decode())
    redisClient.set(name="lastKey",value=str(lastDatabaseMessage+1))
#Uruchomienie przeglądarki użytkownika
eel.start("index.html",block=False)
eel.sleep(5.0)
while True:
    getNewMessages()
    eel.sleep(0.5) 