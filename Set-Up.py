import os, time
terban="""
clear
echo '
----------------
| Installing...|
----------------
'

apt update
clear
echo 'Upgrading...'
apt upgrade
clear
echo 'Install Some Files'
apt install figlet -y
apt install toilet -y
apt install cowsay -y
apt install sl -y
apt install nano -y
apt install ruby -y
gem install lolcat
pkg install python2
pkg install git
pkg install python
clear
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
figlet 'Bash Shell Installed' | lolcat
"""
tools="""
> 1                 Install TBomb                <
•                                                •
> 2                 Install ZPhisher             <
•                                                •
> 3                 Install LittleBrother        <
"""
def gittools():
  print(tools)
  get=input('>>> ')
  if get == ('1'):
    os.system('cd /data/data/com.termux/files/home')
    os.system("echo 'Installing TBomb'")
    os.system("git clone https://github.com/TheSpeedX/TBomb.git")
  elif get == ('2'):
    os.system('cd /data/data/com.termux/files/home')
    os.system("echo 'Installing TBomb'")
    os.system('git clone https://github.com/TheSpeedX/TBomb.git')
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
    os.system(terban)
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
      os.system(terban)
      print(inster)
    elif hats==('no'):
      print('So Bad')
      quit()
    elif hats==('Yes'):
      os.system(terban)
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
