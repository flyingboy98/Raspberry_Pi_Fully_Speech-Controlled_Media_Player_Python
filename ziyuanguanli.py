import os
import re
import sqlite3


PZ_WenJian = "/home/pi/Documents/yuyinbofang/peizhi"
SJK_WenJian = "/home/pi/Documents/yuyinbofang/ziyuan.db"
SJK_DuiHua = "/home/pi/Documents/yuyinbofang/duihua.db"

def JianSuo(MingLing):
    yinyue_mp3_max_id=yinyue_wav_max_id=shici_max_id=pingshu_max_id=langdu_max_id="None"
    LuJing = {
    "js_yinyue_mp3":"/home/pi/Music/mp3/yinyue",
    "js_shici":"/home/pi/Music/mp3/shici",
    "js_pingshu":"/home/pi/Music/mp3/pingshu",
    "js_langdu":"/home/pi/Music/mp3/langdu",
    "js_yinyue_wav":"/home/pi/Music/wav",
    "js_quanbu":"/home/pi/Music"
    }
    
    SJK_LianJie = sqlite3.connect(SJK_WenJian)
    SJK_YouBiao = SJK_LianJie.cursor()
    
    if MingLing == "js_quanbu":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS yinyue_mp3')
        SJK_YouBiao.execute('DROP TABLE IF EXISTS yinyue_wav')
        SJK_YouBiao.execute('DROP TABLE IF EXISTS shici')
        SJK_YouBiao.execute('DROP TABLE IF EXISTS pingshu')
        SJK_YouBiao.execute('DROP TABLE IF EXISTS langdu')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS yinyue_mp3([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [DaXiao] integer, [ZhuanJi] text, [LuJing] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS yinyue_wav([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [GeShi] text, [ZhuanJi] text, [LuJing] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS shici([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ChaoDai] text, [NeiRong] text, [YiWen] text, [ZhuanJi] text, [LuJing] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS pingshu([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS langdu([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS shoucang([XuHao] INTEGER PRIMARY KEY, [MingCheng] text, [RenWu] text, [LuJing] varchar unique)')
        SJK_LianJie.commit()
    elif MingLing == "js_yinyue_mp3":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS yinyue_mp3')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS yinyue_mp3([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [DaXiao] integer, [ZhuanJi] text, [LuJing] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_yinyue_wav":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS yinyue_wav')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS yinyue_wav([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [GeShi] text, [ZhuanJi] text, [LuJing] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_shici":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS shici')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS shici([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ChaoDai] text, [NeiRong] text, [YiWen] text, [ZhuanJi] text, [LuJing] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_pingshu":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS pingshu')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS pingshu([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_langdu":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS langdu')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS langdu([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text)')
        SJK_LianJie.commit()
        
    cate = ""    
    pat = re.compile(r'(.*)\ \-\ ([^\(]*)(\((.*)\))?\.(.{3})')
    pat_zj_mp3 = re.compile(r'.+/yinyue/(.*)/.+')
    pat_zj_wav = re.compile(r'.+/wav/(.*)/.+')
    pat_zj_shici = re.compile(r'.+/shici/(.*)/.+')
    pat_zj_pingshu = re.compile(r'.+/pingshu/(.*)/.+')
    pat_zj_langdu = re.compile(r'.+/langdu/(.*)/.+')
    
    for subdir, dirs, files in os.walk(re.escape(LuJing[MingLing])):
        for filename in files:
            filepath = subdir + os.sep + filename

            m = re.match(pat,filename)
            if filepath.endswith((".mp3",".MP3",".wav",".WAV",".ape",".APE",".flac",".FLAC")):
                if "yinyue" in subdir:
                    if cate != "yinyue":
                        i = 0
                        cate = "yinyue"
                    i += 1
                    daxiao = os.stat(filepath).st_size / (1024 * 1024)
                    try:
                        zhuanji = re.match(pat_zj_mp3,filepath).group(1)
                    except:
                        zhuanji = ""
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), '{0:4.2f}'.format(daxiao), zhuanji, filepath)
                    else:
                        data = (str(i), m.group(2), m.group(1), '{0:4.2f}'.format(daxiao), zhuanji, filepath)
                    SJK_YouBiao.execute('INSERT INTO yinyue_mp3(XuHao_L, MingCheng, RenWu, DaXiao, ZhuanJi, LuJing) VALUES(?,?,?,?,?,?)', data)
                elif "wav" in subdir:
                    if cate != "wav":
                        i = 0
                        cate = "wav"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj_wav,filepath).group(1)
                    except:
                        zhuanji = ""
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), m.group(5), zhuanji, filepath)
                    else:
                        data = (str(i), m.group(2), m.group(1), m.group(5), zhuanji, filepath)
                    SJK_YouBiao.execute('INSERT INTO yinyue_wav(XuHao_L, MingCheng, RenWu, GeShi, ZhuanJi, LuJing) VALUES(?,?,?,?,?,?)', data)
                elif "shici" in subdir:
                    if cate != "shici":
                        i = 0
                        cate = "shici"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj_shici,filepath).group(1)
                    except:
                        zhuanji = ""
                    data = (str(i), m.group(2), m.group(1), m.group(4), "", "", zhuanji, filepath)
                    SJK_YouBiao.execute('INSERT INTO shici(XuHao_L, MingCheng, RenWu, ChaoDai, NeiRong, YiWen, ZhuanJi, LuJing) VALUES(?,?,?,?,?,?,?,?)', data)
                elif "pingshu" in subdir:
                    if cate != "pingshu":
                        i = 0
                        cate = "pingshu"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj_pingshu,filepath).group(1)
                    except:
                        zhuanji = ""
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), zhuanji, filepath)
                    else:
                        data = (str(i), m.group(2), m.group(1), zhuanji, filepath)
                    SJK_YouBiao.execute('INSERT INTO pingshu(XuHao_L, MingCheng, RenWu, ZhuanJi, LuJing) VALUES(?,?,?,?,?)', data)
                elif "langdu" in subdir:
                    if cate != "langdu":
                        i = 0
                        cate = "langdu"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj_langdu,filepath).group(1)
                    except:
                        zhuanji = ""
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), zhuanji, filepath)
                    else:
                        data = (str(i), m.group(2), m.group(1), zhuanji, filepath)
                    SJK_YouBiao.execute('INSERT INTO langdu(XuHao_L, MingCheng, RenWu, ZhuanJi, LuJing) VALUES(?,?,?,?,?)', data)

    SJK_LianJie.commit()
    if MingLing == "js_quanbu" or MingLing == "js_yinyue_mp3":
        SJK_YouBiao.execute('SELECT XuHao_L FROM yinyue_mp3')
        yinyue_mp3_max_id = str(len(SJK_YouBiao.fetchall()))
        print("mp3: "+yinyue_mp3_max_id)
        PaiXu("yinyue_mp3")
    if MingLing == "js_quanbu" or MingLing == "js_yinyue_wav":
        SJK_YouBiao.execute('SELECT XuHao_L FROM yinyue_wav')
        yinyue_wav_max_id = str(len(SJK_YouBiao.fetchall()))
        print("wav: "+yinyue_wav_max_id)
        PaiXu("yinyue_wav")
    if MingLing == "js_quanbu" or MingLing == "js_shici":
        SJK_YouBiao.execute('SELECT XuHao_L FROM shici')
        shici_max_id = str(len(SJK_YouBiao.fetchall()))
        print("shici: "+shici_max_id)
        PaiXu("shici")
    if MingLing == "js_quanbu" or MingLing == "js_pingshu":
        SJK_YouBiao.execute('SELECT XuHao_L FROM pingshu')
        pingshu_max_id = str(len(SJK_YouBiao.fetchall()))
        print("pingshu: "+pingshu_max_id)
        PaiXu("pingshu")
    if MingLing == "js_quanbu" or MingLing == "js_langdu":
        SJK_YouBiao.execute('SELECT XuHao_L FROM langdu')
        langdu_max_id = str(len(SJK_YouBiao.fetchall()))
        print("langdu: "+langdu_max_id)
        PaiXu("langdu")
    SJK_LianJie.close()
    
    PZ_WenJian_ChuShiHua = [
        'MingLing = bf_yinyue\n',
        'MoShi = shunxu\n',
        'yinyue_mp3 = 1/'+yinyue_mp3_max_id+',00:00:00\n',
        'yinyue_wav = 1/'+yinyue_wav_max_id+',00:00:00\n',
        'shici = 1/'+shici_max_id+',00:00:00\n',
        'pingshu = 1/'+pingshu_max_id+',00:00:00\n',
        'langdu = 1/'+langdu_max_id+',00:00:00\n',
        'shoucang = 1/None,00:00:00\n',
        'yuyan = zhongwen\n'
        ]
    with open(PZ_WenJian,'w') as f:
        f.writelines(PZ_WenJian_ChuShiHua)
    print("检索完毕。")
    os.system(Shuo+DuiHua[7][0])

