import os
import shutil
import subprocess as sub

def create_dir():
	try:
			os.chdir('/sdcard')
			os.mkdir('WhatsAppStatus')
			os.chdir('/sdcard/WhatsAppStatus')
			os.mkdir('Videos')
			os.mkdir('Images')
	except FileExistsError as exer:
				pass

src = ('/sdcard/WhatsApp/Media/.Statuses/')
dst_vid = ('/sdcard/WhatsAppStatus/Videos')
dst_img = ('/sdcard/WhatsAppStatus/Images')

def pull_status():
	os.chdir(src)
	#os.system(f'cp -r *.mp4 {dst_vid}')
	os.system('''


''')
	os.system(f'cp -r *.jpg {dst_img}')

def main():
	create_dir()
	pull_status()

#create_dir()
main()
