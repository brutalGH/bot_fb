# MODULE
import os,sys,requests,re,time,bs4,datetime,random
from datetime import datetime
from bs4 import BeautifulSoup as soup
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel
from rich import print as jalan

# LIBRARY
try:
	import bs4
except ImportError:
	print('tunggu instalasi selesai')
	os.system('pip install bs4')
try:
	import rich
except ImportError:
	print('tunggu instalasi selesai')
	os.system('pip install rich')
try:
	print('tunggu instalasi selesai')
	os.system('pkg install play-audio')
except:
	pass

# WARNA
x = '\33[m' 		# PUTIH
m = '\x1b[1;91m' 	# MERAH
s = '\33[100m'		# ABU BG
n = '\33[34m'    	# MATI
k = '\033[93m' 		# KUNING
c = '\33[46m' 		# CYAN BG
h = '\33[92m' 		# HIJAU +
hb = '\33[42m'		# HIJAU BOLD
mb = '\33[41m'		# MERAH BOLD

# REUNI ALL
ses = requests.Session()
session = requests.Session()
jumlah,sm,reac = [],[],[]
tulis,commen,pasi = [],[],[]
jajan = []


# BANNER
def banner():
	if "linux" in sys.platform.lower():
		try:os.system('clear')
		except:pass
	elif "win" in sys.platform.lower():
	    try:os.system('cls')
	    except:pass
	else:
	    try:os.sytem('clear')
	    except:pass
	wel = '# FACEBOOK BOT TOOLS'
	wel2 = mark(wel, style='green')
	sol().print(wel2,style='white')
	text = ('''[white]   ___       __  ____             __             __  \n  / _ )___  / /_/ __/__ ________ / /  ___  ___  / /__\n / _  / _ \/ __/ _// _ `/ __/ -_) _ \/ _ \/ _ \/  '_/\n/____/\___/\__/_/  \_,_/\__/\__/_.__/\___/\___/_/\_\ \n                                                     \n[green]Welcome to script boot facebook[white]''')
	nel2 = Panel(text,style="green")
	jalan(Panel(nel2,style="cyan"))

# LOGIN
def login():
	banner()
	cook = input(f'  {x}[ {h}!{x} ] Enter Cookies :{h} ')
	open('.cookie.txt','w').write(cook)
	bahasa()
	try:
		url = 'https://mbasic.facebook.com/settings/account/?'
		get = ses.get(url,cookies={'cookie':cook})
		sop = soup(get.text,'html.parser')
		sear = sop.findAll('h3')
		for alin in sear:
			pas = alin.text
			if 'Nama' in pas:
				nam = pas.replace('Nama','')
				open('.nama.txt','w').write(nam)
			elif 'Alamat Email' in pas:
				em = pas.replace('Alamat Email','')
				if '@' in em:
					open('.email.txt','w').write(em)
				else:
					ok = 'Unknow'
					open('.email.txt','w').write(ok)
			elif 'Nomor Telepon' in pas:
				ph = pas.replace('Nomor Telepon','')
				if '0' in ph:
					open('.phone.txt','w').write(ph)
				elif '62' in ph:
					open('.phone.txt','w').write(ph)
				else:
					ok = 'Unknow'
					open('.phone.txt','w').write(ok)
			else:pass
	except Exception as e:
	    print(f'  {x}[ {m}•{x} ]{m}Login Failled');time.sleep(2)
	    login()

# CHECKING ACCOUNT
def check():
	bahasa()
	try:
		os.system('rm .nama.txt')
		os.system('rm .email.txt')
		os.system('rm .phone.txt')
		cook = open('.cookie.txt','r').read()
		url = 'https://mbasic.facebook.com/settings/account/?'
		get = ses.get(url,cookies={'cookie':cook})
		sop = soup(get.text,'html.parser')
		sear = sop.findAll('h3')
		if 'Buat akun baru' in sop.text:
		    os.system('clear')
		    print(' Cookie Invalid')
		    time.sleep(3)
		    login()
		else:
		    pass
		for alin in sear:
			pas = alin.text
			if 'Nama' in pas:
				nam = pas.replace('Nama','')
				open('.nama.txt','w').write(nam)
			elif 'Alamat Email' in pas:
				em = pas.replace('Alamat Email','')
				if '@' in em:
					open('.email.txt','w').write(em)
				else:
					ok = 'Unknow'
					open('.email.txt','w').write(ok)
			elif 'Nomor Telepon' in pas:
				ph = pas.replace('Nomor Telepon','')
				if '0' in ph:
					open('.phone.txt','w').write(ph)
				elif '62' in ph:
					open('.phone.txt','w').write(ph)
				else:
					ok = 'Unknow'
					open('.phone.txt','w').write(ok)
			else:pass
	except:
		print(f'  {x}[ {m}•{x} ] {m}Check Failled');time.sleep(2)
		login()

