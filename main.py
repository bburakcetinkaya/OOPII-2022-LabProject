# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:35:41 2022

@author: Burak Çetinkaya
        151220152110
"""
from Manager import Manager
from PyQt5 import QtWidgets
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Manager()
    win.show()
    sys.exit(app.exec())