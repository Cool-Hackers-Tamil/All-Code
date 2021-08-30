import os ,time
starting="""
echo "
|------------------|
|starting server...|
|------------------|
" | lolcat
"""
started="""
echo "
|———————————————————|
|» Server Started… «|
|———————————————————|
" | lolcat
"""
gooff="""
echo "
|=========================|
|«       Turning Off     »|
|        « SERVER »       |
|=========================|
" | lolcat
"""
stoped="""
echo "
|-----------------|
| »server-stoped« |
|-----------------|
" | lolcat
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
          .dNMMMMMMMMMMMMo                   Version 1.2.1
             'oOWMMMMMMMMo
                 .,cdkO0K;                     By Harshad

" | lolcat
"""
os.system('clear')
os.system(logo)
os.system(starting)
time.sleep(2.5)
os.system('clear')
os.system(started)
time.sleep(1)
os.system('apachectl')
os.system('ssh -R 80:localhost:8080 localhost.run')
os.system('clear')
os.system('killall httpd ')
os.system(logo)
os.system(gooff)
time.sleep(2)
os.system(stoped)
