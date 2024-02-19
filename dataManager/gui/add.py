from. import jsonControl
import guiTools
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class ADD (qt.QDialog):
    def __init__ (self,p,index,type):
        super().__init__(p)
        self.p=p
        self.a=""
        self.setWindowTitle(_("add "))
        layout=qt.QFormLayout(self)
        self.name=qt.QLineEdit()
        layout.addRow(_("name"),self.name)
        if index==0:
            self.contry=qt.QComboBox()
            self.contry.addItems(guiTools.dictionarys.countryTelephoneCodes.keys())
            layout.addRow(_("select country"),self.contry)
            self.contry.currentTextChanged.connect(self.change)
        self.content=qt.QLineEdit()
        if index==2:
            self.content.setEchoMode(qt.QLineEdit.EchoMode.Password)
        layout.addRow(_("content"),self.content)
        self.add=qt.QPushButton(_("add"))
        self.add.clicked.connect(self.ADD)
        layout.addWidget(self.add)
    def change(self,text):
        self.a=guiTools.dictionarys.countryTelephoneCodes[text]
    def ADD(self):
        self.p.categories[self.name.text()]=self.a + self.content.text()
        self.p.categoriesList.addItem(self.name.text())
        self.close()