import os
import re
import time
import sqlite3


PZ_WenJian = "/home/pi/Documents/yuyinbofang/peizhi"
SJK_WenJian = "/home/pi/Documents/yuyinbofang/ziyuan.db"
SJK_DuiHua = "/home/pi/Documents/yuyinbofang/duihua.db"

def JianSuo(MingLing):
    yinyue_mp3_max_id=yinyue_wav_max_id=shici_max_id=xiangsheng_max_id=pingshu_max_id=jiangtan_max_id=langdu_max_id=x_max_id="None"
    LuJing = {
    "js_yinyue_mp3":"/home/pi/Music/mp3/yinyue",
    "js_shici":"/home/pi/Music/mp3/shici",
    "js_xiangsheng":"/home/pi/Music/mp3/xiangsheng",
    "js_pingshu":"/home/pi/Music/mp3/pingshu",
    "js_jiangtan":"/home/pi/Music/mp3/jiangtan",
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
        SJK_YouBiao.execute('DROP TABLE IF EXISTS xiangsheng')
        SJK_YouBiao.execute('DROP TABLE IF EXISTS pingshu')
        SJK_YouBiao.execute('DROP TABLE IF EXISTS jiangtan')
        SJK_YouBiao.execute('DROP TABLE IF EXISTS langdu')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS yinyue_mp3([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [DaXiao] integer, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS yinyue_wav([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [GeShi] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS shici([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ChaoDai] text, [NeiRong] text, [YiWen] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS xiangsheng([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS pingshu([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS jiangtan([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS langdu([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS shoucang([XuHao] INTEGER PRIMARY KEY, [MingCheng] text, [RenWu] text, [LuJing] varchar unique)')
        SJK_LianJie.commit()
    elif MingLing == "js_yinyue_mp3":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS yinyue_mp3')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS yinyue_mp3([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [DaXiao] integer, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_yinyue_wav":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS yinyue_wav')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS yinyue_wav([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [GeShi] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_shici":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS shici')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS shici([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ChaoDai] text, [NeiRong] text, [YiWen] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_xiangsheng":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS xiangsheng')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS xiangsheng([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_pingshu":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS pingshu')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS pingshu([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_jiangtan":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS jiangtan')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS jiangtan([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_LianJie.commit()
    elif MingLing == "js_langdu":
        SJK_YouBiao.execute('DROP TABLE IF EXISTS langdu')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS langdu([XuHao] INTEGER, [XuHao_L] text, [MingCheng] text, [RenWu] text, [ZhuanJi] text, [LuJing] text, [PinYin] text)')
        SJK_LianJie.commit()
        
    cate = ""    
    pat = re.compile(r'(.*)\ \-\ ([^\(]*)(\((.*)\))?\.(.{3})')
    pat_zj = re.compile(r'.+/([^/].+)/[^/].+')
    
    # iterate over through the dir
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
                        zhuanji = re.match(pat_zj,filepath).group(1)
                    except:
                        zhuanji = ""
                    pinyin = WenZi_Zhuan_PinYin(m.group(1), m.group(2))
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), '{0:4.2f}'.format(daxiao), zhuanji, filepath, pinyin)
                    else:
                        data = (str(i), m.group(2), m.group(1), '{0:4.2f}'.format(daxiao), zhuanji, filepath, pinyin)
                    SJK_YouBiao.execute('INSERT INTO yinyue_mp3(XuHao_L, MingCheng, RenWu, DaXiao, ZhuanJi, LuJing, PinYin) VALUES(?,?,?,?,?,?,?)', data)
                elif "wav" in subdir:
                    if cate != "wav":
                        i = 0
                        cate = "wav"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj,filepath).group(1)
                    except:
                        zhuanji = ""
                    pinyin = WenZi_Zhuan_PinYin(m.group(1), m.group(2))
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), m.group(5), zhuanji, filepath, pinyin)
                    else:
                        data = (str(i), m.group(2), m.group(1), m.group(5), zhuanji, filepath, pinyin)
                    SJK_YouBiao.execute('INSERT INTO yinyue_wav(XuHao_L, MingCheng, RenWu, GeShi, ZhuanJi, LuJing, PinYin) VALUES(?,?,?,?,?,?,?)', data)
                elif "shici" in subdir:
                    if cate != "shici":
                        i = 0
                        cate = "shici"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj,filepath).group(1)
                    except:
                        zhuanji = ""
                    pinyin = WenZi_Zhuan_PinYin(m.group(1), m.group(2))
                    data = (str(i), m.group(2), m.group(1), m.group(4), "", "", zhuanji, filepath, pinyin)
                    SJK_YouBiao.execute('INSERT INTO shici(XuHao_L, MingCheng, RenWu, ChaoDai, NeiRong, YiWen, ZhuanJi, LuJing, PinYin) VALUES(?,?,?,?,?,?,?,?,?)', data)
                elif "xiangsheng" in subdir:
                    if cate != "xiangsheng":
                        i = 0
                        cate = "xiangsheng"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj,filepath).group(1)
                    except:
                        zhuanji = ""
                    pinyin = WenZi_Zhuan_PinYin(m.group(1), m.group(2))
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), zhuanji, filepath, pinyin)
                    else:
                        data = (str(i), m.group(2), m.group(1), zhuanji, filepath, pinyin)
                    SJK_YouBiao.execute('INSERT INTO xiangsheng(XuHao_L, MingCheng, RenWu, ZhuanJi, LuJing, PinYin) VALUES(?,?,?,?,?,?)', data)
                elif "pingshu" in subdir:
                    if cate != "pingshu":
                        i = 0
                        cate = "pingshu"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj,filepath).group(1)
                    except:
                        zhuanji = ""
                    pinyin = WenZi_Zhuan_PinYin(m.group(1), m.group(2))
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), zhuanji, filepath, pinyin)
                    else:
                        data = (str(i), m.group(2), m.group(1), zhuanji, filepath, pinyin)
                    SJK_YouBiao.execute('INSERT INTO pingshu(XuHao_L, MingCheng, RenWu, ZhuanJi, LuJing, PinYin) VALUES(?,?,?,?,?,?)', data)
                elif "jiangtan" in subdir:
                    if cate != "jiangtan":
                        i = 0
                        cate = "jiangtan"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj,filepath).group(1)
                    except:
                        zhuanji = ""
                    pinyin = WenZi_Zhuan_PinYin(m.group(1), m.group(2))
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), zhuanji, filepath, pinyin)
                    else:
                        data = (str(i), m.group(2), m.group(1), zhuanji, filepath, pinyin)
                    SJK_YouBiao.execute('INSERT INTO jiangtan(XuHao_L, MingCheng, RenWu, ZhuanJi, LuJing, PinYin) VALUES(?,?,?,?,?,?)', data)
                elif "langdu" in subdir:
                    if cate != "langdu":
                        i = 0
                        cate = "langdu"
                    i += 1
                    try:
                        zhuanji = re.match(pat_zj,filepath).group(1)
                    except:
                        zhuanji = ""
                    pinyin = WenZi_Zhuan_PinYin(m.group(1), m.group(2))
                    if m.group(3) != None:
                        data = (str(i), m.group(2)+m.group(3), m.group(1), zhuanji, filepath, pinyin)
                    else:
                        data = (str(i), m.group(2), m.group(1), zhuanji, filepath, pinyin)
                    SJK_YouBiao.execute('INSERT INTO langdu(XuHao_L, MingCheng, RenWu, ZhuanJi, LuJing, PinYin) VALUES(?,?,?,?,?,?)', data)

    SJK_LianJie.commit()
    if MingLing == "js_quanbu" or MingLing == "js_yinyue_mp3":
        SJK_YouBiao.execute('SELECT XuHao_L FROM yinyue_mp3')
        yinyue_mp3_max_id = str(len(SJK_YouBiao.fetchall()))
        x_max_id = yinyue_mp3_max_id
        print("mp3: "+yinyue_mp3_max_id)
        os.system("python3 ../yy/bin/zhspeak.py 搜索到"+yinyue_mp3_max_id+"首音乐")
        PaiXu("yinyue_mp3")
    if MingLing == "js_quanbu" or MingLing == "js_yinyue_wav":
        SJK_YouBiao.execute('SELECT XuHao_L FROM yinyue_wav')
        yinyue_wav_max_id = str(len(SJK_YouBiao.fetchall()))
        x_max_id = yinyue_wav_max_id
        print("wav: "+yinyue_wav_max_id)
        os.system("python3 ../yy/bin/zhspeak.py 搜索到"+yinyue_wav_max_id+"首无损音乐")
        PaiXu("yinyue_wav")
    if MingLing == "js_quanbu" or MingLing == "js_shici":
        SJK_YouBiao.execute('SELECT XuHao_L FROM shici')
        shici_max_id = str(len(SJK_YouBiao.fetchall()))
        x_max_id = shici_max_id
        print("shici: "+shici_max_id)
        os.system("python3 ../yy/bin/zhspeak.py 搜索到"+shici_max_id+"首诗词")
        PaiXu("shici")
    if MingLing == "js_quanbu" or MingLing == "js_xiangsheng":
        SJK_YouBiao.execute('SELECT XuHao_L FROM xiangsheng')
        xiangsheng_max_id = str(len(SJK_YouBiao.fetchall()))
        x_max_id = xiangsheng_max_id
        print("xiangsheng: "+xiangsheng_max_id)
        os.system("python3 ../yy/bin/zhspeak.py 搜索到"+xiangsheng_max_id+"段相声")
        PaiXu("xiangsheng")
    if MingLing == "js_quanbu" or MingLing == "js_pingshu":
        SJK_YouBiao.execute('SELECT XuHao_L FROM pingshu')
        pingshu_max_id = str(len(SJK_YouBiao.fetchall()))
        x_max_id = pingshu_max_id
        print("pingshu: "+pingshu_max_id)
        os.system("python3 ../yy/bin/zhspeak.py 搜索到"+pingshu_max_id+"段评书")
        PaiXu("pingshu")
    if MingLing == "js_quanbu" or MingLing == "js_jiangtan":
        SJK_YouBiao.execute('SELECT XuHao_L FROM jiangtan')
        jiangtan_max_id = str(len(SJK_YouBiao.fetchall()))
        x_max_id = jiangtan_max_id
        print("jiangtan: "+jiangtan_max_id)
        os.system("python3 ../yy/bin/zhspeak.py 搜索到"+jiangtan_max_id+"集百家讲坛")
        PaiXu("jiangtan")
    if MingLing == "js_quanbu" or MingLing == "js_langdu":
        SJK_YouBiao.execute('SELECT XuHao_L FROM langdu')
        langdu_max_id = str(len(SJK_YouBiao.fetchall()))
        x_max_id = langdu_max_id
        print("langdu: "+langdu_max_id)
        os.system("python3 ../yy/bin/zhspeak.py 搜索到"+langdu_max_id+"篇朗读")
        PaiXu("langdu")
    SJK_LianJie.close()
    
    if Shuo == "python3 ../yy/bin/zhspeak.py ":
        yuyan = "zhongwen"
    elif Shuo == "./echo ":
        yuyan = "riyu"
    elif Shuo == "espeak":
        yuyan = "yingyu"
        
    PZ_WenJian_ChuShiHua = [
        'MingLing = bf_yinyue\n',
        'MoShi = shunxu\n',
        'yinyue_mp3 = 1/'+yinyue_mp3_max_id+',00:00:00\n',
        'yinyue_wav = 1/'+yinyue_wav_max_id+',00:00:00\n',
        'shici = 1/'+shici_max_id+',00:00:00\n',
        'xiangsheng = 1/'+xiangsheng_max_id+',00:00:00\n',
        'pingshu = 1/'+pingshu_max_id+',00:00:00\n',
        'jiangtan = 1/'+jiangtan_max_id+',00:00:00\n',
        'langdu = 1/'+langdu_max_id+',00:00:00\n',
        'shoucang = 1/None,00:00:00\n',
        'dianbo = 1/None,00:00:00\n'
        'yuyan = '+yuyan+'\n'
        ]
    try:
        if MingLing == 'js_quanbu' and os.path.isfile("peizhi"):
            os.system('rm peizhi')
        with open(PZ_WenJian) as f:
            lines = f.readlines()
            for line in lines:
                if line.find(MingLing[3:]) == 0:
                    lines[lines.index(line)] = MingLing[3:]+' = 1/'+x_max_id+',00:00:00\n'
                    break
            with open(PZ_WenJian,'w') as f:
                f.writelines(lines)
    except:
        with open(PZ_WenJian,'w') as f:
            f.writelines(PZ_WenJian_ChuShiHua)
    print("搜索完毕。")
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
    
def ChaXun(MingLing):
    LeiBie = {"yinyue_mp3":["音乐","首"],
              "yinyue_wav":["无损音乐","首"],
              "shici":["诗词","首"],
              "xiangsheng":["相声","段"],
              "pingshu":["评书","段"],
              "jiangtan":["百家讲坛","集"],
              "langdu":["朗读","篇"]}

    try:
        with open(PZ_WenJian) as f:
            lines = f.readlines()
            for line in lines:
                if line.find("MingLing") == 0:
                    Biao = re.match(r'MingLing = bf_(.*)(\n)?', line).group(1).strip(' ""')
                    if Biao == "yinyue":
                        Biao = "yinyue_mp3"
                    elif Biao == "wusun":
                        Biao = "yinyue_wav"
                    break
            for line in lines:
                if line.find(Biao) == 0:
                    Max_Id = re.match(r'.+=(.*)/(.*),.+', line).group(2).strip(' ""')
                    XuHao = (int(re.match(r'.+=(.*)/(.*),.+', line).group(1).strip(' ""')),)
                    break
    except:
        print("请先添加文件，然后用搜索命令建立播放列表。")
        os.system(Shuo+DuiHua[6][0])
        HuiDa = ""
        return HuiDa
    
    SJK_LianJie = sqlite3.connect(SJK_WenJian)
    SJK_YouBiao = SJK_LianJie.cursor()
    if MingLing == "cx_renwu":
        SJK_YouBiao.execute('SELECT RenWu FROM '+Biao+' WHERE XuHao =?',XuHao)
        RenWu = SJK_YouBiao.fetchone()[0].strip('0123456789.')
        SJK_YouBiao.execute('SELECT MingCheng FROM '+Biao+' WHERE XuHao =?',XuHao)
        MingCheng = SJK_YouBiao.fetchone()[0]
        if "(" in MingCheng:
            MingCheng = MingCheng.replace('(','')
        if ")" in MingCheng:
            MingCheng = MingCheng.replace(')','')
        HuiDa = r"这{}{}是{}的{}".format(LeiBie[Biao][1], LeiBie[Biao][0], RenWu, MingCheng)
    elif MingLing == "cx_mingcheng":
        SJK_YouBiao.execute('SELECT MingCheng FROM '+Biao+' WHERE XuHao =?',XuHao)
        MingCheng = SJK_YouBiao.fetchone()[0]
        if "(" in MingCheng:
            MingCheng = MingCheng.replace('(','')
        if ")" in MingCheng:
            MingCheng = MingCheng.replace(')','')
        HuiDa = "这{}{}的名字叫{}".format(LeiBie[Biao][1], LeiBie[Biao][0], MingCheng)
    elif MingLing == "cx_zhuanji":
        SJK_YouBiao.execute('SELECT ZhuanJi FROM '+Biao+' WHERE XuHao =?',XuHao)
        ZhuanJi = SJK_YouBiao.fetchone()[0]
        if "(" in ZhuanJi:
            ZhuanJi = ZhuanJi.replace('(','')
        if ")" in ZhuanJi:
            ZhuanJi = ZhuanJi.replace(')','')
        HuiDa = "这{}{}的专辑名字叫{}".format(LeiBie[Biao][1], LeiBie[Biao][0], ZhuanJi)
    elif MingLing == "cx_qumu_shu":
        SJK_YouBiao.execute('SELECT RenWu FROM '+Biao+' WHERE XuHao =?',XuHao)
        RenWu = SJK_YouBiao.fetchone()[0]
        SJK_YouBiao.execute('SELECT MingCheng FROM '+Biao+' WHERE RenWu =?', (RenWu,))
        LieBiao = SJK_YouBiao.fetchall()
        HuiDa = "一共有"+str(len(LieBiao))+"{}他的{}".format(LeiBie[Biao][1], LeiBie[Biao][0])
    elif MingLing == "cx_zhuanji_shu":
        SJK_YouBiao.execute('SELECT RenWu FROM '+Biao+' WHERE XuHao =?',XuHao)
        RenWu = SJK_YouBiao.fetchone()[0]
        SJK_YouBiao.execute('SELECT ZhuanJi FROM '+Biao+' WHERE RenWu =?',(RenWu,))
        LieBiao = SJK_YouBiao.fetchall()
        ZhuanJi_LieBiao = []
        for n in LieBiao:
            if not n in ZhuanJi_LieBiao:
                ZhuanJi_LieBiao.append(n)
        HuiDa = "一共有"+str(len(ZhuanJi_LieBiao))+"个他的专辑"
    SJK_LianJie.close()
    return HuiDa

def DianBo(CanShu):
    SJK_LianJie = sqlite3.connect(SJK_WenJian)
    SJK_YouBiao = SJK_LianJie.cursor()
    
    if len(CanShu) == 1:
        if CanShu == ("quanbu",):
            Biao = ["yinyue_mp3","yinyue_wav","shici","xiangsheng","pingshu","jiangtan","langdu"]
            XinXi_Biao = {}
            for b in Biao:
                SJK_YouBiao.execute('SELECT PinYin,RenWu,MingCheng FROM '+b)
                xs = SJK_YouBiao.fetchall()
                for x in xs:
                    XinXi_Biao[x[0]] = [x[1],x[2]]
            return XinXi_Biao
        else:
            SJK_YouBiao.execute('SELECT PinYin,RenWu,MingCheng FROM '+CanShu[0])
            xs = SJK_YouBiao.fetchall()
            XinXi_Biao = {}
            for x in xs:
                XinXi_Biao[x[0]] = [x[1],x[2]]
            return XinXi_Biao
    elif len(CanShu) == 2:
        SJK_YouBiao.execute('DROP TABLE IF EXISTS dianbo')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS dianbo([XuHao] INTEGER PRIMARY KEY, [MingCheng] text, [RenWu] text, [LuJing] varchar unique)')
        SJK_LianJie.commit()
        i = 0
        if CanShu[1] == "quanbu":
            Biao = ["yinyue_mp3","yinyue_wav","shici","xiangsheng","pingshu","jiangtan","langdu"]
            for b in Biao:
                for n in CanShu[0]:
                    try:
                        SJK_YouBiao.execute('SELECT MingCheng,RenWu,LuJing FROM '+b+' WHERE PinYin=?',(n,))
                        data = (i+1,) + SJK_YouBiao.fetchone()
                        SJK_YouBiao.execute('INSERT INTO dianbo VALUES(?,?,?,?)', data)
                        SJK_LianJie.commit()
                        i += 1
                    except:
                        break
                if i > 0:
                    break
        else:
            for n in CanShu[0]:
                SJK_YouBiao.execute('SELECT MingCheng,RenWu,LuJing FROM '+CanShu[1]+' WHERE PinYin=?',(n,))
                data = (i+1,) + SJK_YouBiao.fetchone()
                SJK_YouBiao.execute('INSERT INTO dianbo VALUES(?,?,?,?)', data)
                SJK_LianJie.commit()
                i += 1
            SJK_LianJie.close()
        with open(PZ_WenJian) as f:
            lines = f.readlines()
            for line in lines:
                if line.find("dianbo") == 0:
                    lines[lines.index(line)] = re.sub(r'= .+/.+,.+\n', r'= 1/'+str(i)+r','+r'00:00:00\n', line)
                    break
            with open(PZ_WenJian,'w') as f:
                f.writelines(lines)

def WenZi_Zhuan_PinYin(RenWu, MingCheng):
    SJK_DuiHua_LianJie = sqlite3.connect(SJK_DuiHua)
    SJK_DuiHua_YouBiao = SJK_DuiHua_LianJie.cursor()
    PinYin = ""
    
    if MingCheng == None:
        for r in RenWu:
            SJK_DuiHua_YouBiao.execute('SELECT PinYin FROM hanzi WHERE HanZi=?', (r,))
            PinYin = PinYin + SJK_DuiHua_YouBiao.fetchone()[0] + " "
        PinYin = PinYin.strip()
        SJK_DuiHua_LianJie.close()
        return PinYin
    
    del_f = [' ', '(', ')', '·', '.', '《', '》', '&', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for f in RenWu:
        if f in del_f:
            RenWu = RenWu.replace(f,"")
    for f in MingCheng:
        if f in del_f:
            MingCheng = MingCheng.replace(f,"")
    WenZi = RenWu+","+MingCheng
    for w in WenZi:
        if w == ",":
            PinYin = PinYin.strip() + w
            continue
        try:
            SJK_DuiHua_YouBiao.execute('SELECT PinYin FROM hanzi WHERE HanZi=?', (w,))
            PinYin = PinYin + SJK_DuiHua_YouBiao.fetchone()[0] + " "
        except:
            PinYin = PinYin + w +" "
    PinYin = PinYin.strip()
    return PinYin
    
def QingKong(MingLing):
    LuJing = "/home/pi/Music/"
    if re.match('qk_(.+)', MingLing).group(1) == "yinyue_mp3":
        WenJianJia = LuJing+"mp3/yinyue"
    elif re.match('qk_(.+)', MingLing).group(1) == "yinyue_wav":
        WenJianJia = LuJing+"wav"
    else:
        WenJianJia = LuJing+"mp3/"+re.match('qk_(.+)', MingLing).group(1)
    os.system("rm -r "+WenJianJia+"/*")
    JianSuo(MingLing.replace("qk","js"))
    os.system(Shuo+DuiHua[19][0])
    
def ShanChu():
    try:
        with open(PZ_WenJian) as f:
            lines = f.readlines()
            for line in lines:
                if line.find("MingLing") == 0:
                    Biao = re.match(r'MingLing = bf_(.*)(\n)?', line).group(1).strip(' ""')
                    if Biao == "yinyue":
                        Biao = "yinyue_mp3"
                    elif Biao == "wusun":
                        Biao = "yinyue_wav"
                    elif Biao == "shoucang" or Biao == "dianbo":
                        print("不能从收藏和点播删除文件。")
                        os.system(Shuo+DuiHua[28][0])
                        return
                    break
            for line in lines:
                if line.find(Biao) == 0:
                    XuHao = (int(re.match(r'.+=(.*)/(.*),.+', line).group(1).strip(' ""')),)
                    break
    except:
        print("请先添加文件，然后用搜索命令建立播放列表。")
        os.system(Shuo+DuiHua[6][0])
        return
        
    SJK_LianJie = sqlite3.connect(SJK_WenJian)
    SJK_YouBiao = SJK_LianJie.cursor()
    SJK_YouBiao.execute('SELECT LuJing FROM '+Biao+' WHERE XuHao=?', XuHao)
    LuJing = SJK_YouBiao.fetchone()[0]
    os.system("rm "+re.escape(LuJing))
    JianSuo("js_"+Biao)
    print("已删除。")
    os.system(Shuo+DuiHua[26][0])
    
def BaoShi(Wen):
    FaYin = {"天":["Sun"],"一":["Mon","Jan","01"],"二":["Tue","Feb","02"],"三":["Wed","Mar","03"],
             "四":["Thu","Apr","04"],"五":["Fri","May","05"],"六":["Sat","Jun","06"],
             "七":["Jul","07"],"八":["Aug","08"],"九":["Sep","09"],"十":["Oct","10"],
             "十一":["Nov","11"],"十二":["Dec","12"],"十三":["13"],"十四":["14"],"十五":["15"],
             "十六":["16"],"十七":["17"],"十八":["18"],"十九":["19"],"二十":["20"],"二十一":["21"],
             "二十二":["22"],"二十三":["23"],"二十四":["24"],"二十五":["25"],"二十六":["26"],
             "二十七":["27"],"二十八":["28"],"二十九":["29"],"三十":["30"],"三十一":["31"],
             "三十二":["32"],"三十三":["33"],"三十四":["34"],"三十五":["35"],"三十六":["36"],
             "三十七":["37"],"三十八":["38"],"三十九":["39"],"四十":["40"],"四十一":["41"],
             "四十二":["42"],"四十三":["43"],"四十四":["44"],"四十五":["45"],"四十六":["46"],
             "四十七":["47"],"四十八":["48"],"四十九":["49"],"五十":["50"],"五十一":["51"],
             "五十二":["52"],"五十三":["53"],"五十四":["54"],"五十五":["55"],"五十六":["56"],
             "五十七":["57"],"五十八":["58"],"五十九":["59"],"六十":["60"]}
    if "几点" in Wen: 
        Shi = re.match(r'(.+) (.+) (.+) (.+) (.+)',time.asctime()).group(4)[:5].split(":")
        for key,value in FaYin.items():
            if Shi[0] in value:
                Dian = key
            if int(Shi[1]) > 10 and Shi[1] in value:
                Fen = key
        print(Dian+"点"+Fen)
        os.system("python3 ../yy/bin/zhspeak.py "+Dian+"点"+Fen)

    elif "几号" in Wen or "日期" in Wen:
        RiQi = re.match(r'(.+) (.+) (.+) (.+) (.+)',time.asctime()).group(3)
        for key,value in FaYin.items():
            if RiQi in value:
                RiQi = key
                break
        print(RiQi+"号")
        os.system("python3 ../yy/bin/zhspeak.py "+RiQi+"号")
    
    elif "星期" in Wen:
        XingQi = re.match(r'(.+) (.+) (.+) (.+) (.+)',time.asctime()).group(1)
        for key,value in FaYin.items():
            if XingQi in value:
                XingQi = key
                break
        print("星期"+XingQi)
        os.system("python3 ../yy/bin/zhspeak.py "+"星期"+XingQi)
    elif "农历" in Wen or "阴历" in Wen or "努力" in Wen or "能力" in Wen or "什么日子" in Wen:
        import wannianli
        if "农历" in Wen or "阴历" in Wen or "努力" in Wen or "能力" in Wen:
            NongLi = wannianli.getCalendar_today().split()[2]
            for n in NongLi:
                if n in "[]":
                    NongLi = NongLi.replace(n,"")
            print(NongLi)
            os.system("python3 ../yy/bin/zhspeak.py "+NongLi)
        else:
            try:
                JieRi = wannianli.getCalendar_today().split()[3].split("#")[1]
                print("今天是"+JieRi)
                os.system("python3 ../yy/bin/zhspeak.py "+"今天是"+JieRi)
            except:
                print("今天没什么特别的")
                os.system("python3 ../yy/bin/zhspeak.py "+"今天没什么特别的")

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
