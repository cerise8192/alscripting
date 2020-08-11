#!/usr/bin/python3

import sys
import datetime
import requests
import json
import time
import re
from bs4 import BeautifulSoup,NavigableString

def debug_html(tag, indent=0, path=''):
	if tag is None:
		return
	indent_str=''
	for i in range(0, indent):
		indent_str=indent_str+'   '

	if path != '':
		path=path+'->'
	path=path+str(tag.name)

	if str(tag.name) != 'None':
		print(indent_str+path)
		printme=indent_str+'<'+str(tag.name)
		for attr in tag.attrs:
			try:
				printme=printme+' '+str(attr)+'='+str(tag[attr])
			except TypeError as e:
				pass
		printme=printme+'>'
		if tag.string is not None and len(tag.string) > 0:
			if tag.name != 'style' and tag.name != 'script':
				printme=printme+' '+tag.string
		print(printme)

	try:
		i=0
		for child in tag.children:
			debug_html(child, indent+1, path+'['+str(i)+']')
			i=i+1
	except AttributeError as e:
		pass

def debug_dict(dict, indent, path=''):
	indent_str=''
	for i in range(0, indent):
		indent_str=indent_str+'   '
	for k in dict:
		print(indent_str+k)
		print(indent_str+path+'->'+k)
		debug(dict[k], indent+1, path+'->'+k)

def debug_array(dict, indent, path=''):
	indent_str=''
	for i in range(0, indent):
		indent_str=indent_str+'   '
	for k in range(0, len(dict)):
		print(indent_str+str(k))
		print(indent_str+path+'->'+str(k))
		debug(dict[k], indent+1, path+'->'+str(k))

def debug_str(dict, indent, path=''):
	indent_str=''
	for i in range(0, indent):
		indent_str=indent_str+'   '
	print(indent_str+dict)

def debug(dict, indent=0, path=''):
	if type(dict) == type({}):
		debug_dict(dict, indent, path)
	elif type(dict) == type([]):
		debug_array(dict, indent, path)
	elif type(dict) == type(''):
		debug_str(dict, indent, path)
	elif type(dict) == type(0):
		debug_str(str(dict), indent, path)
	else:
		print("Unknown type: "+str(type(dict)))
	

def get_stats_page():
	session=requests.Session()
	response=session.get('https://azurlane.koumakan.jp/List_of_Ships_by_Stats#Level_120')
	return BeautifulSoup(response.text, 'html.parser')

def get_columns(tag):
	columns=[]
	column=nav_tag(tag, [0, 0])
	while column.next_sibling is not None:
		if column.string is None:
			if column.img['alt'] is not None:
				columns.append(column.img['alt'])
			else:
				columns.append('')
		else:
			columns.append(column.string)
		column=column.next_sibling
	return columns

def parse(soup):
	db={}
	for ship_type in [16, 20, 24, 28, 32, 36, 40]:
		levels={}
		levels[1]=[2, 3, 5, 7, 11, 0, ship_type, 1, 2, 0]
		levels[100]=[2, 3, 5, 7, 11, 0, ship_type, 3, 2, 0]
		levels[120]=[2, 3, 5, 7, 11, 0, ship_type, 5, 2, 0]
		for level in levels:
			array=levels[level]
			tag=nav_tag(soup, array)
			stats=parse_table(tag)

			for stat in stats:
				name=stat['Ship Name']

				if name not in db:
					db[name]={}
				if level not in db[name]:
					db[name][level]={}
				db[name][level]=stat
	return db

def parse_table(soup):
	columns=get_columns(soup)
	stats=[]
	rows=nav_tag(soup, [2])
	while rows.next_sibling is not None:
		stat={}
		for i in range(0, len(columns)):
			td=nav_tag(rows, [i])
			if td is not None:
				print(columns[i]+' = '+td.string)
				stat[columns[i]]=str(td.string)
			else:
				stat[columns[i]]=''
		stats.append(stat)
		rows=rows.next_sibling
		while isinstance(rows, NavigableString):
			rows=rows.next_sibling
	return stats

def nav_tag(root, path):
	if len(path) == 0:
		return root
	i=0
	n=path.pop(0)
	for child in root.children:
		if i == n:
			return nav_tag(child, path)
		i=i+1
		

soup=get_stats_page()
db=json.dumps(parse(soup))
f=open('al.json', 'w')
f.write(db)
f.close()
