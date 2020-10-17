import os
import re
import sys
from pathlib import Path
from time import sleep
sys.path.insert(1,'..')
import yuyinbofang.ziyuanguanli as ZYGL

sleep(15)
p = Path("/media/pi")
BenDi_LuJing = "/home/pi/Documents/yuyinbofang"
SheBei_LuJing = re.match(r".+\'(.+)\'", str([x for x in p.iterdir() if x.is_dir()])).group(1)+"/yuyinbofang/*"
os.system('sudo rm -r '+BenDi_LuJing+'/*')
sleep(1)
os.system('cp -r '+SheBei_LuJing+' '+BenDi_LuJing)
os.system('sudo chmod 755 ../yuyinbofang/echo')
print('升级完成！')
os.system('sudo umount '+re.match(r'(.+)/yuyinbofang', SheBei_LuJing).group(1))
sleep(1)
os.system('sudo eject /dev/sda')
os.system(ZYGL.Shuo+ZYGL.DuiHua[18][0])
