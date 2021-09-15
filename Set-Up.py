import os, time
from banner import tools,setbash,welban,about
from color import red,green,pink,blue,yellow

def terban():
 try:
   os.system('clear')
   print(green+'[+] '+yellow+'Checking For Updates')
   os.system('apt-get -y update &>> install.log')
   print(green+'[+] '+yellow+'Upgrading...')
   os.system('apt-get upgrade -y &>> install.log')
   print(green+'[+] '+yellow+'Installing Root-Repo')
   os.system('pkg install root-repo &>> install.log')
   print(green+'[+] '+yellow+'Installing Unstable-Repo')

   os.system('pkg install unstable-repo &>> install.log')

   print(green+'[+] '+yellow+'Installing x11-repo')
   os.system('pkg install x11-repo &>> install.log')
   print(green+'[+] '+yellow+'Installing Some Packages')
   print(green+'[+] '+yellow+'installing Figlet')
   os.system('apt-get install figlet -y &>> install.log')
   print(green+'[+] '+yellow+'Installing Toilet')
   os.system('apt install toilet -y &>> install.log')
   print(green+'[+] '+yellow+'Installing Cow Say')
   os.system('apt install cowsay -y &>> install.log')
   print(green+'[+] '+yellow+'Installing SL')
   os.system('apt install sl -y &>> install.log')
   print(green+'[+] '+yellow+'Installing Nano')
   os.system('apt install nano -y &>> install.log')
   print(green+'[+] '+yellow+'Installing Ruby')
   os.system('apt install ruby -y &>> install.log')
   print(green+'[+] '+yellow+'Installing Lolcat')
   os.system('gem install lolcat &>> install.log')
   print(green+'[+] '+yellow+'Installing Python 2')
   os.system('pkg install python2 &>> install.log')
   print(green+'[+] '+yellow+'Installing Git' )
   os.system('pkg install git &>> install.log')
   print(green+'[+] '+yellow+'Installing Python 3')
   os.system('pkg install python &>> install.log')
   print(green+'[+] '+yellow+'Installed Packages' )
   print(red+'[+] '+green+'Removing Installation Log')
   os.system('rm install.log')
 except:
   quit()
   print(red+"[+] "+pink+"User Exited")

def old():
   try:
     print(green+'[+] '+yellow+'Removed Old Bash Shell')
     os.system("cd /data/data/com.termux/files/usr/etc && rm bash.bashrc ")
     os.system("cd /data/data/com.termux/files/home/All-Code")
     os.system("cp bash.bashrc /data/data/com.termux/files/usr/etc && cd /data/data/com.termux/files/usr/etc && chmod 777 bash.bashrc")
     print(green+ '[+] '+yellow+"Adding New Bash Shell")
     os.system("cd /data/data/com.termux/files/home/All-Code")
     print(green+'[+] '+yellow+ "Adding Codeing Files")
     os.system("cp color.py /data/data/com.termux/files/usr/etc")
     os.system("cp update.py /data/data/com.termux/files/usr/etc")
     os.system("cp logo.py /data/data/com.termux/files/usr/etc")
     os.system("cp web.py /data/data/com.termux/files/usr/etc")
     os.system("cp molafix.py /data/data/com.termux/files/usr/etc")
     print(green+'[+] '+yellow+"Bash Shell Installed")
   except:
     print(red+"[+] "+blue+"User Exited")
     quit()
