#!/bin/python3

import os
import sys

banner = 'figlet -c "H4ck3r313"'
os.system(banner)

if not 'SUDO_UID' in os.environ.keys():
    print ("This program requires super user priv and You're not one of em.")
    proud = input("\n>Are you proud of yourself? [default \"n\"] (y/n): ")
    if(proud == "y"):
        print ("""\nHow can you be!, You're not ROOT! ;)
(sighs)
                If you still wanna update
                Try \"sudo ./update.py\" """)
    elif(proud == "n" or proud == ""):
        print ("""\nmate, You good? :)
        Now just try \"sudo ./update.py\" """)        
    else:
        print("""\nYou IDIOT!,
                I asked you to say 'y' or 'n'
                Now just try \"sudo ./update.py\" 
                You creepy Lil bastard!""")

    bye = os.system('figlet -c Be ROOT +')    
    exit(1)

else:
    print("------------------ Wow you're root and I'm groot! -----------------\n")
    
    print("---------"*2 + "UPDATING" + "---------"*2 )
    # update = ("sudo apt update")
    # os.system(update)

    upg = input("\n> Do you want to full-upgrade? [default \"y\"] (y/n): ")
    if (upg == "y" or upg == ""):
        print("\n" + "---------"*2 + "FULL-UPGRADING" + "---------"*2 )
        # upgrade = ("sudo apt full-upgrade")
        # os.system(upgrade)

        uph = input("\n> Do you want to upgrade youre kernel headers? [default \"y\"] (y/n): ")
        if (uph == "y" or uph == ""):
            print("\n" + "---------"*2 + "INSTALLING/UPDATING KERNEL HEADERS" + "---------"*2)
            # headers = ("sudo apt install linux-headers-$(uname -r)")
            # os.system(headers)
    else:
        print("\nYou missed full-upgrade and kernel headers")

    clean = input("\n> Do You want to run autoclean and autoremove? [default \"y\"] (y/n): ")
    if (clean == "y" or clean == "Y" or clean == ""):
        print("\n" + "---------"*2 + "CLEANING..." + "---------"*2 )
        # autoclean = ("sudo apt autoclean")
        # autoremove = ("sudo apt autoremove")
        # os.system(autoclean + "&&" + autoremove)

    elif(clean == "n" or clean == "N"):
        print("\nHave a nice day!")
        
    else:
        print("\nInvalid choice I'm done here! BYE :>")
        

    if((upg == "y" or upg == "") and (uph == "y" or uph == "") and (clean == "y" or clean == "")):
        print("Manh!, You're all set...")
    else:
        print("You've missed upgrade or cleanup!")

    bye = os.system('figlet -c bye +')
    exit(0)
