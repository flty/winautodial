# !/usr/bin/env python
# -*- coding:utf-8 -*- 


import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8') 
# os.path.dirname(__file__)

class autodial(object):
	def __init__(self, user, password, num, pbk = 'autodial.pbk'):
		self._user = user
		self._password = password
		self._num = num
		self._phoneBook = pbk
		self._disconnetStr = r'rasdial "autodial" /d /phonebook:%s' % os.path.join(os.path.dirname(__file__), self._phoneBook)
		self._connectStr = r'rasdial "autodial" %s %s /phonebook:%s' % (self._user, self._password, os.path.join(os.path.dirname( __file__ ), self._phoneBook))

	def connect(self):
		num  = self._num
		num1 = 0
		urls = ['www.163.com','www.baidu.com','www.sina.com.cn']
		res = []
		while True:
			for x in urls:
				try:
					r = os.popen(r'ping %s' % x).readlines()
					if len(r) >= 4:
						print('you netword is OK!')
						return 0
				except :
					break
			print('rasdial connecting network automaticly...')

			for lines in os.popen(self._disconnetStr):
				print(lines)
			for lines in os.popen(self._connectStr):
				print(lines)
			time.sleep(10)
			num1 += 1
			if num1 >= num:
				print('try to connect Max times ago, please check you hardwork!')
				return 1

if __name__ == '__main__':

	ad = autodial('user', '1234', 10)
	ad.connect()

	print('OK, please enjoy you internet surfing......')