def ShouCang():
    with open(PZ_WenJian) as f:
        lines = f.readlines()
        for line in lines:
            if line.find("MingLing") == 0:
                if re.match(r'MingLing =(.*)(\n)?', line).group(1).strip(" bf_") == "yinyue":
                    Biao = "yinyue_mp3"
                elif re.match(r'MingLing =(.*)(\n)?', line).group(1).strip(" bf_") == "wusun":
                    Biao = "yinyue_wav"
                else:
                    Biao = re.match(r'MingLing =(.*)(\n)?', line).group(1).strip(" bf_")
                break
        for line in lines:
            if line.find(Biao) == 0:
                XuHao = (int(re.match(r'.+=(.*)/(.*),.+', line).group(1).strip(' ""')),)
                break
    
    SJK_LianJie = sqlite3.connect(SJK_WenJian)
    SJK_YouBiao = SJK_LianJie.cursor()
    SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS shoucang([XuHao] INTEGER PRIMARY KEY, [MingCheng] text, [RenWu] text, [LuJing] varchar unique)')
    SJK_LianJie.commit()
    SJK_YouBiao.execute('SELECT max(XuHao) FROM shoucang')
    shoucang_max_id = SJK_YouBiao.fetchone()[0]
    if shoucang_max_id == None:
        i = 1
    else:
        i = shoucang_max_id + 1
    SJK_YouBiao.execute('SELECT MingCheng, RenWu, LuJing FROM '+Biao+' WHERE XuHao =?',XuHao)
    data = SJK_YouBiao.fetchone()
    try:
        with SJK_LianJie:
            SJK_LianJie.execute('INSERT INTO shoucang(MingCheng, RenWu, LuJing) VALUES(?,?,?)', data)
    except sqlite3.IntegrityError:
        print("已经收藏过了！")
        os.system(Shuo+DuiHua[15][0])
        return
    SJK_LianJie.close()

    try:
        with open(PZ_WenJian) as f:
            lines = f.readlines()
            for line in lines:
                if line.find("shoucang") == 0:
                    lines[lines.index(line)] = re.sub(r'/(.*),', r'/'+str(i)+r',', line)
                    break
            with open(PZ_WenJian,'w') as f:
                f.writelines(lines)
        print("已添加到收藏。")
        os.system(Shuo+DuiHua[14][0])
    except:
        print("请先添加文件，然后用搜索命令建立播放列表。")
        os.system(Shuo+DuiHua[6][0])
        
