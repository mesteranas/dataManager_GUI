from . import jsonControl,categoryContent
import guiTools
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
indexes={0:"contacts",1:"links",2:"passwords",3:"notes"}
class CategoryManager (qt.QDialog):
    def __init__ (self,p,index):
        super().__init__(p)
        self.p=p
        self.setWindowTitle(_("category manager"))
        self.currentCategory=indexes[index]
        self.categories=jsonControl.getCatagory(self.currentCategory)
        self.categoriesList=qt.QListWidget()
        self.categoriesList.addItems(self.categories.keys())
        self.categoriesList.setAccessibleName(_("categories"))
        self.categoriesList.setContextMenuPolicy(qt2.Qt.ContextMenuPolicy.CustomContextMenu)
        self.categoriesList.customContextMenuRequested.connect(self.context)
        qt1.QShortcut("delete",self).activated.connect(self.delete)
        qt1.QShortcut("f2",self).activated.connect(self.edit)
        self.open=qt.QPushButton(_("open"))
        self.open.clicked.connect(lambda: categoryContent.CategoryContentManager(self,index,self.categoriesList.currentItem().text()).exec())
        self.add=qt.QPushButton(_("add category"))
        self.add.clicked.connect(self.ADD)
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.categoriesList)
        layout.addWidget(self.open)
        layout.addWidget(self.add)
        qt1.QShortcut("escape",self).activated.connect(lambda:self.closeEvent(None))
    def ADD(self):
        name,ok=qt.QInputDialog.getText(self,_("add category"),_("inter category name"))
        if ok:
            self.categories[name]={}
            self.categoriesList.addItem(name)
            self.closeEvent(1)
    def closeEvent(self, event):
        jsonControl.saveCatagories(self.currentCategory,self.categories)
        if not event==1:
            self.close()
    def context(self):
        menu=qt.QMenu(self)
        delete=qt1.QAction(_("delete"),self)
        delete.triggered.connect(self.delete)
        edit=qt1.QAction(_("edit"),self)
        edit.triggered.connect(self.edit)
        menu.addAction(delete)
        menu.addAction(edit)
        menu.exec()
    def delete(self):
        try:
            del(self.categories[self.categoriesList.currentItem().text()])
            self.categoriesList.clear()
            self.categoriesList.addItems(self.categories)
            guiTools.speak(_("category was deleted"))
        except:
            guiTools.speak(_("error"))
    def edit(self):
        try:
            textBox=qt.QInputDialog(self)
            textBox.setWindowTitle(_("edit category name"))
            textBox.setLabelText(_("inter new name"))
            textBox.setTextValue(self.categoriesList.currentItem().text())
            if textBox.exec()==qt.QDialog.DialogCode.Accepted:
                self.categories[textBox.textValue()]=self.categories.pop(self.categoriesList.currentItem().text())
                self.categoriesList.clear()
                self.categoriesList.addItems(self.categories.keys())
        except:
            guiTools.speak(_("error"))