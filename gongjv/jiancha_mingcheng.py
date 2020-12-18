import os
import re
import sys
sys.path.insert(1,'..')
#sys.path.append('/home/pi/Document/yuyinbofang')
import yuyinbofang.ziyuanguanli as ZYGL


LuJing = input("input path: ")
XiuGai_WenJian = "xiugai.txt"
os.chdir(LuJing)
cuowu = []
pat = re.compile(r'(.*)\ \-\ ([^\(]*)(\((.*)\))?\.(.{3})')

for subdir, dirs, files in os.walk(re.escape(LuJing)):
    for filename in files:
        filepath = subdir + os.sep + filename
        m = re.match(pat,filename)
        if filepath.endswith((".mp3",".MP3",".wav",".WAV",".ape",".APE",".flac",".FLAC")):
            try:
                if m.group(3) != None:
                    data = (m.group(2)+m.group(3), m.group(1))
                else:
                    data = (m.group(2), m.group(1))
            except:
                cuowu.append(re.match('.+Music/(.*)',filepath).group(1)+'\n')
                pass

if cuowu != []:
    with open(XiuGai_WenJian,'w') as f:
        f.writelines(cuowu)
    print("检查完成！发现错误，请查看媒体文件夹下的xiugai.txt文件．")
else:
    print("检查完成！完全正确！")
#os.system(ZYGL.Shuo+ZYGL.DuiHua[11][0])