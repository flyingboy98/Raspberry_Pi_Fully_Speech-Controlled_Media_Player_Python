import os
import re
from pathlib import Path
from time import sleep

sleep(15)
p = Path("/media/pi")
BenDi_LuJing = "/home/pi/Documents/ls"
SheBei_LuJing = re.match(r".+\'(.+)\'", str([x for x in p.iterdir() if x.is_dir()])).group(1)+"/ls"
os.system('sudo cp -r '+BenDi_LuJing+' '+SheBei_LuJing)
print('copying completed!')
#print(os.system('lsblk'))
#sleep(1)
#os.system('sudo umount '+re.match(r'(.+)/ls', SheBei_LuJing).group(1))
sleep(1)
os.system('sudo eject /dev/sda4')

