#!/usr/local/bin/python3
import time
import os  
import sys
import shutil
import select

from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  

class HandleNames:

	def __init__(self, filePath = ''):
		self.filePath = filePath

	def copyFile(self, specificFilePath):
		myFolderPath = '/Library/Mobile Documents/com~apple~CloudDocs/SJSUSPRING17'
		basePath = os.path.expanduser("~") + myFolderPath
		if not os.path.exists(basePath+specificFilePath):
    			os.makedirs(basePath+specificFilePath)
		shutil.copy2(self.filePath, basePath+specificFilePath)
		shutil.os.remove(self.filePath)

	def nameNotEvident(self):
		print("Would you like to move the file to any of these special directories?")
		print("Enter 0 to pass")
		print("1. CMPE 140")
		print("2. CMPE 146")
		print("3. CMPE 188")
		print("4. CMPE 110")
		print("5. Senior Project")
		#Try to put a time on the input but it isn't working
		'''This is a straightforward interface to the Unix select() system call. 
		The first three arguments are sequences of ‘waitable objects’'''
		# selectInput, selectOutput, selectExcept = select.select( [sys.stdin], [], [], 1 )
		# if selectInput:
		# 	choice = int(sys.stdin.readline().strip())
		choice = int(input("Choice: "))
		if choice == 1:
			self.copyFile('/CMPE140')
		elif choice == 2:
			self.copyFile('/CMPE146')
		elif choice == 3:
			self.copyFile('/CMPE188')
		elif choice == 4:
			self.copyFile('/CMPE110')
		elif choice == 5:
			self.copyFile('/SeniorProject')
		else:
			self.copyFile('/UnsortedDownloads')

	def nameEvident(self):
		#edit this variable to the path of your own folders
		myFolderPath = '/Library/Mobile Documents/com~apple~CloudDocs/SJSUSPRING17'
		basePath = os.path.expanduser("~") + myFolderPath

		if "140" in self.filePath:
			self.copyFile('/CMPE140')
		elif "146" in self.filePath:
			self.copyFile('/CMPE146')
		elif "188" in self.filePath or "ipynb" in self.filePath:
			self.copyFile('/CMPE188')
		elif "110" in self.filePath:
			self.copyFile('/CMPE110')
		elif "195" in self.filePath:
			self.copyFile('/SeniorProject')
		else:
			self.nameNotEvident()



class MyHandler(PatternMatchingEventHandler):
	
    def process(self, event):
    	handle = HandleNames(event.src_path)
    	handle.nameEvident()
    	print("Transfer Complete")
    	#print( event.src_path, event.event_type)  # print now only for debug

    def on_created(self, event):
        self.process(event)

if __name__ == '__main__':
    args = os.path.expanduser('~/Downloads/')
    observer = Observer()
    observer.schedule(MyHandler(), path=args)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()