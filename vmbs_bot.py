from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep
import requests
import datetime
import csv
from goto import with_goto #goto, comefrom, label
import secret 


##### THINGS NOT YET IMPLEMENTED ######
#	1. Exception Handling
#	2. Email alert when $0 balance is detected
#	3. Email of final report 
#	4. Pulling of requisite data from Signature/APS/FDA when $0 balance occurs 

##### REDESIGN TASKS ######
#	1. Create global variable for webdriver
#	2. Create init() de_init() functions for webdriver
#	3. Re-use webdriver until all account balance check attempts are completed 

URL = "https://myvmonline.vmbs.com/#/login"
DASHBOARD_URL = "https://myvmonline.vmbs.com/#/dashboard"
LOGOUT_URL = "https://myvmonline.vmbs.com/#/logout"
account_balances = list()
time_of_acct_bal = datetime.datetime.now()
my_driver = None

def init_webdriver():
	return webdriver.Chrome()

def exit_webdriver(my_webdriver):
	my_webdriver.quit()

@with_goto
def get_account_balance():	

	global my_driver	
	my_driver.get(URL)
	
	wait = WebDriverWait(my_driver, 20)

	label .login_page
	try:
		login_page_up = wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div/form/div/div/div[1]/div[1]/div/div/div[1]/h1")))
	except Exception:
		if is_error_page() == True:
			my_driver.get(URL)
		goto .login_page


	label .username
	try:
		username_field = my_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/form/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div/input")
		username_field.send_keys(secret.username + Keys.RETURN)
	except Exception:
		goto .username

	label .password
	try:
		wait.until(presence_of_element_located((By.XPATH,"/html/body/div[1]/div[3]/div/div/form/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/input[2]")))
	except Exception:
		goto .password

	password_field = my_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/form/div/div/div[1]/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/input[2]")
	password_field.send_keys(secret.password + Keys.RETURN)

	# Windows need to be checked 

	label .main_page
	try:
		main_page_up = wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/form/div[2]/div[1]/div[2]/div/div/ul/li[2]/div/ul[2]/li[1]/div")))
		avail_bal_page_result = my_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/form/div[2]/div[1]/div[2]/div/div/ul/li[2]/div/ul[2]/li[1]/div")
	except Exception:
		goto .main_page


	#main_page_up = wait.until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/form/div[1]/div[1]/div[3]/ul/li[1]/strong")))
	#avail_bal_page_result = my_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div[1]/form/div[1]/div[1]/div[3]/ul/li[1]/strong")
	time_of_acct_bal = datetime.datetime.now()
	
	logout = my_driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[4]/responsive-menu/div/div[3]/div[1]/div[2]/ul/li[5]/a/span")
	
	account_balances.append([time_of_acct_bal.strftime("%H:%M:%S"), str(avail_bal_page_result.text).split("\n")[0]])
	sleep(2)

	my_driver.get(LOGOUT_URL)


def display_timestamps_and_balances(time_stamp_acct_bal_list):
	print("#" * 70)
	print("#TIMESTAMP\t\t\t      ACCOUNT BALANCE" )
	for item in time_stamp_acct_bal_list:
		print(" {}\t\t\t\t{}".format(item[0], item[1]))

	
def write_to_csv(*kargs):
	fields = ['TimeStamp', 'Account Balance'] 
  
	# name of csv file 
	filename = kargs[0] #"jse_price_history_update.csv"
	  
	# writing to csv file 
	with open(filename, 'a', newline='') as csvfile: 
	    # creating a csv writer object 
	    csvwriter = csv.writer(csvfile) 
	    if len(kargs) == 1:
	    	# writing the fields 
	    	csvwriter.writerow(fields) 
	    	#csvwriter.writerow(kargs[0])
	    else:
	    	# writing the data rows 
	    	csvwriter.writerow(kargs[1])


def display_last_timestamp_and_balance(time_stamp_acct_bal_list):

	print(" {}\t\t\t\t{}".format(time_stamp_acct_bal_list[-1][0], time_stamp_acct_bal_list[-1][1]))

def is_error_page():
    return my_driver.current_url == "https://myvmonline.vmbs.com/#/error"

def run_acct_bal_check(*kargs):

	global my_driver
	my_driver = init_webdriver()

	if kargs[0] == "attempts":		
		countdown = kargs[1]
		write_to_csv("Account_Balances_Checks.csv")
		while countdown > 0:
			get_account_balance()
			display_last_timestamp_and_balance(account_balances)
			countdown = countdown - 1
			write_to_csv("Account_Balances_Checks.csv", account_balances[-1])
			sleep(1)

	if kargs[0] == "time":
		start_time = datetime.datetime(kargs[1], kargs[2])
		end_time = datetime.datetime(kargs[3], kargs[4])
		print(start_time.hour)
		print(start_time.minute)
		print(end_time.hour)
		print(end_time.minute)


	#display_timestamps_and_balances(account_balances)
	#write_to_csv(account_balances, "Account_Balances_Checks.csv")
	exit_webdriver(my_driver)

	"""
def run_acct_bal_check(number_of_attempts):
	global my_driver
	my_driver = init_webdriver()

	countdown = number_of_attempts
	while countdown > 0:
		try:
			get_account_balance()
		except Exception:
			print("Exception occured. Retrying...")
			get_account_balance()

		display_last_timestamp_and_balance(account_balances)
		countdown = countdown - 1
		sleep(1)


	display_timestamps_and_balances(account_balances)
	write_to_csv(account_balances, "Account_Balances_Checks.csv")
	exit_webdriver(my_driver)


	/html/body/div[1]/div[3]/div/div[1]/form/div[2]/div[1]/div[2]/div/div/ul/li[2]/div/ul[2]/li[1]/div
	/html/body/div[1]/div[3]/div/div[1]/form/div[2]/div[1]/div[2]/div/div/ul/li[2]/div/ul[2]/li[1]/div/span[2]

	/html/body/div[1]/div[3]/div/div[1]/form/div[2]/div[1]/div[2]/div/div/ul/li[2]/div/ul[2]/li[2]/div
	/html/body/div[1]/div[3]/div/div[1]/form/div[2]/div[1]/div[2]/div/div/ul/li[2]/div/ul[2]/li[2]/div/span[2]
	"""