# UBAH BAHASA
def bahasa():
	try:
		cook = open('.cookie.txt','r').read()
		req = ses.get('https://mbasic.facebook.com/language/',cookies={'cookie':cook})
		pra = soup(req.content,'html.parser')
		for x in pra.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				header = {
				'initiator': 'mbasic.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'cache-control': 'max-age=0',
				'content-length': '94',
				'content-type': 'application/x-www-form-urlencoded',
				'origin': 'https://mbasic.facebook.com',
				'referer': 'https://mbasic.facebook.com/language',
				'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'same-origin',
				'upgrade-insecure-requests': '1',
				'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
				}
				bahasa = {
				"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
				"jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
				"submit"  : "Bahasa Indonesia"
				}
				url = 'https://mbasic.facebook.com' + x['action']
				ses.post(url,headers=header,data=bahasa,cookies={'cookie':cook})
	except:pass

# MENU
def menu():
	check()
	banner()
	ip = requests.get("https://api.ipify.org").text
	nam,ema,pho = open('.nama.txt','r').read(),open('.email.txt','r').read(),open('.phone.txt','r').read()
	print(f'{x} ╔ {x}[ {h}•{x} ] Your Name  : {h}'+nam)
	print(f'{x} ╠ {x}[ {h}•{x} ] Your Email : {h}'+ema)
	print(f'{x} ╠ {x}[ {h}•{x} ] Your Phone : {h}'+pho)
	print(f'{x} ╠ {x}[ {h}•{x} ] Your Ip    : {h}{ip}{x}')
	print(f'{x} ║')
	print(f'{x} ╠══ [ {h}•{x} ] MENU UTAMA TOOLS')
	print(f'{x} ║')
	print(f'{x} ╠══ [ {h}1{x} ] Bot auto confirmations		[{h} ✔ {x}]')
	print(f'{x} ╠══ [ {h}2{x} ] Bot komen target			[{h} ✔ {x}]')
	print(f'{x} ╠══ [ {h}3{x} ] Bot komen & Reaction beranda		[{h} ✔ {x}]')
	print(f'{x} ╠══ [ {h}4{x} ] Bot pesan masal			[{h} ✔ {x}]')
	print(f'{x} ╠══ [ {h}5{x} ] Bot auto balas pesan			[{h} ✔ {x}]')
	print(f'{x} ╠══ [ {h}6{x} ] Lihat log aktifitas			[{h} ✔ {x}]')
	print(f'{x} ╠══ [ {h}7{x} ] Setting info 			[{h} ✔ {x}]')
	print(f'{x} ╠══ [ {h}8{x} ] Setting Foto komentar 		[{h} ✔ {x}]')
	print(f'{x} ╠══ [ {h}0{x} ] Log out')
	print(f'{x} ║')
	pilih = input(f'{x} ╚══ [ {h}!{x} ] Pilih : ')
	if pilih in ['1','2','3','4','5','6','7','8']:
		setting(pilih)
	elif '0' in pilih:
		os.system('rm -rf .cookie.txt')
		exit()
	else:
		print(f'{x} ═══ [ {m}!{x} ] EROR MENU SELEC')
		time.sleep(3)
		menu()

