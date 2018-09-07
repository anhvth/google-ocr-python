import os

python2_path = "/Users/bi/miniconda3/envs/py2/bin/python "
gdcmd_path = "/Users/bi/gitprojects/google-ocr-python/gdcmdtools"


def path2ocr(path, clean=True):
	def get_id():
		resultfile = open("result.log","r").readlines()	
		for line in resultfile:
			if "id:" in line:
				fileid = line.split(":")[1].strip()
				return fileid
		return None
		
	print("uploading " + path)
	command = "{} {}/gdput.py -t ocr  ".format(python2_path, gdcmd_path) + path + " > result.log"

	print("running " + command)
	os.system(command)
	fileid = get_id()	
	assert fileid is not None

	txt_file = os.path.split(path)[-1].split(".")[0] + ".txt"
	get_command = "{} {}/gdget.py -f txt -s ".format(python2_path, gdcmd_path) + txt_file + " " + fileid
	print("running "+ get_command)
	os.system(get_command)
	text = open(txt_file, 'r').readlines()
	if clean:
		os.system('rm result.log {}'.format(txt_file))
	return text