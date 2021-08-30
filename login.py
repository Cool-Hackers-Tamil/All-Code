#!/data/data/com.termux/files/usr/bin/env python

import getpass
import hashlib
import sys
import os,time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
txt = '''
                   -o          o-
                    +hydNNNNdyh+
                  +mMMMMMMMMMMMMm+
                `dMMm^NMMMMMMN^mMMd`
                hMMMMMMMMMMMMMMMMMMh
            ..  yyyyyyyyyyyyyyyyyyyy  ..
          .mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.
          :MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
          :MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
          :MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
          :MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
          -MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
           +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
                mMMMMMMMMMMMMMMMMMMm
                `/++MMMMh++hMMMM++/`
                    MMMMo  oMMMM
                    MMMMo  oMMMM
                    oNMm-  -mMNs

               |-------------------|
               | Welcome To Termux |
               |-------------------|

'''
logo="""
echo "
                  Welcome To Termux

                 ..;lxO0KXXXK0Oxl:..
              ,o0WMMMMMMMMMMMMMMMMMMKd,
           'xNMMMMMMMMMMMMMMMMMMMMMMMMMWx,
         :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:
       .KMMMMMMMMMMMMMMMWNNNWMMMMMMMMMMMMMMMX,
      lWMMMMMMMMMMMXd:..     ..;dKMMMMMMMMMMMMo
     xMMMMMMMMMMWd.               .oNMMMMMMMMMMk
    oMMMMMMMMMMx.                    dMMMMMMMMMMx
   .WMMMMMMMMM:                       :MMMMMMMMMM,
   xMMMMMMMMMo                         lMMMMMMMMMO
   NMMMMMMMMW                    ,cccccoMMMMMMMMMWlccccc;
   MMMMMMMMMX                     ;KMMMMMMMMMMMMMMMMMMX:
   NMMMMMMMMW.                      ;KMMMMMMMMMMMMMMX:
   xMMMMMMMMd                        ,0MMMMMMMMMMK;
   .WMMMMMMMMMc                         'OMMMMMM0,
    lMMMMMMMMMMk.                         .kMMO'
     dMMMMMMMMMMWd'                         ..
      cWMMMMMMMMMMMNxc'.                     Version 1.03
       .0MMMMMMMMMMMMMMMMWc
         ;0MMMMMMMMMMMMMMMo.
           .dNMMMMMMMMMMMMo
              'oOWMMMMMMMMo
                  .,cdkO0K;                  By Harshad" | lolcat -a -d 1
"""
out="""
echo "
                   Termux Locked
                  Invalid Password

                 ..;lxO0KXXXK0Oxl:..
              ,o0WMMMMMMMMMMMMMMMMMMKd,
           'xNMMMMMMMMMMMMMMMMMMMMMMMMMWx,
         :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:
       .KMMMMMMMMMMMMMMMWNNNWMMMMMMMMMMMMMMMX,
      lWMMMMMMMMMMMXd:..     ..;dKMMMMMMMMMMMMo
     xMMMMMMMMMMWd.               .oNMMMMMMMMMMk
    oMMMMMMMMMMx.                    dMMMMMMMMMMx
   .WMMMMMMMMM:                       :MMMMMMMMMM,
   xMMMMMMMMMo                         lMMMMMMMMMO
   NMMMMMMMMW                    ,cccccoMMMMMMMMMWlccccc;
   MMMMMMMMMX                     ;KMMMMMMMMMMMMMMMMMMX:
   NMMMMMMMMW.                      ;KMMMMMMMMMMMMMMX:
   xMMMMMMMMd                        ,0MMMMMMMMMMK;
   .WMMMMMMMMMc                         'OMMMMMM0,
    lMMMMMMMMMMk.                         .kMMO'
     dMMMMMMMMMMWd'                         ..
      cWMMMMMMMMMMMNxc'.                     Version 1.03
       .0MMMMMMMMMMMMMMMMWc
         ;0MMMMMMMMMMMMMMMo.
           .dNMMMMMMMMMMMMo
              'oOWMMMMMMMMo
                  .,cdkO0K;                  By Harshad" | lolcat -a -d 1
"""
os.system(logo)
print(bcolors.OKBLUE)

password = getpass.getpass()

filepass = open("/data/data/com.termux/files/usr/share/login/.pass", "r")
filepass = filepass.read().split("\n")[0]

password = password.encode()
password = hashlib.sha1(password).hexdigest()

if password != filepass:
    os.system('clear')
    os.system(out)
    time.sleep(5)
    os.system("exit")
else:
    prefix = "/data/data/com.termux/files/usr"
    home = "/data/data/com.termux/files/home"
    motd = False
    hush = False

    os.system("clear")

    try:
        open(prefix + "/etc/motd")
        motd = True
    except:
        motd = False

    try:
        open(home + "/.hushlogin")
        hush = True
    except:
        hush = False

    if motd and not hush:
        print(open(prefix + "/etc/motd").read())
    
    os.system(sys.argv[1] + " " + sys.argv[2])
