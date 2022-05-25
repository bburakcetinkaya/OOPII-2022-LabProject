# -*- coding: utf-8 -*-
"""
Created on Wed May 25 05:06:43 2022

@author: piton
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QFileDialog
from PyQt5.QtGui import QImage
from Failed import Failed
from PIL import ImageQt

from ImageProcessing import ImageProcessing

class Manager(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalSlots()
        
    

    def connectSignalSlots(self):
        self.fileAction_openSource.triggered.connect(self.loadSourceImage)
        self.fileAction_exportAsSource.triggered.connect(self.exportAsSource)
        self.fileAction_exportAsOutput.triggered.connect(self.exportAsOutput)
        self.fileAction_saveOutput.triggered.connect(self.saveOutput)
        self.fileAction_saveAsOutput.triggered.connect(self.saveAsOutput)
        self.fileAction_Exit.triggered.connect(self.Exit)
        
        self.editAction_clearSource.triggered.connect(self.clearSource)
        self.editAction_clearOutput.triggered.connect(self.clearOutput)
        self.editAction_undoOutput.triggered.connect(self.undoOutput)
        self.editAction_redoOutput.triggered.connect(self.redoOutput)
        
        self.conversionAction_RGBtoGrayscale.triggered.connect(self.RGBtoGrayscale)
        self.conversionAction_RGBtoHSV.triggered.connect(self.RGBtoHSV)
        
        self.segmentationAction_multiOtsuThresholding.triggered.connect(self.multiOtsuThresholding)
        self.segmentationAction_chanVeseSegmentation.triggered.connect(self.chanVeseSegmentation)
        self.segmentationAction_morphologicalSnakes.triggered.connect(self.morphologicalSnakes)
        
        self.edgeDetectionAction_Roberts.triggered.connect(self.Roberts)
        self.edgeDetectionAction_Sobel.triggered.connect(self.Sobel)
        self.edgeDetectionAction_Scharr.triggered.connect(self.Scharr)
        self.edgeDetectionAction_Prewitt.triggered.connect(self.Prewitt)
        
    def enableAfterSourceObtained(self):
        self.fileAction_exportAsSource.setEnabled(True)
        # self.fileAction_exportAsOutput.setEnabled(False)
        # self.fileAction_saveOutput.setEnabled(False)
        # self.fileAction_saveAsOutput.setEnabled(False)

        self.editAction_clearSource.setEnabled(True)
        
        self.conversionAction_RGBtoGrayscale.setEnabled(True)
        self.conversionAction_RGBtoHSV.setEnabled(True)
        
        self.segmentationAction_multiOtsuThresholding.setEnabled(True)
        self.segmentationAction_chanVeseSegmentation.setEnabled(True)
        self.segmentationAction_morphologicalSnakes.setEnabled(True)
        
        self.edgeDetectionAction_Roberts.setEnabled(True)
        self.edgeDetectionAction_Sobel.setEnabled(True)
        self.edgeDetectionAction_Scharr.setEnabled(True)
        self.edgeDetectionAction_Prewitt.setEnabled(True)
        
    def disableAfterSourceCleared(self):
        self.fileAction_exportAsSource.setEnabled(False)
        self.fileAction_exportAsOutput.setEnabled(False)
        self.fileAction_saveOutput.setEnabled(False)
        self.fileAction_saveAsOutput.setEnabled(False)

        self.editAction_clearSource.setEnabled(False)
        self.editAction_clearOutput.setEnabled(False)
        self.editAction_undoOutput.setEnabled(False)
        self.editAction_redoOutput.setEnabled(False)
        
        self.conversionAction_RGBtoGrayscale.setEnabled(False)
        self.conversionAction_RGBtoHSV.setEnabled(False)
        
        self.segmentationAction_multiOtsuThresholding.setEnabled(False)
        self.segmentationAction_chanVeseSegmentation.setEnabled(False)
        self.segmentationAction_morphologicalSnakes.setEnabled(False)
        
        self.edgeDetectionAction_Roberts.setEnabled(False)
        self.edgeDetectionAction_Sobel.setEnabled(False)
        self.edgeDetectionAction_Scharr.setEnabled(False)
        self.edgeDetectionAction_Prewitt.setEnabled(False)
        
    def enableAfterOutputObtained(self):
        self.fileAction_exportAsOutput.setEnabled(True)
        self.fileAction_saveOutput.setEnabled(True)
        self.fileAction_saveAsOutput.setEnabled(True)
        self.editAction_clearOutput.setEnabled(True)
        self.editAction_undoOutput.setEnabled(True)
        
    def disableAfterOutputCleared(self):
        self.fileAction_exportAsOutput.setEnabled(False)
        self.fileAction_saveOutput.setEnabled(False)
        self.fileAction_saveAsOutput.setEnabled(False)
        self.editAction_clearOutput.setEnabled(False)
        self.editAction_undoOutput.setEnabled(False)
        

        
    def loadSourceImage(self):
        self.filePath = QFileDialog.getOpenFileName(filter=("Image Files (*.png *.jpg)"))[0]
        self.inputLabel.setPixmap(QtGui.QPixmap(self.filePath))
        
        import os
        self.splitedPath = os.path.split(str(self.filePath))
        self.splitedFileName = str(self.splitedPath[1]).split(".")
        
        self.enableAfterSourceObtained()
        
    def saveOutput(self):
        import os
        self.splitedPath = os.path.split(str(self.filePath))
        self.splitedFileName = str(self.splitedPath[1]).split(".")
        print(self.splitedFileName)
        self.img = ImageQt.fromqpixmap(self.outputLabel.pixmap())   
        self.img.save(self.splitedPath[0]+"/Output."+self.splitedFileName[1]) 
        
    def saveAsOutput(self):
        print("save as output")
        self.saveFilePath = QFileDialog.getSaveFileName(filter=("PNG(*.png);;JPG(*.jpg)"))[0]
        self.img = ImageQt.fromqpixmap(self.outputLabel.pixmap())
        self.img.save(self.saveFilePath)
        
    def exportAsSource(self):
       
        self.img = ImageQt.fromqpixmap(self.inputLabel.pixmap())   
        extension = str("png") if self.splitedFileName[1] == "jpg" or "JPG" or "jpeg" else str("jpg")
        self.img.save(self.splitedPath[0]+"/"+self.splitedFileName[0]+"."+ extension) 
        print("export as source")
        
    def exportAsOutput(self):
        import os
        self.img = ImageQt.fromqpixmap(self.outputLabel.pixmap())   
        extension = str("png") if self.splitedFileName[1] == "jpg" else str("jpg")
        self.img.save(self.splitedPath[0]+"/"+Output+"."+ extension)
        print("export as output")       
        
    def Exit(self):
        self.close()
        
    def clearSource(self):
        self.inputLabel.setText("INPUT")    
        
        self.editAction_clearSource.setEnabled(True)
        
        self.conversionAction_RGBtoGrayscale.setEnabled(False)
        self.conversionAction_RGBtoHSV.setEnabled(False)
        
        self.segmentationAction_multiOtsuThresholding.setEnabled(False)
        self.segmentationAction_chanVeseSegmentation.setEnabled(False)
        self.segmentationAction_morphologicalSnakes.setEnabled(False)
        
        self.edgeDetectionAction_Roberts.setEnabled(False)
        self.edgeDetectionAction_Sobel.setEnabled(False)
        self.edgeDetectionAction_Scharr.setEnabled(False)
        self.edgeDetectionAction_Prewitt.setEnabled(False)
               
        
    def clearOutput(self):
        self.outputLabel.setText("OUTPUT")
        self.disableAfterOutputCleared()
        
    def undoOutput(self):
        print("undo output")
        
    def redoOutput(self):
        print("redo output")
        
    def RGBtoGrayscale(self):
        print("rgb to gray")
        imgPrc = ImageProcessing()
        try:
            self.result = imgPrc.RGBtoGreyscale(self.filePath)
        except:
            self.errorHandler()
        else:            
            self.grayscale = QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                    self.result.strides[0], QImage.Format_Indexed8)
            self.outputLabel.setPixmap(QtGui.QPixmap(self.grayscale))
            
            self.enableAfterOutputObtained()
        
    def RGBtoHSV(self):
        print("rgb to hsv")
        imgPrc = ImageProcessing()
        try:
            self.result = imgPrc.RGBtoHSV(self.filePath)
        except:
            self.errorHandler()
        else:
            self.hsv = QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                              self.result.strides[0], QImage.Format_RGB888)
            self.outputLabel.setPixmap(QtGui.QPixmap(self.hsv))
            
            self.enableAfterOutputObtained()
        
    def multiOtsuThresholding(self):
        print("multi otsu thresholding")
        imgPrc = ImageProcessing()
        try:            
            self.result = imgPrc.multiOtsuThresholding(self.filePath)
        except:
            self.errorHandler()
        else:
            self.multiOtsuThresholding = QImage(self.result.data,  self.result.shape[1], self.result.shape[1], 
                                                self.result.strides[0], QImage.Format_RGB888)
            self.outputLabel.setPixmap(QtGui.QPixmap(self.multiOtsuThresholding))
            
            self.enableAfterOutputObtained()
        
    def chanVeseSegmentation(self):
        print("chan vese segmentation")
        imgPrc = ImageProcessing()
        try:
            self.result = imgPrc.chanVeseSegmentation(self.filePath)
        except:
            self.errorHandler()
        else:            
            self.cv = QImage(self.result,  self.result.shape[1], self.result.shape[1], 
                                            self.result.strides[0], QImage.Format_Indexed8)
            self.outputLabel.setPixmap(QtGui.QPixmap(self.cv))
            
            self.enableAfterOutputObtained()
        
    def morphologicalSnakes(self):
        imgPrc = ImageProcessing()
        try:
            print("morphological snakes")
            self.result = imgPrc.Roberts(self.filePath)
        except:
            self.errorHandler()
        else:
            print("ok")
            self.cv = QImage(self.result,  self.result.shape[1], self.result.shape[1], 
                                            self.result.strides[0], QImage.Format_Indexed8)
            self.outputLabel.setPixmap(QtGui.QPixmap(self.cv))
            
            self.enableAfterOutputObtained()
        
    def Roberts(self):
        imgPrc = ImageProcessing()
        try:
            print("Roberts")
            self.result = imgPrc.Roberts(self.filePath)
        except:
            self.errorHandler()
        else:
            print("ok")
            self.grayscale = QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                    self.result.strides[0], QImage.Format_Indexed8)
            self.outputLabel.setPixmap(QtGui.QPixmap(self.grayscale))
            
            self.enableAfterOutputObtained()
        
    def Sobel(self):
        imgPrc = ImageProcessing()
        try:
            print("Sobel")
            self.result = imgPrc.Sobel(self.filePath)
        except:
            self.errorHandler()
        else:
            print("ok")
            self.grayscale = QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                    self.result.strides[0], QImage.Format_Indexed8)
            self.outputLabel.setPixmap(QtGui.QPixmap(self.grayscale))   
            
            self.enableAfterOutputObtained()
        
    def Scharr(self):
        imgPrc = ImageProcessing()
        try:
            print("Scharr")
            self.result = imgPrc.Scharr(self.filePath)
        except:
            self.errorHandler()
        else:
            print("ok")
            self.grayscale = QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                    self.result.strides[0], QImage.Format_Indexed8)
            self.outputLabel.setPixmap(QtGui.QPixmap(self.grayscale))
            
            self.enableAfterOutputObtained()
        
    def Prewitt(self):
        imgPrc = ImageProcessing()
        try:
            print("prewitt")
            self.result = imgPrc.Prewitt(self.filePath)
        except:
            self.errorHandler()
        else:
            print("ok")
            self.grayscale = QImage(self.result.data, self.result.shape[1], self.result.shape[0],
                                    self.result.strides[0], QImage.Format_Indexed8)
            self.outputLabel.setPixmap(QtGui.QPixmap(self.grayscale))
            
            self.enableAfterOutputObtained()
        
    def errorHandler(self):
        global exception
        exception = QtWidgets.QMainWindow()
        self.exception = Failed()
        self.exception.setupUi(exception)
        exception.show()     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Manager()
    win.show()
    sys.exit(app.exec())