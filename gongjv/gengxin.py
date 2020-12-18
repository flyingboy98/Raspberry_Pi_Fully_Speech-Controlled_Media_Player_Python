import os
import re
import sys
from pathlib import Path
from time import sleep
sys.path.insert(1,'..')
#sys.path.append('/home/pi/Document/yuyinbofang')
import yuyinbofang.ziyuanguanli as ZYGL

sleep(15)
p = Path("/media/pi")
BenDi_LuJing_ChengXu = "/home/pi/Documents/yuyinbofang"
BenDi_LuJing_GongJv = "/home/pi/Documents/gongjv"
SheBei_LuJing_ChengXu = re.match(r".+\'(.+)\'", str([x for x in p.iterdir() if x.is_dir()])).group(1)+"/yuyinbofang/*"
SheBei_LuJing_GongJv = re.match(r".+\'(.+)\'", str([x for x in p.iterdir() if x.is_dir()])).group(1)+"/gongjv/*"
try:
    os.system('cp -r '+SheBei_LuJing_ChengXu+' '+BenDi_LuJing_ChengXu)
except:
    print("程序更新错误。")
    os.system(ZYGL.Shuo+ZYGL.DuiHua[20][0])
    pass
try:
    os.system('cp -r '+SheBei_LuJing_GongJv+' '+BenDi_LuJing_GongJv)
except:
    print("工具更新错误。")
    os.system(ZYGL.Shuo+ZYGL.DuiHua[21][0])
    pass
os.system('sudo chmod 755 ../yuyinbofang/echo')
print('更新完成！')
os.system('sudo umount '+re.match(r'(.+)/yuyinbofang', SheBei_LuJing_ChengXu).group(1))
sleep(1)
os.system('sudo eject /dev/sda')
os.system(ZYGL.Shuo+ZYGL.DuiHua[17][0])
os.system('reboot')
