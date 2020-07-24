#-*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from uiEvents.AWindowBase import *
from uiDefines.Ui_MainWindow import *
import os
import sys
import pathlib

'''
    这是MainWindow窗体的实现类
'''
#class EventMainWindowImpl(IWindowImpl):
class EventMainWindowImpl(IWindowImplM):
    '''
       初始化所有数据(抽象函数)
    '''
    def initUIAndData(self):
        self.initEvents()

    '''
        初始化事件
    '''
    def initEvents(self):
        self.uiObj.btnTestA.clicked.connect(self.btnTestAClicked)
        self.uiObj.btnTestB.clicked.connect(self.btnTestBClicked)
        self.uiObj.btnTestC.clicked.connect(self.btnTestCClicked)

    '''
       返回UI定义类的实例(例如uiDefines/Ui_MainWindow.py的实例,抽象函数)
    '''
    def getUIDefineObject(self):
        return Ui_MainWindow()

    '''
        按钮A
    '''
    def btnTestAClicked(self,e):
        self.uiObj.txtContent.setText('aaaaaaaaaaaaa')

    '''
        按钮B
    '''
    def btnTestBClicked(self,e):
        self.uiObj.txtContent.setText('bbbbbbbbbbbbb')

    '''
        按钮C
    '''
    def btnTestCClicked(self,e):
        self.uiObj.txtContent.setText('ccccccccccccc')