# SETTING
def setting(pilih):
	banner()
	if '1' in pilih:
		konfirmasi('/friends/center/requests/?')
		print(f'\r{x} ╚══ [ {h}•{x} ] Berhasil mengonfirmasi{h} {len(sm)}{x} Requests')
	elif '2' in pilih:
		print(f'{x} ║')
		print(f'{x} ╠ {x}[ {h}•{x} ] Menu Komentar')
		print(f'{x} ╠ {x}[ {h}•{x} ] Note url harus mbasic.facebook.com')
		print(f'{x} ║')
		print(f'{x} ╠ {x}[ {h}1{x} ] Dengan foto	[{h} ✔ {x}]')
		print(f'{x} ╠ {x}[ {h}2{x} ] Hanya text 	[{h} ✔ {x}]')
		print(f'{x} ║')
		pilih = input(f'{x} ╠══ [ {h}!{x} ] Pilih : ')
		commen.append(pilih)
		print(f'{x} ║')
		jumlah = input(f'{x} ╠══ {x}[ {h}!{x} ] Jumlah Komentar : ')
		print(f'{x} ╠══ [ {k}!{x} ] Gunakan [{h} , {x}] jika ingin komentar random ')
		text = input(f'{x} ╠══ [ {h}!{x} ] Masukan text : ')
		url = input(f'{x} ╚══ [ {h}!{x} ] Input url : ')
		if ',' in text:
			co = text.split(',')
			for ok in co:
				tulis.append(ok)
		else:
			tulis.append(text)
		banner()
		lop = 1
		for i in range(int(jumlah)):
			print(f'\r{x} ╠══[ {h}•{x} ] Komentar ke :',str(lop))
			komen_target(url)
			lop+=1
	elif '3' in pilih:
		print(f'{x} ╠ {x}[ {h}•{x} ] Menu ')
		print(f'{x} ╠ {x}[ {h}1{x} ] Dengan Reaction')
		print(f'{x} ╠ {x}[ {h}2{x} ] Hanya Komentar')
		print(f'{x} ║')
		pas = input(f'{x} ╠══ [ {h}!{x} ] Pilih : ')
		pasi.append(pas)
		if '1' in pas:
			print(f'{x} ║')
			print(f'{x} ╠ {x}[ {h}•{x} ] Menu Reaction')
			print(f'{x} ╠ {x}[ {h}1{x} ] Suka		[ {h}5{x} ] Wow')
			print(f'{x} ╠ {x}[ {h}2{x} ] Super		[ {h}6{x} ] Sedih')
			print(f'{x} ╠ {x}[ {h}3{x} ] Peduli		[ {h}7{x} ] Marah')
			print(f'{x} ╠ {x}[ {h}4{x} ] Haha		[ {h}8{x} ] Kembali')
			print(f'{x} ║')
			pil = input(f'{x} ╠══ [ {h}!{x} ] Pilih : ')
			reac.append(pil)
		else:
			pass
		print(f'{x} ║')
		print(f'{x} ╠ {x}[ {h}•{x} ] Menu Komentar')
		print(f'{x} ╠ {x}[ {h}1{x} ] Dengan foto	[{h} ✔ {x}]')
		print(f'{x} ╠ {x}[ {h}2{x} ] Hanya text 	[{h} ✔ {x}]')
		print(f'{x} ║')
		pilih = input(f'{x} ╠══ [ {h}!{x} ] Pilih : ')
		commen.append(pilih)
		if '1' in pilih:
			print(f'{x} ║')
			print(f'{x} ╠══ [ {k}!{x} ] Gunakan [{h} , {x}] jika ingin komentar random ')
			text = input(f'{x} ╠══ [ {h}!{x} ] Masukan text : ')
			if ',' in text:
				co = text.split(',')
				for ok in co:
					tulis.append(ok)
			else:
				tulis.append(text)
			banner()
			komen('https://mbasic.facebook.com/home.php')
		elif '2' in pilih:
			print(f'{x} ║')
			print(f'{x} ╠══ [ {k}!{x} ] Gunakan [{h} , {x}] jika ingin komentar random ')
			text = input(f'{x} ╠══ [ {h}!{x} ] Masukan text : ')
			if ',' in text:
				co = text.split(',')
				for ok in co:
					tulis.append(ok)
			else:
				tulis.append(text)
			banner()
			komen('https://mbasic.facebook.com/home.php')
	elif '4' in pilih:
		print(f'{x} ╠══ [ {h}!{x} ] Gunakan [{h} , {x}] jika ingin komentar random ')
		text = input(f'\r{x} ╚══ [ {h}•{x} ] Masukan Pesan :{h} ')
		if ',' in text:
			co = text.split(',')
			for ok in co:
				tulis.append(ok)
		else:
			tulis.append(text)
		banner()
		pessan('https://mbasic.facebook.com/messages/?')
	elif '5' in pilih:
		banner()
		bot_pesan()
	elif '6' in pilih:
		logger('/allactivity')
	elif '7' in pilih:
		set_info()
	elif '8' in pilih:
		set_foto()
	else:
		print(' Tidak ada pilihan');time.sleep(3)
		menu()

# CONFIRMATIONS
def konfirmasi(urll):
	try:
		cook = open('.cookie.txt','r').read()
		url = 'https://mbasic.facebook.com'
		header = {
		'initiator': 'mbasic.facebook.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
		}
		get = ses.get(url+urll,cookies={'cookie':cook}).text
		ambil = re.findall('a\ class\=\"..\"\ href\=\".*\"\>(.*?)\<\/a\>\<div(.*?)\<\/div\>\<div\ class\=\"..\"\>\<a\ href\=\"(.*?)\"\>',get)
		for co in ambil:
			sm.append(co[0])
			bhn = url+co[2].split('"')[0]
			print(f'\r{x} ╚══ [ {h}•{x} ] Sedang mengonfirmasi{h} {len(sm)}{x} Requests',end='')
			ok = soup(ses.get(bhn,cookies={'cookie':cook}).content,'html.parser')
			fom = ok.find('form',{'method':'post'})
			dat = {
			'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
			'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
			'submit' : 'Konfirmasi'
			}
			uri = url+co[2].split('"')[0]
			post = ses.post(uri,data=dat,cookies={'cookie':cook})
			if '<Response [200]>' in str(post):
				print(f'\r{x} ╚══ [ {h}•{x} ] Berhasil mengonfirmasi,{h} '+co[0])
			else:
				print(f'\r{x} ╚══ [ {m}•{x} ] Gagal mengonfirmasi, '+co[0])

		if 'Lihat selengkapnya' in get:
			konfirmasi(soup(get, "html.parser").find("a", string="Lihat selengkapnya").get("href"))
		elif 'Tidak ada permintaan' in get:
			print(f'\r{x} ╚══ [ {m}•{x} ] Tidak Ada permintaan Pertemanan')
		else:
			pass
	except:pass

