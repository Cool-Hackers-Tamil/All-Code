#!/data/data/com.termux/files/usr/bin/bash

rm $PREFIX/bin/login.py
cp old_login $PREFIX/bin/login
chmod 700 $PREFIX/bin/login
echo termux-login removed
echo "
                Termux Login Removed

                 ..;lxO0KXXXK0Oxl:..
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
   xMMMMMMMMd                        ,0MMMMMMMMMMK;
   .WMMMMMMMMMc                         'OMMMMMM0,
    lMMMMMMMMMMk.                         .kMMO'
     dMMMMMMMMMMWd'                         ..
      cWMMMMMMMMMMMNxc'.                     Version 1.03
       .0MMMMMMMMMMMMMMMMWc
         ;0MMMMMMMMMMMMMMMo.
           .dNMMMMMMMMMMMMo
              'oOWMMMMMMMMo
                  .,cdkO0K;                  By Harshad" | lolcat
