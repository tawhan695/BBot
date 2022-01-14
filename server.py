import requests
import re
# from credentials import username
# https://accounts.google.com/signin
# from credentials import password
# import pyautogui
import pyautogui
import time
import json
import pathlib
import os
pyautogui.FAILSAFE = True



class API():

    def __init__(self):
        super().__init__
        #print('api run')
        self.URL = ''
        
        self.uname = ''
        self.email =''
        self.token =''
        self.day = 0
        #thats all about the code
    def Run(self):
        
        s = self.Login()
        #print('status :',s)
    def Login(self):
        exit = False
        status = False
        while True:
            date = 10
            Email =  pyautogui.prompt(text='Login', title='Email' , default='adminbbot@gmail.com')
            #print(Email)
            Pass = pyautogui.password(text='', title='', default='adminbbot', mask='*')
            #print(Pass)
            if Pass != None and Email != None :
                URL = 'https://api.tawhan.xyz'
                session = requests.session()
                front = session.get(URL)
                cookies = session.cookies

                payload = {
                    'username': Email,
                    'password': Pass,
                    'device_name': 'mobile',
                    # device_name
                }
                r = requests.post(URL + '/api/login', data=payload, cookies=cookies)
                #print(r.status_code)
                if r.status_code == 200:
                    jsonResponse = r.json()
                    # #print(jsonResponse)
                    if 'error' in jsonResponse :
                        pyautogui.alert(text='ไม่สามารถเข้าสู่ระบบได้ '+str(jsonResponse['error']), title='แจ้งเตือน', button='OK')
                        con =  pyautogui.confirm(text='แจ้งเตือน', title='แจ้งเตือน', buttons=['Login', 'Exit'])
                        if con == "Exit":
                            break
                    if 'sucess' in jsonResponse :
                        if jsonResponse['sucess'] == True:
                            self.uname = jsonResponse['user']['name']
                            self.email = jsonResponse['user']['email']
                            self.token = jsonResponse['token']
                            self.id = jsonResponse['user']['id']
                            
                            #print('self.uname : ',self.uname)
                            #print('self.uname : ',self.uname)
                            #print('self.email : ',self.email)
                            #print('self.token : ',self.token)
                            token = "Bearer " + self.token
                            headers = {"Authorization": token, 'Accept': 'application/json'}
                            data = {    
                                'id' : self.id,
                                }
                          
                            r2 = requests.post(URL + '/api/getday',data=data, headers=headers,cookies=cookies)
                            if r2.status_code == 200:
                                data = r2.json()  
                                #print(data['days'])
                                pyautogui.alert(text='เวลาคงเหลือ {} วัน'.format(data['days']), title='', button='OK')  
                                if date <= 0:
                                    pyautogui.alert(text='ไม่สามารถใช้งานโปรแกรมได้', title='แจ้งเตือน', button='OK')
                                    exit = True
                                    break
                                else:
                                    exit = True
                                    status = True
                    else:
                        pyautogui.alert(text='ไม่สามารถเข้าสู่ระบบได้ '+str(jsonResponse['error']), title='แจ้งเตือน', button='OK')
                        con =  pyautogui.confirm(text='แจ้งเตือน', title='แจ้งเตือน', buttons=['Login', 'Exit'])
                        if con == "Exit":
                            break
                else :
                    pyautogui.alert(text='status_code {} : {} '.format(r.status_code,jsonResponse), title='', button='OK')  
                    
            else:
                pyautogui.alert(text='ไม่สามารถเข้าสู่ระบบได้', title='แจ้งเตือน', button='OK')
                # pyautogui.alert(text='ไม่สามารถเข้าสู่ระบบได้ '+str(jsonResponse['error']), title='แจ้งเตือน', button='OK')
                if 'error' in jsonResponse :
                    con =  pyautogui.confirm(text='แจ้งเตือน', title='แจ้งเตือน', buttons=['Login', 'Exit'])
                    if con == "Exit":
                        break
            if exit == True : break
       
        return True,{'username':self.uname, 'day':self.day}
if __name__ == '__main__':
    app = API()
    app.Run()
    