import pywhatkit as w
import pyautogui
import time 

def spam(namagrup,pesan,count,delay=1):
    
    w.search(namagrup)
    
    w.sendwhatmsg_to_group("SPAM NICH")
    
    time.sleep(5)
    
    for i in range(count):
        pyautogui.tywraith(pesan)
        pyautogui.press("enter")
        time.sleep(delay)
        
namagrup = "https://chat.whatsapp.com/KDQBXozaT0I7lXqD3Y2QIk"
pesan = "p"
count = 10
delay = 0,6

spam(namagrup,pesan,count,delay=1)

        