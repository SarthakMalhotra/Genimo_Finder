#Credits To HackerSarthak
import requests
import urllib
from urllib.request import *
from urllib.error import *
from colorama import Fore
import os
from urllib.error import HTTPError
from urllib.request import urlopen, HTTPError
import time


links = open('links.txt', 'r')

banner = Fore.GREEN + """
 ██████  ███████ ███    ██ ██ ███    ███  ██████  
██       ██      ████   ██ ██ ████  ████ ██    ██ 
██   ███ █████   ██ ██  ██ ██ ██ ████ ██ ██    ██ 
██    ██ ██      ██  ██ ██ ██ ██  ██  ██ ██    ██ 
 ██████  ███████ ██   ████ ██ ██      ██  ██████  
 """
os.system('clear')
print(banner)
print(Fore.YELLOW+" The Best Admin Panel Finder With Over 421 Links!")
print("")
link = (input(Fore.RED+"Enter Website Address : "))

while True:
	sublink = links.readline().split('\n') [0]

	if not sublink:
		break

	reqlink = 'http://'+link+'/'+sublink

	try:
		response = urlopen(reqlink)
	except HTTPError as e:
		print(Fore.RED+"[-] "+reqlink+"    ")
		continue
	except URLError as e:
		print(Fore.RED+"[-] "+reqlink+"    ")
		continue
	else:
		print(Fore.GREEN+"[+] "+reqlink)
