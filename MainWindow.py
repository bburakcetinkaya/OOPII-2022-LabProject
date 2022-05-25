# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 650)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.inputLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout.addWidget(self.inputLabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout.addWidget(self.outputLabel, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        self.menuExport_As.setEnabled(False)
        self.menuExport_As.setObjectName("menuExport_As")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setEnabled(False)
        self.menuEdit.setObjectName("menuEdit")
        self.menuClear = QtWidgets.QMenu(self.menuEdit)
        self.menuClear.setObjectName("menuClear")
        self.menuConversion = QtWidgets.QMenu(self.menubar)
        self.menuConversion.setEnabled(False)
        self.menuConversion.setObjectName("menuConversion")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setEnabled(False)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setEnabled(False)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.sourceOutputToolbar = QtWidgets.QToolBar(MainWindow)
        self.sourceOutputToolbar.setMovable(True)
        self.sourceOutputToolbar.setFloatable(False)
        self.sourceOutputToolbar.setObjectName("sourceOutputToolbar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.sourceOutputToolbar)
        MainWindow.insertToolBarBreak(self.sourceOutputToolbar)
        self.operationsToolBar = QtWidgets.QToolBar(MainWindow)
        self.operationsToolBar.setFloatable(False)
        self.operationsToolBar.setObjectName("operationsToolBar")
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.operationsToolBar)
        self.fileAction_openSource = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.fileAction_openSource.setIcon(icon)
        self.fileAction_openSource.setShortcutVisibleInContextMenu(True)
        self.fileAction_openSource.setObjectName("fileAction_openSource")
        self.fileAction_saveOutput = QtWidgets.QAction(MainWindow)
        self.fileAction_saveOutput.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/save-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.fileAction_saveOutput.setIcon(icon1)
        self.fileAction_saveOutput.setShortcutVisibleInContextMenu(True)
        self.fileAction_saveOutput.setObjectName("fileAction_saveOutput")
        self.fileAction_saveAsOutput = QtWidgets.QAction(MainWindow)
        self.fileAction_saveAsOutput.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/save-as.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.fileAction_saveAsOutput.setIcon(icon2)
        self.fileAction_saveAsOutput.setShortcutVisibleInContextMenu(True)
        self.fileAction_saveAsOutput.setObjectName("fileAction_saveAsOutput")
        self.fileAction_exportAsSource = QtWidgets.QAction(MainWindow)
        self.fileAction_exportAsSource.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/export-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.fileAction_exportAsSource.setIcon(icon3)
        self.fileAction_exportAsSource.setShortcutVisibleInContextMenu(True)
        self.fileAction_exportAsSource.setObjectName("fileAction_exportAsSource")
        self.fileAction_exportAsOutput = QtWidgets.QAction(MainWindow)
        self.fileAction_exportAsOutput.setEnabled(False)
        self.fileAction_exportAsOutput.setIcon(icon3)
        self.fileAction_exportAsOutput.setShortcutVisibleInContextMenu(True)
        self.fileAction_exportAsOutput.setObjectName("fileAction_exportAsOutput")
        self.fileAction_Exit = QtWidgets.QAction(MainWindow)
        self.fileAction_Exit.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.fileAction_Exit.setIcon(icon4)
        self.fileAction_Exit.setShortcutVisibleInContextMenu(True)
        self.fileAction_Exit.setObjectName("fileAction_Exit")
        self.editAction_undoOutput = QtWidgets.QAction(MainWindow)
        self.editAction_undoOutput.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/back-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.editAction_undoOutput.setIcon(icon5)
        self.editAction_undoOutput.setShortcutVisibleInContextMenu(True)
        self.editAction_undoOutput.setObjectName("editAction_undoOutput")
        self.editAction_redoOutput = QtWidgets.QAction(MainWindow)
        self.editAction_redoOutput.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/front-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.editAction_redoOutput.setIcon(icon6)
        self.editAction_redoOutput.setShortcutVisibleInContextMenu(True)
        self.editAction_redoOutput.setObjectName("editAction_redoOutput")
        self.editAction_clearSource = QtWidgets.QAction(MainWindow)
        self.editAction_clearSource.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/clean.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.editAction_clearSource.setIcon(icon7)
        self.editAction_clearSource.setShortcutVisibleInContextMenu(True)
        self.editAction_clearSource.setObjectName("editAction_clearSource")
        self.editAction_clearOutput = QtWidgets.QAction(MainWindow)
        self.editAction_clearOutput.setEnabled(False)
        self.editAction_clearOutput.setIcon(icon7)
        self.editAction_clearOutput.setShortcutVisibleInContextMenu(True)
        self.editAction_clearOutput.setObjectName("editAction_clearOutput")
        self.conversionAction_RGBtoGrayscale = QtWidgets.QAction(MainWindow)
        self.conversionAction_RGBtoGrayscale.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/rgb-to-greyscale.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.conversionAction_RGBtoGrayscale.setIcon(icon8)
        self.conversionAction_RGBtoGrayscale.setShortcutVisibleInContextMenu(True)
        self.conversionAction_RGBtoGrayscale.setObjectName("conversionAction_RGBtoGrayscale")
        self.conversionAction_RGBtoHSV = QtWidgets.QAction(MainWindow)
        self.conversionAction_RGBtoHSV.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/rgb-to-hsv.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.conversionAction_RGBtoHSV.setIcon(icon9)
        self.conversionAction_RGBtoHSV.setShortcutVisibleInContextMenu(True)
        self.conversionAction_RGBtoHSV.setObjectName("conversionAction_RGBtoHSV")
        self.segmentationAction_multiOtsuThresholding = QtWidgets.QAction(MainWindow)
        self.segmentationAction_multiOtsuThresholding.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/white-one.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.segmentationAction_multiOtsuThresholding.setIcon(icon10)
        self.segmentationAction_multiOtsuThresholding.setShortcutVisibleInContextMenu(True)
        self.segmentationAction_multiOtsuThresholding.setObjectName("segmentationAction_multiOtsuThresholding")
        self.segmentationAction_chanVeseSegmentation = QtWidgets.QAction(MainWindow)
        self.segmentationAction_chanVeseSegmentation.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/white-two.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.segmentationAction_chanVeseSegmentation.setIcon(icon11)
        self.segmentationAction_chanVeseSegmentation.setShortcutVisibleInContextMenu(True)
        self.segmentationAction_chanVeseSegmentation.setObjectName("segmentationAction_chanVeseSegmentation")
        self.segmentationAction_morphologicalSnakes = QtWidgets.QAction(MainWindow)
        self.segmentationAction_morphologicalSnakes.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/white-three.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.segmentationAction_morphologicalSnakes.setIcon(icon12)
        self.segmentationAction_morphologicalSnakes.setShortcutVisibleInContextMenu(True)
        self.segmentationAction_morphologicalSnakes.setObjectName("segmentationAction_morphologicalSnakes")
        self.edgeDetectionAction_Roberts = QtWidgets.QAction(MainWindow)
        self.edgeDetectionAction_Roberts.setEnabled(False)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/one.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.edgeDetectionAction_Roberts.setIcon(icon13)
        self.edgeDetectionAction_Roberts.setShortcutVisibleInContextMenu(True)
        self.edgeDetectionAction_Roberts.setObjectName("edgeDetectionAction_Roberts")
        self.edgeDetectionAction_Sobel = QtWidgets.QAction(MainWindow)
        self.edgeDetectionAction_Sobel.setEnabled(False)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/two.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.edgeDetectionAction_Sobel.setIcon(icon14)
        self.edgeDetectionAction_Sobel.setShortcutVisibleInContextMenu(True)
        self.edgeDetectionAction_Sobel.setObjectName("edgeDetectionAction_Sobel")
        self.edgeDetectionAction_Scharr = QtWidgets.QAction(MainWindow)
        self.edgeDetectionAction_Scharr.setEnabled(False)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/three.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.edgeDetectionAction_Scharr.setIcon(icon15)
        self.edgeDetectionAction_Scharr.setShortcutVisibleInContextMenu(True)
        self.edgeDetectionAction_Scharr.setObjectName("edgeDetectionAction_Scharr")
        self.edgeDetectionAction_Prewitt = QtWidgets.QAction(MainWindow)
        self.edgeDetectionAction_Prewitt.setEnabled(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("icons/four.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.edgeDetectionAction_Prewitt.setIcon(icon16)
        self.edgeDetectionAction_Prewitt.setShortcutVisibleInContextMenu(True)
        self.edgeDetectionAction_Prewitt.setObjectName("edgeDetectionAction_Prewitt")
        self.menuExport_As.addAction(self.fileAction_exportAsSource)
        self.menuExport_As.addAction(self.fileAction_exportAsOutput)
        self.menuFile.addAction(self.fileAction_openSource)
        self.menuFile.addAction(self.fileAction_saveOutput)
        self.menuFile.addAction(self.fileAction_saveAsOutput)
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.fileAction_Exit)
        self.menuClear.addAction(self.editAction_clearSource)
        self.menuClear.addAction(self.editAction_clearOutput)
        self.menuEdit.addAction(self.menuClear.menuAction())
        self.menuEdit.addAction(self.editAction_undoOutput)
        self.menuEdit.addAction(self.editAction_redoOutput)
        self.menuConversion.addAction(self.conversionAction_RGBtoGrayscale)
        self.menuConversion.addAction(self.conversionAction_RGBtoHSV)
        self.menuSegmentation.addAction(self.segmentationAction_multiOtsuThresholding)
        self.menuSegmentation.addAction(self.segmentationAction_chanVeseSegmentation)
        self.menuSegmentation.addAction(self.segmentationAction_morphologicalSnakes)
        self.menuEdge_Detection.addAction(self.edgeDetectionAction_Roberts)
        self.menuEdge_Detection.addAction(self.edgeDetectionAction_Sobel)
        self.menuEdge_Detection.addAction(self.edgeDetectionAction_Scharr)
        self.menuEdge_Detection.addAction(self.edgeDetectionAction_Prewitt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuConversion.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())
        self.sourceOutputToolbar.addAction(self.fileAction_openSource)
        self.sourceOutputToolbar.addAction(self.fileAction_exportAsSource)
        self.sourceOutputToolbar.addAction(self.editAction_clearSource)
        self.sourceOutputToolbar.addSeparator()
        self.sourceOutputToolbar.addAction(self.fileAction_saveOutput)
        self.sourceOutputToolbar.addAction(self.fileAction_saveAsOutput)
        self.sourceOutputToolbar.addAction(self.fileAction_exportAsOutput)
        self.sourceOutputToolbar.addAction(self.editAction_undoOutput)
        self.sourceOutputToolbar.addAction(self.editAction_redoOutput)
        self.sourceOutputToolbar.addAction(self.editAction_clearOutput)
        self.operationsToolBar.addAction(self.conversionAction_RGBtoGrayscale)
        self.operationsToolBar.addAction(self.conversionAction_RGBtoHSV)
        self.operationsToolBar.addSeparator()
        self.operationsToolBar.addAction(self.segmentationAction_multiOtsuThresholding)
        self.operationsToolBar.addAction(self.segmentationAction_chanVeseSegmentation)
        self.operationsToolBar.addAction(self.segmentationAction_morphologicalSnakes)
        self.operationsToolBar.addSeparator()
        self.operationsToolBar.addAction(self.edgeDetectionAction_Roberts)
        self.operationsToolBar.addAction(self.edgeDetectionAction_Sobel)
        self.operationsToolBar.addAction(self.edgeDetectionAction_Scharr)
        self.operationsToolBar.addAction(self.edgeDetectionAction_Prewitt)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputLabel.setText(_translate("MainWindow", "INPUT"))
        self.outputLabel.setText(_translate("MainWindow", "OUTPUT"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_As.setTitle(_translate("MainWindow", "Export As"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuConversion.setTitle(_translate("MainWindow", "Conversion"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.sourceOutputToolbar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.operationsToolBar.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.fileAction_openSource.setText(_translate("MainWindow", "Open Source"))
        self.fileAction_openSource.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.fileAction_saveOutput.setText(_translate("MainWindow", "Save Output"))
        self.fileAction_saveAsOutput.setText(_translate("MainWindow", "Save As Output"))
        self.fileAction_exportAsSource.setText(_translate("MainWindow", "Source"))
        self.fileAction_exportAsOutput.setText(_translate("MainWindow", "Output"))
        self.fileAction_Exit.setText(_translate("MainWindow", "Exit"))
        self.fileAction_Exit.setShortcut(_translate("MainWindow", "Shift+F4"))
        self.editAction_undoOutput.setText(_translate("MainWindow", "Undo Output"))
        self.editAction_undoOutput.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.editAction_redoOutput.setText(_translate("MainWindow", "Redo Output"))
        self.editAction_redoOutput.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.editAction_clearSource.setText(_translate("MainWindow", "Source"))
        self.editAction_clearSource.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.editAction_clearOutput.setText(_translate("MainWindow", "Output"))
        self.editAction_clearOutput.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))
        self.conversionAction_RGBtoGrayscale.setText(_translate("MainWindow", "RGB to Grayscale"))
        self.conversionAction_RGBtoHSV.setText(_translate("MainWindow", "RGB to HSV"))
        self.segmentationAction_multiOtsuThresholding.setText(_translate("MainWindow", "Multi-Otsu Thresholding"))
        self.segmentationAction_chanVeseSegmentation.setText(_translate("MainWindow", "Chan-Vese Segmentation"))
        self.segmentationAction_morphologicalSnakes.setText(_translate("MainWindow", "Morphological Snakes"))
        self.edgeDetectionAction_Roberts.setText(_translate("MainWindow", "Roberts"))
        self.edgeDetectionAction_Sobel.setText(_translate("MainWindow", "Sobel"))
        self.edgeDetectionAction_Scharr.setText(_translate("MainWindow", "Scharr"))
        self.edgeDetectionAction_Prewitt.setText(_translate("MainWindow", "Prewitt"))