def PaiXu(Biao):
    SJK_LianJie = sqlite3.connect(SJK_WenJian)
    SJK_YouBiao = SJK_LianJie.cursor()
    SJK_YouBiao.execute('SELECT XuHao_L FROM '+Biao+' ORDER BY LuJing ASC')
    XuHao_Yuan = list(SJK_YouBiao.fetchall())
    XuHao_Xian = [(x+1,) for x in range(len(XuHao_Yuan))]
    data = [XuHao_Xian[n]+XuHao_Yuan[n] for n in range(len(XuHao_Yuan))]
    SJK_YouBiao.executemany("UPDATE "+Biao+" SET XuHao =? WHERE XuHao_L =?", data)
    SJK_LianJie.commit()
    SJK_LianJie.close()

def YuYan(MingLing):
    SJK_DuiHua_LianJie = sqlite3.connect(SJK_DuiHua)
    SJK_DuiHua_YouBiao = SJK_DuiHua_LianJie.cursor()
    yuyan = ""
    shuo = ""
    try:
        with open(PZ_WenJian) as f:
            lines = f.readlines()
            for line in lines:
                if line.find("yuyan") == 0:
                    yuyan = re.match(r'yuyan =(.*)(\n)?', line).group(1).strip(' ""')
                    break
    except:
        yuyan = MingLing
    if MingLing == "":
        if yuyan == "zhongwen" or yuyan == "":
            SJK_DuiHua_YouBiao.execute('SELECT ZhongWen FROM yuyan')
            shuo = "python3 ../yy/bin/zhspeak.py "
        elif yuyan == "riyu":
            SJK_DuiHua_YouBiao.execute('SELECT RiYu FROM yuyan')
            shuo = "./echo "
        elif yuyan == "yingyu":
            SJK_DuiHua_YouBiao.execute('SELECT YingYu FROM yuyan')
            shuo = "espeak "
    else:
        if MingLing == "zhongwen":
            SJK_DuiHua_YouBiao.execute('SELECT ZhongWen FROM yuyan')
            shuo = "python3 ../yy/bin/zhspeak.py "
        elif MingLing == "riyu":
            SJK_DuiHua_YouBiao.execute('SELECT RiYu FROM yuyan')
            shuo = "./echo "
        else:
            SJK_DuiHua_YouBiao.execute('SELECT YingYu FROM yuyan')
            shuo = "espeak "
        if MingLing != yuyan:
            try:
                with open(PZ_WenJian) as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.find("yuyan") == 0:
                            lines[lines.index(line)] = re.sub(r'=(.*)(\n)?', r'= '+MingLing+r'\n', line)
                            break
                    with open(PZ_WenJian,'w') as f:
                        f.writelines(lines)
            except:
                pass
    duihua = SJK_DuiHua_YouBiao.fetchall()
    SJK_DuiHua_LianJie.close()
    return (duihua, shuo)
    
DuiHua, Shuo = YuYan("")
