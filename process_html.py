#!/usr/bin/python
# coding=utf-8

import sys
import os

with open('README_number.html', 'r') as f:
	str_html = f.read()

title = '<title>README_number</title>'
indexOfTitle = str_html.find(title)

if indexOfTitle != -1 :
	title_length = len(title)
	new_str_html = str_html[:indexOfTitle + title_length] + '\n' + '<link rel="shortcut icon" href=" image/favicon.ico" />' + str_html[indexOfTitle + title_length:]
	new_str_html = new_str_html.replace('<title>README_number</title>', '<title>Cocos 资料大全</title>')
	with open('index.html', 'w') as f:
		f.write(new_str_html)
else :
	print 'title is not found'
	sys.exit()

os.remove('README_number.html')
os.remove('README_number.md')