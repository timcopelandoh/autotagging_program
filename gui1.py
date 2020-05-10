# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(754, 520)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(9, 15, 511, 341))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 380, 131, 121))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 380, 131, 121))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 380, 131, 121))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(460, 380, 131, 121))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(610, 380, 131, 121))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(600, 180, 131, 71))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Main"))
        self.label_2.setText(_translate("Form", "thumbnail1"))
        self.label_3.setText(_translate("Form", "thumbnail2"))
        self.label_4.setText(_translate("Form", "thumbnail3"))
        self.label_5.setText(_translate("Form", "thumbnail4"))
        self.label_6.setText(_translate("Form", "thumbnail5"))
        self.label_7.setText(_translate("Form", "Info"))


        img = QtGui.QPixmap('wedding.jpg')
        img = img.scaledToWidth(50)
        img = img.scaledToHeight(125)

        self.label_2.setPixmap(img)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

