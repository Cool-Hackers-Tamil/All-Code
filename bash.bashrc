if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi

PS1='\[\e[31m\]┌─[\[\e[37m\]\T\[\e[31m\]]────\e[1;36m[Mola@Harshad]\e[0;31m────[\#]\n|\n\e[0;31m└─[\[\e[34m\]\e[0;32m\W>'


 alias mola='python /data/data/com.termux/files/usr/etc/update.py' 
 alias molafix='python /data/data/com.termux/files/usr/etc/molafix.py'
 alias logo='python /data/data/com.termux/files/usr/etc/logo.py'
 alias start-web='python /data/data/com.termux/files/usr/etc/web.py'
clear
sl | lolcat -s 190

clear
cowsay -f eyes Leader Of Mola Gaming | lolcat -a -s 120
toilet -f big ' Harshad' -F gay | lolcat -a  -s 100