def new():
  try:
     print(green+'[+] '+yellow+'Removed Old Bash Shell')
     os.system("cd /data/data/com.termux/files/usr/etc && rm bash.bashrc")
     os.system("cd /data/data/com.termux/files/home/All-Code")
     os.system("cp bash.bashrc-1.4 /data/data/com.termux/files/usr/etc")
     os.system("cd /data/data/com.termux/files/usr/etc && cp bash.bashrc-1.4 bash.bashrc && rm bash.bashrc-1.4 && chmod 777 bash.bashrc")
     os.system("cp color.py /data/data/com.termux/files/usr/etc")
     print(green+ '[+] '+yellow+"Add New Bash Shell")
     os.system("cd /data/data/com.termux/files/home/All-Code")
     print(green+'[+] '+yellow+ "Adding Codeing Files")
     os.system("cp update.py /data/data/com.termux/files/usr/etc")
     os.system("cp logo.py /data/data/com.termux/files/usr/etc")
     os.system("cp web.py /data/data/com.termux/files/usr/etc")
     os.system("cp molafix.py /data/data/com.termux/files/usr/etc")
     print(green+'[+] '+yellow+"Bash Shell Installed")
  except:
     print(red+"[+] "+blue+"User Exited")
     quit()
def code():
  try:
    got=input(green+'Bash '+yellow+'>>> ')
    if got == ('1'):
      terban()
      old()
    elif got == ('2'):
      terban()
      new()
    else:
      print(red+'[+] '+yellow+'Input wrong')
      print(red+'[+] '+yellow+'Exiting')
      quit()
  except:
    print(red+"[+] "+blue+"User Exited")
    quit()
def gittools():
  try:
    print(tools)
    get=input(green+'>>> '+yellow)
    if get == ('1'):
      os.system('')
      print(green+'[+]'+yellow+'Installing TBomb')
      os.system("cd /data/data/com.termux/files/home && git clone https://github.com/TheSpeedX/TBomb.git &>> installing")
      os.system("rm installing")

    elif get == ('2'):
      print(green+'[+]'+yellow+'Installing ZPhisher')
      os.system('cd /data/data/com.termux/files/home && git clone https://github.com/htr-tech/zphisher.git &>> installing')
      os.system("rm installing")


    elif get == ('3'):
      print(green+'[+]'+yellow+'Installing Little Brother')
      os.system('cd /data/data/com.termux/files/home && git clone https://github.com/lulz3xploit/LittleBrother.git &>> installing')
      os.system("cd /data/data/com.termux/files/home/LittleBrother && python3 -m pip install -r requirements.txt && cd /data/data/com.termux/files/home/All-Code &&  clear")
      os.system("rm installing")
    else:
      print(red+'[+]'+yellow+'Wrong Input')
      print(red+'[+]'+yellow+'Exiting')
      quit()
  except:
    print(red+'[+]'+yellow+'User Exit')
    print(red+'[+]'+yellow+'Exiting')
    quit()
#-This-IS-too-Old-Code-So-Don't-Use-This...----------------|
HackTool=""" #                                             |
cd $HOME #                                                 |
echo 'Installing TBomb' #                                  |
git clone https://github.com/TheSpeedX/TBomb.git #         |
clear  #                                                   |
echo 'Installing  Zphisher' #                              |
git clone git://github.com/htr-tech/zphisher.git #         |
clear #                                                    |
echo 'Installing Little Brother'  #                        |
git clone https://github.com/lulz3xploit/LittleBrother.git |
cd /data/data/com.termux/files/home/LittleBrother #        |
python3 -m pip install -r requirements.txt   #             |
cd /data/data/com.termux/files/home/All-Code #             |
clear                                      #               | 
""" #                                                      |
#----------------------------------------------------------
def start():
  os.system('clear')
  print(welban)
  user=input('>>> ')
  if user==('1'):
    print(setbash)
    code()
    print(about)
  elif user==('2'):
    gittools()
  elif user==('3'):
    terban()
    gittool()
    os.system('bash setpass.sh')

  elif user==('4'):
    os.system('clear')
    os.system('bash setpass.sh')
  elif user==('5'):
    print('Exited')
    quit()
  else:
     print('Plz Type Number')
     start()
try:
  import requests
except:
  print(green+"[+]"+yellow+" Installing Some Python Packages")
  os.system("pip install requests &>> req.txt")
  print(green+"[+] "+yellow+"All Most Done")
  os.system("pip3 install requests &>> req.txt")
start()
