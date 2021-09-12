import os, time
def sys(txt):
  os.system(txt)

update="""
echo '[*] Updating...'
apt update -y &>> Update.log
echo '[*] All Most Done...'
pkg update -y &>> Update.log
rm Update.log
"""
upgrade="""
echo '[*] Upgrading...'
pkg upgrade -y &>> Upgrade.log 
echo '[*] Upgrading Some Packages...'
apt-get upgrade -y &>> Upgrade.log
echo '[*] Your Termux UP To Date'
rm Upgrade.log
"""
os.system(update+upgrade)
# Old Code
#print('[*] Updating')
#sys('pkg update -y &>> Update')
#print('[*] All Most Done')
#sys('apt-get update -y &>> Update')
#print('[*] Upgrading')
#sys('pkg upgrade -y >> Update')
#print('[*] Upgrading Some Packages')
#sys('apt-get upgrade -y >> Update')
#print('[*] Your Termux UP To Date')
#os.system('rm Update')
