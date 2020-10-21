import os
import re
import sys
import shutil
from time import sleep
from pathlib import Path
sys.path.insert(1,'..')
import yuyinbofang.ziyuanguanli as ZYGL


sleep(15)
try:
    p = Path("/media/pi")
    BenDi_LuJing = "/home/pi/Music"
    SheBei_LuJing = re.match(r".+\'(.+)\'",str([x for x in p.iterdir() if x.is_dir()])).group(1)+"/Music"
    v1 = int(re.match(r'.+\ free=(.+)\)', str(shutil.disk_usage(BenDi_LuJing))).group(1))
    v2 = int(re.match(r'.+\ used=(.+)\,.+', str(shutil.disk_usage(SheBei_LuJing))).group(1))
    if v1 > v2:
        os.system("cp -r "+SheBei_LuJing+"/mp3/yinyue/* "+BenDi_LuJing+"/mp3/yinyue/")
        os.system("cp -r "+SheBei_LuJing+"/mp3/shici/* "+BenDi_LuJing+"/mp3/shici/")
        os.system("cp -r "+SheBei_LuJing+"/mp3/pingshu/* "+BenDi_LuJing+"/mp3/pingshu/")
        os.system("cp -r "+SheBei_LuJing+"/mp3/langdu/* "+BenDi_LuJing+"/mp3/langdu/")            
        os.system("cp -r "+SheBei_LuJing+"/wav/* "+BenDi_LuJing+"/wav/")
        print("添加完成！")
        os.system(ZYGL.Shuo+ZYGL.DuiHua[10][0])
    else:
        print("磁盘空间不足。")
        os.system(ZYGL.Shuo+ZYGL.DuiHua[8][0])
except:
    print("请检查Ｕ盘路迳和文件名。")
    os.system(ZYGL.Shuo+ZYGL.DuiHua[9][0])
finally:
    os.system('sudo umount '+re.match(r'(.+)/Music', SheBei_LuJing).group(1))
    sleep(1)
    os.system('sudo eject /dev/sda')
    print("可以取下U盘了。")
    os.system(ZYGL.Shuo+ZYGL.DuiHua[12][0])


