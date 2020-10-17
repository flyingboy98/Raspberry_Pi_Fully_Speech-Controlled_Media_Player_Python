#!/usr/bin/env python3

from time import sleep, time
import subprocess
import sqlite3
import random
import re
import os
import ziyuanguanli as ZYGL


BoFangFangShi = subprocess.Popen
BoFangQi_MoRen = ["omxplayer","-o","alsa","-l","00:00:00"]
BoFangQi_WuSun = ["omxplayer","-o","hdmi","-p","-l","00:00:00"]
TingZhi_MoRen = ['killall','omxplayer.bin']
MingLing_Biao = {
    "bf_yinyue":"yinyue_mp3",
    "bf_wusun":"yinyue_wav",
    "bf_shici":"shici",
    "bf_pingshu":"pingshu",
    "bf_langdu":"langdu",
    "bf_shoucang":"shoucang"
    }

def ZhiXing(MoShi, MingLing):
    ZhuanJi = ""
    ZhuanJiQuMu = []
    if MingLing in list(MingLing_Biao):
        Biao = MingLing_Biao[MingLing]
        DangQian_MoShi = "shunxu"
        try:
            with open(ZYGL.PZ_WenJian) as f:
                lines = f.readlines()
                for line in lines:
                    if line.find("MingLing") == 0:
                        if re.match(r'MingLing =(.*)(\n)?', line).group(1).strip(' ""') != MingLing:
                            lines[lines.index(line)] = re.sub(r'=(.*)(\n)?', r'= '+MingLing+r'\n', line)
                    elif line.find("MoShi") == 0:
                        if re.match(r'MoShi =(.*)(\n)?', line).group(1).strip(' ""') != DangQian_MoShi:
                            lines[lines.index(line)] = re.sub(r'=(.*)(\n)?', r'= '+DangQian_MoShi+r'\n', line)
                    elif line.find(Biao) == 0:
                        XuHao = (int(re.match(r'.+=(.*)/(.*),.+', line).group(1).strip(' ""')),)
                        Max_Id = re.match(r'.+=(.*)/(.*),.+', line).group(2).strip(' ""')
                        Kill_Time = re.match(r'.+,(.*)(\n)?', line).group(1).strip(' ""')
                        if Max_Id == "None":
                            print("还没有此类资源，请添加。")
                            os.system(ZYGL.Shuo+ZYGL.DuiHua[4][0])
                            return
                        lines[lines.index(line)] = re.sub(r'[0-9]{2}:[0-9]{2}:[0-9]{2}(\n)?',r'00:00:00\n', line)
                with open(ZYGL.PZ_WenJian,'w') as f:
                    f.writelines(lines)
        except:
            print("请重新搜索。")
            os.system(ZYGL.Shuo+ZYGL.DuiHua[3][0])
    elif MingLing == "bf_jixu" or MingLing == "bf_danqu" or MingLing == "bf_suiji" or MingLing == "bf_shunxu" or MingLing == "bf_shangyi" or MingLing == "bf_xiayi" or MingLing == "bf_congtou" or MingLing == "bf_zhuanjixunhuan" or MingLing == "bf_shangzhuanji" or MingLing == "bf_xiazhuanji":
        try:
            with open(ZYGL.PZ_WenJian) as f:
                lines = f.readlines()
                for line in lines:
                    if line.find("MingLing") == 0:
                        Biao = MingLing_Biao[re.match(r'MingLing =(.*)(\n)?', line).group(1).strip(' ""')]
                        break
                for line in lines:
                    if line.find("MoShi") == 0:
                        line_id = lines.index(line)
                        if MingLing == "bf_danqu" or MingLing == "bf_shunxu" or MingLing == "bf_suiji" or MingLing =="bf_zhuanjixunhuan":
                            if re.match(r'MoShi =(.*)(\n)?', line).group(1).strip(' ""') != MingLing.strip('bf_'):
                                lines[line_id] = re.sub(r'=(.*)(\n)?', r'= '+MingLing.strip('bf_')+r'\n', line)
                        elif MingLing == "bf_congtou" or MingLing == "bf_shangzhuanji" or MingLing == "bf_xiazhuanji":
                            lines[line_id] = re.sub(r'=(.*)(\n)?', r'= shunxu\n', line)
                        DangQian_MoShi = re.match(r'MoShi =(.*)(\n)?', lines[line_id]).group(1).strip(' ""')
                for line in lines:
                    if line.find(Biao) == 0:
                        line_id = lines.index(line)
                        Max_Id = re.match(r'.+=(.*)/(.*),.+', line).group(2).strip(' ""')
                        XuHao = (int(re.match(r'.+=(.*)/(.*),.+', line).group(1).strip(' ""')),)
                        Kill_Time = re.match(r'.+,(.*)(\n)?', line).group(1).strip(' ""')
                        if Max_Id == "None":
                            print("还没有此类资源，请添加。")
                            os.system(ZYGL.Shuo+ZYGL.DuiHua[4][0])
                            return
                        if MingLing == "bf_suiji" or MingLing == "bf_congtou" or MingLing == "bf_shangyi" or MingLing == "bf_xiayi" or MingLing == "bf_shangzhuanji" or MingLing == "bf_xiazhuanji":
                            Kill_Time = "00:00:00"
                            if MingLing == "bf_congtou":
                                XuHao = (1,)
                            elif MingLing == "bf_shangyi" or MingLing == "bf_xiayi" or MingLing == "bf_shangzhuanji" or MingLing == "bf_xiazhuanji":
                                if DangQian_MoShi == "zhuanjixunhuan" or MingLing == "bf_shangzhuanji" or MingLing == "bf_xiazhuanji":
                                    SJK_LianJie = sqlite3.connect(ZYGL.SJK_WenJian)
                                    SJK_YouBiao = SJK_LianJie.cursor()
                                    SJK_YouBiao.execute('SELECT Zhuanji FROM '+Biao+' WHERE XuHao =?',XuHao)
                                    ZhuanJi = SJK_YouBiao.fetchall()[0]
                                    SJK_YouBiao.execute('SELECT XuHao FROM '+Biao+' WHERE ZhuanJi =?',ZhuanJi)
                                    ZhuanJiQuMu = SJK_YouBiao.fetchall()
                                    if  MingLing == "bf_shangzhuanji":
                                        if min(ZhuanJiQuMu) != (1,):
                                            XuHao = ((min(ZhuanJiQuMu)[0] - 1),)
                                        else:
                                            XuHao = (int(Max_Id),)
                                        SJK_YouBiao.execute('SELECT Zhuanji FROM '+Biao+' WHERE XuHao =?',XuHao)
                                        ZhuanJi = SJK_YouBiao.fetchall()[0]
                                        SJK_YouBiao.execute('SELECT XuHao FROM '+Biao+' WHERE ZhuanJi =?',ZhuanJi)
                                        ZhuanJiQuMu = SJK_YouBiao.fetchall()
                                        XuHao = min(ZhuanJiQuMu)
                                    elif MingLing == "bf_xiazhuanji":
                                        if max(ZhuanJiQuMu) != (int(Max_Id),):
                                            XuHao = ((max(ZhuanJiQuMu)[0] + 1),)
                                        else:
                                            XuHao = (1,)
                                        SJK_YouBiao.execute('SELECT Zhuanji FROM '+Biao+' WHERE XuHao =?',XuHao)
                                        ZhuanJi = SJK_YouBiao.fetchall()[0]
                                        SJK_YouBiao.execute('SELECT XuHao FROM '+Biao+' WHERE ZhuanJi =?',ZhuanJi)
                                        ZhuanJiQuMu = SJK_YouBiao.fetchall()
                                        XuHao = min(ZhuanJiQuMu)
                                    SJK_LianJie.close()
                                    if MingLing == "bf_shangyi":
                                        if XuHao != (1,):
                                            if XuHao != min(ZhuanJiQuMu):
                                                XuHao = (XuHao[0]-1,)
                                            else:
                                                XuHao = max(ZhuanJiQuMu)
                                        else:
                                            XuHao = max(ZhuanJiQuMu)
                                    elif MingLing == "bf_xiayi":
                                        if XuHao[0] != Max_Id:
                                            if XuHao != max(ZhuanJiQuMu):
                                                XuHao = (XuHao[0]+1,)
                                            else:
                                                XuHao = min(ZhuanJiQuMu)
                                        else:
                                            XuHao = min(ZhuanJiQuMu)
                                else:
                                    if MingLing == "bf_shangyi":
                                        if XuHao[0] == 1:
                                            XuHao = (int(Max_Id),)
                                        else:
                                            XuHao = (XuHao[0]-1,)
                                    elif MingLing == "bf_xiayi":
                                        if XuHao[0] == int(Max_Id):
                                            XuHao = (1,)
                                        else:
                                            XuHao = (XuHao[0]+1,)
                            lines[line_id] = re.sub(r'=(.*)/',r'= '+str(XuHao[0])+r'/', line)
                        lines[line_id] = re.sub(r'[0-9]{2}:[0-9]{2}:[0-9]{2}(\n)?',r'00:00:00\n', lines[line_id])
                with open(ZYGL.PZ_WenJian,'w') as f:
                    f.writelines(lines)
        except:
            print('这是第一次运行本程序,请先用"添加"和"搜索"命令建立相关文件。')
            os.system(ZYGL.Shuo+ZYGL.DuiHua[5][0])
            return

    if Biao == "yinyue_wav":
        print("将通过HDMI设备输出。")
        os.system(ZYGL.Shuo+ZYGL.DuiHua[16][0])
        
    SJK_LianJie = sqlite3.connect(ZYGL.SJK_WenJian)
    SJK_YouBiao = SJK_LianJie.cursor()

    Max_Id = int(Max_Id)    
    if MingLing == "bf_suiji":
        SuiJi_Biao = str(list(range(1,Max_Id+1))).strip('[]').split(', ')
        random.shuffle(SuiJi_Biao)
        SJK_YouBiao.execute('DROP TABLE IF EXISTS suiji')
        SJK_LianJie.commit()
        SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS suiji([XuHao] INTEGER PRIMARY KEY, [SuiJi_id] text)')
        SJK_LianJie.commit()
        i = 0
        for SuiJi_id in SuiJi_Biao:
            i += 1
            data = (i, int(SuiJi_id))
            SJK_YouBiao.execute('INSERT INTO suiji VALUES(?,?)', data)
        SJK_LianJie.commit()
        SuiJi_XuHao = (1,)
        XuHao = (int(SuiJi_Biao[0]),)
        with open(ZYGL.PZ_WenJian) as f:
            lines = f.readlines()
            for line in lines:
                if line.find(Biao) == 0:
                    lines[lines.index(line)] = re.sub(r'=(.*)/',r'= '+str(XuHao[0])+r'/', line)
                    with open(ZYGL.PZ_WenJian,'w') as f:
                        f.writelines(lines)
                    break
    elif MingLing == "bf_jixu":
        get_moshi = MoShi()
        if get_moshi[2]:
            SJK_YouBiao.execute('SELECT XuHao FROM suiji WHERE SuiJi_id =?',XuHao)
            SuiJi_XuHao = (SJK_YouBiao.fetchone()[0],)
   
    while True:
        try:
            SJK_YouBiao.execute('SELECT LuJing FROM '+Biao+' WHERE XuHao =?',XuHao)
            BoFangQuMu = SJK_YouBiao.fetchone()[0]
        except:
            print("请先添加文件，然后用搜索命令建立播放列表。")
            os.system(ZYGL.Shuo+ZYGL.DuiHua[6][0])
            return

        BoFangCanShu = []
        if Biao == "yinyue_wav":
            for cs in BoFangQi_WuSun:
                BoFangCanShu.append(cs)
        else:
            for cs in BoFangQi_MoRen:
                BoFangCanShu.append(cs)
        BoFangCanShu.append(BoFangQuMu)
        if BoFangQi_MoRen[0] == "omxplayer":
            if Biao == "yinyue_wav":
                BoFangCanShu[5] = Kill_Time
            else:
                BoFangCanShu[4] = Kill_Time
        ZhuangTai = BoFangFangShi(BoFangCanShu)
        print("正在播放："+BoFangQuMu)
        sleep(1)
        JiShi_KaiShi = time()
        
        while True:
            if ZhuangTai.poll() != None:
                Kill_Time = "00:00:00"
                break
            get_moshi = MoShi()
            if get_moshi[0]:
                ZhuangTai = BoFangFangShi(TingZhi_MoRen)
                
                JiShi_JieShu = time()
                if JiShi_JieShu - JiShi_KaiShi > 10:
                    Kill_Time = ['{0:02}'.format(int((JiShi_JieShu-JiShi_KaiShi-10)//60)),'{0:02}'.format(int((JiShi_JieShu-JiShi_KaiShi-10)%60))]
                    if int(Kill_Time[0]) < 60:
                        Kill_Time = ':'.join(['00','{0:02}'.format(int(Kill_Time[0])),'{0:02}'.format(int(Kill_Time[1]))])
                    elif int(Kill_Time[0]) > 60:
                        Kill_Time = ':'.join(['{0:02}'.format(int(Kill_Time[0]) // 60),'{0:02}'.format(int(Kill_Time[0]) % 60),Kill_Time[1]])
                else:
                    Kill_Time = "00:00:00"
                print(Kill_Time)
                with open(ZYGL.PZ_WenJian) as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.find(Biao) == 0:
                            lines[lines.index(line)] = re.sub(r'[0-9]{2}:[0-9]{2}:[0-9]{2}(\n)?',Kill_Time+r'\n', line)
                            with open(ZYGL.PZ_WenJian,'w') as f:
                                f.writelines(lines)
                            break
                SJK_LianJie.close()
                return

        get_moshi = MoShi()
        if get_moshi[1]:
            DangQian_MoShi = "danqu"
        elif get_moshi[2]:
            DangQian_MoShi = "suiji"
        elif get_moshi[3]:
            DangQian_MoShi = "zhuanjixunhuan"
        else:
            DangQian_MoShi = "shunxu"
        with open(ZYGL.PZ_WenJian) as f:
            lines = f.readlines()
            for line in lines:
                if line.find("MoShi") == 0:
                    if re.match(r'MoShi =(.*)(\n)?', line).group(1).strip(' ""') != DangQian_MoShi:
                        lines[lines.index(line)] = re.sub(r'=(.*)(\n)?', r'= '+DangQian_MoShi+r'\n', line)
                        with open(ZYGL.PZ_WenJian,'w') as f:
                            f.writelines(lines)
                        break
                    
        if DangQian_MoShi == "shunxu":
            if XuHao[0] != Max_Id:
                XuHao = (XuHao[0]+1,)
            else:
                XuHao = (1,)
        elif DangQian_MoShi == "suiji":
            if SuiJi_XuHao[0] != Max_Id:
                SuiJi_XuHao = (SuiJi_XuHao[0] + 1,)
            else:
                SuiJi_XuHao = (1,)
            SJK_YouBiao.execute('SELECT SuiJi_id FROM suiji WHERE XuHao =?',SuiJi_XuHao)
            XuHao = (SJK_YouBiao.fetchone()[0],)
        elif DangQian_MoShi == "zhuanjixunhuan":
            if ZhuanJiQuMu == []:
                SJK_YouBiao.execute('SELECT Zhuanji FROM '+Biao+' WHERE XuHao =?',XuHao)
                ZhuanJi = SJK_YouBiao.fetchall()[0]
                SJK_YouBiao.execute('SELECT XuHao FROM '+Biao+' WHERE ZhuanJi =?',ZhuanJi)
                ZhuanJiQuMu = SJK_YouBiao.fetchall()
            if XuHao[0] != Max_Id:
                if XuHao != max(ZhuanJiQuMu):
                    XuHao = (XuHao[0]+1,)
                else:
                    XuHao = min(ZhuanJiQuMu)
            else:
                XuHao = min(ZhuanJiQuMu)
            
        if not get_moshi[1]:
            with open(ZYGL.PZ_WenJian) as f:
                lines = f.readlines()
                for line in lines:
                    if line.find(Biao) == 0:
                        lines[lines.index(line)] = re.sub(r'=(.*)/',r'= '+str(XuHao[0])+r'/', line)
                        with open(ZYGL.PZ_WenJian,'w') as f:
                            f.writelines(lines)
                        break

            

