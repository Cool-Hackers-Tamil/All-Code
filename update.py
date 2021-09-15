import os, time
from color import red,green,pink,blue,yellow
try:
  print(green+'[+] '+yellow+'Updating...')
  os.system("apt update -y &>> Update.log")
  print(yellow+'[+] '+green+'All Most Done...')
  os.system("pkg update -y &>> Update.log")
  os.system("rm Update.log")

  print(green+'[+] '+blue+'Upgrading...')
  os.system("pkg upgrade -y &>> Upgrade.log")
  print(green+ '[+] '+yellow+'Upgrading Some Packages...')
  os.system("apt-get upgrade -y &>> Upgrade.log")
  os.system("rm Upgrade.log")
  print(green+'[+] '+yellow+'Your Termux UP To Date')
except:
  print(red+"[+] "+pink+"User Exited")
