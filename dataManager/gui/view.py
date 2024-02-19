import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class View(qt.QDialog):
    def __init__ (self,p,text):
        super().__init__(p)
        self.p=p
        self.setWindowTitle(_("view"))
        layout=qt.QVBoxLayout(self)
        self.result=qt.QPlainTextEdit()
        self.result.setPlainText(text)
        self.result.setReadOnly(True)
        layout.addWidget(self.result)