# KOMEN BERANDA
def komen_target(url):
	cook = open('.cookie.txt','r').read()
	sasi = ["oyo","Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
	now = datetime.now();hari = now.day;blx = now.month;bulan = sasi[blx];tahun = now.year;tanggal = str(hari)+' - '+str(bulan)+' - '+str(tahun);jam = now.hour;menit = now.minute;detik = now.second;hari1 = now.strftime("%A")
	date = '\n\n [ '+str(hari1)+', '+str(tanggal)+' ] [ Pukul, '+str(jam)+' : '+str(menit)+', '+str(detik)+' ]'
	text = random.choice(tulis)
	if '1' in commen:
		try:
			ambil = session.get(url,cookies={'cookie':cook}).text
			url1 = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"',ambil)
			jaz = re.findall('name\=\"jazoest\"\ value\=\"(.*?)\"',ambil)
			dtsg = re.findall('name\=\"fb_dtsg\"\ value\=\"(.*?)\"',ambil)
			data = {
				'fb_dtsg':	dtsg[1],
				'jazoest':	jaz[1],
				'view_photo':	'Lampirkan Foto'
			}
			urll = 'https://mbasic.facebook.com'+url1[1].replace('amp;','')
			get = session.post(urll,data=data,cookies={'cookie':cook}).text
			url2 = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"',get)
			jaz1 = re.findall('name\=\"jazoest\"\ value\=\"(.*?)\"',get)
			dtsg1 = re.findall('name\=\"fb_dtsg\"\ value\=\"(.*?)\"',get)
			header = {
				'initiator':	'https://mbasic.facebook.com',
				'Accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'Accept-Encoding':	'gzip, deflate, br',
				'Accept-Language':	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'Origin':	'https://mbasic.facebook.com',
				'Referer':	'https://mbasic.facebook.com/',
				'sec-ch-ua':	'"Not:A-Brand";v="99", "Chromium";v="112"',
				'sec-ch-ua-mobile':	'?1',
				'sec-ch-ua-platform':	'"Android"',
				'Sec-Fetch-Dest':	'document',
				'Sec-Fetch-Mode':	'navigate',
				'Sec-Fetch-Site':	'same-site',
				'Sec-Fetch-User':	'?1',
				'Upgrade-Insecure-Requests':	'1',
				'User-Agent':	'Mozilla/5.0 (Linux; Android 13; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
			}
			foto = 'image.jpg'
			tes = {'photo':(foto,open(foto,'rb'),"multipart/form-data")}
			url3 = url2[0].replace('amp;','')
			data = {
				'comment_text':	f'{text}{date}',
				'fb_dtsg':	dtsg1[0],
				'jazoest':	jaz1[0],
				'post':	'Komentari'
			}
			post = session.post(url3,headers=header,files=tes,data=data,cookies={'cookie':cook})
			if '<Response [200]>' in str(post):
				print(f'\r{x} ╠══[ {h}•{x} ] Berhasil mengomentari postingan')
				print(f'\r{x} ╠══[ {h}•{x} ] Isi text :{h} {text}')
				print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
		except Exception as e:
			print('\r',e)
			print(f'\r{x} ╚══[ {m}!{x} ] Tidak ada akses untuk komentar\n')
	else:
		try:
			req = ses.get(url,cookies={'cookie':cook}).text
			par = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"\>\<input',req)
			ok = soup(req,'html.parser')
			fom = ok.find('form',{'method':'post'})
			text = random.choice(tulis)
			dat = {
			'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
			'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
			'comment_text': f'{text}{date}',
			'submit' : 'Komentari'
			}
			header = {
			'initiator': 'https://mbasic.facebook.com',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://mbasic.facebook.com',
			'referer': url,
			'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
			}
			if 'https://mbasic.facebook.com' in par[0]:
				ukr = par[0].replace('amp;','')
			else:
				ukr = 'https://mbasic.facebook.com'+par[0].replace('amp;','')
			post = ses.post(ukr,headers=header,data=dat,cookies={'cookie':cook})
			if '<Response [200]>' in str(post):
				print(f'\r{x} ╠══[ {h}•{x} ] Berhasil mengomentari postingan')
				print(f'\r{x} ╠══[ {h}•{x} ] Isi text :{h} {text}')
				print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
		except:
			print(f'\r{x} ╚══[ {m}!{x} ] Tidak ada akses untuk komentar\n')

# KOMEN BERANDA
def komen(tar):
	try:
		sasi = ["oyo","Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
		now = datetime.now();hari = now.day;blx = now.month;bulan = sasi[blx];tahun = now.year;tanggal = str(hari)+' - '+str(bulan)+' - '+str(tahun);jam = now.hour;menit = now.minute;detik = now.second;hari1 = now.strftime("%A")
		date = '\n\n [ '+str(hari1)+', '+str(tanggal)+' ] [ Pukul, '+str(jam)+' : '+str(menit)+', '+str(detik)+' ]'
		url = tar
		cook = open('.cookie.txt','r').read()
		gett = ses.get(url,cookies={'cookie':cook}).text
		al = re.findall('Suka\<\/a\>\<span\>\ · \<\/span\>\<a\ href\=\"(.*?)\"\>Tanggapi\<\/a\>\<\/span\>\<span\>\ ·\ <\/span\>\<a\ href\=\"(.*?)\"\>',gett)
		for pisah in al:
			try:
				jajan.append(pisah[1])
				print(f'\r{x} ═══[ {h}•{x} ] Postingan ke,{h} {len(jajan)} {x}      ')
				if '1' in pasi:
					try:
						urll = 'https://mbasic.facebook.com'+pisah[0]
						post = ses.get(urll,cookies={'cookie':cook}).text
						dic = {'1':'tanggapan\<\/h1\>','2':'Suka','3':'Super','4':'Peduli','5':'Haha','6':'Wow','7':'Sedih'}
						au = (dic[random.choice(reac)])
						if 'Wow' in post:
							target = re.findall(f'{au}\<\/span\>\<\/td\>(.*?)\<a\ href\=\"(.*?)\"\ style\=',post)
							for ok in target:
								uri = 'https://mbasic.facebook.com'+ok[1].replace('amp;','')
								gas = ses.get(uri,cookies={'cookie':cook})
								if '<Response [200]>' in str(gas):
									dic = {'1':'Suka','2':'Super','3':'Peduli','4':'Haha','5':'Wow','6':'Sedih','7':'Marah'}
									ae = (dic[random.choice(reac)])
									print(f'\r{x} ╠══[ {h}•{x} ] Berhasil menanggapi, [{h} {ae} {x}] postingan')
									sys.stdout.write(f'\r{x}  ══[ {k}!{x} ] Wait 10 detik');sys.stdout.flush()
								time.sleep(10)
						else:
							pass
					except:pass

				else:
					pass
				if '1' in commen:
					try:
						if 'https://mbasic.facebook.com' in pisah[1]:
							tes = pisah[1].replace('amp;','')
							try:
								urlk = tes.split('"')[0]
							except:
								urlk = tes
						else:
							urlk = 'https://mbasic.facebook.com'+pisah[1].replace('amp;','')
						req = ses.get(urlk,cookies={'cookie':cook}).text
						try:
							targett = re.findall('id\=1000(.*?)&',req)
							id_target = '1000'+targett[0]
						except:
							id_target = 'None'
						text = random.choice(tulis)
						if '[ Pukul' in str(req):
							print(f'\r{x} ╠══[ {m}•{x} ] postingan ini sudah di komentari')
							print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
						elif 'Anda Diblokir Sementara' in str(req):
							print(f'\r{x} ╠══[ {m}•{x} ] Anda di larang berkomentar untuk sementara')
							print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
						else:
							ambil = session.get(urlk,cookies={'cookie':cook}).text
							url1 = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"',ambil)
							jaz = re.findall('name\=\"jazoest\"\ value\=\"(.*?)\"',ambil)
							dtsg = re.findall('name\=\"fb_dtsg\"\ value\=\"(.*?)\"',ambil)
							data = {
								'fb_dtsg':	dtsg[1],
								'jazoest':	jaz[1],
								'view_photo':	'Lampirkan Foto'
							}
							urll = 'https://mbasic.facebook.com'+url1[1].replace('amp;','')
							get = session.post(urll,data=data,cookies={'cookie':cook}).text
							url2 = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"',get)
							jaz1 = re.findall('name\=\"jazoest\"\ value\=\"(.*?)\"',get)
							dtsg1 = re.findall('name\=\"fb_dtsg\"\ value\=\"(.*?)\"',get)
							header = {
								'initiator':	'https://mbasic.facebook.com',
								'Accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
								'Accept-Encoding':	'gzip, deflate, br',
								'Accept-Language':	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
								'Origin':	'https://mbasic.facebook.com',
								'Referer':	'https://mbasic.facebook.com/',
								'sec-ch-ua':	'"Not:A-Brand";v="99", "Chromium";v="112"',
								'sec-ch-ua-mobile':	'?1',
								'sec-ch-ua-platform':	'"Android"',
								'Sec-Fetch-Dest':	'document',
								'Sec-Fetch-Mode':	'navigate',
								'Sec-Fetch-Site':	'same-site',
								'Sec-Fetch-User':	'?1',
								'Upgrade-Insecure-Requests':	'1',
								'User-Agent':	'Mozilla/5.0 (Linux; Android 13; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
							}
							foto = 'image.jpg'
							tes = {'photo':(foto,open(foto,'rb'),"multipart/form-data")}
							url3 = url2[0].replace('amp;','')
							data = {
								'comment_text':	f'{text}{date}',
								'fb_dtsg':	dtsg1[0],
								'jazoest':	jaz1[0],
								'post':	'Komentari'
							}
							post = session.post(url3,headers=header,files=tes,data=data,cookies={'cookie':cook})
							if '<Response [200]>' in str(post):
								print(f'\r{x} ╠══[ {h}•{x} ] Berhasil mengomentari postingan')
								print(f'\r{x} ╠══[ {h}•{x} ] Isi text  :{h} {text}')
								print(f'\r{x} ╠══[ {h}•{x} ] ID target :{h} {id_target}')
								print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
								sys.stdout.write(f'\r{x}  ══[ {k}!{x} ] Wait 60 detik');sys.stdout.flush()
								time.sleep(60)
					except Exception as e:
						print(e)
						print(f'\r{x} ╚══[ {m}!{x} ] Tidak ada akses untuk komentar\n')
				else:
					try:
						if 'https://mbasic.facebook.com' in pisah[1]:
							tes = pisah[1].replace('amp;','')
							try:
								urlk = tes.split('"')[0]
							except:
								urlk = tes
						else:
							urlk = 'https://mbasic.facebook.com'+pisah[1].replace('amp;','')
						req = ses.get(urlk,cookies={'cookie':cook}).text
						par = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"\>\<input',req)
						ok = soup(req,'html.parser')
						fom = ok.find('form',{'method':'post'})
						text = random.choice(tulis)
						if '[ Pukul' in str(req):
							print(f'\r{x} ╠══[ {m}•{x} ] postingan ini sudah di komentari')
							print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
						elif 'Anda Diblokir Sementara' in str(req):
							print(f'\r{x} ╠══[ {m}•{x} ] Anda di larang berkomentar untuk sementara')
							print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
						else:
							dat = {
							'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
							'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
							'comment_text': f'{text}{date}',
							'submit' : 'Komentari'
							}
							header = {
							'initiator': 'https://mbasic.facebook.com',
							'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
							'accept-encoding': 'gzip, deflate, br',
							'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
							'content-type': 'application/x-www-form-urlencoded',
							'origin': 'https://mbasic.facebook.com',
							'referer': urlk,
							'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
							'sec-ch-ua-mobile': '?1',
							'sec-ch-ua-platform': '"Android"',
							'sec-fetch-dest': 'document',
							'sec-fetch-mode': 'navigate',
							'sec-fetch-site': 'same-origin',
							'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
							}
							if 'https://mbasic.facebook.com' in par[0]:
								ukr = par[0].replace('amp;','')
							else:
								ukr = 'https://mbasic.facebook.com'+par[0].replace('amp;','')
							post = ses.post(ukr,headers=header,data=dat,cookies={'cookie':cook})
							if '<Response [200]>' in str(post):
								print(f'\r{x} ╠══[ {h}•{x} ] Berhasil mengomentari postingan')
								print(f'\r{x} ╠══[ {h}•{x} ] Isi text  :{h} {text}')
								print(f'\r{x} ╠══[ {h}•{x} ] ID target :{h} {id_target}')
								print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
								sys.stdout.write(f'\r{x}  ══[ {k}!{x} ] Wait 60 detik');sys.stdout.flush()
								time.sleep(60)
					except:
						print(f'\r{x} ╚══[ {m}!{x} ] Tidak ada akses untuk komentar\n')
			except:
				print(f'\r{x} ╚══[ {k}!{x} ] Getting Url Error\n')
		if 'Lihat Berita Lain' in get:
			target = soup(get, "html.parser").find("a", string='Lihat Berita Lain').get('href')
			komen('https://mbasic.facebook.com'+target)
		else:
			komen('https://mbasic.facebook.com/home.php')
	except:pass

# LOG AKTIFITAS
def logger(urll):
	try:
		banner()
		cook = open('.cookie.txt','r').read()
		url = 'https://mbasic.facebook.com'+urll
		post = ses.get(url,cookies={'cookie':cook}).text
		get = soup(post,'html.parser')
		sop = get.findAll('h3')
		#open('wri.txt','w').write(post)
		for ok in sop:
			if 'Log Aktivitas' in ok.text:
				pass
			elif 'Filter' in ok.text:
				pass
			elif 'Arsip' in ok.text:
				pass
			elif 'Sampah' in ok.text:
				pass
			else:
				print(f'\r{x} ╚══[ {h}•{x} ] {ok.text}')
		pilih = input(f'\r{x} ╚══[ {k}!{x} ] Pilih [ y/t ] : ')
		if 'y' in pilih:
			sasi = ["oyo", "Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
			now = datetime.now();blx = now.month;bulan = sasi[blx]
			urll = get.find("a", string=f"Muat lebih banyak dari {str(bulan)}").get("href")
			logger(urll)
			print(f'\r{x} ╚══[ {k}!{x} ] Tidak ada lagi aktifitas\n')
			
		else:
			menu()
	except Exception as e:
		print(e)

# BOT PESAN
def pessan(urll):
	try:
		url = urll
		cook = open('.cookie.txt','r').read()
		get = ses.get(url,cookies={'cookie':cook}).text
		sasi = ["oyo","Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
		now = datetime.now();hari = now.day;blx = now.month;bulan = sasi[blx];tahun = now.year;tanggal = str(hari)+' - '+str(bulan)+' - '+str(tahun);jam = now.hour;menit = now.minute;detik = now.second;hari1 = now.strftime("%A")
		date = '\n\n[ by brutalID ]\n[ '+str(hari1)+', '+str(tanggal)+'/ '+str(jam)+' : '+str(menit)+', '+str(detik)+' ]'
		te = re.findall('table\>\<table\ class\=\".*?\"\>\<tr\>\<td\ class\=\".*?\"\>\<div\>\<h3\ class\=\".*?\"\>\<a\ href\=\"(.*?)\"\>(.*?)\<',get)
		for de in te:
			text = random.choice(tulis)
			pesan = text+date
			jajan.append(de[1])
			print(f'\r{x} ═══[ {h}•{x} ] Pesan ke,{h} {len(jajan)} {x}       ')
			try:
				ukl = 'https://mbasic.facebook.com'+de[0].replace('amp;','')
				uo = ses.get(ukl,cookies={'cookie':cook}).text
				par = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"',uo)
				ok = soup(uo,'html.parser')
				fom = ok.find('form',{'method':'post'})
				dat = {
				'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
				'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
				'body': f'{pesan}',
				'send' : 'Kirim',
				'tids' : re.search('name="tids" type="hidden" value="(.*?)"',str(fom)).group(1),
				'wwwupp' : re.search('name="wwwupp" type="hidden" value="(.*?)"',str(fom)).group(1),
				'platform_xmd': '',
				'referrer': '',
				'ctype': '',
				'cver' : re.search('name="cver" type="hidden" value="(.*?)"',str(fom)).group(1)
				}
				header = {
				'initiator': 'https://mbasic.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
				'content-type': 'application/x-www-form-urlencoded',
				'origin': 'https://mbasic.facebook.com',
				'referer': ukl,
				'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'sec-fetch-dest': 'document',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-site': 'same-origin',
				'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
				}
				ukr = 'https://mbasic.facebook.com'+par[0].replace('amp;','')
				post = ses.post(ukr,headers=header,data=dat,cookies={'cookie':cook})
				if '<Response [200]>' in str(post):
					text = '[green]Penerima[white] :[cyan] '+ de[1] + '\n[green]Pesan[white] :[cyan] ' + pesan + '[white]'
					pan = Panel(text,title='>[green] Succes[cyan] <',style="cyan")
					jalan(pan)
					sys.stdout.write(f'\r{x}  ══[ {k}!{x} ] Wait 30 detik');sys.stdout.flush()
					time.sleep(30)
				else:
					print(f'\r{x} ╚══[ {m}!{x} ] Gagal Mengirim pesan \n')
			except:
				print(f'\r{x} ╚══[ {m}!{x} ] Tidak ada akses untuk mengirim pesan\n')
				sys.stdout.write(f'\r{x}  ══[ {k}!{x} ] Wait 30 detik');sys.stdout.flush()
				time.sleep(60)
		if 'Lihat Pesan Sebelumnya' in get:
			target = soup(get, "html.parser").find("a", string='Lihat Pesan Sebelumnya').get('href')
			pessan('https://mbasic.facebook.com'+target)
		else:
			print(f'\r{x} ╚══[ {k}!{x} ] Hei anda sudah mengirimi semua pesan yang ada di table\n')
	except Exception as e:
		print(e)

# BOT AUTO PESAN
def bot_pesan():
	cookie = open('.cookie.txt','r').read()
	ambil = session.get('https://mbasic.facebook.com/home.php?',cookies={'cookie':cookie}).text
	url_read = re.findall('Menu\<\/a\>\<a\ href\=\"(.*?)\"\ class\=\"..\ ..\"\>',ambil)
	for mentah in url_read:
		urll = 'https://mbasic.facebook.com'+mentah.replace('amp;','')
		gabung = session.get(urll,cookies={'cookie':cookie}).text
		read_pesan(gabung,urll)
	print(f'\r{x} ╚══[ {k}!{x} ] Tidak ada pesan baru',end='')
	time.sleep(5)
	bot_pesan()

# READ PESAN
def read_pesan(gabung,urll):
	cookie = open('.cookie.txt','r').read()
	read = re.findall('div\ class\=\"..\"\>\<a\ class\=\"..\ ..\"\ href="(.*?)\"\>\<strong\ class\=\"..\"\>(.*?)\<\/strong\>\<\/a\>\<br\ \/\>\<div\>\<span\>(.*?)\<\/span',gabung)
	jum = []
	for lah in read:
		jum.append(lah)
	jumlah = len(jum)-1
	isi = read[jumlah]
	if './menu' in isi[2]:
		pesan = 'kirim :\n  ./contak (untuk no wa)\n  ./translate (terjemah)\n  ./mutiara (kata" mutiara)\n  ./motivasi (kata" motivasi)\n  ./gombal (kata" gombal)'
	elif './translate' in isi[2]:
		pesan = 'kirim :\n  ./inggris=(kata)\nuntuk translate ing ke indo\n\n  ./indo=(kata)\nuntuk translate indo ke ing\n\ncontoh : ./inggris=ayam'
	elif './contak' in isi[2]:
		wa = open('kumpul/.whatsapp.txt','r').read()
		ig = open('kumpul/.instagram.txt','r').read()
		em = open('kumpul/.email.txt','r').read()
		pesan = f'Wa    : {wa}\nIg      : {ig}\nEmail : {em}'
	elif './inggris' in isi[2]:
		try:
			text = isi[2].split('=')[1]
			langue = 'indo'
			translate(gabung,urll,text,isi[1],langue)
		except:pass
	elif './indo' in isi[2]:
		try:
			text = isi[2].split('=')[1]
			langue = 'englis'
			translate(gabung,urll,text,isi[1],langue)
		except:pass
	elif './gombal' in isi[2]:
		text = 'kata kata gombal :\n'+random.choice(open('kumpul/gombal.txt','r').readlines())
		pesan = text
	elif './motivasi' in isi[2]:
		text = 'kata kata motivasi :\n'+random.choice(open('kumpul/motivasi.txt','r').readlines())
		pesan = text
	elif './mutiara' in isi[2]:
		text = 'kata kata mutiara :\n'+random.choice(open('kumpul/mutiara.txt','r').readlines())
		pesan = text
	else:
		pesan = f'HI, {isi[1]}\nmohon maaf untuk waktu sekarang owner jarang aktif, mohon hubungi kembali pada pukul 06:00 - 22:00.\natau kirim pesan :\n  ./menu (untuk menu bot)\n\nterimakasih\nbot by brutalID'
	send_pesan(gabung,urll,pesan,isi[1])

# SEND PESAN
def send_pesan(gabung,urll,pesan,nama):
	try:
		cookie = open('.cookie.txt','r').read()
		par = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"',gabung)
		ok = soup(gabung,'html.parser')
		fom = ok.find('form',{'method':'post'})
		dat = {
		'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
		'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
		'body': f'{pesan}',
		'send' : 'Kirim',
		'tids' : re.search('name="tids" type="hidden" value="(.*?)"',str(fom)).group(1),
		'wwwupp' : re.search('name="wwwupp" type="hidden" value="(.*?)"',str(fom)).group(1),
		'platform_xmd': '',
		'referrer': '',
		'ctype': '',
		'cver' : re.search('name="cver" type="hidden" value="(.*?)"',str(fom)).group(1)
		}
		header = {
		'initiator': 'https://mbasic.facebook.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://mbasic.facebook.com',
		'referer': urll,
		'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
		}
		ukr = 'https://mbasic.facebook.com'+par[0].replace('amp;','')
		post = session.post(ukr,headers=header,data=dat,cookies={'cookie':cookie})
		if '<Response [200]>' in str(post):
			print(f'\r{x} ╠══[ {h}•{x} ] Berhasil membalas pesan',nama)
		else:
			print(f'\r{x} ╠══[ {m}•{x} ] Gagal Mengirim pesan')
	except Exception as e:
		print(e)
		print(f'\r{x} ╠══[ {m}!{x} ] Tidak ada akses untuk mengirim pesan')
	bot_pesan()

# TRANSLATE
def translate(gabung,urll,text,nama,langue):
	try:
		header = {
			'authority':	'https://mobile.sederet.com',
			'accept':	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-encoding':	'gzip, deflate, br',
			'accept-language':	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
			'content-type':	'application/x-www-form-urlencoded',
			'origin':	'https://mobile.sederet.com',
			'referer':	'https://mobile.sederet.com/translate.php',
			'sec-ch-ua':	'"Not:A-Brand";v="99", "Chromium";v="112"',
			'sec-ch-ua-full-version-list':	'"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
			'sec-ch-ua-mobile':	'?1',
			'sec-ch-ua-platform':	'"Android"',
			'sec-ch-ua-platform-version':	'"13.0.0"',
			'sec-fetch-dest':	'document',
			'sec-fetch-mode':	'navigate',
			'sec-fetch-site':	'same-origin',
			'sec-fetch-user':	'?1',
			'upgrade-insecure-requests':	'1',
			'user-agent':	'Mozilla/5.0 (Linux; Android 13; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
		}
		if 'indo' in langue:
			data = {
				'lang': 'en_id',
				'q': text
			}
		elif 'englis' in langue:
			data = {
				'lang': 'id_en',
				'q': text
			}
		else:
			pass
		post = session.post('https://mobile.sederet.com/translate.php',headers=header,data=data).text
		sop = soup(post,'html.parser')
		get = sop.findAll('table')
		try:
			if ' ' in text:
				table = get[3]
				find = re.findall('div\ class\=\"result_text\"\>(.*?)\<',str(get[3]))
				isi = ''
				for ok in find:
					try:
						isi+=ok.split(';')[0]+' '
					except:
						isi+=ok+' '
			else:
				table = get[2]
				find = table.find('div', class_="result_text")
				isi = find.text
			if 'indo' in langue:
				pesan = f'hasil translate eng ke ind :\n\n{isi}'
			else:
				pesan = f'hasil translate ind ke eng :\n\n{isi}'
		except:
			pesan = f'hasil translate eng ke ind :\n\nperiksa kembali kosa kata'
		send_pesan(gabung,urll,pesan,nama)
	except Exception as e:
		print(e)
		pass

# SET INFO
def set_info():
	banner()
	print(f'\r{x} ╠══[ {h}•{x} ] Input info pribadi')
	wa = input(f'\r{x} ╠══[ {h}•{x} ] Input Nomer wa 	: ')
	ig = input(f'\r{x} ╠══[ {h}•{x} ] Input user IG 	: ')
	em = input(f'\r{x} ╚══[ {h}•{x} ] Input email 		: ')
	open('kumpul/.whatsapp.txt','w').write(wa)
	open('kumpul/.instagram.txt','w').write(ig)
	open('kumpul/.email.txt','w').write(em)
	print(f'\r{x}\n ═══[ {h}•{x} ] SUCCES')
	menu()

# SET FOTO
def set_foto():
	banner()
	try:
		print(f'\r{x} ╠══[ {k}!{x} ] Format file harus ( image.jpg )')
		print(f'\r{x} ╠══[ {k}!{x} ] Input tempat file ( /sdcard/download/image.jpg )')
		foto = input(f'\r{x} ╚══[ {m}!{x} ] Input : ')
		os.system(f'mv {foto} ~/bot_fb')
		print(f'\r{x}\n ═══[ {h}•{x} ] SUCCES')
		menu()
	except:
		print(f'\r{x} ╚══[ {m}!{x} ] File tidak di temukan')
		time.sleep(3);set_foto()

# GAS OM
if __name__=='__main__':
	os.popen('play-audio musik/intro.mp3')
	menu()
