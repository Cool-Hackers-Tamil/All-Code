import os, time
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
fixed="""
echo '
|———————————————————|
|»  Server Fixed…  «|
|———————————————————|
' | lolcat
"""
starting="""
echo '
|————————————————————|
|» Server Starting… «|
|————————————————————|
' | lolcat
"""
started="""
echo '
|———————————————————|
|» Server Started… «|
|———————————————————|
' | lolcat
"""
logo="""
echo "
                 .;lxO0KXXXK0Oxl:.
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
  xMMMMMMMMMd                        ,0MMMMMMMMMMK;
  .WMMMMMMMMMc                         'OMMMMMM0,
   lMMMMMMMMMMk.                         .kMMO'
    dMMMMMMMMMMWd'                         ..
     cWMMMMMMMMMMMNxc'.
      .0MMMMMMMMMMMMMMMMWc
        ;0MMMMMMMMMMMMMMMo.
          .dNMMMMMMMMMMMMo                    Version 1.6.4
             'oOWMMMMMMMMo
                 .,cdkO0K;                     By Harshad
" | lolcat
"""
exited="""
echo '
|———————————|
|» Exited… «|
|———————————|
' | lolcat
"""
os.system('clear')
os.system(logo)
print(bcolors.OKBLUE)
print('type any text to exit : )')
inpu=input('entet to fix files :')
if inpu=='':
  os.system('clear')
  os.system(logo)
  os.system('cd .. &&  cd usr/var/run/apache2 && rm httpd.pid && apachectl ') 
  os.system(fixed)
  time.sleep(0.5)
  os.system(starting)
  time.sleep(2)
  os.system(started)
  quit()
else:
  os.system('clear')
  print('          ')
  os.system(logo)
  os.system(exited)
  quit()
