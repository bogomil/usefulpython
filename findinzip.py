'''
Imagine you have bunch of zip files containing bunch of files and 
you need to find out which one of them contains the string you need.

Just put this script into the directory with the zip files and run it.

'''

import zipfile, os

src = raw_input("enter the search term:")
for fn in os.listdir('.'):
	if zipfile.is_zipfile(fn):
		z = zipfile.ZipFile(fn, "r")
		for filename in z.namelist():
			if src in z.read(filename):  
				print fn+" : "+filename