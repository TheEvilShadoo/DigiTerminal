## Requirements and Simple Installation Instructions:

##### **IF YOU ARE USING WINDOWS, YOU ONLY NEED TO DOWNLOAD THE CHROME WEBDRIVER AND PUT IT IN YOUR WINDOWS PATH (SEE THE INSTRUCTIONS BELOW UNDER THE "If you are on Windows" SECTION), OTHER THAN THAT, JUST DOWNLOAD AND RUN THE .EXE FILE FROM THE RELEASE**

#### If you want to run the source file, or if you are on another OS, then follow the steps below:

## You will Need:

- Python 3.5 or higher (Just download the latest version from the website.)

- Selenium Python Library (To install, just install Python, then open a
Command Prompt/Terminal window and type "pip install selenium")

- The latest version of Google Chrome and its corresponding Webdriver
link: https://chromedriver.chromium.org/downloads
Again, I really prefer Firefox, but the Chrome webdriver
is much easier to use and has better support.

- The last thing you need to do before you can use DigiTerminal is to put
the Chrome webdriver in your "PATH". What this means is you need to
have the Chromedriver in a special location called the "PATH" in order
for Python to locate it. This is the hardest part of the setup process, but
trust me, it's easy:

## If you are on Windows:
Open control panel, click on or search for "System", click on advanced system settings,
click on environment variables, double click on "Path" or click on "Path" once and click edit,
click new, and type in the file path of the Chromedriver executable. I reccomend using
C:\Users\YOUR USERNAME\AppData\Local\Programs\Python\Python38-32\Selenium Chrome Webdriver\,
but you can add any location as long as you don't plan on moving it or its contents.
Of course, before adding this location to your path, you should make sure the location exists
and create any folders if they don't exist already (Note, the AppData folder is hidden by default in Windows, 
set your File Explorer settings to show hidden folders and files before creating new folders.)
Now click "Ok" or "Apply" and "Ok" to close all of your open settings windows.
#### You are now ready to use DigiTerminal!

## If you are on a Mac or Linux:
I only know how to set custom PATH locations on Windows, so
if you use a Mac or Linux, you'll have to just edit line 14 of DigiTerminal.py from:

driver = webdriver.Chrome(options=chrome_options)
to
driver = webdriver.Chrome(executable_path="CHROMEDRIVER FILE PATH HERE", options=chrome_options)

Lastly, make sure you leave the quotation marks around the file path. If you remove them, Python will throw an error and DigiTerminal will be unusable.
#### You are now ready to use DigiTerminal!
