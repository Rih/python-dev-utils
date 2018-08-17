# utils
import json
def writeFile(data, filepathname):

		with open(filepathname,'a') as f:
			f.write('----- d u m p -- d a t a ---------\n')
			if type(data) is dict:
				f.write(json.dumps(data, sort_keys=True,indent=2,separators=(',',': ')) + '\n')
			elif type(data) is str:
				f.write(data + '\n')
			else:
				f.write(str(data) + '\n')


