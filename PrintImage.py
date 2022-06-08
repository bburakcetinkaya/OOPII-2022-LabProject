"""
Created on May  25 23:45:47 2022

@author: Burak Çetinkaya
        151220152110
"""
from PyQt5.QtWidgets import QUndoCommand

class PrintImage(QUndoCommand):

    def __init__(self,area,image):
        """

        """
        super(PrintImage, self).__init__()        
        self.__img = image
        self.__area = area  
    def printImg(self):
        self.__area.setPixmap(self.__img)        
            
    def undo(self): 
        self.printImg()
        
    def redo(self):
        self.printImg()
  