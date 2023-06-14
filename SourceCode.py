import os
import sys
import hashlib
import requests
from time import sleep

import getpass
import msvcrt

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PASS_STR: str = "e376efc583bc93b5b38402ee7ea5ee4b"

os.system("cls")

#response = requests.get("https://raw.githubusercontent.com/90-C0KE/VenApp/main/Servers")
#print(response.text)

print("""
░█████╗░███╗░░██╗░█████╗░███╗░░░███╗░█████╗░██╗░░░░░██╗░░░██╗
██╔══██╗████╗░██║██╔══██╗████╗░████║██╔══██╗██║░░░░░╚██╗░██╔╝
███████║██╔██╗██║██║░░██║██╔████╔██║███████║██║░░░░░░╚████╔╝░
██╔══██║██║╚████║██║░░██║██║╚██╔╝██║██╔══██║██║░░░░░░░╚██╔╝░░
██║░░██║██║░╚███║╚█████╔╝██║░╚═╝░██║██║░░██║███████╗░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░
""")
print("===================================")
print("= Website Unblocker")
print("= Made by 1K0DE")
print("===================================")

print("\nSecurity key required to use tool!")
P_WORD = getpass.getpass(prompt="Enter key here: ").encode()

if hashlib.md5(P_WORD).hexdigest() != PASS_STR:
    print("\n | Error : Invalid Security Key!")
    print("\n[ Press Any Key ]\n")
    msvcrt.getch()
    sys.exit()
else:
    print("\n-> Success: Correct security key!")
    print("-> Checking app stats...")

def check_stats():
    response_1 = requests.get("https://raw.githubusercontent.com/90-C0KE/Anomaly_Stats/main/Stats")

    if str(response_1.text).lower() != "_up_\n":
        os.system("cls")
        print(response_1.text)
        print(type(response_1.text))
        print("""
    ░██████╗██╗░░██╗██╗░░░██╗████████╗██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗
    ██╔════╝██║░░██║██║░░░██║╚══██╔══╝██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║
    ╚█████╗░███████║██║░░░██║░░░██║░░░██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║
    ░╚═══██╗██╔══██║██║░░░██║░░░██║░░░██║░░██║██║░░██║░░████╔═████║░██║╚████║
    ██████╔╝██║░░██║╚██████╔╝░░░██║░░░██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║
    ╚═════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝
        """)
        print("===================================")
        print("Anomaly has been temporarily shutdown by 1K0DE.")
        print("\n[ Press Any Key ]\n")
        msvcrt.getch()
        sys.exit()

def ask():
    check_stats()
    WEB_URL = input("\nWhat website would you like to unblock? > ")

    if WEB_URL == "exit":
        sys.exit()

    if WEB_URL[:8] != "https://":
        print("\n | Error : Your website must begin with \"https://\". Please try again.")
        ask()

    if len(WEB_URL) <= 8:
        print("\n | Error : Your URL must be more than five characters since it includes \"https://\" and a domain. Please try again.")
        ask()

    print(f"\n | Attemping to run website... {WEB_URL}")

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--guest')
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(WEB_URL)
    #close_inp = input("Type anything to close window > ")
    sleep(5)
    print("\n | Successfully ran website in unblocked browser...")
    print(" | Thank you for using this tool!")
    print(" | Made by 1K0DE")
    ask()

ask()
