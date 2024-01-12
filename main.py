from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import undetected_chromedriver as uc


email = "munnyvalasai5@gmail.com"
password = "Manesh@97"
USER_ID = 32902079

STARTING_AMOUNT = int(input("Enter Your trading AMount? "))
WANT_TO_PROFIT_AMOUNT = float(input("Enter Profit amount (means how much profit you want to get)?  "))

GET_PROFIT_AMOUNT = 0.0

driver = uc.Chrome()
driver.get("https://qxbroker.com/en/sign-in")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Enter the email and password work
driver.find_element(By.XPATH, "//form[@action='https://qxbroker.com/en/sign-in/']//input[@placeholder='Email']").send_keys(email)
driver.find_element(By.XPATH, "//form[@action='https://qxbroker.com/en/sign-in/']//input[@placeholder='Password']").send_keys(password)
sleep(2)

# Click on the login button
driver.find_element(By.XPATH, "//div[normalize-space()='Sign in']").click()
sleep(15)


# # After login all work goes here!...
#
# driver.find_element(By.XPATH, "//div[@class='usermenu__info-wrapper']").click()
# sleep(5)
#
# # Get the User ID
# user_id = driver.find_element(By.XPATH, "//span[@class='usermenu__number']").text
# user_id = int(user_id.replace("ID:", ""))
# sleep(3)
#
#
# # Switch to the demo account
# driver.find_element(By.XPATH, "//a[normalize-space()='Demo Account']").click()
# sleep(10)
#
# TRADING_FIRST_TIME_CHECK = 0
# TRADING_NEXT_TIME_CHECK = 0
# profit_amount = ""
# is_profit = False
#
#
# # Trading on Up Button
# def up_button_trading():
#     investment = driver.find_element(By.XPATH, "//input[@class='input-control__input']")
#     investment.send_keys(Keys.CONTROL + "a")
#     investment.send_keys(Keys.DELETE)
#     investment.send_keys(STARTING_AMOUNT)
#     up_button = driver.find_element(By.XPATH, "//button[contains(@class,'button button--success button--spaced call-btn section-deal__button')]")
#     return up_button
#
#
# # Trading on Down Button
# def down_button_trading():
#     investment = driver.find_element(By.XPATH, "//input[@class='input-control__input']")
#     investment.send_keys(Keys.CONTROL + "a")
#     investment.send_keys(Keys.DELETE)
#     investment.send_keys(STARTING_AMOUNT * 2)
#     down_button = driver.find_element(By.XPATH, "//button[contains(@class,'button button--danger button--spaced put-btn section-deal__button')]")
#     return down_button
#
# # Match the User ID here
# if user_id == USER_ID:
#     print("ID matched")
#
#     # Trading work done here
#     while True:
#         sleep(0.1)
#         timer = driver.find_element(By.XPATH, "//div[@class='server-time online']")
#         time_seconds = timer.text
#         time_seconds = time_seconds.replace('UTC+5', '')
#         seconds = int(time_seconds.split(":")[-1])
#         print(seconds)
#
#         # To break the loop here
#         if GET_PROFIT_AMOUNT >= WANT_TO_PROFIT_AMOUNT:
#             print("You profit matched to your desired profit\nSo end of trading")
#             break
#
#         if seconds == 0:
#             print("Your trading start on this time", seconds)
#
#             # First time trading start when there is no any profit
#             if TRADING_FIRST_TIME_CHECK == 0:
#
#                 # up_button_trading function calling
#                 up_btn_result = up_button_trading()
#                 up_btn_result.click()
#                 sleep(60)
#
#                 # get the profit or loss amount here
#                 profit = driver.find_elements(By.XPATH, "//div[contains(@class,'trades-list-item__delta-right')][1]")
#                 for item in range(len(profit)):
#                     profit_amount = profit[item].text
#                     break
#                 profit_amount = profit_amount.replace(" $", "")
#
#                 if profit_amount[0] == "+":
#                     """Geting Profit """
#                     print("Profit")
#                     profit = float(profit_amount.replace("+", ""))
#                     GET_PROFIT_AMOUNT += profit
#                     is_profit = True
#                 else:
#                     """Geting Loss """
#                     print("Loss")
#                     is_profit = False
#
#                 TRADING_FIRST_TIME_CHECK == 2 # to change the mode of starting
#                 TRADING_NEXT_TIME_CHECK = 1   # to change the next mode of trading
#
#
#             # Next time trading start when there is profit or loss
#             if TRADING_NEXT_TIME_CHECK == 1:
#
#                 if is_profit == True:
#                     """Up Btn
#                     When we get the Profit"""
#                     # up_button_trading function calling
#                     up_btn_result = up_button_trading()
#                     up_btn_result.click()
#                     sleep(60)
#
#                     # get the profit or loss amount here
#                     profit = driver.find_elements(By.XPATH, "//div[contains(@class,'trades-list-item__delta-right')][1]")
#                     for item in range(len(profit)):
#                         profit_amount = profit[item].text
#                         break
#                     profit_amount = profit_amount.replace(" $", "")
#
#                     if profit_amount[0] == "+":
#                         """Geting Profit """
#                         print("Profit")
#                         profit = float(profit_amount.replace("+", ""))
#                         GET_PROFIT_AMOUNT += profit
#                         is_profit = True
#                     else:
#                         """Geting Loss """
#                         print("Loss")
#                         is_profit = False
#
#                 elif is_profit == False:
#                     """ Down Btn
#                     When we get the Loss """
#
#                     # up_button_trading function calling
#                     down_btn_result = down_button_trading()
#                     down_btn_result.click()
#                     sleep(60)
#
#                     # get the trading amount here
#                     profit = driver.find_elements(By.XPATH,  "//div[contains(@class,'trades-list-item__delta-right')][1]")
#                     for item in range(len(profit)):
#                         profit_amount = profit[item].text
#                         break
#                     profit_amount = profit_amount.replace(" $", "")
#
#                     # To check the loss or profit
#                     if profit_amount[0] == "+":
#                         """Getting The Profit """
#
#                         print("Profit")
#                         profit = float(profit_amount.replace("+", ""))
#                         GET_PROFIT_AMOUNT += profit
#                         is_profit = True
#                     else:
#                         """Getting The Loss """
#
#                         print("Loss")
#                         is_profit = False
#
# else:
#     print("Not ID match!...")


# driver.quit()
input()