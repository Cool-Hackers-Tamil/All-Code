import os, time
def sys(txt):
  os.system(txt)
print('[*] Updating')
sys('pkg update -y &>> Update')
print('[*] All Most Done')
sys('apt-get update -y &>> Update')
print('[*] Upgrading')
sys('pkg upgrade -y >> Update')
print('[*] Upgrading Some Packages')
sys('apt-get upgrade -y >> Update')
print('[*] Your Termux UP To Date')
os.system('rm Update')
