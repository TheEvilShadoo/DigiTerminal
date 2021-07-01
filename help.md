## Dependencies and _Simple_ Installation Instructions

## You will Need:

- Python 3.5 or higher: https://www.python.org/

- Selenium Python Library (To install, just install Python, then open a
Command Prompt/Terminal window and type "pip install selenium" (use "pip3 if on Mac or Linux"))

- The latest version of Google Chrome and its corresponding Webdriver
link for the webdriver: https://chromedriver.chromium.org/downloads

## How to set up DigiTerminal:

Before you can use DigiTerminal, you need to put the Chrome webdriver in your "PATH". What this means is you need to
have the Chromedriver in a special location called the "PATH" in order
for Python to locate it.

### If you are on Windows:
Open control panel, click on or search for "System", click on advanced system settings,
click on environment variables, double click on "Path" or click on "Path" once and click edit,
click new, and type in the file path of the Chromedriver executable. I reccomend using
C:\Users\YOUR USERNAME\AppData\Local\Programs\Python\Python38-32\Selenium Chrome Webdriver\,
but you can add any location as long as you don't plan on moving it or its contents.
Of course, before adding this location to your path, you should make sure the location exists
and create any folders if they don't exist already (Note, the AppData folder is hidden by default in Windows, 
set your File Explorer settings to show hidden folders and files before creating new folders.)
Now click "Ok" or "Apply" and "Ok" to close all of your open settings windows.
#### You are now ready to run DigiTerminal! (DigiTerminal.py)

### If you are on a Mac or Linux:
I only know how to set custom PATH locations on Windows, so
if you use a Mac or Linux, you'll have to just edit line 14 of DigiTerminal.py from:

driver = webdriver.Chrome(options=chrome_options)
to
driver = webdriver.Chrome(executable_path="<CHROMEDRIVER FILE PATH HERE>", options=chrome_options)

Where <CHROMEDRIVER FILE PATH HERE> should be replaced with the path to your Chromedriver executable. The file can be located anywhere as long as the path points to it.
#### You are now ready to run DigiTerminal!
