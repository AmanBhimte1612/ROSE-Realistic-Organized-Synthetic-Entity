import sys 
import os 

from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2 import *
from ui_path import *
# from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect('manager.db')
cursor = conn.cursor()


class Main_p_Window(QMainWindow):
     def __init__(self):
         QMainWindow.__init__(self)
         self.pi =Ui_PMainWindow()
         self.pi.setupUi(self) 
         self.pi.tableWidget.setColumnWidth(0, 100)
         self.pi.tableWidget.setColumnWidth(1, 600)         
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
         
         self.pi.centralwidget.setGraphicsEffect(self.shadow)
         
         #set window icon
         #this ico and title will not appear on our app main window
         
         self.setWindowIcon(QtGui.QIcon(":/icon/icons/char1.png"))
         
         
         #set window tittle
         
         self.setWindowTitle("Sam UI")
         
         #window size grip        
         
         #minimize window
         
         self.pi.minimize_window_button.clicked.connect(lambda:self.showMinimized())
         
         #close window
         self.pi.close_windowbutton.clicked.connect(lambda:self.close())
        
         
         #restore button
         self.pi.restore_window_button.clicked.connect(lambda:self.restore_or_maiximize_window())
         
         def moveWindow(e):
             if self.isMaximized()==False:
                 #move window when sixe is normal
                 
                 if e.buttons()==Qt.LeftButton:
                     self.move(self.pos()+ e.globalPos() - self.clickPosition)
                     self.clickPosition = e.globalPos()
                     e.accept()
                              
                     
         self.pi.Header.mouseMoveEvent = moveWindow     
         self.pi.Submit_btn.clicked.connect(lambda:self.submit())  
         self.pi.delete_btn.clicked.connect(lambda:self.delete())     
         self.pi.view_btn.clicked.connect(lambda:self.loaddata())     
         self.pi.reset_btn.clicked.connect(lambda:self.reset())     
         self.pi.search_btn.clicked.connect(lambda:self.search())          
         self.pi.update_btn.clicked.connect(lambda:self.update())       
         self.pi.tableWidget.selectionModel().selectionChanged.connect(self.select) 
           
         self.pi.open_close_side_bar_btn.clicked.connect(lambda: self.Side_Menu_Def_0())              
         self.loaddata()          
         self.show()
         
          
     
     def Side_Menu_Def_0(self):
         if self.pi.side_container.width() <= 50 :
            self.pi.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/OPT_DONE.png"))
            self.animation1 = QtCore.QPropertyAnimation(self.pi.side_container,b"maximumWidth")
            self.animation1.setDuration(250)
            self.animation1.setStartValue(0)
            self.animation1.setEndValue(300)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation1.start()
            
            self.animation2 = QtCore.QPropertyAnimation(self.pi.side_container, b"minimumWidth")
            self.animation2.setDuration(250)
            self.animation2.setStartValue(0)
            self.animation2.setEndValue(300)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()
         else:
            self.pi.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/OPT_ADD.png"))
            self.animation1 = QtCore.QPropertyAnimation(self.pi.side_container, b"maximumWidth")
            self.animation1.setDuration(100)
            self.animation1.setStartValue(300)
            self.animation1.setEndValue(0)
            self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutSine)
            self.animation1.start()
            
            self.animation2 = QtCore.QPropertyAnimation(self.pi.side_container, b"minimumWidth")
            self.animation2.setDuration(100)
            self.animation2.setStartValue(300)
            self.animation2.setEndValue(0)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutSine)
            self.animation2.start()
            
        
         
     def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()
        
          
     def restore_or_maiximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.pi.restore_window_button.setIcon(QtGui.QIcon(u":/icons/max.png"))
            
        else:
            self.showMaximized()
            self.pi.restore_window_button.setIcon(QtGui.QIcon(u":/icons/max.png"))
      
     def select(self):
         global  r ,t
        
         selected_items = self.pi.tableWidget.selectedItems()
         t = self.pi.tableWidget.currentColumn ()
         for item in selected_items:
            r = item.text()
            break
         print(r)
         print(t)
    
         if t == 0:
            self.reset()
            connection= sqlite3.connect("manager.db")
            query=f"SELECT * FROM PATH WHERE NAME LIKE '%{r}%'"
 
            result = connection.execute(query)
            
            for row_data in result:
                self.reset()
                self.pi.f_name_input.setText(row_data[0])
                self.pi.l_name_input.setText(row_data[1])
            
            connection.close()
         elif t == 1:
            self.reset()
            connection= sqlite3.connect("manager.db")
            query=f"SELECT * FROM PATH WHERE PATH LIKE '%{r}%'"

            result = connection.execute(query)
            
            for row_data in result:
                self.reset()
                self.pi.f_name_input.setText(row_data[0])
                self.pi.l_name_input.setText(row_data[1])
                
            connection.close()
         
     
     def delete(self):
         R=r
         T=t
         if T == 0:  
             J=self.pi.f_name_input.text()
            
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f'''DELETE FROM PATH WHERE NAME = '{R}' ''')
             conn.commit()
             conn.close()
   
         elif T == 1:
             J=self.pi.l_name_input.text()
           
             conn = sqlite3.connect('manager.db')
             cursor = conn.cursor()
             cursor.execute(f"DELETE FROM PATH WHERE PATH = '{R}'")
             conn.commit()
             conn.close()
       
            
         self.loaddata()

     
     def search(self):
        search_key=self.pi.search_input.text()
        if search_key != "":
            try:
            
                self.reset()
                conn = sqlite3.connect('manager.db')
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM PATH WHERE NAME LIKE '%{search_key}%'")
                son = cursor.fetchall()
                son=son[0]
                self.pi.f_name_input.setText(son[0])
                self.pi.l_name_input.setText(son[1])
                               
            except:
                pass 
                
     def submit(self):
         self.Database()
         global fname
         global lname
         global cont_act
         global E_mail
         
         name = self.pi.f_name_input.text()
         path = self.pi.l_name_input.text()

         
         conn.execute(f"INSERT INTO PATH (NAME,PATH) VALUES ('{name}','{path}');")
         conn.commit()
      
         self.loaddata()
     
       
     def reset(self):
         self.pi.f_name_input.clear()
         self.pi.l_name_input.clear()
     
     def loaddata(self):
             self.Database()
             connection= sqlite3.connect("manager.db")
             query="SELECT * FROM PATH"
             result = connection.execute(query)
             self.pi.tableWidget.setRowCount(0)
             for row_number, row_data in enumerate(result):
                 self.pi.tableWidget.insertRow(row_number)
                 for column_number,data in enumerate(row_data):
                     self.pi.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
             connection.close()
    
    
     def Database(self):
        global conn, cursor
        #creating contact database
        conn = sqlite3.connect("manager.db")
        cursor = conn.cursor()
        #creating REGISTRATION table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS PATH (NAME TEXT, PATH TEXT)")                 


if __name__=="__main__":
    app =QApplication(sys.argv)
    window = Main_p_Window()
    sys.exit(app.exec_())
    
    