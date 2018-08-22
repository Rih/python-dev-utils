<<<<<<< HEAD
# coding=utf-8
# utils
import json
from datetime import datetime
import time
def writeFile(data, filepathname):

		with open(filepathname,'a') as f:
			f.write('----- d u m p -- d a t a ---------\n')
			if type(data) is dict:
				f.write(json.dumps(data, sort_keys=True,indent=2,separators=(',',': ')) + '\n')
			elif type(data) is str:
				f.write(data + '\n')
			else:
				f.write(str(data) + '\n')



def currentDate():

	# get current local time and utc time
	localnow = datetime.now()
	utcnow = datetime.utcnow()
	#seed =  isoformat_offset(datetime.now(),0) # +"+00:00"
	print localnow.strftime('%Y-%m-%dT%H:%M:%S+00:00')
	print utcnow.strftime('%Y-%m-%dT%H:%M:%S+00:00')

