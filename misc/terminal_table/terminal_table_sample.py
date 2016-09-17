from __future__ import print_function
from terminaltables import AsciiTable

from colorclass import Color

class ColoredText(object):
	def __init__(self,txt,color=None):
		self._txt = txt
		self._color = color

	@property
	def text(self):
		return self._txt

	@text.setter
	def text(self,_txt):
		self._txt = str(_txt)

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, _color):
		#print("Setting color to {0}".format(_color))
		self._color = _color
	
	def __repr__(self):
		return Color.colorize(self._color,self._txt)

class ColoredTimeText(ColoredText):
	def __init__(self,txt,color=None):
		super().__init__(txt,color)
		self.text = txt
	
	@ColoredText.text.setter
	def text(self,_txt):
		#print("Setting text to {0}".format(_txt))
		val = int(_txt)
		if val % 2 == 0:
			self.color = 'green'
		else:
			self.color = 'red'
		self._txt = str(val)
	
class ColoredPriceText(ColoredText):
	def __init__(self,txt,color=None):
		super().__init__(txt,color)
		self.text = txt
	
	@ColoredText.text.setter
	def text(self,_txt):
		val = float(_txt)
		#print("val={0},txt={1}".format(val,self._txt))
		if val >= float(self.text):
			self.color = 'green'
		else:
			self.color = 'red'
		self._txt = str(val) 

table_data = [
    ['Time', 'Price'],
	['1','1.0'],
]

#from datetime import datetime
#now = int(datetime.now().time().strftime("%s"))

import time,random,os

now = lambda: int(round(time.time() * 1000))
current_milli_time = now()

table_data[1][0] = ColoredTimeText(current_milli_time)
table_data[1][1] = ColoredPriceText(random.randrange(0, 101))

for i in range(20):

	os.system('clear')
	
	table = AsciiTable(table_data)

	print(table.table)

	current_milli_time = now()

	table_data[1][0].text = current_milli_time
	table_data[1][1].text = random.randrange(0, 101)
	
	time.sleep(1)


