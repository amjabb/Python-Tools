# Python-Tools
Various python scripts for file access / making life easier.

Directory Update:

Given a GitHub link this script will download a folder from Github unzip, and replace or add a folder with the same name in your current working directory. Github link is an argument passed through command line. 

Dependencies: Python, Google Chrome, chromedriver (for selenium) found here https://sites.google.com/a/chromium.org/chromedriver/

Downloads Handler:
 
Python script to watch downloads folder, as soon as a new file is added that file is added to the correct folder and removed from the downloads folder. 
v1 File paths are hardcoded to my computer, doesn't work for folders

TODO: 

Terminal should be hidden until user input is needed.

Script should run at startup.

File paths should be set by user.

Dependencies: Python, Watchdog(pip install watchdog)
