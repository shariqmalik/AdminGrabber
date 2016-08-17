#!/usr/bin/python

import urllib2
import time
import sys

flag = 0 # A Flag to varify if no admin panel found
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
sap = "-" * 69

def urlFix(url): #Fix URL if http or https missing
        if "http://" in url or "https://" in url:
                return url

        return "http://" + url

def AdminGrabber():
	try:
		url = urlFix(raw_input("Enter URL: "))
		ua = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36"
		header = {'User-Agent' : ua}

		req = urllib2.Request(url, None, header)
		resp = urllib2.urlopen(req)

		print(sap)
		print("[Connecting] : %s..." % url)

		if resp.code == 200:
			time.sleep(2)
			print("[Connected]  : %s is connected" % url)
			print(sap)

	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")

	except:
		print(sap)
		print("[Connecting] : %s" % url)
		time.sleep(2)

		print("[Failed] : %s is offline or invalid URL" % url)
		print(sap)
		sys.exit()

        flag = 0
        panel = []
        wordlist = raw_input("Enter Wordlist: ")

	try:
		with open(wordlist) as adm: # default open is 'r'
			print(sap)
			print("[Loading] : Loading Panels..")
			time.sleep(2)

			for panels in adm:
				grab = panels.rstrip() # will remove end of line \n
				panel.append(grab)

		badlength = len(panel)
		print("[Loaded]  : %d Panels Loaded.." % badlength)
		time.sleep(2)
		
		panel = list(set(panel)) # this will remove duplicates [a set has no duplicates]
		length = len(panel)
		print("[Using]   :"),
		print("%d/%d Panels being used (%d duplicates).." % (length, badlength, badlength - length))

	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")

	except IOError as error:
		print("[Error]   : %s not found" % wordlist)
		print(sap)
		sys.exit()

	try:
		print(sap)
                

		if length > 0: # Checking validity of Wordlist
			time.sleep(2)
			print("\n[Checking] : Checking Admin Panels  ")
			print("---------------------------------------")
			print("| Resp     :        Results           |")
			print("---------------------------------------")
			counter = 1
			for x in panel:
				x = "/" + x
				payload = url + x
				try:
					#correction of duplication of http or https
					payload = payload.replace("//", "/")
					payload = payload.replace("http:/", "http://")
					payload = payload.replace("https:/", "https://")

					plreq = urllib2.Request(payload, None, header)
					plresp = urllib2.urlopen(plreq)

				except KeyboardInterrupt:
					sys.exit("\n[User Interrupt] : Exiting .. ")

				except:
					continue
				else:
					if plresp.code == 200: #show pages with proper response
						flag = 1
						print("[OK] : %s" % payload)

					elif plresp.code == 302: #show redirected pages
						flag = 1
						print("[FOUND] : %s" % payload)

					elif plresp.code == 403: #show Forbbiden pages
						flag = 1
						print("[FORBBIDEN] : %s" % payload)

			if not flag:
				print("[NO PANEL] : No Panel Found.. ")

		else:
			print("[Error]    : Enter a valid wordlist ..")

	except KeyboardInterrupt:
		sys.exit("\n[User Interrupt] : Exiting .. ")

def Main():
	AdminGrabber()
if __name__ == "__main__":
	Main()
