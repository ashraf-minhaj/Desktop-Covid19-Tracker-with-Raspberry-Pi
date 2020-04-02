"""* Realtime Covid19 International and Local Tracker With Clock *"""

"""
************** Stay Home Stay Safe. Live, let Live *************
"""

"""
author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
site: ashrafminhajfb.blogspot.com
"""

#import necessary libraries
import PyQt5                        #QT GUI Library for python3
from PyQt5.QtCore import Qt, QTimer #timer to update
from PyQt5.QtWidgets import *       #import everything
from PyQt5.QtGui import QFont       #for fonts
import sys                    #necessary for QT applications
#import os
import COVID19Py  #covid19 information -api
import datetime   #you know what this is for


class CoronaTracker(QWidget):
    """main class that contains everything"""
    
    def __init__(self):
        """initialize things"""
        super().__init__()
        
        self.covid = COVID19Py.COVID19()  #initialize
        self.timer = QTimer() #initialize
        
        self.timer.timeout.connect(self.update) #if timer reaches threshold - call update
        
        self.ui()  #user interface


    def ui(self):
        """User Interface section"""
        self.setWindowTitle("Covid19 International and Local Tracker")
        #self.setWindowFlags(Qt.CustomizeWindowHint) #hide title bar
        self.setStyleSheet("Background-color: black")
        self.setFixedSize(640, 480)  #as per my display (x, y) /rpi resolution

        #main label
        self.banner_label = QLabel(self)
        self.banner_label.setGeometry(50, 5, 560, 50)  #(x_origin, y_origin, till_x, till_y)
        self.banner_label.setText("CORONA Pandemic - COVID19 TRACKER")
        self.banner_label.setFont(QFont('SansSerif', 20))
        self.banner_label.setStyleSheet("""
                           background-color: black; 
                           color: white;
                           border-style: outset; 
                           border-width: 1px
                           """)

        """________________________worlds latest data_______________________________________"""
        
        #world label
        self.w = QLabel(self)
        self.w.setGeometry(200, 55, 400, 40)
        self.w.setText("World at a Glance")
        self.w.setFont(QFont('SansSerif', 18))
        self.w.setStyleSheet("""
                           background-color: black; 
                           color: blue; 
                           border-style: outset; 
                           border-width: 1px
                           """)

        #worldwide confirmed cases
        self.w_cases = QLabel(self)
        self.w_cases.setGeometry(5, 90, 100, 40)
        self.w_cases.setText("Cases:")
        self.w_cases.setFont(QFont('SansSerif', 18))
        self.w_cases.setStyleSheet("""
                           background-color: black; 
                           color: orange; 
                           border-style: outset; 
                           border-width: 1px
                           """)
        
        #cases number
        self.w_cases_num = QLabel(self)
        self.w_cases_num.setGeometry(110, 90, 100, 40)
        self.w_cases_num.setFont(QFont('SansSerif', 18))
        self.w_cases_num.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)

        #worldwide deaths 
        self.w_death = QLabel(self)
        self.w_death.setGeometry(350, 90, 100, 40)
        self.w_death.setText("Deaths:")
        self.w_death.setFont(QFont('SansSerif', 18))
        self.w_death.setStyleSheet("""
                           background-color: black; 
                           color: red; 
                           border-style: outset; 
                           border-width: 1px
                           """)
        #death number
        self.w_death_num = QLabel(self)
        self.w_death_num.setGeometry(460, 90, 100, 40)
        self.w_death_num.setFont(QFont('SansSerif', 18))
        self.w_death_num.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)

        #worldwide cured
        self.w_cured = QLabel(self)
        self.w_cured.setGeometry(5, 140, 100, 40)
        self.w_cured.setText("Cured:")
        self.w_cured.setFont(QFont('SansSerif', 18))
        self.w_cured.setStyleSheet("""
                           background-color: black; 
                           color: cyan; 
                           border-style: outset; 
                           border-width: 1px
                           """)

        #worldwide cured number
        self.w_cured_num = QLabel(self)
        self.w_cured_num.setGeometry(110, 140, 100, 40)
        self.w_cured_num.setFont(QFont('SansSerif', 18))
        self.w_cured_num.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)


        """_______________________Local-By country Code________________________________"""
        
        #local - Country 
        self.c = QLabel(self)
        self.c.setGeometry(170, 200, 400, 40)
        self.c.setText("My Country: Bangladesh")
        self.c.setFont(QFont('SansSerif', 18))
        self.c.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)
        
        #local confirm cases
        self.c_cases = QLabel(self)
        self.c_cases.setGeometry(5, 240, 400, 40)
        self.c_cases.setText("Cases:")
        self.c_cases.setFont(QFont('SansSerif', 18))
        self.c_cases.setStyleSheet("""
                           background-color: black; 
                           color: orange; 
                           border-style: outset; 
                           border-width: 1px
                           """)
        
        #local cases number
        self.c_cases_num = QLabel(self)
        self.c_cases_num.setGeometry(110, 240, 100, 40)
        self.c_cases_num.setFont(QFont('SansSerif', 18))
        self.c_cases_num.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)

        #local deaths
        self.c_death = QLabel(self)
        self.c_death.setGeometry(350, 240, 100, 40)
        self.c_death.setText("Deaths:")
        self.c_death.setFont(QFont('SansSerif', 18))
        self.c_death.setStyleSheet("""
                           background-color: black; 
                           color: red; 
                           border-style: outset; 
                           border-width: 1px
                           """)

        #local deaths number
        self.c_death_num = QLabel(self)
        self.c_death_num.setGeometry(460, 240, 100, 40)
        self.c_death_num.setFont(QFont('SansSerif', 18))
        self.c_death_num.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)
   
        
        #local cured
        self.c_cured = QLabel(self)
        self.c_cured.setGeometry(5, 280, 100, 40)
        self.c_cured.setText("Cured:")
        self.c_cured.setFont(QFont('SansSerif', 18))
        self.c_cured.setStyleSheet("""
                           background-color: black; 
                           color: cyan; 
                           border-style: outset; 
                           border-width: 1px
                           """)
        
        #local cured number
        self.c_cured_num = QLabel(self)
        self.c_cured_num.setGeometry(110, 280, 100, 40)
        self.c_cured_num.setFont(QFont('SansSerif', 18))
        self.c_cured_num.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)



        """_______________________Time, Date, Clock________________________________"""
        #clock
        self.clock = QLabel(self)
        self.clock.setGeometry(115, 340, 400, 70)
        self.clock.setFont(QFont('SansSerif', 60))
        self.clock.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)
        
        #label for weekday
        self.weekday = QLabel(self)
        self.weekday.setGeometry(5, 360, 110, 20)
        self.weekday.setFont(QFont('SansSerif', 13))
        self.weekday.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)
        
        #date label
        self.date = QLabel(self)
        self.date.setGeometry(510, 360, 110, 20)
        #self.clock.setText("22:49:00")
        self.date.setFont(QFont('SansSerif', 13))
        self.date.setStyleSheet("""
                           background-color: black; 
                           color: white; 
                           border-style: outset; 
                           border-width: 1px
                           """)


        
        #check the timer
        if not self.timer.isActive():
            #if timer is stopped (reached threshold)
            #After 1 second (approx.) or 1000ms

            try:
                """try to get data, else run the code anyway"""
                self.latest = self.covid.getLatest() #gte covid19 latest data

                #get latest data by country code 'BD'-Bangladesh, 'IN'-India etc
                self.local = self.covid.getLocationByCountryCode('BD', timelines=False)
                #print(self.local)
                #print(self.latest)

            except:
                """couldn't get data"""
                print("Internet Error!!")

                pass #ignore, run anyway

            self.timer.start(1000) #start the timer
        
        self.show() #show our User Interface


    def update(self):
        """update labels with information"""

        """_________________Extract ad Update Time and Date Information________________"""
        #set up clock and date time (update values)
        #get and update values
        #to know more read python datetime documentation

        self.dt = datetime.datetime.now() #get datetime data
        self.clock.setText(self.dt.strftime('%X'))
        self.weekday.setText(self.dt.strftime('%A'))
        self.date.setText(self.dt.strftime('%x'))
        
        
        """__________________________update covid19 data______________________________"""
        
        #worldwide latest data
        self.w_cases_num.setText(str(self.latest['confirmed']))
        self.w_death_num.setText(str(self.latest['deaths']))
        self.w_cured_num.setText(str(self.latest['recovered']))
        
        #local latest data
        self.c_cured_num.setText(str(self.local[0]['latest']['recovered']))
        self.c_death_num.setText(str(self.local[0]['latest']['deaths']))
        self.c_cases_num.setText(str(self.local[0]['latest']['confirmed']))

        print("updating")

        return



  
def main():
    app = QApplication(sys.argv)  
    win = CoronaTracker()  #instantiate
    sys.exit(app.exec())
   
#run the application 
if __name__ == '__main__':
    main()
