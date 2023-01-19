import openai

openai.api_key = "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"

import sys 
import os 

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2 import *
from ui_samgui import *

from __ijnit__ import VOICEAssistant
########################################################################
##################importing other windows###############################
########################################################################
from main_cont import Main_c_Window
from main_path import Main_p_Window
from main_config import Main_cf_Window
###################################################################################
###################################################################################
import re
import os
import random
import pprint
import datetime
import requests
import webbrowser
import sys
import urllib.parse  
import pyjokes
import time
import pyautogui
import sqlite3

import wolframalpha
from PIL import Image
from VOICE.config import config


import urllib.request

def check_internet_connection():
  try:
    urllib.request.urlopen('https://www.google.com')
    return True
  except:
    return False

if check_internet_connection():
    import speech_recognition as sr
    import pywhatkit
    
    print('Connected to the internet')
else:
    from vosk import Model, KaldiRecognizer
    import pyaudio

    model = Model("speech\\vosk-model-small-en-us-0.15")
    recognizer = KaldiRecognizer(model, 16000)
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream()
    print('Not connected to the internet')
global master
conn = sqlite3.connect('manager.db')
cursor = conn.cursor()
cursor.execute(f"SELECT GENDER from CONFIG")
master = cursor.fetchall()
master = master[0] 
master1 = master[0]
master= master1
print(master)

obj = VOICEAssistant()

# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello ROSE", "ROSE", "wake up ROSE", "you there ROSE", "time to work ROSE", "hey ROSE",
             "ok ROSE", "are you there"]
GREETINGS_RES = [f"always there for you {master}", f"i am ready {master}",
                 f"your wish my command", f"how can i help you {master}?", f"i am online and ready {master}"]



CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
# =


def speak(text):
    obj.tts(text)


app_id = config.wolframalpha_id

EMAIL=config.EMAIL
PASSWORD=config.PASSWORD
CONTACT=config.sendercontact


