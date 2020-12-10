import os
import shutil

def create_dir():
	try:
			os.mkdir('WhatsApp\ Status')
			os.chdir('/sdcard/WhatsApp\ Status')
			os.mkdir('Videos')
			os.mkdir('Images')
	except FileExistsError as exer:
				pass
				
def change_dir():
	try:
		os.chdir('/sdcard/WhatsApp/Media/.Statuses')
	except FileNotFoundError as dir_err:
		print(dir_err)
		print('WhatsApp folder is not exist.')
		
def coppy():
	os.system('cp -r *.mp4 /sdcard/WhatsApp\ Status')
	os.system('cp -r *.jpg /sdcard/WhatsApp\ Status')
	os.system('cp -r *.jpeg /sdcard/WhatsApp\ Status')
	try:
		shutil.copy2