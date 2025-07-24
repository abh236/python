#introduction of PyQt5

'''import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
  def __init__(self):
    super( ).__init__()
    self.setWindowTitle("Abhi")
    self.setGeometry(100,100,400,400)
    self.setWindowIcon(QIcon('image.png'))


def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())


if __name__ == "__main__":
  main()'''

# PyQt5 labels

'''import sys 
from PyQt5.QtWidgets  import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(20,30,500,500)
    label=QLabel("I am Abhi",self)
    #label.move(100,100) # move the label to the specified position
    label.setFont(QFont("Arial",10))
    label.setGeometry(0,0,500,100)
    label.setStyleSheet("color:blue;"
                        "background-color:#87a2f5;"
                        "font-style:Italic;"
                        "font-weight:Bold;"
                        "text-decoration:underline;")
    label.setAlignment(Qt.AlignTop) # align the text to the top of the label
    label.setAlignment(Qt.AlignBottom) # align the text to the bottom of the label    
    label.setAlignment(Qt.AlignVCenter) # align the text to the center of the label
    label.setAlignment(Qt.AlignLeft) # align the text to the left of the label
    label.setAlignment(Qt.AlignRight) # align the text to the right of the label
    label.setAlignment(Qt.AlignHCenter) # align the text to the horizontal center of the label
    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # align the text to the horizontal and vertical center of the label


def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__=="__main__":
  main()'''

# pyQt5 images

'''import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(700,300,500,500)
    label=QLabel(self)
    label.setGeometry(0,0,500,500)
    pixle=QPixmap("image.png")
    label.setPixmap(pixle)
    label.setScaledContents(True)
    label.setGeometry(self.width()-label.width()//2,self.height()-label.height()//2,label.width(),label.height())   



def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__=="__main__":
  main()'''

# PyQt5 layout manager

'''import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QHBoxLayout,QVBoxLayout,QGridLayout,QWidget
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(700,300,500,500)
    self.initUI()
  
  def initUI(self):
      central_wiget=QWidget()
      self.setCentralWidget(central_wiget)
      label1=QLabel("#1",self)
      label2=QLabel("#2",self)
      label3=QLabel("#3",self)
      label4=QLabel("#4",self)
      label5=QLabel("#5",self)
      label6=QLabel("#6",self)
      label7=QLabel("#7",self)
      label1.setStyleSheet("background-color:red;")
      label2.setStyleSheet("background-color:yellow;")
      label3.setStyleSheet("background-color:orange;")
      label4.setStyleSheet("background-color:blue;")
      label5.setStyleSheet("background-color:green;")
      label6.setStyleSheet("background-color:brown;")
      label7.setStyleSheet("background-color:pink;")
      # vbox=QVBoxLayout()
      # vbox.addWidget(label1) 
      # vbox.addWidget(label2) 
      # vbox.addWidget(label3) 
      # vbox.addWidget(label4) 
      # vbox.addWidget(label5) 
      # vbox.addWidget(label6) 
      # vbox.addWidget(label7) 
      # central_wiget.setLayout(vbox)       
      # hbox=QHBoxLayout()
      # hbox.addWidget(label1) 
      # hbox.addWidget(label2) 
      # hbox.addWidget(label3) 
      # hbox.addWidget(label4) 
      # hbox.addWidget(label5) 
      # hbox.addWidget(label6) 
      # hbox.addWidget(label7)       
      # central_wiget.setLayout(hbox) 

      grid=QGridLayout()
      grid.addWidget(label1,0,0) 
      grid.addWidget(label2,1,0) 
      grid.addWidget(label3,1,2) 
      grid.addWidget(label4,1,0) 
      grid.addWidget(label5,1,2) 
      grid.addWidget(label6,2,1) 
      grid.addWidget(label7,1,1)       
      central_wiget.setLayout(grid)


      




def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__=="__main__":
  main()'''