def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.command(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak(f"Sorry {master} I couldn't fetch your question's answer. Please try again ")
        return None
    


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak(f"I am ROSE. Online and ready {master}. Please tell me how may I help you")
# if __name__ == "__main__":

# command= "adsf"

class MainThread(QThread):
    output_signal = QtCore.Signal(str)
    speak_signal = QtCore.Signal(str)
    rec_signal = QtCore.Signal(str)
    alert_signal = QtCore.Signal(str)
    
    def __init__(self):
    
        super(MainThread, self).__init__()
        self.running = True
      

    def run(self):
        # self.sta()
        self.TaskExecution()
        
       
    def startup(self):
        self.rec_signal.emit("Initializing R.O.S.E.")
        speak("Initializing ROSE")
        self.rec_signal.emit("Starting all systems applications")
        speak("Starting all systems applications")
        self.rec_signal.emit("Installing and checking all drivers")
        speak("Installing and checking all drivers")
        self.rec_signal.emit("Caliberating and examining all the core processors")
        speak("Caliberating and examining all the core processors")
        self.rec_signal.emit("Checking the internet connection")
        speak("Checking the internet connection")
        self.rec_signal.emit(f"Wait a moment {master}")
        speak(f"Wait a moment {master}")
        self.rec_signal.emit("All drivers are up and running")
        speak("All drivers are up and running")
        self.rec_signal.emit("All systems have been activated")
        speak("All systems have been activated")
        self.rec_signal.emit("Now I am online")
        speak("Now I am online")
        hour = int(datetime.datetime.now().hour)
        # if hour>=0 and hour<=12:
        #     speak("Good Morning")
        # elif hour>12 and hour<18:
        #     speak("Good afternoon")
        # else:
        #     speak("Good evening")
        # c_time = obj.tell_time()
        # speak(f"Currently it is {c_time}")
        # speak("I am ROSE. Online and ready {master}. Please tell me how may I help you")
    
        
    def Listen(self):
        print("")
        self.rec_signal.emit("Listening...OFFLINE")
        print("Listening...vosk")
        print("")

        while True:
            data = stream.read(1024)
            if recognizer.AcceptWaveform(data):
                    text = recognizer.Result()
                    p = text[14:-3]
                    # self.output_signal.emit(f"User Said:{p}")
                    print(f"You Said : {p}")
                    
                    if len(p)>0:
                        return p
                    else:
                        p="Please try again"
                        return p

    def mic_input(self):
        """
        Fetch input from mic
        return: user's voice input as text if true, false if fail
        """
        try:
            r = sr.Recognizer()
            # r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source, duration=1)
            with sr.Microphone() as source:
                self.rec_signal.emit("Listening...")
                print("Listening....")
                r.energy_threshold = 4000
                audio = r.listen(source,timeout=15,phrase_time_limit=5)
            try:
                # self.speak_signal.emit(date)
                print("Recognizing...")
                self.rec_signal.emit("Recognizing...")
                command = r.recognize_google(audio, language='en-in').lower()
                print(f'User said: {command}')
                
            except:
                # self.speak_signal.emit(date)
                self.rec_signal.emit("Please try again")
                print('Please try again')
                command = self.mic_input()
            return command
        except Exception as e:
            print(e)
            print("llllll")
 
            
            
    # def mail(self):
    #     try:
    #         conn = sqlite3.connect('manager.db')
    #         cursor = conn.cursor()
    #         self.alert_signal.emit(f"To:{naam}")
    #         cursor.execute(f"SELECT FNAME from CONTACT")
    #         son = cursor.fetchall()
    #         print(son)
    #         naaam = son[0] 
    #         print(naaam)
    #         naam1 = naaam[0]
    #         print(naaam[0])
    #         if  naaam in son:
    #             cursor.execute(f"SELECT EMAIL from CONTACT WHERE FNAME LIKE '%{naam1}%'")
    #             son = cursor.fetchall()
    #             cont=son[0]
    #             contact=cont[0]
    #             contact_mail=f"{contact}"
    #             print(contact)
                
                
    #             self.speak_signal.emit("what you want put subject on it")
    #             speak("what you want put subject on it")
    #             subject=self.mic_input()
            
        
    #             self.speak_signal.emit("what you want to me to say")
    #             speak("what you want to me to say")
    #             mail_content=self.mic_input()
    #             print(f"con{content}")
    #         else:
    #             mail
    #             self.speak_signal.emit(f"sorry {master} please try again ")
    #             speak(f"sorry {master} please try again ")
                    
    #         #The mail addresses and password
    #         # sender_address = 'amanbhimtessgss@gmail.com'
    #         sender_address = EMAIL
    #         # sender_pass = 'qljwlyafjjnfdiex'
    #         sender_pass = PASSWORD
    #         receiver_address = contact_mail
    #         # mail_content = content
    #         #Setup the MIME
    #         message = MIMEMultipart()
    #         message['From'] = sender_address
    #         message['To'] = receiver_address
    #         message['Subject'] = subject #The subject line
    #         #The body and the attachments for the mail
    #         message.attach(MIMEText(mail_content, 'plain'))
    #         #Create SMTP session for sending the mail
    #         session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    #         session.starttls() #enable security
    #         session.login(sender_address, sender_pass) #login with mail_id and password
    #         text = message.as_string()
    #         session.sendmail(sender_address, receiver_address, text)
    #         session.quit()
    #         self.alert_signal.emit('Mail Sent')    
    #     except:
    #         self.speak_signal.emit(f"Sorry {master}. Couldn't send your mail. Please try again")
    #         speak(f"Sorry {master}. Couldn't send your mail. Please try again")               

    def TaskExecution(self):
        if check_internet_connection():
            pass
        else:
            self.alert_signal.emit("Alert:No internet Connection!!!!!!")
            speak("Please speak in English or connect system to the internet for best experience ")
        # self.startup()

        while True:

            if check_internet_connection():
                command = self.mic_input()
                command=str(command)
            else:
                command = self.Listen()
            # command = sr.Listen()
            # command = obj.mic_input()
            
            self.output_signal.emit(f"User said:{command}")

            # if 'today`s date' in command:
            #     date = obj.tell_me_date()
            #     print(date)
            #     self.speak_signal.emit(date)
            #     speak(date)
###########################################################################################
#####################chat####################################            
            if 'hello ' in command:

                self.speak_signal.emit(f"hello {master} how are you today")
                speak(f"hello {master} how are you today")

            elif 'how are you' in command:
                self.speak_signal.emit("I am fine, Thank you")
                speak("I am fine, Thank you")
                self.speak_signal.emit(f"How are you, {master}")
                speak(f"How are you, {master}")
                

            elif 'fine' in command or "good" in command:
               self.speak_signal.emit("It's good to know that your fine")  
               speak("It's good to know that your fine")  

            elif "who made you" in command or "who created you" in command:
                self.speak_signal.emit("I have been created by Aman.")
                speak("I have been created by Aman.")

            elif "who i am" in command:
                self.speak_signal.emit("If you talk then definitely your human.")
                speak("If you talk then definitely your human.")

            elif "why you came to world" in command:
                self.speak_signal.emit("Thanks to Aman. further It's a secret")
                speak("Thanks to Aman. further It's a secret")

            elif 'is love' in command:
                self.speak_signal.emit("It is 7th sense that destroy all other senses")
                speak("It is 7th sense that destroy all other senses")

            elif "who are you" in command:
                self.speak_signal.emit("I am your virtual assistant created by Aman")
                speak("I am your virtual assistant created by Aman")

            elif 'reason for you' in command:
                self.speak_signal.emit("I was created as a Minor project by Mister  Aman")
                speak("I was created as a Minor project by Mister  Aman")

            elif "will you be my gf" in command or "will you be my bf" in command:
                self.speak_signal.emit("I'm not sure about, may be you should give me some time")
                speak("I'm not sure about, may be you should give me some time")
            
                    
            elif "i love you" in command:
                self.speak_signal.emit("It's hard to understand")
                speak("It's hard to understand")

####################################################

            elif "time now" in command:
                time_c = obj.tell_time()
                print(time_c)
                self.speak_signal.emit(f"{master} the time is {time_c}")
                speak(f"{master} the time is {time_c}")

            elif re.search('launch', command):
                dict_app = {
                    'chrome': 'C:/Program Files/Google/Chrome/Application/chrome'
                }

                app = command.split(' ', 1)[1]
                path = dict_app.get(app)

                if path is None:
                    speak('Application path not found')
                    print('Application path not found')

                else:
                    speak(f'Launching: ' + app + 'for you {master}!')
                    obj.launch_any_app(path_of_app=path)

            elif command in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            elif re.search('open', command):
                
                if check_internet_connection():
                    domain = command.split(' ')[-1]
                    open_result = obj.website_opener(domain)
                    speak(f'Alright {master} !! Opening {domain}')
                    print(open_result)
                else:
                    self.alert_signal.emit('Alert:No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")

            elif re.search('weather', command):
                city = command.split(' ')[-1]
                weather_res = obj.weather(city=city)
                print(weather_res)
                speak(weather_res)

            elif re.search('tell me about', command):
                if check_internet_connection():
                    topic = command.split(' ')[-1]
                    if topic:
                        wiki_res = obj.tell_me(topic)
                        print(wiki_res)
                        speak(wiki_res)
                    else:
                        speak(
                            f"Sorry {master}. I couldn't load your command from my database. Please try again")

                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")

            elif "buzzing" in command or "news" in command or "headlines" in command:
                if check_internet_connection():
                    news_res = obj.news()
                    self.speak_signal.emit("Source: The Times Of India\n Todays Headlines are..")
                    speak('Source: The Times Of India')
                    speak('Todays Headlines are..')
                    for index, articles in enumerate(news_res):
                        pprint.pprint(articles['title'])
                        self.speak_signal.emit(articles['title'])
                        speak(articles['title'])
                        if index == len(news_res)-2:
                            break
                    self.speak_signal.emit(f'These were the top headlines, Have a nice day {master}!!..')
                    speak(f'These were the top headlines, Have a nice day {master}!!..')
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")


            elif 'search google for' in command:
                if check_internet_connection():
                    obj.search_anything_google(command)
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")

                
            
            elif "play music" in command or "hit some music" in command:
                music_dir = "D://download//Music//Jap"
                songs = os.listdir(music_dir)
                rd=random.choice(songs)
                os.startfile(os.path.join(music_dir,rd))

            elif 'youtube' in command:
                if check_internet_connection():
                    video = command.split(' ')[1]
                    print(video)
                    speak(f"Okay {master}, playing {video} on youtube")
                    self.speak_signal.emit(f"Okay {master}, playing {video} on youtube")
                    pywhatkit.playonyt(video)
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")

            elif "send mail to " in command or "send email to " in command:
                original_string = command
                split_string = original_string.split(" to ")
                global naam
                naam = split_string[1]

                if check_internet_connection():
                    self.mail()
                try:
                        
                    conn = sqlite3.connect('manager.db')
                    cursor = conn.cursor()
                    self.alert_signal.emit(f"To:{naam}")
                    cursor.execute(f"SELECT FNAME from CONTACT")
                    son = cursor.fetchall()
                    print(son)
                    naaam = son[0] 
                    print(naaam)
                    naam1 = naaam[0]
                    print(naaam[0])
                    if  naaam in son:
                        cursor.execute(f"SELECT EMAIL from CONTACT WHERE FNAME LIKE '%{naam1}%'")
                        son = cursor.fetchall()
                        cont=son[0]
                        contact=cont[0]
                        contact_mail=f"{contact}"
                        print(contact)
                        
                        
                        self.speak_signal.emit("what you want put subject on it")
                        speak("what you want put subject on it")
                        subject=self.mic_input()
                    
                
                        self.speak_signal.emit("what you want to me to say")
                        speak("what you want to me to say")
                        mail_content=self.mic_input()
                        print(f"con{content}")
                    else:
                        mail
                        self.speak_signal.emit(f"sorry {master} please try again ")
                        speak(f"sorry {master} please try again ")
                            
                    #The mail addresses and password
                    # sender_address = 'amanbhimtessgss@gmail.com'
                    sender_address = EMAIL
                    # sender_pass = 'qljwlyafjjnfdiex'
                    sender_pass = PASSWORD
                    receiver_address = contact_mail
                    # mail_content = content
                    #Setup the MIME
                    message = MIMEMultipart()
                    message['From'] = sender_address
                    message['To'] = receiver_address
                    message['Subject'] = subject #The subject line
                    #The body and the attachments for the mail
                    message.attach(MIMEText(mail_content, 'plain'))
                    #Create SMTP session for sending the mail
                    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
                    session.starttls() #enable security
                    session.login(sender_address, sender_pass) #login with mail_id and password
                    text = message.as_string()
                    session.sendmail(sender_address, receiver_address, text)
                    session.quit()
                    self.alert_signal.emit('Mail Sent')    
                except:
                    self.speak_signal.emit(f"Sorry {master}. Couldn't send your mail. Please try again")
                    speak(f"Sorry {master}. Couldn't send your mail. Please try again")
                            
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")

                
            elif "calculate" in command:
                if check_internet_connection():
                    question = command
                    answer = computational_intelligence(question)
                    speak(answer)
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")

               
            
            elif "what is" in command or "who is" in command:
                if check_internet_connection():
                    question = command
                    answer = computational_intelligence(question)
                    speak(answer)
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")
                
            # elif "what do i have" in command or "do i have plans" or "am i busy" in command:
            #     obj.google_calendar_events(command)

            if "make a note" in command or "write this down" in command or "remember this" in command:
                speak("What would you like me to write down?")
                note_text = obj.mic_input()
                obj.take_note(note_text)
                speak("I've made a note of that")

            elif "close the note" in command or "close notepad" in command:
                speak(f"Okay {master}, closing notepad")
                os.system("taskkill /f /im notepad++.exe")

            elif "some joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "system" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)

            elif "where is" in command:
                if check_internet_connection():
                    place = command.split('where is ', 1)[1]
                    current_loc, target_loc, distance = obj.location(place)
                    city = target_loc.get('city', '')
                    state = target_loc.get('state', '')
                    country = target_loc.get('country', '')
                    time.sleep(1)
                    try:

                        if city:
                            res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                            print(res)
                            speak(res)

                        else:
                            res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                            print(res)
                            speak(res)

                    except:
                        res = "Sorry {master}, I couldn't get the co-ordinates of the location you requested. Please try again"
                        speak(res)
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")
                

            elif "ip address" in command:
                if check_internet_connection():
                    print(ip)
                    speak(f"Your ip address is {ip}")
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")
                ip = requests.get('https://api.ipify.org').text
                
            elif "switch the window" in command or "switch window" in command:
                speak(f"Okay {master}, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "where i am" in command or "current location" in command or "where am i" in command:
                if check_internet_connection():
                    try:
                        city, state, country = obj.my_location()
                        print(city, state, country)
                        speak(
                            f"You are currently in {city} city which is in {state} state and country {country}")
                    except Exception as e:
                        speak("Sorry {master}, I coundn't fetch your current location. Please try again")
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")
                

            elif "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                speak("By what name do you want to save the screenshot?")
                name = obj.mic_input()
                speak(f"Alright {master}, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")

            elif "show me the screenshot" in command:
                try:
                    img = Image.open('D://ROSE//ROSE_2.0//' + name)
                    img.show(img)
                    speak("Here it is {master}")
                    time.sleep(2)

                except IOError:
                    speak(f"Sorry {master}, I am unable to display the screenshot")

            elif "hide all files" in command or "hide this folder" in command:
                os.system("attrib +h /s /d")
                speak(f"{master}, all the files in this folder are now hidden")

            elif "visible" in command or "make files visible" in command:
                os.system("attrib -h /s /d")
                speak(f"{master}, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

            # if "calculate" in command or "what is" in command:
            #     command = command
            #     answer = computational_intelligence(command)
            #     speak(answer) 

            elif "goodbye" in command or "offline" in command or "bye" in command:
                speak("Alright {master}, going offline. It was nice working with you")
                break
            
            elif "Question is " in command:
                if check_internet_connection():
                    command=command.split(' ')[2]
                    print(command)
                    ask = command
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=ask,
                        temperature=0.9,
                        max_tokens=150,
                        top_p=1,
                        frequency_penalty=0,
                        presence_penalty=0.6,
                        stop=[" Human:", " AI:"]
                        )
                    text = response['choices'][0]['text']
                    self.speak_signal.emit(text)
                    speak(text)
                    print ('Reply: '+text)
                else:
                    self.alert_signal.emit('Alert: No internet Connection!!!!!!')
                    speak("please connect to internet to use this function")
                
    
    # def sta(self):
    #     startup()
       
    #     if __name__=="__main__":
    #       speak(f"hello {master}")
    #       #   TaskExecution()
    #       while True:
    #            permission = obj.mic_input()
    #            if 'sam wake up' in permission or 'sam you here' in permission or 'sam you there' in permission :
    #                 speak(f"Yes {master} ,how can i help you")
    #                 TaskExecution()
    #            elif'you can turn off' in permission or 'you can turn it off' in permission:
    #                 sys.exit()


startExecution = MainThread()


class MainWindow(QMainWindow):
     def __init__(self):
         QMainWindow.__init__(self)
         self.ui =Ui_MainWindow()
         self.ui.setupUi(self) 
         
         self.ui.run_btn.clicked.connect(self.startTask)
         self.ui.termi_btn.clicked.connect(self.endTask)
         
         # remove window tittle bar 
         self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
         #  set main backgroundto transparent
         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
         # shadow effect style
        
         self.shadow = QGraphicsDropShadowEffect(self)
         self.shadow.setBlurRadius(50)
         self.shadow.setXOffset(0)
         self.shadow.setYOffset(0)
         self.shadow.setColor(QColor(0,92,157,550))
         
         #appy shadow to central  widget 
         
         self.ui.centralwidget.setGraphicsEffect(self.shadow)
         
         #set window icon
         #this ico and title will not appear on our app main window
         
         self.setWindowIcon(QtGui.QIcon(":/icon/icons/char1.png"))
         
         
         #set window tittle
         
         self.setWindowTitle("Sam UI")
         
         #window size grip
         
         QSizeGrip(self.ui.size_grip)
         
         #minimize window
         
         self.ui.minimize_window_button.clicked.connect(lambda:self.showMinimized())
         
         #close window
         self.ui.close_windowbutton.clicked.connect(lambda:self.close())
         self.ui.exit_button.clicked.connect(lambda:self.close())
         
         #restore button
        
         self.ui.restore_window_button.clicked.connect(lambda:self.restore_or_maiximize_window())
         
         def moveWindow(e):
             if self.isMaximized()==False:
                 #move window when sixe is normal
                 
                 if e.buttons()==Qt.LeftButton:
                     self.move(self.pos()+ e.globalPos() - self.clickPosition)
                     self.clickPosition = e.globalPos()
                     e.accept()
           
           
                   
                     
         self.ui.header_frame.mouseMoveEvent = moveWindow
                     
                   
         startExecution.output_signal.connect(self.display_output)
         startExecution.speak_signal.connect(self.speak_output)
         startExecution.rec_signal.connect(self.rec_output)
         startExecution.alert_signal.connect(self.rec_output)
         self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.Side_Menu_Def_0())              

         self.ui.cont_but.clicked.connect(lambda:self.cont())
         self.ui.path_but.clicked.connect(lambda:self.pat())
         self.ui.config_but.clicked.connect(lambda:self.conf())
         self.ui.instagram_btn.clicked.connect(lambda:self.insta())
         self.ui.facebook_btn.clicked.connect(lambda:self.face_())
                  
         self.show()
         
     
     
     
     def Side_Menu_Def_0(self):
         if self.ui.slide_menu_container.width() <= 50 :
            self.ui.header_frame.setStyleSheet("border-top-left-radius: 0px; border-top-right-radius: 15px;background-color:rgb(143, 192, 255);")
            self.ui.footer.setStyleSheet("border-bottom-left-radius: none;background-color:rgb(143, 192, 255);")
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":\icon\icons\slide.png"))
            self.animation1 = QtCore.QPropertyAnimation(self.ui.slide_menu_container,b"maximumWidth")
            self.animation1.setDuration(300)
            self.animation1.setStartValue(0)
            self.animation1.setEndValue(200)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()
            
            self.animation2 = QtCore.QPropertyAnimation(self.ui.slide_menu_container, b"minimumWidth")
            self.animation2.setDuration(300)
            self.animation2.setStartValue(0)
            self.animation2.setEndValue(200)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
         else:
             
            self.ui.header_frame.setStyleSheet("border-top-left-radius: 15px; border-top-right-radius: 15px;background-color:rgb(143, 192, 255);")
            self.ui.footer.setStyleSheet("border-bottom-left-radius: 15px;background-color:rgb(143, 192, 255);")

            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":\icon\icons\opt2.png"))
            self.animation1 = QtCore.QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")
            self.animation1.setDuration(100)
            self.animation1.setStartValue(200)
            self.animation1.setEndValue(0)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
            self.animation1.start()
            
            self.animation2 = QtCore.QPropertyAnimation(self.ui.slide_menu_container, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(200)
            self.animation2.setEndValue(0)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
            self.animation2.start()
            
         
     
     def __del__(self):
        sys.stdout = sys.__stdout__

     def startTask(self):
         startExecution.running = True
         startExecution.start()
         
     def endTask(self):
         startExecution.running = False
         self.ui.sam_text.setText("task ended")
   

     def cont(self):
         self.window1 = QtWidgets.QMainWindow()
         self.cui=Main_c_Window()
         self.cui.setupUi(self.window1)
         self.window1.show()
     def conf(self):
         self.window3 = QtWidgets.QMainWindow()
         self.cfui=Main_cf_Window()
         self.cfui.setupUi(self.window3)
         self.window3.show()
         
     def insta(self):
         webbrowser.open("https://www.instagram.com/yujin_a.rts/")
         
     def face_(self):
         webbrowser.open("https://www.facebook.com/aman.bhimte.71/")
         
    #  def mail_(self):
    #      webbrowser.open("")
     def pat(self):
         self.window2 = QtWidgets.QMainWindow()
         self.pui=Main_p_Window()
         self.pui.setupUi(self.window2)
         self.window2.show()
         
         
     def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
        
     def display_output(self, output):
        self.ui.user_said_text.clear()  # Append the output to the text browser
        self.ui.user_said_text.append(output)
     def speak_output(self, output):
        self.ui.user_said_text.clear()  # Append the output to the text browser
        self.ui.user_said_text.append(output)
     def rec_output(self, output):
        self.ui.sam_text.clear()  # Append the output to the text browser
        self.ui.sam_text.append(output)
     def alert_output(self, output):
        self.ui.sam_text.clear()  # Append the output to the text browser
        self.ui.sam_text.append(output)
             
     def restore_or_maiximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icon/icons/max.png"))
            
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icon/icons/restore.png"))
                      

if __name__=="__main__":
    app =QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    
    
 