#!/usr/bin/env python3
import sys
import os 
import shutil

sys.argv[1]

Array_of_file = ['']

os.mkdir('Indexed_Files')

for eachArg in sys.argv:
	if "py" in eachArg:
		print ('pass')
	else:
		shutil.move(eachArg,'Indexed_Files')
		print('into the folder')