#PyQt5 buttons
'''import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QWidget
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(700,300,500,500)
    self.label=QLabel("Hello",self)
    self.button=QPushButton("Clicked Me",self)
    self.initUI()
  def initUI(self):
    self.button.setGeometry(250,250,100,50)
    self.button.setStyleSheet("font-size:20;"
                         "background-color:yellow;")
    self.button.clicked.connect(self.clicked)
    
    
    
  def clicked(self):
      print("you clicked")
      self.button.setText("Clicked!")
      self.button.setDisabled(True)
      self.label.setText("GoodBye!")


  



def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__=="__main__":
  main()'''

#PyQt5 checkbox
'''import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(700,300,500,500)
    self.label=QLabel(self)
    self.label.setGeometry(0,0,500,500)
    self.checkbox=QCheckBox("You like food",self)
    self.label.setGeometry(0,0,500,500)
    self.label.setStyleSheet("font-size:30px;")

    self.initUI()
  def initUI(self):
    self.checkbox.setGeometry(10,10,500,200)
    self.checkbox.setStyleSheet("font-size:30px;")
    self.checkbox.setChecked(False)
    self.checkbox.stateChanged.connect(self.checking)

  def checking(self,state):
    if state==Qt.Checked:
      self.label.setText("you like food")
      print("you like food")
    else:
      self.label.setText(" ")
      print("you don't like food")  




def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__=="__main__":
  main()'''

# PyQt5 checkbox with radio button
'''import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QCheckBox,QRadioButton,QButtonGroup
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(700,300,500,500)
    self.label=QLabel(self)
    self.label.setGeometry(0,0,500,500)
    
    self.label.setGeometry(0,0,500,500)
    self.label.setStyleSheet("font-size:30px;")
    self.radio1=QRadioButton("Patym",self)
    self.radio2=QRadioButton("Phonepay",self)
    self.radio3=QRadioButton("Googlepay",self)
    self.radio4=QRadioButton("Visa",self)
    self.radio5=QRadioButton("Credit Card",self)
    self.radio6=QRadioButton("Debit Card",self)
    self.radio7=QRadioButton("MasterCard",self)
    self.group1=QButtonGroup(self)
    self.group2=QButtonGroup(self)

    self.initUI()
  def initUI(self):

    self.radio1.setGeometry(0,0,300,50)
    self.radio2.setGeometry(0,50,300,50)
    self.radio3.setGeometry(0,100,300,50)
    self.radio4.setGeometry(0,150,300,50)
    self.radio5.setGeometry(0,200,300,50)
    self.radio6.setGeometry(0,250,300,50)
    self.radio7.setGeometry(0,300,300,50)
    self.setStyleSheet("QRadioButton{""font-size:30px;""font-style:Arial;""}")
    self.group1.addButton(self.radio1)
    self.group1.addButton(self.radio2)
    self.group1.addButton(self.radio3)
    self.group2.addButton(self.radio4)
    self.group2.addButton(self.radio5)
    self.group2.addButton(self.radio6)
    self.group2.addButton(self.radio7)
    self.radio1.toggled.connect(self.radio)
    self.radio2.toggled.connect(self.radio)
    self.radio3.toggled.connect(self.radio)
    self.radio4.toggled.connect(self.radio)
    self.radio5.toggled.connect(self.radio)
    self.radio6.toggled.connect(self.radio)
    self.radio7.toggled.connect(self.radio)

  def radio(self,state):
    radio_button=self.sender()
    if radio_button.isChecked():
      self.label.setText(radio_button.text())





def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__=="__main__":
  main()'''

# PyQt5 line edits
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setGeometry(700,300,500,500)
    self.label=QLabel(self)
    self.label.setGeometry(0,0,500,500)
    self.lineedit=QLineEdit(self)
    self.submit=QPushButton("Submit",self)
    self.lineedit.setPlaceholderText("Enter your name")
    self.label.setGeometry(0,0,500,500)
    self.label.setStyleSheet("font-size:30px;")

    self.initUI()
  def initUI(self):
    self.lineedit.setGeometry(10,10,200,30)
    self.submit.setGeometry(220,10,100,30)
    self.lineedit.setStyleSheet("font-size:30px;")
    self.submit.clicked.connect(self.Submit)

  def Submit(self,state):
    self.label.setText(f"Hello  {self.lineedit.text()}")






def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__=="__main__":
  main()