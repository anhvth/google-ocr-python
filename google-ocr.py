import glob
import os
import argparse
import json
import sys
# os.chdir('./google-ocr-python')
p = argparse.ArgumentParser()

p.add_argument('--input_dir', '-i', required=True, help='input directory')
a = p.parse_args()
files = []
paths = glob.glob(os.path.join(a.input_dir, '*.png'))
for filename in paths:
	print(filename)
	files.append(filename)


for image in paths:
	print("uploading " + image)
	command = "/usr/bin/python gdcmdtools/gdput.py -t ocr  " + image + " > result.log"
	print("running " + command)
	os.system(command)
	
	resultfile = open("result.log","r").readlines()
	
	for line in resultfile:
		if "id:" in line:
			fileid = line.split(":")[1].strip()
			filename = os.path.split(image)[-1].split(".")[0] + ".txt"
			get_command = "/usr/bin/python gdcmdtools/gdget.py -f txt -s " + filename + " " + fileid
			print("running "+ get_command)
			os.system(get_command)

# 1/0
print("Merging all text files into ocr-result.txt")
	
files = glob.glob('*.txt' )
results = {}
def read_text(fn):
	text = open(fn, 'r').readlines()
	text.remove('\ufeff________________\n')
	text.remove('\n')
	return text

for fn in files:
	text = read_text(fn)
	results[os.path.split(fn)[-1].replace('txt', 'png')] = text

json.dump(results, open('result.json', 'w')) 
# with open('ocr-result.txt', 'w' ) as result:
#     for textfile in files:
#         for line in open( textfile, 'r' ):
#             result.write( line )

# print("Done")
# os.system('cat {}'.format('ocr-result.txt'))