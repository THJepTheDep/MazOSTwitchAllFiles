import urllib.request
import os
import time as tm
from getpass import getpass
import colorama
from colorama import Fore, Back, Style
import subprocess

print("""Welcome To MazOS v0.1.2
            ╭━╮╭━┳━━━┳━━━━╮╱╭━━━┳━━━╮       
            ┃┃╰╯┃┃╭━╮┣━━╮━┃╱┃╭━╮┃╭━╮┃
            ┃╭╮╭╮┃┃╱┃┃╱╭╯╭╯╱┃┃╱┃┃╰━━╮
            ┃┃┃┃┃┃╰━╯┃╭╯╭╋━━┫┃╱┃┣━━╮┃
            ┃┃┃┃┃┃╭━╮┣╯━╰┻┳━┫╰━╯┃╰━╯┃
            ╰╯╰╯╰┻╯╱╰┻━━━━╯╱╰━━━┻━━━╯                   By -----> Maz Inc.      
""")
print("Loading...")
tm.sleep(3)

print("""
[1]     Log in
[2]     Sign up
""")

lg_or_su = input("[?] : ")

if lg_or_su == '1':
    print('Loading Log-In page...')
    tm.sleep(1)
    print("""
    ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
    ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
    ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
    ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
    ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
    ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝           Login saving is currently not working.
    """)
    name = input("Please enter your username: ")
    pwd = getpass("Please enter your password: ")
    print("Logging in...")
    tm.sleep(1)
    print("Checking username...")
    tm.sleep(1)
    print("Checking password...")
    tm.sleep(2)
    print("Successfully logged in!")
    tm.sleep(1)
    print("Loading OS...")
    tm.sleep(1)
    print(Fore.GREEN + "Successfully loaded Maz-OS")
    print(Style.RESET_ALL)
elif lg_or_su == '2':
    print('Loading Sign-up page...')
    tm.sleep(1)
    print("""  
    ░██████╗██╗░██████╗░███╗░░██╗██╗░░░██╗██████╗░
    ██╔════╝██║██╔════╝░████╗░██║██║░░░██║██╔══██╗
    ╚█████╗░██║██║░░██╗░██╔██╗██║██║░░░██║██████╔╝
    ░╚═══██╗██║██║░░╚██╗██║╚████║██║░░░██║██╔═══╝░
    ██████╔╝██║╚██████╔╝██║░╚███║╚██████╔╝██║░░░░░
    ╚═════╝░╚═╝░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░
    """)
    name = input("Please enter your desired username: ")
    password = getpass("Please enter your desired password: ")
    tm.sleep(1)
    print("Successfully signed up!")
    tm.sleep(1)
    print("Loading OS...")
    tm.sleep(1)
    print(Fore.GREEN + "Successfully loaded Maz-OS")
    print(Style.RESET_ALL)
else:
    print('Please select either 1 or 2')
    tm.sleep(1)

while True:
    command = input(f"{name}@root>>>")

    if command == "help":
        print("""
        Here's a list of all the commands:

        help ------------ Lists all the commands
        youtube --------- URL To my youtube channel
        twitch ---------- URL To my twitch channel
        ls -------------- Lists all the files in the directory
        install --------- Install the full version of the OS [Desktop version]

        """)

    elif command == "youtube":
        print("""
        Youtube: https://www.youtube.com/channel/UC752BKj7p_9ipimxmkZr-bg
        """)

    elif command == '':
        print()

    elif command == "twitch":
        print("Twitch: https://www.twitch.tv/thjepthedep")

    elif command == "ls":
        print("List here!")  # TODO: Make 'ls' list all the files in th directory

    elif command == "install":
        print("Installing full version of OS...")
        tm.sleep(3)
        print("Getting Data from Github...")
        tm.sleep(2)
        print("Downloading OS...")

        Y_N = input("Are you sure you want to continue? y/n > ")

        if Y_N == "y" or "Y" or "yes" or "Yes":
            print("Downloading OS...")
            tm.sleep(2)
            url = "https://raw.githubusercontent.com/THJepTheDep/MazOSTwitch/master/DesktopOS.py"
            filename, headers = urllib.request.urlretrieve(url, filename="DesktopOS.py")
            print("download file location: ", filename)
            print("download headers: ", headers)
            tm.sleep(2)
            print("Rebooting.")
            tm.sleep(1)
            print("Rebooting..")
            os.system('python reboot.py')
        elif Y_N == "n" or "N" or "No" or "no":
            print("Installation cancelled.")
            tm.sleep(2)
        else:
            print("Please choose either y or n")


    else:
        print('Please enter a valid command or type help for more information.')
