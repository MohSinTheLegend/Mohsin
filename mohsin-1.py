# coding=utf-8
#!/usr/bin/python2
# soucre code by Tech Abm
#--------------------------#

import os
import re
import random
import datetime
import requests
import getpass
import hashlib
import threading
import json
import getpass
import time
import hashlib

c = "\033[1;92m"
c2 = "\033[0;97m"
c3 = "\033[1;95m"
c4 = "\033[1;93m"
c5 = "\033[1;91m"
c6 = "\033[0;90m"


banner="""
\033[1;97m      .d888888      888888ba     8888ba.88ba  
\033[1;91m     d8'    88      88    `8b    88  `8b  `8b 
\033[1;97m     88aaaaa88a    a88aaaa8P'    88   88   88 
\033[1;91m     88     88      88   `8b.    88   88   88 
\033[1;97m     88     88      88    .88    88   88   88 
\033[1;91m     88     88      88888888P    dP   dP   dP 
\033[1;97m--------------------------------------------------
\033[1;93m(~)\033[1;97m Tool Author : Tech Abm
\033[1;93m(~)\033[1;97m Github ID   : https://github.com/Tech-abm 
\033[1;93m(~)\033[1;97m Fb Page     : https://m.facebook.com/Techabm
\033[1;97m--------------------------------------------------
"""

def action():
  os.system("clear")
  print banner
  print("")
  try:
    abm = open("/sdcard/.info.txt", "r").read()
  except (KeyError , IOError):
        os.system("cd .loading && python3 .loading.xo")
        os.system("clear")
        print banner
        time.sleep(2)
        print("")
        print("[!] You can not run this tool without api key")
        time.sleep(1)
        print("")
        print("[!] This tool is temporarily locked")
        time.sleep(1)
        print("")
        print("[!] Please confirm api key then to run this tool")
        time.sleep(1)
        print("")
        raw_input("[!] Press enter to chat admin")
        time.sleep(1)
        print("")
        os.system("xdg-open https://wa.me/+923121702940")
        user_action()

def user_action():
  os.system("clear")
  print banner
  print("")
  time.sleep(1)
  os.system("cd .loading && python3 .loading.xo")
  os.system("clear")
  print banner
  print("[ Enter Api Key ]").center(50)
  print("")
  api = raw_input("[!] Put Api Key : ")
  if api =="CFBID11N0V20SPIDABM11N0V2":
    print("")
    time.sleep(1)
    print("\033[1;92mTool login sucessfully").center(50)
    time.sleep(3)
    abm_selection_menu()
  else:
    print("")
    print("\033[1;91mApi key is invalid").center(50)
    print("")
    time.sleep(3)
    user_action()

def abm_selection_menu():
  os.system("clear")
  print banner
  print("")
  print("\033[1;97m[\033[1;93m1\033[1;97m] \033[1;97m Cloning With Auto Password b-api")
  print("")
  print("\033[1;97m[\033[1;94m2\033[1;97m] \033[1;97m Cloning With Custom Password b-api")
  print("")
  print("\033[1;97m[\033[1;95m3\033[1;97m] \033[1;97m Cloning With File/Path Custom Password")
  print("")
  print("\033[1;97m[\033[1;96m0\033[1;97m] \033[1;97m Direct logout")
  main_menu()

def main_menu():
  user_select = raw_input("\n\033[1;97m[!] Choose :\033[1;91m ")
  if user_select =="1":
    os.system("python2 .auto.indirect")
  if user_select =="2":
    os.system("python2 .run.indirect")
  if user_select =="3":
    os.system("python2 .file.indirect")
  if user_select =="0":
    os.system("exit")
  else:
    print("")
    print("\033[1;97mPlease select a valid option").center(50)
    print("")
    time.sleep(1)
    raw_input("\tPress enter to back")
    abm_selection_menu()

if __name__ == '__main__':
  action()
