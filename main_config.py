
import sys 
import os 

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2 import *
from ui_config import *
# from windows import ui_config
import sqlite3


class Main_cf_Window(QMainWindow):
     def __init__(self):
         QMainWindow.__init__(self)
         self.ui =Ui_MainWindow()
         self.ui.setupUi(self) 
        
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
         
         
         #minimize window
         
         self.ui.minimize_window_button.clicked.connect(lambda:self.showMinimized())
         
         #close window
         self.ui.close_windowbutton.clicked.connect(lambda:self.close())

         
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
         self.ui.apply_btn.clicked.connect(lambda:self.apply_fun())     
         self.ui.ok_btn.clicked.connect(lambda:self.ok_fun())     
         self.ui.cancel_btn.clicked.connect(lambda:self.close())     
         self.load()  
         self.show()           
       
        
     def __del__(self):
        sys.stdout = sys.__stdout__
 
     def check_radio_button(self):
         global gender
         if self.ui.male_btn.isChecked():
            gender="sir"
         elif self.ui.female_btn.isChecked():
            gender="mam"
         elif self.ui.nick_btn.isChecked():
            gender= self.ui.nick_name.text()
         else :
            gender="sir"
        
        
            

     def apply_fun(self):
         self.Database()
         global fullname
         global nickname
         global contact
         global Email
         
         self.check_radio_button()
         
         fullname = self.ui.full_name.text()
         nickname = self.ui.nick_name.text()
         contact = self.ui.contact_no.text()
         Email= self.ui.E_mail.text()
         paass= self.ui.password.text()
         gender1=gender
         conn.execute(f"DELETE FROM CONFIG")
         conn.execute(f"INSERT INTO CONFIG (FULLNAME,NICKNAME,CONTACT,EMAIL,PASSWORD,GENDER) VALUES ('{fullname}','{nickname}','{contact}','{Email}','{paass}','{gender1}');")
         conn.commit()
         conn.close()
         self.load()
     
     def ok_fun(self):
         self.apply_fun()
         self.close()
         

      
     def Database(self):
        global conn, cursor
        #creating contact database
        conn = sqlite3.connect("manager.db")
        cursor = conn.cursor()
        #creating REGISTRATION table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS CONFIG (FULLNAME TEXT, NICKNAME TEXT, CONTACT INTEGER,EMAIL TEXT,PASSWORD TEXT,GENDER TEXT)")                 

     
     def load(self):
         self.Database()
         connection= sqlite3.connect("manager.db")
         query=f"SELECT * FROM CONFIG"

         result = connection.execute(query)
         gender="ohyea"
         for row_data in result:
            self.ui.full_name.setText(str(row_data[0]))
            self.ui.nick_name.setText(str(row_data[1]))
            self.ui.contact_no.setText(str(row_data[2]))
            self.ui.E_mail.setText(str(row_data[3]))
            self.ui.password.setText(str(row_data[4]))
            gender= str(row_data[5])
           
         if gender=="sir":
            self.ui.male_btn.setChecked(True)
            self.ui.female_btn.setChecked(False)
            self.ui.nick_btn.setChecked(False)
         elif gender=="mam":
            self.ui.male_btn.setChecked(False)
            self.ui.female_btn.setChecked(True)
            self.ui.nick_btn.setChecked(False)
         else:
            self.ui.male_btn.setChecked(False)
            self.ui.female_btn.setChecked(False)
            self.ui.nick_btn.setChecked(True)   
                 
         connection.close()
         
     
          
     def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
        
          
     def restore_or_maiximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icon/icons/max.png"))
            
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icon/icons/restore.png"))
                      

if __name__=="__main__":
    app =QApplication(sys.argv)
    window = Main_cf_Window()
    sys.exit(app.exec_())
    
    
 