#!/usr/bin/python

import urllib2
import time
import sys
flag=0
banner = '''
  ___      _           _       _____           _     _               
 / _ \    | |         (_)     |  __ \         | |   | |              
/ /_\ \ __| |_ __ ___  _ _ __ | |  \/_ __ __ _| |__ | |__   ___ _ __ 
|  _  |/ _` | '_ ` _ \| | '_ \| | __| '__/ _` | '_ \| '_ \ / _ \ '__|
| | | | (_| | | | | | | | | | | |_\ \ | | (_| | |_) | |_) |  __/ |   
\_| |_/\__,_|_| |_| |_|_|_| |_|\____/_|  \__,_|_.__/|_.__/ \___|_|   
                                                                      
        Author: Shariq Malik
'''
print(banner)
sap = "---------------------------------------------------------------------"
def AdminGrabber():
	try:
		url = raw_input("Enter URL: ")
		if "http://" in url or "https://" in url:
			pass
		else:
			url = "http://" + url
		ua = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
		header = {'User-Agent' : ua}
		req = urllib2.Request(url, None, header)
		resp = urllib2.urlopen(req)
		print(sap)
		print  "[Connecting] : " + url + "..."
		if resp.code == 200:
			time.sleep(2)
			print "[Connected]  : " + url + " is connected"
			print(sap)
	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")
	except:
		print(sap)
		print "[Connecting] : " + url + ""
		time.sleep(2)
		print"[Failed] : " + url + " is offline or invalid URL"
		print(sap) 
		exit()
	wordlist = raw_input("Enter Wordlist: ")
	flag=0
	panel = []
	try:
		with open(str(wordlist),'r') as adm:
			print(sap)
			print "[Loading] : Loading Panels.."
			time.sleep(2)
			for panels in adm:
				grab = str(panels.replace("\n",""))
				panel.append(grab)
		lenght = str(len(panel))
		print "[Loaded]  : " + lenght + " Panels Loaded.."
	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")
	except IOError as error:
		print "[Error]   : "+ wordlist +" not found"
		print(sap)
		exit()
	try:
		print(sap)
		if lenght >= 1:
			time.sleep(2)
			print "\n[Checking] : Checking Admin Panels  "
			print "---------------------------------------"
			print "| Resp      :       Results           |"
			print "---------------------------------------"
			for x in panel:
				x = x.replace("\n","")
				x = "/" + x
				payload = url + x
				try:
					payload = payload.replace("//","/")
					payload = payload.replace("http:/","http://")
					payload = payload.replace("https:/","https://")

					plreq = urllib2.Request(payload, None, header)
					plresp = urllib2.urlopen(plreq)
					if plresp.code == 200:
						print "[OK] : "+ payload +""
						flag=1
					elif plresp.code == 302:
						print "[FOUND] : "+ payload +""
					elif plresp.code == 403:
						print "[FORBBIDEN] : "+ payload +""
					
				except KeyboardInterrupt:
					sys.exit("\n[User Interrupt] : Exiting .. ")
				except:
					continue
			
			if not flag:
				print "[NO PANEL] : No Panel Found.. "
		elif lenght == 0:
			print "[Error]    : Enter a valid wordlist .."
		else:
			print "[Complete] : Task Complete!"
	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")

def Main():
	AdminGrabber()
if __name__ == "__main__":
	Main()
