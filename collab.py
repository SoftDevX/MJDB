# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_colab.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddColab_(object):
    def setupUi(self, AddColab_):
        AddColab_.setObjectName("AddColab_")
        AddColab_.resize(800, 400)
        AddColab_.setMinimumSize(QtCore.QSize(800, 400))
        AddColab_.setMaximumSize(QtCore.QSize(800, 400))
        AddColab_.setStyleSheet("")
        self.frame = QtWidgets.QFrame(AddColab_)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 71))
        self.frame.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelffff = QtWidgets.QLabel(self.frame)
        self.labelffff.setGeometry(QtCore.QRect(20, 20, 115, 44))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(25)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.labelffff.setFont(font)
        self.labelffff.setObjectName("labelffff")
        self.l_date = QtWidgets.QLabel(self.frame)
        self.l_date.setGeometry(QtCore.QRect(560, 20, 121, 44))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.l_date.setFont(font)
        self.l_date.setObjectName("l_date")
        self.l_time = QtWidgets.QLabel(self.frame)
        self.l_time.setGeometry(QtCore.QRect(680, 20, 121, 44))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        self.l_time.setFont(font)
        self.l_time.setObjectName("l_time")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.user = QtWidgets.QLabel(self.frame)
        self.user.setGeometry(QtCore.QRect(280, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(16)
        self.user.setFont(font)
        self.user.setText("")
        self.user.setObjectName("user")
        self.layoutWidget = QtWidgets.QWidget(AddColab_)
        self.layoutWidget.setGeometry(QtCore.QRect(430, 80, 261, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(62)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.first_name = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.first_name.setFont(font)
        self.first_name.setStyleSheet("background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #9f9f9f;\n"
"")
        self.first_name.setObjectName("first_name")
        self.horizontalLayout_3.addWidget(self.first_name)
        self.layoutWidget1 = QtWidgets.QWidget(AddColab_)
        self.layoutWidget1.setGeometry(QtCore.QRect(430, 140, 261, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(85)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.last_name = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.last_name.setFont(font)
        self.last_name.setStyleSheet("background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #9f9f9f;\n"
"")
        self.last_name.setObjectName("last_name")
        self.horizontalLayout_4.addWidget(self.last_name)
        self.layoutWidget2 = QtWidgets.QWidget(AddColab_)
        self.layoutWidget2.setGeometry(QtCore.QRect(430, 200, 261, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(49)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.pass_ = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_.setFont(font)
        self.pass_.setStyleSheet("background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid #9f9f9f;\n"
"")
        self.pass_.setText("")
        self.pass_.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_.setObjectName("pass_")
        self.horizontalLayout_5.addWidget(self.pass_)
        self.tableWidget = QtWidgets.QTableWidget(AddColab_)
        self.tableWidget.setGeometry(QtCore.QRect(5, 81, 421, 311))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(139)
        self.tableWidget.verticalHeader().setVisible(False)
        self.wrong1 = QtWidgets.QLabel(AddColab_)
        self.wrong1.setGeometry(QtCore.QRect(440, 250, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.wrong1.setFont(font)
        self.wrong1.setStyleSheet("color: rgb(255, 0, 0);")
        self.wrong1.setText("")
        self.wrong1.setObjectName("wrong1")
        self.btn_remove = QtWidgets.QPushButton(AddColab_)
        self.btn_remove.setGeometry(QtCore.QRect(680, 350, 111, 28))
        self.btn_remove.setStyleSheet("")
        self.btn_remove.setObjectName("btn_remove")
        self.btn_add = QtWidgets.QPushButton(AddColab_)
        self.btn_add.setGeometry(QtCore.QRect(440, 350, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("")
        self.btn_add.setObjectName("btn_add")
        self.btn_edit = QtWidgets.QPushButton(AddColab_)
        self.btn_edit.setGeometry(QtCore.QRect(560, 350, 111, 28))
        self.btn_edit.setStyleSheet("")
        self.btn_edit.setObjectName("btn_edit")

        self.retranslateUi(AddColab_)
        QtCore.QMetaObject.connectSlotsByName(AddColab_)

    def retranslateUi(self, AddColab_):
        _translate = QtCore.QCoreApplication.translate
        AddColab_.setWindowTitle(_translate("AddColab_", "AddColab_"))
        self.labelffff.setText(_translate("AddColab_", "MJDB"))
        self.l_date.setText(_translate("AddColab_", "00/00/00"))
        self.l_time.setText(_translate("AddColab_", "00:00:00"))
        self.label_5.setText(_translate("AddColab_", "Utilisateur:"))
        self.label_2.setText(_translate("AddColab_", "Prénom"))
        self.first_name.setPlaceholderText(_translate("AddColab_", "Prénom"))
        self.label_3.setText(_translate("AddColab_", "Nom"))
        self.last_name.setPlaceholderText(_translate("AddColab_", "Nom"))
        self.label_4.setText(_translate("AddColab_", "Password"))
        self.pass_.setPlaceholderText(_translate("AddColab_", "Password"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AddColab_", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AddColab_", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AddColab_", "Password"))
        self.btn_remove.setText(_translate("AddColab_", "Supprimer"))
        self.btn_add.setText(_translate("AddColab_", "Ajouter"))
        self.btn_edit.setText(_translate("AddColab_", "Editer"))
