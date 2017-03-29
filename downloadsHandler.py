'''
	Basic python script handling downloads in real time
	once file is run any download matching an existing folders
	name will be place in the appropriate folder
'''

__author__ = "Amir Jabbari"
__version__ = '0.1'

#!/usr/local/bin/python3
import time
import os  
import sys
import shutil
from select import select

from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler  

class HandleNames:


	def __init__(self, filePath = ''):

		self.filePath = filePath

	'''
		If Directory doesn't exist create it, if it does exist then copy the file
		to the proper directory and delete the file from downloads.
		@param: specificFilePath is the name of the folder to which the file is copied 
	'''
	def copyFile(self, specificFilePath):

		myFolderPath = '/Library/Mobile Documents/com~apple~CloudDocs/SJSUSPRING17'
		finalFolder = os.path.expanduser("~") + myFolderPath + specificFilePath
		if os.path.isfile(self.filePath):
			if not os.path.exists(finalFolder):
	    			os.makedirs(finalFolder)
			shutil.copy2(self.filePath, finalFolder)
			shutil.os.remove(self.filePath)
		elif os.path.isdir(self.filePath):
			dirName = '/' + (self.filePath.split('/'))[-1]
			if not os.path.exists(finalFolder):
	    			os.makedirs(finalFolder)
			try:
				shutil.copytree(self.filePath,finalFolder + dirName)
			except OSError:
				print("Folder not recognized. Leaving it there.")
			else:
				shutil.rmtree(self.filePath)
		else:
			shutil.copy2(self.filePath, finalFolder)
			shutil.os.remove(self.filePath)

	'''
		If the directory name is not found in the file name then prompt the
		use which directory they would like to pass the file into
	'''
	def nameNotEvident(self):

		print("Would you like to move the file to any of these special directories?")
		print("Enter 0 to pass")
		print("1. CMPE 140")
		print("2. CMPE 146")
		print("3. CMPE 188")
		print("4. CMPE 110")
		print("5. Senior Project")
		'''This is a straightforward interface to the Unix select() system call. 
		The first three arguments are sequences of ‘waitable objects’'''
		selectInput, _, _ = select( [sys.stdin], [], [], 10 )
		if selectInput:
		  choice = int(sys.stdin.readline().strip())
		else:
			choice = 0
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

	'''
		If the directory name is  found in the file name then copy the 
		file into the corresponding directory
	'''
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

    #Once a file is added to the folder process file
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