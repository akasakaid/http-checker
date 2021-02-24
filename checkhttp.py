import threading
import os
try:
	from colorama import *
	import requests
	from concurrent.futures import ThreadPoolExecutor
except ImportError:
	exit("module not installed\npip3 install colorama requests")
r = requests.Session()
init(autoreset=True)
merah = Fore.LIGHTRED_EX
kuning = Fore.LIGHTYELLOW_EX
hijau = Fore.LIGHTGREEN_EX
biru = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
cyan = Fore.LIGHTCYAN_EX
hitam = Fore.LIGHTBLACK_EX
putih = Fore.LIGHTWHITE_EX
reset = Fore.RESET


def banner():
	os.system("cls" if os.name == "nt" else "clear")
	if not os.path.exists("results"):os.makedirs("results")
	if not os.path.exists("results/_http_200.txt"):open("results/_http_200.txt","a+").write("")
	print(f"""
{hijau}    __  __________________  {putih}   ________              __            
{hijau}   / / / /_  __/_  __/ __ \ {putih}  / ____/ /_  ___  _____/ /_____  _____
{hijau}  / /_/ / / /   / / / /_/ / {putih} / /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
{hijau} / __  / / /   / / / ____/  {putih}/ /___/ / / /  __/ /__/ ,< /  __/ /    
{hijau}/_/ /_/ /_/   /_/ /_/       {putih}\____/_/ /_/\___/\___/_/|_|\___/_/ 

{hijau}coded : {putih}AkasakaID
{hijau}team  : {putih}Black Coder Crush
		""")

def cek(host):
	try:
		req = r.get(host,timeout=75,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74"}).status_code
		if req == 200:
			print(f"{cyan}{host} {hitam}~> {putih}[{hijau}{req}{putih}]")
			if host in open("results/_http_200.txt").read():
				return False
			else:
				open("results/_http_200.txt","a+").write(f"{host}\n")
				return True
		else:
			print(f"{cyan}{host} {hitam}~> {putih}[{merah}{req}{putih}]")
			return False
	except requests.exceptions.ReadTimeout:print(f"{cyan}{host} {hitam}~> {putih}[{merah}timeout{putih}]")
	except requests.exceptions.ConnectionError:print(f"{cyan}{host} {hitam}~> {putih}[{merah}failed get info{putih}]")

try:
	banner()
	li = open(input("input list : ")).read().splitlines()
	for web in li:
		if "http://" not in web or "https://" not in web:
			web = f"http://{web}"
		cek(web)
except KeyboardInterrupt:exit()
except FileNotFoundError:exit(f'{merah}file not found !')