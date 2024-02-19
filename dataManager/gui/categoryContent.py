from . import jsonControl,add,view
import guiTools
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
indexes={0:"contacts",1:"links",2:"passwords",3:"notes"}
class CategoryContentManager (qt.QDialog):
    def __init__ (self,p,index,category):
        super().__init__(p)
        self.p=p
        self.setWindowTitle(_("category content manager"))
        self.currentCategory=indexes[index]
        self.category=category
        self.categories=jsonControl.getCategoryContent(self.currentCategory,self.category)
        self.categoriesList=qt.QListWidget()
        self.categoriesList.addItems(self.categories.keys())
        self.categoriesList.setAccessibleName(_("content"))
        self.categoriesList.setContextMenuPolicy(qt2.Qt.ContextMenuPolicy.CustomContextMenu)
        self.categoriesList.customContextMenuRequested.connect(self.context)
        qt1.QShortcut("delete",self).activated.connect(self.delete)
        self.add=qt.QPushButton(_("add "))
        self.add.clicked.connect(lambda:add.ADD(self,index,self.category).exec())
        layout=qt.QVBoxLayout(self)
        layout.addWidget(self.categoriesList)
        layout.addWidget(self.add)
        qt1.QShortcut("escape",self).activated.connect(lambda:self.closeEvent(None))
    def closeEvent(self, event):
        jsonControl.saveCatagoryContents(self.currentCategory,self.category,self.categories)
        self.p.categories=jsonControl.getCatagory(self.p.currentCategory)
        self.p.categoriesList.clear()
        self.p.categoriesList.addItems(self.p.categories.keys())
        self.close()
    def context(self):
        menu=qt.QMenu(self)
        delete=qt1.QAction(_("delete"),self)
        delete.triggered.connect(self.delete)
        menu.addAction(delete)
        View=qt1.QAction(_("view"),self)
        if self.currentCategory=="links":
            View.triggered.connect(lambda:guiTools.OpenLink(self,self.categories[self.categoriesList.currentItem().text()]))
        else:
            View.triggered.connect(lambda:view.View(self,self.categories[self.categoriesList.currentItem().text()]).exec())
        menu.addAction(View)
        menu.exec()
    def delete(self):
        try:
            del(self.categories[self.categoriesList.currentItem().text()])
            self.categoriesList.clear()
            self.categoriesList.addItems(self.categories)
            guiTools.speak(_("item was deleted"))
        except:
            guiTools.speak(_("error"))
