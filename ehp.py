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

def get_ehp(stats):
	EVA=0
	HP=0
	LUCK=0
	if 'Evasion' in stats and stats['Evasion'] !='':
		EVA=int(stats['Evasion'])
	if 'Health' in stats and stats['Health'] !='':
		HP=int(stats['Health'])
	if 'Luck' in stats and stats['Luck'] !='':
		LUCK=int(stats['Luck'])

	DR=0
	eHIT=100
	eLUCK=50
	danger=1
	air_superiority=1
	EVA_rate_buff=0
	EVA_stat_buff=0
	burn_percent=1
	bullet_count=0
	burn_reset=1
	burn_coeff=1
	AVI_DR=0
	if stats['Armor'] == 'Heavy':
		armor_mod=0.25
	elif stats['Armor'] == 'Medium':
		armor_mod=0.55
	elif stats['Armor'] == 'Light':
		armor_mod=1
	else:
		confess("Unknown armor type: "+stats['Armor'])

	ehp = HP/(1-DR)/((0.1+(eHIT/(eHIT+(EVA*(1+EVA_stat_buff)+2)))+((eLUCK-LUCK)/1000)-(EVA_rate_buff)))/armor_mod
	return ehp


f=open('al.json', 'r')
db=json.loads(f.read())
f.close()
for ship in db:
	levels=db[ship]
	for level in levels:
		if level != str(120):
			continue
		stat=levels[level]
		ehp=get_ehp(stat)
		print(str(int(ehp))+' '+ship+'('+stat['Type']+')')
