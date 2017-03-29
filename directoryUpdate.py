'''
    Basic python script handling github downloads
    this script takes a github link as a parameter and
    downloads the respective folder from the link
    and replaces an existing folder with the same name
'''

__author__ = "Amir Jabbari"
__version__ = '0.1'

#!/usr/local/bin/python3
import os
import shutil
import sys
import requests
import glob
import zipfile
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


pathOfFolderToBeReplaced = ''
driver = webdriver.Chrome()
scriptDirectory = os.getcwd()

gitHubLink = str(sys.argv[1])

#Use Selenium driver to download zip file from github link
driver.get(gitHubLink)
directoryName = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[1]/div[1]/h1/strong/a')
print(directoryName.text)
cloneOrDownloadButton = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[4]/div[1]/button')
cloneOrDownloadButton.click()
downloadZipButton = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[4]/div[1]/div/div/div[2]/a[2]')
downloadZipButton.click()
driver.close()
driver.quit()

#wait for async download this has to be changed later
time.sleep(5)

#Change directory to downloads and unzip newly downloaded file
os.chdir(os.path.expanduser('~/Downloads/'))
zipFileName = min(glob.iglob('*.zip'), key = os.path.getctime) #get most recent zip file
zipFilePath = os.path.abspath(zipFileName) # get full path of files
zipFileObject = zipfile.ZipFile(zipFilePath) # create zipfile object
zipFileObject.extractall('.') # extract file to dir
zipFileObject.close() # close file

#Get folder name by concatenating zip file name
if zipFileName.endswith('.zip'):
    folderName = zipFileName[:-4]
    zipFilePath = zipFilePath[:-4]
else:
	folderName = zipFileName

'''In case multiple files have been downloaded we need to get rid of the number
	at the end of the file name i.e. file(1).zip'''
if folderName.endswith(')'):
    folderName = folderName[:-4]

'''Search current working directory as well as subdirectories
	for folder with the same name to replace'''
os.chdir(os.path.expanduser(scriptDirectory)) #move to script directory
for (dirpath, dirnames, folderNames) in os.walk('.'): 
    for dir in dirnames:
        if dir == folderName:
            pathOfFolderToBeReplaced = os.path.abspath(dir)

#If the folder exists remove it
if folderName in pathOfFolderToBeReplaced:
	shutil.rmtree(pathOfFolderToBeReplaced)

#Copy the downloaded directory to a directory of the same name
pathOfFolderToBeReplaced = folderName
shutil.copytree(zipFilePath,pathOfFolderToBeReplaced)

#Cleanup
os.chdir(os.path.expanduser('~/Downloads/'))
os.remove(zipFilePath) # delete zipped file
shutil.rmtree(folderName) #delete folder from downloads
