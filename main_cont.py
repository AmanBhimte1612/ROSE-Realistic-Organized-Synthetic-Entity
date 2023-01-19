import sys 
import os 

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2 import *
from ui_CONT1 import *
# from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
global conn,cursor
conn = sqlite3.connect('manager.db')
cursor = conn.cursor()


class Main_c_Window(QMainWindow):
     def __init__(self):
         QMainWindow.__init__(self)
         self.ci =Ui_CMainWindow()
         self.ci.setupUi(self) 
         self.ci.tableWidget.setColumnWidth(0, 100)
         self.ci.tableWidget.setColumnWidth(1, 100)
         self.ci.tableWidget.setColumnWidth(2, 150)
         self.ci.tableWidget.setColumnWidth(3, 400)         
        #  self.ci.tableWidget.setColumnWidth(4, 350)         
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
         
         self.ci.centralwidget.setGraphicsEffect(self.shadow)
         
         #set window icon
         #this ico and title will not appear on our app main window
         
         self.setWindowIcon(QtGui.QIcon(":/icon/icons/char1.png"))
         
         
         #set window tittle
         
         self.setWindowTitle("Sam UI")
         
         #window size grip        
         
         #minimize window
         
         self.ci.minimize_window_button.clicked.connect(lambda:self.showMinimized())
         
         #close window
         self.ci.close_windowbutton.clicked.connect(lambda:self.close())
        
         
         #restore button
         self.ci.restore_window_button.clicked.connect(lambda:self.restore_or_maiximize_window())
         
         def moveWindow(e):
             if self.isMaximized()==False:
                 #move window when sixe is normal
                 
                 if e.buttons()==Qt.LeftButton:
                     self.move(self.pos()+ e.globalPos() - self.clickPosition)
                     self.clickPosition = e.globalPos()
                     e.accept()
                              
                     
         self.ci.Header.mouseMoveEvent = moveWindow     
         self.ci.Submit_btn.clicked.connect(lambda:self.submit())     
         self.ci.delete_btn.clicked.connect(lambda:self.delete())     
         self.ci.view_btn.clicked.connect(lambda:self.loaddata())     
         self.ci.reset_btn.clicked.connect(lambda:self.reset())     
         self.ci.search_btn.clicked.connect(lambda:self.search())          
         self.ci.update_btn.clicked.connect(lambda:self.update())       
         self.ci.tableWidget.selectionModel().selectionChanged.connect(self.select) 
         self.ci.open_close_side_bar_btn.clicked.connect(lambda: self.Side_Menu_Def_0()) 
                    
         self.loaddata()      
         self.show()
         
         
          
     
     def Side_Menu_Def_0(self):
         if self.ci.side_container.width() <= 50 :
            self.ci.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/OPT_DONE.png"))
            self.animation1 = QtCore.QPropertyAnimation(self.ci.side_container,b"maximumWidth")
            self.animation1.setDuration(250)
            self.animation1.setStartValue(0)
            self.animation1.setEndValue(300)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()
            
            self.animation2 = QtCore.QPropertyAnimation(self.ci.side_container, b"minimumWidth")
            self.animation2.setDuration(250)
            self.animation2.setStartValue(0)
            self.animation2.setEndValue(300)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
            self.ci.maintable.setStyleSheet("border-bottom-right-radius: 15px;border-bottom-left-radius: 0px;background-color:rgb(204,229,255)")
         else:
            self.ci.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/OPT_ADD.png"))
            self.animation1 = QtCore.QPropertyAnimation(self.ci.side_container, b"maximumWidth")
            self.animation1.setDuration(100)
            self.animation1.setStartValue(300)
            self.animation1.setEndValue(0)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
            self.animation1.start()
            
            self.animation2 = QtCore.QPropertyAnimation(self.ci.side_container, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(300)
            self.animation2.setEndValue(0)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
            self.animation2.start()
            self.ci.maintable.setStyleSheet("border-bottom-right-radius: 15px;border-bottom-left-radius: 10px;background-color:rgb(204,229,255)")
            
        
         
     def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
     
     def select(self):
         global  r ,t
         selected_items = self.ci.tableWidget.selectedItems()
         t = self.ci.tableWidget.currentColumn ()
         for item in selected_items:
            r = item.text()
            print(r)
            break
    
         if t == 0:
            self.reset()
            connection= sqlite3.connect("manager.db")
            query=f"SELECT * FROM CONTACT WHERE FNAME LIKE '%{r}%'"
 
            result = connection.execute(query)
            
            for row_data in result:
                self.reset()
                self.ci.f_name_input.setText(str(row_data[0]))
                self.ci.l_name_input.setText(str(row_data[1]))
                self.ci.cont_input.setText(str(row_data[2]))
                self.ci.mail_input.setText(str(row_data[3]))
            
            connection.close()
         elif t == 1:
            self.reset()
            connection= sqlite3.connect("manager.db")
            query=f"SELECT * FROM CONTACT WHERE LNAME LIKE '%{r}%'"

            result = connection.execute(query)
            
            for row_data in result:
                self.reset()
                self.ci.f_name_input.setText(str(row_data[0]))
                self.ci.l_name_input.setText(str(row_data[1]))
                self.ci.cont_input.setText(str(row_data[2]))
                self.ci.mail_input.setText(str(row_data[3]))
            
            connection.close()
             
         elif t == 2:
            self.reset()
            connection= sqlite3.connect("manager.db")
            query=f"SELECT * FROM CONTACT WHERE CONTACT LIKE '%{r}%'"

            result = connection.execute(query)
            
            for row_data in result:
                self.reset()
                self.ci.f_name_input.setText(str(row_data[0]))
                self.ci.l_name_input.setText(str(row_data[1]))
                self.ci.cont_input.setText(str(row_data[2]))
                self.ci.mail_input.setText(str(row_data[3]))
            
            connection.close()
         elif t == 3:
            self.reset()
            connection= sqlite3.connect("manager.db")
            query=f"SELECT * FROM CONTACT WHERE EMAIL LIKE '%{r}%'"

            result = connection.execute(query)
            
            for row_data in result:
                self.reset()
                self.ci.f_name_input.setText(str(row_data[0]))
                self.ci.l_name_input.setText(str(row_data[1]))
                self.ci.cont_input.setText(str(row_data[2]))
                self.ci.mail_input.setText(str(row_data[3]))
            
            connection.close()
             
    
     def delete(self):
         R=r
         T=t
         if T == 0:  
             J=self.ci.f_name_input.text()
            
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f'''DELETE FROM CONTACT WHERE FNAME = '{R}' ''')
             conn.commit()
             conn.close()
   
         elif T == 1:
             J=self.ci.l_name_input.text()
           
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f"DELETE FROM CONTACT WHERE LNAME = '{R}'")
             conn.commit()
             conn.close()
       
         elif T == 2:
             J = self.ci.cont_input.text()
          
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f"DELETE FROM CONTACT WHERE CONTACT = '{R}'")
             conn.commit()
             conn.close()
         elif T == 3:
             J = self.ci.mail_input.text()
    
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f"DELETE FROM CONTACT WHERE EMAIL = '{R}'")
             conn.commit()
             conn.close()
            
         self.loaddata()

                    
     def update(self):
         R=r
         T=t
         if T == 0:  
             J=self.ci.f_name_input.text()
            
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f'''UPDATE CONTACT SET FNAME= '{J}' WHERE FNAME = '{R}' ''')
             conn.commit()
             conn.close()
   
         elif T == 1:
             J=self.ci.l_name_input.text()
           
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f"UPDATE CONTACT SET LNAME ='{J}' WHERE LNAME = '{R}'")
             conn.commit()
             conn.close()
       
         elif T == 2:
             J = self.ci.cont_input.text()
          
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f"UPDATE CONTACT SET CONTACT ='{J}' WHERE CONTACT = '{R}'")
             conn.commit()
             conn.close()
         elif T == 3:
             J = self.ci.mail_input.text()
    
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f"UPDATE CONTACT SET EMAIL = '{J}' WHERE EMAIL = '{R}'")
             conn.commit()
             conn.close()
            
         self.loaddata()
                
     
     def search(self):
        search_key=self.ci.search_input.text()
        if search_key != "":
            try:
            
                self.reset()
                conn = sqlite3.connect('manager.db')
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM CONTACT WHERE FNAME LIKE '%{search_key}%'")
                son = cursor.fetchall()
                son=son[0]
                self.ci.f_name_input.setText(son[0])
                self.ci.l_name_input.setText(son[1])
                self.ci.cont_input.setText(son[2])
                self.ci.mail_input.setText(son[3]) 
                               
            except:
                pass 
                
     def restore_or_maiximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ci.restore_window_button.setIcon(QtGui.QIcon(u":/icons/max.png"))
            
        else:
            self.showMaximized()
            self.ci.restore_window_button.setIcon(QtGui.QIcon(u":/icons/max.png"))
      
     def reset(self):
         self.ci.f_name_input.clear()
         self.ci.l_name_input.clear()
         self.ci.cont_input.clear()
         self.ci.mail_input.clear()
      
     def submit(self):
         
         self.Database()
         global fname
         global lname
         global cont_act
         global E_mail
         
         fname = self.ci.f_name_input.text()
         lname = self.ci.l_name_input.text()
         cont_act = self.ci.cont_input.text()
         E_mail= self.ci.mail_input.text()
         
         conn.execute(f"INSERT INTO CONTACT (FNAME,LNAME,CONTACT,EMAIL) VALUES ('{fname}','{lname}','{cont_act}','{E_mail}');")
         conn.commit()
      
         self.loaddata()
         
     def loaddata(self):
         self.reset()
         self.Database()
         self.select()  
         connection= sqlite3.connect("manager.db")
         query="SELECT FNAME,LNAME,CONTACT,EMAIL FROM CONTACT"
         result = connection.execute(query)
         self.ci.tableWidget.setRowCount(0)
         

         for row_number, row_data in enumerate(result):
             self.ci.tableWidget.insertRow(row_number)
             
             for column_number,data in enumerate(row_data):

    
                 self.ci.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
                 
         connection.close()
      
     def Database(self):
        global conn, cursor
        #creating contact database
        conn = sqlite3.connect("manager.db")
        cursor = conn.cursor()
        #creating REGISTRATION table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS CONTACT (FNAME TEXT, LNAME TEXT, CONTACT INTEGER,EMAIL TEXT)")                 


if __name__=="__main__":
    
    app =QApplication(sys.argv)
    window = Main_c_Window()
    sys.exit(app.exec_())
    
    