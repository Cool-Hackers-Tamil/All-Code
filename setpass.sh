#!/data/data/com.termux/files/usr/bin/bash
clear
echo '[*] Updating...'
pkg update -y  &>> update
echo '[*] Upgrading...'
apt upgrade -y &>> upgrade
echo '[*] Installing Figlet...'
apt install figlet -y &>> upgrade
echo '[*] Installing Toilet...'
apt install toilet -y &>> upgrade
echo '[*] Installing CowSay...'
apt install cowsay -y &>> upgrade
echo '[*] Installing SL...'
apt install sl -y &>> upgrade
echo '[*] Installing Nano...'
apt install nano -y &>> upgrade
echo '[*] Installing Ruby...'
apt install ruby -y &>> upgrade
echo '[*] Installing Lolcat...'
gem install lolcat &>> upgrade
echo '[*] Installing Python 2'
pkg install python2 -y &>> upgrade
echo '[*] Installing Git...'
pkg install git -y &>> upgrade
echo '[*] Installing Python 3...'
pkg install python -y &>> upgrade

cp login.py $PREFIX/bin/
chmod 700 $PREFIX/bin/login.py
cp login $PREFIX/bin/
chmod 700 $PREFIX/bin/login
mkdir /data/data/com.termux/files/usr/share/login/
clear

#TODO: hide input
read -p "Enter new password: " passone;
read -p "Repeat password: " passtwo;

if [ $passone = $passtwo ];
then
	touch /data/data/com.termux/files/usr/share/login/.pass
	python -c "import hashlib; print(hashlib.sha1(b'$passone').hexdigest())" > /data/data/com.termux/files/usr/share/login/.pass
	echo 'Login installed'

elif [ $passone != $passtwo ];
then
	echo 'Password dont match'
fi
