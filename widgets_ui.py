# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 581)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 6, 2, 3)
        self.top_label = QtWidgets.QLabel(self.centralwidget)
        self.top_label.setObjectName("top_label")
        self.gridLayout.addWidget(self.top_label, 1, 0, 1, 2)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 1, 9, 9, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 6, 1, 1)
        self.bottom_line0 = QtWidgets.QFrame(self.centralwidget)
        self.bottom_line0.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottom_line0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bottom_line0.setObjectName("bottom_line0")
        self.gridLayout.addWidget(self.bottom_line0, 11, 5, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 1, 4, 9, 1)
        self.buildButton = QtWidgets.QPushButton(self.centralwidget)
        self.buildButton.setObjectName("buildButton")
        self.gridLayout.addWidget(self.buildButton, 6, 11, 1, 2)

        self.Tc_list = QtWidgets.QTreeView(self.centralwidget)
        self.Tc_list.setAutoFillBackground(True)
        self.Tc_list.setObjectName("Tc_list")


        self.gridLayout.addWidget(self.Tc_list, 3, 5, 7, 4)
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setObjectName("runButton")
        self.gridLayout.addWidget(self.runButton, 9, 11, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 11, 1, 1)
        self.top_title_label = QtWidgets.QLabel(self.centralwidget)
        self.top_title_label.setObjectName("top_title_label")
        self.gridLayout.addWidget(self.top_title_label, 0, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 9, 12, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 12, 12, 1, 1)
        self.cleanButton = QtWidgets.QPushButton(self.centralwidget)
        self.cleanButton.setObjectName("cleanButton")
        self.gridLayout.addWidget(self.cleanButton, 3, 11, 1, 2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 0, 4, 1, 2)
        self.top_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.top_lineEdit.setObjectName("top_lineEdit")
        self.gridLayout.addWidget(self.top_lineEdit, 1, 2, 1, 2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 10, 1, 1)
        self.bottom_line1 = QtWidgets.QFrame(self.centralwidget)
        self.bottom_line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.bottom_line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.bottom_line1.setObjectName("bottom_line1")
        self.gridLayout.addWidget(self.bottom_line1, 11, 8, 1, 5)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 7, 1, 2)
        self.preprocButton = QtWidgets.QPushButton(self.centralwidget)
        self.preprocButton.setObjectName("preprocButton")
        self.gridLayout.addWidget(self.preprocButton, 5, 11, 1, 2)
        self.info_output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.info_output.setEnabled(True)
        self.info_output.setReadOnly(True)
        self.info_output.setObjectName("info_output")
        self.gridLayout.addWidget(self.info_output, 13, 5, 1, 8)
        self.addLinksButton = QtWidgets.QPushButton(self.centralwidget)
        self.addLinksButton.setObjectName("addLinksButton")
        self.gridLayout.addWidget(self.addLinksButton, 4, 11, 1, 2)
        self.top_line0 = QtWidgets.QFrame(self.centralwidget)
        self.top_line0.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_line0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_line0.setObjectName("top_line0")
        self.gridLayout.addWidget(self.top_line0, 0, 0, 1, 1)

        self.left_list = QtWidgets.QTreeView(self.centralwidget)
        self.left_list.setAutoFillBackground(True)
        self.left_list.setObjectName("left_list")


        self.gridLayout.addWidget(self.left_list, 3, 0, 11, 4)
        self.top_line1 = QtWidgets.QFrame(self.centralwidget)
        self.top_line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.top_line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_line1.setObjectName("top_line1")
        self.gridLayout.addWidget(self.top_line1, 0, 3, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 12, 1, 1)
        self.right_option_file = QtWidgets.QLineEdit(self.centralwidget)
        self.right_option_file.setEnabled(True)
        self.right_option_file.setReadOnly(True)
        self.right_option_file.setObjectName("right_option_file")
        self.gridLayout.addWidget(self.right_option_file, 1, 12, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 11, 1, 1)
        self.ClassOptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ClassOptionLabel.setObjectName("ClassOptionLabel")
        self.gridLayout.addWidget(self.ClassOptionLabel, 8, 12, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "info output"))
        self.top_label.setText(_translate("MainWindow", "rl_input"))
        self.label_2.setText(_translate("MainWindow", "TC"))
        self.buildButton.setText(_translate("MainWindow", "build_sim_script"))
        self.runButton.setText(_translate("MainWindow", "RUN"))
        self.label.setText(_translate("MainWindow", "option select"))
        self.top_title_label.setText(_translate("MainWindow", "File"))
        self.clearButton.setText(_translate("MainWindow", "clear"))
        self.cleanButton.setText(_translate("MainWindow", "clean"))
        self.preprocButton.setText(_translate("MainWindow", "preproc"))
        self.addLinksButton.setText(_translate("MainWindow", "add_links"))
        self.label_4.setText(_translate("MainWindow", "option file"))
        self.ClassOptionLabel.setText(_translate("MainWindow", "class option"))