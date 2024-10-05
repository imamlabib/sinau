import pyautogui as  auto
import time

time.sleep(10)

kirim_sebanyak = 50

# modul spam
print('[+] SPAM DALAM wAKTU 10 DETIK')

for i in range(kirim_sebanyak):
    i = i+1
    
    # modul spam
    auto.write('ping')
    time.sleep(0.1)
    auto.press('enter')
    time.sleep(0.1)     