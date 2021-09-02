import os, time
terban="""
clear
echo '
----------------
| Installing...|
----------------
'

apt update -y
clear
echo 'Upgrading...'
apt upgrade -y
clear
echo 'Install Some Files'
apt install figlet -y
clear
apt install toilet -y
clear
apt install cowsay -y
clear
apt install sl -y
clear
apt install nano -y
clear
apt install ruby -y
clear
gem install lolcat
clear
pkg install python2
clear
pkg install git
clear
pkg install python
clear
"""
tools="""
> 1                 Install TBomb                <
•                                                •
> 2                 Install ZPhisher             <
•                                                •
> 3                 Install LittleBrother        <
"""
setbash="""
> 1                 Set Bash Ver 1.0                <
•                                                   •
> 2                 Set Bash Ver 1.4                <

"""

old= """
   echo 'Removed Old Bash Shell'
   cd /data/data/com.termux/files/usr/etc
   rm bash.bashrc                                            
   cd /data/data/com.termux/files/home/All-Code
   cp bash.bashrc /data/data/com.termux/files/usr/etc
   cd /data/data/com.termux/files/usr/etc
   chmod 777 bash.bashrc
   echo 'Add New Bash Shell'
   cd /data/data/com.termux/files/home/All-Code
   echo 'Adding Codeing Files'
   cp logo.py /data/data/com.termux/files/usr/etc
   cp web.py /data/data/com.termux/files/usr/etc
   cp molafix.py /data/data/com.termux/files/usr/etc
   figlet 'Bash Shell Installed' | lolcat"""

new= """
   echo 'Removed Old Bash Shell'
   cd /data/data/com.termux/files/usr/etc
   rm bash.bashrc
   cd /data/data/com.termux/files/home/All-Code
   cp bash.bashrc-1.4 /data/data/com.termux/files/usr/etc
   cd /data/data/com.termux/files/usr/etc
   cp bash.bashrc-1.4 bash.bashrc
   chmod 777 bash.bashrc
   echo 'Add New Bash Shell'
   cd /data/data/com.termux/files/home/All-Code
   echo 'Adding Codeing Files'
   cp logo.py /data/data/com.termux/files/usr/etc
   cp web.py /data/data/com.termux/files/usr/etc
   cp molafix.py /data/data/com.termux/files/usr/etc
   figlet 'Bash Shell Installed' | lolcat"""

def code():
  got=input('Bash >>> ')
  if got == ('1'):
    os.system(terban+old)
  elif got == ('2'):
    os.system(terban+new)
  else:
    print('Input wrong')
    print('exiting')
    quit()

def gittools():
  print(tools)
  get=input('>>> ')
  if get == ('1'):
    os.system('cd /data/data/com.termux/files/home')
    os.system("echo 'Installing TBomb'")
    os.system("git clone https://github.com/TheSpeedX/TBomb.git")
  elif get == ('2'):
    os.system('cd /data/data/com.termux/files/home')
    os.system("echo 'Installing ZPhisher'")
    os.system('git clone https://github.com/htr-tech/zphisher.git')
  elif get == ('3'):
    os.system('cd /data/data/com.termux/files/home')
    os.system("echo 'Installing Little Brother'")
    os.system('git clone https://github.com/lulz3xploit/LittleBrother.git')
    os.system("cd /data/data/com.termux/files/home/LittleBrother && python3 -m pip install -r requirements.txt && cd /data/data/com.termux/files/home/All-Code &&  clear")
  else:
    print('Input wrong')
    print('exiting')
    quit()
HackTool="""
cd $HOME
echo 'Installing TBomb'
git clone https://github.com/TheSpeedX/TBomb.git
clear
echo 'Installing  Zphisher'
git clone git://github.com/htr-tech/zphisher.git
clear
echo 'Installing Little Brother'
git clone https://github.com/lulz3xploit/LittleBrother.git

cd /data/data/com.termux/files/home/LittleBrother
python3 -m pip install -r requirements.txt
cd /data/data/com.termux/files/home/All-Code
clear
"""
hac="""
>           Do U Want To Install Hacking Tools            <
•                                                         •
>                    Type Yes Or No                       <
•                                                         •
>          If U Type yes Will Install Hacking Tool        <
"""
bac="""
>            Do U Want To Install Bash Shell              <
•                                                         •
>                    Type Yes Or No                       <
•                                                         •
>           If U Type yes Will Install Bash Shell         <
"""

welban="""
>                  Welcome To Installer                   <
•
•
•
•
> 1          Install Bash Shell And Web Sever             <
•
> 2               Install Hacking Tools                   <
•
> 3         Bash Shell, Web Sever, Hacking Tools          <
•
> 4               Set Password For Termux
•
> 5 Exit                                                  <
"""
inster="""
>              Type Mola To Update & Upgrade              <
•                                                         •
>              Type molafix To fix Apache Sever           <
•                                                         •
>                  Type logo To Show version              <
"""



def start():
  os.system('clear')
  print(welban)
  user=input('>>> ')
  if user==('1'):
    print(setbash)
    os.system(code)
    print(inster)
    print(hac)
    hats=input('>>> ')
    if hats==('yes'):
      os.system('clear')
      gittools()
    elif hats==('no'):
      print('So Bad')
      quit()
    elif hats==('Yes'):
      os.system('clear')
      gittools()
    elif hats==('No'):
      print('So Bad')
      quit()
    else:
     quit()
  elif user==('2'):
    gittools()
    print(bac)
    hats=input('>>> ')
    if hats==('yes'):
      os.system(code)
      print(inster)
    elif hats==('no'):
      print('So Bad')
      quit()
    elif hats==('Yes'):
      os.system(code)
      print(inster)
    elif hats==('No'):
      print('So Bad')
      quit()
  elif user==('3'):
    os.system(terban)
    gittool()
    os.system('bash setpass.sh')
    quit()

  elif user==('4'):
    os.system('clear')
    os.system('bash setpass.sh')
  elif user==('5'):
    print('Exited')
    quit()
  else:
     print('Plz Type Number')
     start()
start()
