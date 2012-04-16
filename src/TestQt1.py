#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
import sys
from PyQt4.QtGui import *  # компоненты интерфейса
 
# Каждое приложение должно создать объект QApplication
# sys.argv - список аргументов командной строки
a = QApplication(sys.argv)
 
# QWidget - базовый класс для всех объектов интерфейса
# пользователя; если использовать для виджета конструктор
# без родителя, такой виджет станет окном
w = QWidget()
 
w.resize(320, 240)  # изменить размеры виджета
w.setWindowTitle("Hello, World!")  # установить заголовок
w.show()  # отобразить окно на экране
 
sys.exit(a.exec_())  # запуск основного цикла приложения

if __name__ == "__main__":
    print ('Hello World')
