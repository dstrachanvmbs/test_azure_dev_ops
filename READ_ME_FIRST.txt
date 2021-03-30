***** INSTALLATION GUIDE *****

DOWNLOAD AND INSTALL GOOGLE CHROME:
https://www.google.com/chrome/

DOWNLOAD AND INSTALL PYTHON:
https://www.python.org/ftp/python/3.7.6/python-3.7.6.exe

DOWNLOAD AND INSTALL PIP:
1. DOWNLOAD LINK: https://bootstrap.pypa.io/get-pip.py
2. OPEN A COMMAND PROMPT, NAVIGATE TO THE FOLDER WITH get-pip.py FILE AND TYPE "python get-pip.py"

DOWNLOAD AND INSTALL GOOGLE CHROME WEBDRIVER FOR PYTHON/SELENIUM:
1. GO TO https://chromedriver.chromium.org/downloads AND DOWNLOAD AND INSTALL THE APPROPRIATE VERSION DRIVER FOR YOUR GOOGLE CHROME
NOTE: IN A GOOGLE CHROME TAB, TYPE "chrome://settings/help" TO SEE CHROME VERSION


INSTALL PYTHON LIBRARY REQUIREMENTS:
1. DOWNLOAD THE requirements.txt file
2. OPEN A COMMAND PROMPT, NAVIGATE TO THE FOLDER WITH THE requirements.txt FILE AND TYPE "pip install -r requirements.txt"

SETUP FILE WITH ACCESS CREDENTIALS:
1. DOWNLOAD FILE secret.py
2. INPUT YOUR USERNAME AND PASSWORD IN THE APPROPRIATE FIELDS AND SAVE THE FILE

***** HOW TO RUN THE SCRIPT *****
1. DOWNLOAD THE SCRIPT vmbs_bot.py (MAKE SURE THIS IS SAVED IN THE SAME FOLDER AS secret.py)
2. OPEN A COMMAND PROMPT, NAVIGATE TO THE FOLDER WITH THE vmbs_bot.py FILE AND TYPE "python -i vmbs_bot.py"
3. ">>>" WILL APPEAR. TYPE "run_acct_bal_check("attempts", <num>)" where <num> is the number of times you want the application to check the available balance
	OR TYPE "run_acct_bal_check("time", <start hour>, <start minute>, <end hour>, <end minute>)"
