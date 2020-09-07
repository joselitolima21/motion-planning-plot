# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './programa/untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
import re
import random
import subprocess
# Essas
import matplotlib
matplotlib.use('Qt4Agg')
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
# -----
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tela1 = QtGui.QWidget()
        self.tela1.setObjectName(_fromUtf8("tela1"))
        self.pushButton_4 = QtGui.QPushButton(self.tela1)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 370, 111, 41))
        self.pushButton_4.setStyleSheet(_fromUtf8("box-shadow: 0 1px 0 #f0c14b;\n"
"border:  1px solid #a88734 #9c7e31 #846a29;;\n"
"border-radius: 3px;\n"
"background-color: qlineargradient(spread:pad, x1:0.514, y1:0, x2:0.514, y2:1, stop:0 #f7dfa5, stop:1 #f0c14b);"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.executeLaunch)
        self.pushButton_5 = QtGui.QPushButton(self.tela1)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 370, 111, 41))
        self.pushButton_5.setStyleSheet(_fromUtf8("box-shadow: 0 1px 0 rgba(255,255,255,.6);\n"
"border:  1px solid #adb1b8 #a2a6ac #8d9096;\n"
"border-radius: 3px;\n"
"background-color: qlineargradient(spread:pad, x1:0.514, y1:0, x2:0.514, y2:1, stop:0 #f7f8fa, stop:1 #e7e9ec);"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.killLaunch)
        self.Monitor = QtGui.QFrame(self.tela1)
        self.Monitor.setGeometry(QtCore.QRect(30, 180, 681, 121))
        self.Monitor.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Monitor.setFrameShadow(QtGui.QFrame.Raised)
        self.Monitor.setObjectName(_fromUtf8("Monitor"))
        self.label = QtGui.QLabel(self.Monitor)
        self.label.setGeometry(QtCore.QRect(20, 20, 311, 71))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tela1)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tela1)
        self.label_3.setGeometry(QtCore.QRect(70, 60, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tela1)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 611, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.widget = QtGui.QWidget(self.tela1)
        self.widget.setGeometry(QtCore.QRect(40, 40, 16, 16))
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(44, 44, 44);\n"
"border-radius: 8px;"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(self.tela1)
        self.widget_2.setGeometry(QtCore.QRect(40, 120, 16, 16))
        self.widget_2.setStyleSheet(_fromUtf8("background-color: rgb(44, 44, 44);\n"
"border-radius: 8px;"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.tabWidget.addTab(self.tela1, _fromUtf8(""))
        self.tela2 = QtGui.QWidget()
        self.tela2.setObjectName(_fromUtf8("tela2"))
        self.frame_2 = QtGui.QFrame(self.tela2)
        self.frame_2.setGeometry(QtCore.QRect(310, 10, 461, 511))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))

        # Para adicionar o gráfico
        self.mapLayout = QtGui.QVBoxLayout(self.frame_2)
        self.sc = MplCanvas(self, width=4.61, height=5.11, dpi=100)
        self.mapToolbar = NavigationToolbar(self.sc,self.frame_2)
        self.mapLayout.addWidget(self.mapToolbar)
        self.mapLayout.addWidget(self.sc)

        # Adicionando os dados
        self.data = []
        self.sc.xdata = []
        self.sc.ydata = []
        self.sc.ydata1 = []
        self.sc.ydata2 = []
        self.sc.ydata3 = []
        self.sc.ydata4 = []
        self.sc.ydata5 = []
        self.sc.ydata6 = []
        self._plot_ref = None
        self._plot_ref1 = None
        self._plot_ref2 = None
        self._plot_ref3 = None
        self._plot_ref4 = None
        self._plot_ref5 = None
        self._plot_ref6 = None
        self.sc.show()

        self.tabWidget_2 = QtGui.QTabWidget(self.tela2)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 10, 291, 511))
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 241, 311))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_16.addWidget(self.label_18)
        self.lineEdit_17 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.horizontalLayout_16.addWidget(self.lineEdit_17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_10.addWidget(self.label_12)
        self.lineEdit_11 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.horizontalLayout_10.addWidget(self.lineEdit_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_17.addWidget(self.label_19)
        self.lineEdit_18 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.horizontalLayout_17.addWidget(self.lineEdit_18)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_18.addWidget(self.label_20)
        self.lineEdit_19 = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.horizontalLayout_18.addWidget(self.lineEdit_19)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 400, 111, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.moveTheRobot)
        self.tabWidget_2.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 241, 311))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_11.addWidget(self.label_13)
        self.lineEdit_12 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.horizontalLayout_11.addWidget(self.lineEdit_12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_8.addWidget(self.label_10)
        self.lineEdit_9 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.horizontalLayout_8.addWidget(self.lineEdit_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_9.addWidget(self.label_11)
        self.lineEdit_10 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.horizontalLayout_9.addWidget(self.lineEdit_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_15.addWidget(self.label_17)
        self.lineEdit_16 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.horizontalLayout_15.addWidget(self.lineEdit_16)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_12.addWidget(self.label_14)
        self.lineEdit_13 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.horizontalLayout_12.addWidget(self.lineEdit_13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_14.addWidget(self.label_16)
        self.lineEdit_15 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.horizontalLayout_14.addWidget(self.lineEdit_15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_13.addWidget(self.label_15)
        self.lineEdit_14 = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.horizontalLayout_13.addWidget(self.lineEdit_14)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(80, 400, 111, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget_2.addTab(self.tab_2, _fromUtf8(""))
        self.tabWidget.addTab(self.tela2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Motion Planning Plot", None))
        self.tela1.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        self.pushButton_4.setText(_translate("MainWindow", "Iniciar RViz", None))
        self.pushButton_5.setText(_translate("MainWindow", "Encerrar RViz", None))
        self.label_2.setText(_translate("MainWindow", "Nesta aba pode-se iniciar ou encerrrar o RViz,", None))
        self.label_3.setText(_translate("MainWindow", "que está configurado com o robô Panda", None))
        self.label_4.setText(_translate("MainWindow", "E então será possivel exeutar o planejamento de movimento", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tela1), _translate("MainWindow", "Conexão", None))
        self.label_18.setText(_translate("MainWindow", "Valor de X", None))
        self.label_12.setText(_translate("MainWindow", "Valor de Y", None))
        self.label_19.setText(_translate("MainWindow", "Valor de Z", None))
        self.label_20.setText(_translate("MainWindow", "Orientação", None))
        self.pushButton_2.setText(_translate("MainWindow", "Executar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Posição cartesiana", None))
        self.label_13.setText(_translate("MainWindow", "Joint 1", None))
        self.label_10.setText(_translate("MainWindow", "Joint 2", None))
        self.label_11.setText(_translate("MainWindow", "Joint 3", None))
        self.label_17.setText(_translate("MainWindow", "Joint 4", None))
        self.label_14.setText(_translate("MainWindow", "Joint 5", None))
        self.label_16.setText(_translate("MainWindow", "Joint 6", None))
        self.label_15.setText(_translate("MainWindow", "Joint 7", None))
        self.pushButton.setText(_translate("MainWindow", "Executar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Juntas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tela2), _translate("MainWindow", "Planejamento de movimento", None))

    def executeLaunch(self):
        self.threadRviz = rvizThread(self.label)
        self.threadRviz.start()
    
    def killLaunch(self):
        subprocess.call('kill -INT `cat /tmp/demo.pid`',shell =True)
        subprocess.call('killall -9 roslaunch',shell =True)
        self.label.setText('O RViz foi finalizado com sucesso!')

    def moveTheRobot(self):
        self.threadMove = moveThread(self)
        self.threadMove.start()
        

class rvizThread(QtCore.QThread):

    def __init__(self,label):
        self.label = label
        super(rvizThread,self).__init__(label)

    def run(self):
        self.label.setText('O RViz foi inicializado com sucesso! \nAguarde alguns segundos para ele aparecer')
        return_code = subprocess.call('roslaunch --pid=/tmp/demo.pid panda_moveit_config demo.launch',shell=True)

class moveThread(QtCore.QThread):

    def __init__(self,ref):
        self.ref = ref
        super(moveThread,self).__init__()

    def run(self):
        cmd = 'rosrun panda_moveit_config move.py' 

        #return_code = subprocess.call(cmd,shell=True)
        #return_code = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)

        def printResult(command):
            process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            while True:
                line = process.stdout.readline().rstrip()
                if not line:
                    break
                if not re.compile('\(').match(line):
                    pass
                yield line
        i = 0
        for path in printResult(cmd):
            if (i > 2):
                currentTuple = eval(path)
                self.ref.data.append(currentTuple)
            
                self.ref.sc.xdata = self.ref.sc.xdata + [i-3]
                self.ref.sc.ydata = self.ref.sc.ydata + [currentTuple[0]]
                self.ref.sc.ydata1 = self.ref.sc.ydata1 + [currentTuple[1]]
                self.ref.sc.ydata2 = self.ref.sc.ydata2 + [currentTuple[2]]
                self.ref.sc.ydata3 = self.ref.sc.ydata3 + [currentTuple[3]]
                self.ref.sc.ydata4 = self.ref.sc.ydata4 + [currentTuple[4]]
                self.ref.sc.ydata5 = self.ref.sc.ydata5 + [currentTuple[5]]
                self.ref.sc.ydata6 = self.ref.sc.ydata6 + [currentTuple[6]]
            
                if self.ref._plot_ref is None:
                    plot_refs = self.ref.sc.axes.plot(self.ref.sc.xdata, self.ref.sc.ydata, 'r',label='Joint 1')
                    plot_refs1 = self.ref.sc.axes.plot(self.ref.sc.xdata, self.ref.sc.ydata1, 'g',label='Joint 2')
                    plot_refs2 = self.ref.sc.axes.plot(self.ref.sc.xdata, self.ref.sc.ydata2, 'b',label='Joint 3')
                    plot_refs3 = self.ref.sc.axes.plot(self.ref.sc.xdata, self.ref.sc.ydata3, 'y',label='Joint 4')
                    plot_refs4 = self.ref.sc.axes.plot(self.ref.sc.xdata, self.ref.sc.ydata4, 'k',label='Joint 5')
                    plot_refs5 = self.ref.sc.axes.plot(self.ref.sc.xdata, self.ref.sc.ydata5, 'c',label='Joint 6')
                    plot_refs6 = self.ref.sc.axes.plot(self.ref.sc.xdata, self.ref.sc.ydata6, 'm',label='Joint 7')
                    self.ref._plot_ref = plot_refs[0]
                    self.ref._plot_ref1 = plot_refs1[0]
                    self.ref._plot_ref2 = plot_refs2[0]
                    self.ref._plot_ref3 = plot_refs3[0]
                    self.ref._plot_ref4 = plot_refs4[0]
                    self.ref._plot_ref5 = plot_refs5[0]
                    self.ref._plot_ref6 = plot_refs6[0]
                    self.ref.sc.axes.legend(loc=2,fontsize='x-small')
                else:
                    self.ref._plot_ref.set_xdata(self.ref.sc.xdata)
                    self.ref._plot_ref.set_ydata(self.ref.sc.ydata)

                
                    self.ref._plot_ref1.set_xdata(self.ref.sc.xdata)
                    self.ref._plot_ref1.set_ydata(self.ref.sc.ydata1)
                    self.ref._plot_ref2.set_xdata(self.ref.sc.xdata)
                    self.ref._plot_ref2.set_ydata(self.ref.sc.ydata2)
                    self.ref._plot_ref3.set_xdata(self.ref.sc.xdata)
                    self.ref._plot_ref3.set_ydata(self.ref.sc.ydata3)
                    self.ref._plot_ref4.set_xdata(self.ref.sc.xdata)
                    self.ref._plot_ref4.set_ydata(self.ref.sc.ydata4)
                    self.ref._plot_ref5.set_xdata(self.ref.sc.xdata)
                    self.ref._plot_ref5.set_ydata(self.ref.sc.ydata5)
                    self.ref._plot_ref6.set_xdata(self.ref.sc.xdata)
                    self.ref._plot_ref6.set_ydata(self.ref.sc.ydata6)
                    self.ref.sc.axes.legend(loc=2,fontsize='x-small')

                maximosList = []    
                maximosList.append(max(self.ref.sc.ydata))
                maximosList.append(max(self.ref.sc.ydata1))
                maximosList.append(max(self.ref.sc.ydata2))
                maximosList.append(max(self.ref.sc.ydata3))
                maximosList.append(max(self.ref.sc.ydata4))
                maximosList.append(max(self.ref.sc.ydata5))
                maximosList.append(max(self.ref.sc.ydata6))
                
                minumusList = []    
                minumusList.append(min(self.ref.sc.ydata))
                minumusList.append(min(self.ref.sc.ydata1))
                minumusList.append(min(self.ref.sc.ydata2))
                minumusList.append(min(self.ref.sc.ydata3))
                minumusList.append(min(self.ref.sc.ydata4))
                minumusList.append(min(self.ref.sc.ydata5))
                minumusList.append(min(self.ref.sc.ydata6))

                self.ref.sc.axes.set_xlim(-0.1,self.ref.sc.xdata[-1])
                self.ref.sc.axes.set_ylim(min(minumusList),max(maximosList))

                self.ref.sc.draw()
            i = i + 1


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window =  QtGui.QMainWindow()
    classe = Ui_MainWindow()
    classe.setupUi(window)
    window.show()
    sys.exit(app.exec_())