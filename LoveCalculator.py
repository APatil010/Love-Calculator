#! /usr/bin/python

import sys,os
from PyQt4 import QtGui,QtCore,uic

form_class = uic.loadUiType("LoveCalculator.ui")[0]

class TextEditor(QtGui.QMainWindow,form_class):
	temp = []
	charactersList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	nameOfFirstPerson = ""
	nameOfSecondPerson = ""
	sumOfNumbers = 0
	totalCount = 0

	def __init__(self,parent=None):
		QtGui.QMainWindow.__init__(self,parent)
		self.setupUi(self)
		self.loveButton.clicked.connect(self.loveButton_clicked)
		self.clearButton.clicked.connect(self.clearButton_clicked)
		self.firstPersonName.setFocus()


	def loveButton_clicked(self):
		nameOfFirstPerson = self.firstPersonName.text()
		nameOfSecondPerson = self.secondPersonName.text()

		for i in nameOfFirstPerson:
			if self.charactersList.__contains__(i):
				self.temp.append(self.charactersList.index(i) + 1)

		for i in nameOfSecondPerson:
			if self.charactersList.__contains__(i):
				self.temp.append(self.charactersList.index(i) + 1)

		
		for i in self.temp:
			self.sumOfNumbers += int(i)

		lovePercentage = ((self.sumOfNumbers) % 10 ) * 10
		loveString = "Love is : " + str(lovePercentage) + "%"

		self.outputLabel.setText(loveString)
		self.loveButton.setDisabled(1)

	def clearButton_clicked(self):
		self.firstPersonName.clear()
		self.secondPersonName.clear()
		self.nameOfFirstPerson = ""
		self.nameOfSecondPerson = ""
		self.sumOfNumbers = 0
		self.totalCount = 0
		self.temp = []
		self.loveButton.setDisabled(0)
		self.outputLabel.setText("")
		self.firstPersonName.setFocus()


app = QtGui.QApplication(sys.argv)
Editor = TextEditor(None)
Editor.show()
app.exec_()
