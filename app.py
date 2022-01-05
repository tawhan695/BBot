import random
import time
import pyautogui
import keyboard
import json
from getmac import get_mac_address
import pathlib
import os

class App():
    def __init__(self):
        super().__init__
        root =str(pathlib.Path(__file__).parent.resolve()).replace("\\", "/")
        self.setting_wallet = False
        self.setting_sign = False
        self.setting_play = False
        self.setting_choose = False
        self.setting_heroes = False
        self.setting_work = False
        self.setting_exit_hero = False
        self.save_ = False
        self.setting_center = False
        self.CD = 1
        self.path = root
        with open(os.path.abspath('{}\config.txt'.format(self.path)).replace("\\", "/"), 'r') as f:
            self.KeySave = json.loads(f.readline())    
    def setPath(self, path):
        self.path = path
    def reset(self):
        self.setting_wallet = False
        self.setting_sign = False
        self.setting_play = False
        self.setting_choose = False
        self.setting_heroes = False
        self.setting_work = False
        self.setting_exit_hero = False
        self.save_ = False
        self.setting_center = False
        self.KeySave = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        with open(os.path.abspath('{}\config.txt'.format(self.path)).replace("\\", "/"), 'w') as f:
                f.write(json.dumps(self.KeySave))
    def run(self):
        print('run..')
        self.Setup()  
        while True:
            self.start_bot()

    def Start_w(self):
        pyautogui.click(self.KeySave[7])
        pyautogui.press('f5') 
        time.sleep(15)
        pyautogui.moveTo(self.KeySave[0])
        time.sleep(1.5)
        pyautogui.click(self.KeySave[0])
        
        time.sleep(15)
        pyautogui.moveTo(self.KeySave[1])
        time.sleep(1.5)
        pyautogui.click(self.KeySave[1])
        
        time.sleep(20)
        pyautogui.moveTo(self.KeySave[2])
        time.sleep(1.5)
        pyautogui.click(self.KeySave[2])
    def start_bot(self):
        self.Start_w()
        while True:
            time.sleep(3)
            pyautogui.moveTo(self.KeySave[3])
            time.sleep(1.5)
            pyautogui.click(self.KeySave[3])
            n = random.randint(2,3)
            for i in range(n):
                print(n)
                n-=1
                time.sleep(1)
            pyautogui.moveTo(self.KeySave[4])
            time.sleep(1.5)
            pyautogui.click(self.KeySave[4])
            n = random.randint(2,3)
            for i in range(n):
                print(n)
                n-=1
                time.sleep(1)
            for i in range(100):
                pyautogui.scroll(-50) 
                pyautogui.moveTo(self.KeySave[5])
                
            time.sleep(1.5)
            pyautogui.moveTo(self.KeySave[5])
            for i in range(50):
                # pyautogui.scroll(-30) 
                pyautogui.moveTo(self.KeySave[5])
                time.sleep(0.1)
                pyautogui.click(self.KeySave[5])
                time.sleep(0.1)
            n = random.randint(2,3)
            for i in range(n):
                print(n)
                n-=1
                time.sleep(1)
            pyautogui.moveTo(self.KeySave[6])
            time.sleep(0.5)
            pyautogui.click(self.KeySave[6])
            time.sleep(2)
            pyautogui.moveTo(self.KeySave[6])
            time.sleep(0.5)
            pyautogui.click(self.KeySave[6])
            time.sleep(2)
            # pyautogui.doubleClick(self.KeySave[6])
            n =60 * self.CD
            h=n-50
            for i in range(n):
                n-=1
                time.sleep(1)
                print('Work in :',n)
                if n == h:
                    h=n-50
                    # pyautogui.click(self.KeySave[6])
            self.Start_w()
            time.sleep(10)
        
    def Setup(self):
         while True:
            if self.save_ == True:
                print('exit setting')
                cd =pyautogui.prompt(text='{} นาที'.format(self.CD), title='ตั้งเวลาพัก "นาที" ' , default='{}'.format(self.CD))
                print(cd, 'นาที')
                self.CD = int(cd)
                break
            setting = pyautogui.confirm(
                'Setting Click.',
                buttons=[
                    'กลางจอเกม :{}'.format(self.setting_center),
                    'เชื่อมต่อวอเล็ต :{}'.format(self.setting_wallet),
                        'เซ็นชื่อ :{}'.format(self.setting_sign),
                        'playGame :{}'.format(self.setting_play),
                        'เลือกฮีโร่ :{}'.format(self.setting_choose),
                        'HEROES :{}'.format(self.setting_heroes),
                        # 'Menu Heroes :{}'.format(self.setting_work),
                        'Work :{}'.format(self.setting_work),
                        'Exit :{}'.format(self.setting_exit_hero),
                        'Reset',
                        'เริ่มเกม',
                        
                        ])
            
            self.chackSetting(setting)
            
    def settingKey(self,index,pos):
        x,y = pos
        self.KeySave[index]=(x,y)
    def chackSetting(self,val):
        if val == 'Reset':
            print('Reset')
            self.reset()
        elif val == 'กลางจอเกม :False' :
            print('กลางจอเกม :True')
            pyautogui.alert(text=' ชื้อเม้าส์ไปตำแหน่ง กลางจอเกม กด alt เพื่อบันทึก ', title='ตั้งค่า Step 0', button='OK')
            keyboard.wait('alt')
            pos = pyautogui.position()
            self.settingKey(7,(pos))
            pyautogui.alert(text='บันทึกแล้ว ', title='Step 0' , button='OK')
            pyautogui.click(pos)
            self.setting_center = True
        elif val == 'เชื่อมต่อวอเล็ต :False' :
            print('เชื่อมต่อวอเล็ต :True')
            pyautogui.alert(text=' ชื้อเม้าส์ไปตำแหน่งเชื่อมต่อวอเล็ต กด alt เพื่อบันทึก ', title='ตั้งค่า Step 1', button='OK')
            keyboard.wait('alt')
            pos = pyautogui.position()
            self.settingKey(0,(pos))
            pyautogui.alert(text='บันทึกแล้ว ', title='Step 1' , button='OK')
            pyautogui.click(pos)
            self.setting_wallet = True          
        elif val == 'เซ็นชื่อ :False':
            pyautogui.alert(text='ชื้อเม้าส์ไปตำแหน่ง ลงชื่อ กด alt เพื่อบันทึก ', title='ตั้งค่า Step 2', button='OK')
            keyboard.wait('alt')
            pos = pyautogui.position()
            self.settingKey(1,(pos))
            pyautogui.alert(text='บันทึกแล้ว ', title='Step 2', button='OK')
            pyautogui.click(pos)
            self.setting_sign = True
        elif val == 'playGame :False':
            pyautogui.alert(text='ชื้อเม้าส์ไปตำแหน่ง playGame กด alt เพื่อบันทึก ', title='ตั้งค่า Step 3', button='OK')
            keyboard.wait('alt')
            pos = pyautogui.position()
            self.settingKey(2,(pos))
            pyautogui.alert(text='บันทึกแล้ว ', title='Step 3', button='OK')
            pyautogui.click(pos)
            self.setting_play  = True
        elif val == 'เลือกฮีโร่ :False':
            pyautogui.alert(text='ชื้อเม้าส์ไปตำแหน่ง เลือกฮีโร่ กด alt เพื่อบันทึก ', title='ตั้งค่า Step 4', button='OK')
            keyboard.wait('alt')
            pos = pyautogui.position()
            self.settingKey(3,(pos))
            pyautogui.alert(text='บันทึกแล้ว ', title='Step 4', button='OK')
            pyautogui.click(pos)
            self.setting_choose  = True
        elif val == 'HEROES :False':
            pyautogui.alert(text='ชื้อเม้าส์ไปตำแหน่ง HEROES กด alt เพื่อบันทึก ', title='ตั้งค่า Step 5', button='OK')
            keyboard.wait('alt')
            pos = pyautogui.position()
            self.settingKey(4,(pos))
            pyautogui.alert(text='บันทึกแล้ว ', title='Step 5', button='OK')
            pyautogui.click(pos)
            self.setting_heroes  = True
        elif val == 'Work :False':
            pyautogui.alert(text='ชื้อเม้าส์ไปตำแหน่ง Work กด alt เพื่อบันทึก ', title='ตั้งค่า Step 6', button='OK')
            keyboard.wait('alt')
            pos = pyautogui.position()
            self.settingKey(5,(pos))
            pyautogui.alert(text='บันทึกแล้ว ', title='Step 6', button='OK')
            pyautogui.click(pos)
            self.setting_work  = True
        elif val == 'Exit :False':
            pyautogui.alert(text='ชื้อเม้าส์ไปตำแหน่ง Exit กด alt เพื่อบันทึก ', title='ตั้งค่า Step 7', button='OK')
            keyboard.wait('alt')
            pos = pyautogui.position()
            self.settingKey(6,(pos))
            time.sleep(2)
            self.settingKey(6,(pos))
            pyautogui.alert(text='บันทึกแล้ว ', title='Step 7', button='OK')
            pyautogui.doubleClick(pos)
            self.setting_exit_hero = True
        elif val == 'เริ่มเกม': 
            self.save_ = True
            with open('config.txt', 'w') as f:
                f.write(json.dumps(self.KeySave))
            
if __name__=='__main__':
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    host_mac = get_mac_address(ip="{}".format(ip))
    if str(host_mac) == '74:40:bb:28:b9:4b' or str(host_mac) ==  'dc:f5:05:da:8c:91' or str(host_mac) ==  '80:91:33:7d:fc:5b':
        # App().setPath(root)
        App().run()
    else:
         pyautogui.alert(text='มึงต้องชื้อโปรแกรมกูก่อน ', title='ไม่ได้ละไอ้สาส', button='OK')
