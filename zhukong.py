#!/usr/bin/env python3

from multiprocessing.pool import ThreadPool
from vosk import Model, KaldiRecognizer
from difflib import SequenceMatcher
from random import choice
from time import sleep
import RPi.GPIO as GPIO
import speech_recognition as sr
import threading
import sqlite3
import json
import wave
import os
import re
import bofangqi as BFQ
import tongyinzi as TYZ
import ziyuanguanli as ZYGL


def LuYin():
    YuYinLuZhi = sr.Recognizer()
    if MingLing == "":os.system(ZYGL.Shuo+choice(ZYGL.DuiHua[0][0].split()))
    print("start Listening ...")
    with sr.Microphone(device_index = 1, sample_rate = 16000, chunk_size = 512) as source:
               YuYinLuZhi.adjust_for_ambient_noise(source)
               audio = YuYinLuZhi.listen(source)
               print("start point!")
    with open("yuyin.wav", "wb") as f:
        f.write(audio.get_wav_data())
        os.system(ZYGL.Shuo+ZYGL.DuiHua[1][0])

'''this is for testing, not convenient when daemon.
def LuYin():
    #if MingLing == "":os.system(ZYGL.Shuo+choice(ZYGL.DuiHua[0][0].split()))
    print("start Listening ...")
    os.system("arecord -f S16_LE -t wav -r 16000 -d 5 yuyin.wav")
'''

def ShiBie_ZiFu():
    if PanDuan == "":
        ZiFuJi = "继 续 检 搜 索 全 部 无 损 听 歌 播 放 音 乐 停 止 诗 词 单 曲 专 辑 循 环 顺 序 随 相 声 评 书 讲 坛 朗 读 关 机 复 制 上 下 一 个 从 头 添 加 收 藏 中 文 日 语 英 更 新 升 级 清 空 谁 多 少 什 么 唱 名 叫 他 的"
    else:
        ZiFuJi = "对 是 嗯 没 错"
    wenben = ""
    model = Model("model")
    rec = KaldiRecognizer(model, 16000, ZiFuJi)
    WaveWenJian = open("yuyin.wav", "rb")
    WaveWenJian.read(44)
    while True:
        data = WaveWenJian.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            wenben = res['text']
            print("识别结果是：　"+res['text'])

    res = json.loads(rec.FinalResult())
    if wenben == "":
        wenben = res['text']
    print ("最终结果是：　"+wenben)

    return wenben
    
def ShiBie_ZiRanYuYan():
    wf = wave.open('yuyin.wav', "rb")
    model = Model("model")
    rec = KaldiRecognizer(model, wf.getframerate())
    wenben = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            wenben = res['text']
            #print("识别结果：",wenben)
        else:
            pass
            #if '"text" : "' in rec.PartialResult():
                #wenben = rec.PartialResult()
            #print("部分识别结果：",rec.PartialResult())
    
    if wenben == "":
        res = json.loads(rec.FinalResult())
        wenben = res['text']
#    n = wenben.find('"text" : "')
#    wenben = wenben[n+10:].strip('}""')
    del_zf = ' "\n'
    for c in wenben:
        if c in del_zf:
            wenben = wenben.replace(c,'')
            
    return wenben

    
def ChaZiDian(data):
    data = "".join(data.split())
    for key in ZiDian_MingLing:
        i = 0
        n = []
        check_word = []
        for k in key:
            i += 1
            if k in data:
                n.append(data.index(k))
                if data.index(k) - i < 2:
                    if len(n) > 1:
                        if n[len(n)-1] > n[len(n)-2]:
                            check_word.append(k)
                    else:
                        check_word.append(k)
            else:
                break
            if "".join(check_word) == key:
                return key
    return ""    

def DuiBi(JieGuo_ZiRanYuYan):
    LeiBie_Biao = {"音乐":["歌","歌曲","个","哥","音乐"],"诗词":["诗","事","时","吃","诗词","誓词","是此","支持"],"相声":["相声","向上"],"评书":["评书","评述","评出","频出","频谱",],"讲坛":["讲坛","讲堂"],"朗读":["朗读"]}
    def get_key(val):
        l = []
        for key, value in XinXi_Biao.items():
            if val in value:
                l.append(key)
        return l

    RenWu = ""
    MingCheng = ""
    LeiBie = ""
    Biao = ""
    pat = re.compile(r'(.+),(.+)')
    if re.match(r'.*(有没)?(有|听|停|放|找)(.+)的(歌|歌曲|个|哥|音乐|相声|向上|诗|诗词|是此|支持|誓词|事|时|吃|评书|评述|评出|频出|频谱|朗读|讲坛|讲堂).*', JieGuo_ZiRanYuYan):
        RenWu = re.match(r'.*(有没)?(有|听|停|放|找)(.+)的(歌|歌曲|个|哥|音乐|相声|向上|诗|诗词|是此|支持|誓词|事|时|吃|誓|评书|评述|评出|频出|频谱|朗读|讲坛|讲堂).*', JieGuo_ZiRanYuYan).group(3)
        LeiBie = re.match(r'.*(有没)?(有|听|停|放|找)(.+)的(歌|歌曲|个|哥|音乐|相声|向上|诗|诗词|是此|支持|誓词|事|时|吃|评书|评述|评出|频出|频谱|朗读|讲坛|讲堂).*', JieGuo_ZiRanYuYan).group(4)
    elif re.match(r'.*(.{2,4})的(歌|歌曲|个|哥|音乐|音乐|相声|向上|诗|诗词|是此|支持|誓词|事|时|吃|评书|评述|评出|频出|频谱|朗读|讲坛|讲堂).*', JieGuo_ZiRanYuYan):
        RenWu = re.match(r'(.+)的(歌|歌曲|个|哥|音乐|相声|向上|诗|诗词|是此|支持|誓词|事|时|吃|评书|评述|评出|频出|频谱|朗读|讲坛|讲堂).*', JieGuo_ZiRanYuYan).group(1)
        LeiBie = re.match(r'(.+)的(歌|歌曲|个|哥|音乐|相声|向上|诗|诗词|是此|支持|誓词|事|时|吃|评书|评述|评出|频出|频谱|朗读|讲坛|讲堂).*', JieGuo_ZiRanYuYan).group(2)
    elif re.match(r'.*?(歌曲|音乐|相声|向上|诗词|是此|支持|誓词|评书|评述|评出|频出|频谱|朗读|讲坛|讲堂)(.+)(吗)?', JieGuo_ZiRanYuYan):
        MingCheng = re.match(r'.*?(歌曲|音乐|相声|向上|诗词|是此|支持|誓词|评书|频出|频谱|评述|评出|朗读|讲坛|讲堂)(.+)(吗)?', JieGuo_ZiRanYuYan).group(2)
        LeiBie = re.match(r'.*?(歌曲|音乐|相声|向上|诗词|是此|支持|誓词|评书|评述|评出|频出|频谱|朗读|讲坛|讲堂)(.+)(吗)?', JieGuo_ZiRanYuYan).group(1)
    elif re.match(r'.+的.+',JieGuo_ZiRanYuYan):
        Biao = "quanbu"
    elif JieGuo_ZiRanYuYan == "删除":
        print("确定要删除吗？")
        os.system(ZYGL.Shuo+ZYGL.DuiHua[27][0])
        return "shanchu?"
    elif re.match(r'.*(几点|几号|日期|星期|农历|努力|能力|阴历|什么日子).*', JieGuo_ZiRanYuYan):
        ZYGL.BaoShi(JieGuo_ZiRanYuYan)
        return ""
    else:
        print("没听明白，请再说一遍。")
        os.system(ZYGL.Shuo+ZYGL.DuiHua[22][0])
        return ""
    if len(RenWu) > 4:
        RenWu = re.match('.+(.{3})', RenWu).group(1)
    for key, value in LeiBie_Biao.items():
        if LeiBie in value:
            LeiBie = key
            break
    if RenWu != "" or MingCheng != "" or Biao != "":
        print("请稍等，我看看。")
        os.system(ZYGL.Shuo+ZYGL.DuiHua[23][0])
        if LeiBie == "音乐":
            Biao = "yinyue_mp3"
        elif LeiBie == "诗词":
            Biao = "shici"
        elif LeiBie == "相声":
            Biao = "xiangsheng"
        elif LeiBie == "评书":
            Biao = "pingshu"
        elif LeiBie == "讲坛":
            Biao = "jiangtan"
        elif LeiBie == "朗读":
            Biao = "langdu"
        XinXi_Biao = ZYGL.DianBo((Biao,))
        if RenWu != "":
            RenWu = ZYGL.WenZi_Zhuan_PinYin(RenWu, None)
            for key in XinXi_Biao:
                try:
                    sim = SequenceMatcher(None, RenWu, re.match(pat, key).group(1)).ratio()
                except:
                    sim = 0.01
                XinXi_Biao[key].append(float('{:.2f}'.format(sim*100)))
            XiangSiDu_LieBiao = []
            for l in list(XinXi_Biao.values()):
                if not l in XiangSiDu_LieBiao:
                    XiangSiDu_LieBiao.append(l[2])
            XiangSiDu_LieBiao = sorted(XiangSiDu_LieBiao, reverse=True)
            if len(XiangSiDu_LieBiao) > 0:
                XiangSiDu1 = XiangSiDu_LieBiao[0]
                print("相似度1: "+str(XiangSiDu1)+"%。")
#            if len(XiangSiDu_LieBiao) > 1:
#                XiangSiDu2 = XiangSiDu_LieBiao[1]
#                print("相似度2: "+str(XiangSiDu2)+"%。")
#            if len(XiangSiDu_LieBiao) > 2:
#                XiangSiDu3 = XiangSiDu_LieBiao[2]
#                print("相似度3: "+str(XiangSiDu3)+"%。")
            if XiangSiDu1 > 70:
                BiJiao_JieGuo1 = get_key(XiangSiDu1)
                for key, value in XinXi_Biao.items():
                    if XiangSiDu1 in value:
                        RenWu_WenZi = value[0]
                        break
                print("是要听"+RenWu_WenZi+"的"+LeiBie+"吗")
                os.system("python3 ../yy/bin/zhspeak.py "+"是要听"+RenWu_WenZi+"的"+LeiBie+"吗")
                return (BiJiao_JieGuo1, Biao)
            else:
                print("好象没有哦！")
                os.system(ZYGL.Shuo+ZYGL.DuiHua[24][0])
                return ""
        elif MingCheng != "":
            MingCheng = ZYGL.WenZi_Zhuan_PinYin(MingCheng, None)
            for key in XinXi_Biao:
                try:
                    sim = SequenceMatcher(None, MingCheng, re.match(pat, key).group(2)).ratio()
                except:
                    sim = 0.01
                XinXi_Biao[key].append(float('{:.2f}'.format(sim*100)))
            XiangSiDu_LieBiao = []
            for l in list(XinXi_Biao.values()):
                if not l in XiangSiDu_LieBiao:
                    XiangSiDu_LieBiao.append(l[2])
            XiangSiDu_LieBiao = sorted(XiangSiDu_LieBiao, reverse=True)
            if len(XiangSiDu_LieBiao) > 0:
                XiangSiDu1 = XiangSiDu_LieBiao[0]
                print("相似度1: "+str(XiangSiDu1)+"%。")
#            if len(XiangSiDu_LieBiao) > 1:
#                XiangSiDu2 = XiangSiDu_LieBiao[1]
#                print("相似度2: "+str(XiangSiDu2)+"%。")
#            if len(XiangSiDu_LieBiao) > 2:
#                XiangSiDu3 = XiangSiDu_LieBiao[2]
#                print("相似度3: "+str(XiangSiDu3)+"%。")
            if XiangSiDu1 > 50:
                BiJiao_JieGuo1 = get_key(XiangSiDu1)
                for key, value in XinXi_Biao.items():
                    if XiangSiDu1 in value:
                        MingCheng = value[1]
                        break
                for m in MingCheng:
                    if m in "()":
                        MingCheng = MingCheng.replace(m,"")
                print("是要听"+LeiBie+re.escape(MingCheng)+"吗")
                os.system("python3 ../yy/bin/zhspeak.py "+"是要听"+LeiBie+re.escape(MingCheng)+"吗")
                return (BiJiao_JieGuo1, Biao)
            else:
                print("好象没有哦！")
                os.system(ZYGL.Shuo+ZYGL.DuiHua[24][0])
                return ""
        elif Biao == "quanbu":
            Ren_Ming = ZYGL.WenZi_Zhuan_PinYin(JieGuo_ZiRanYuYan.split("的")[0], JieGuo_ZiRanYuYan.split("的")[1])
            print(Ren_Ming)
            for key in XinXi_Biao:
                try:
                    sim = SequenceMatcher(None, Ren_Ming, key).ratio()
                except:
                    sim = 0.01
                XinXi_Biao[key].append(float('{:.2f}'.format(sim*100)))
            XiangSiDu_LieBiao = []
            for l in list(XinXi_Biao.values()):
                if not l in XiangSiDu_LieBiao:
                    XiangSiDu_LieBiao.append(l[2])
            XiangSiDu_LieBiao = sorted(XiangSiDu_LieBiao, reverse=True)
            if len(XiangSiDu_LieBiao) > 0:
                XiangSiDu1 = XiangSiDu_LieBiao[0]
                print("相似度1: "+str(XiangSiDu1)+"%。")
#            if len(XiangSiDu_LieBiao) > 1:
#                XiangSiDu2 = XiangSiDu_LieBiao[1]
#                print("相似度2: "+str(XiangSiDu2)+"%。")
#            if len(XiangSiDu_LieBiao) > 2:
#                XiangSiDu3 = XiangSiDu_LieBiao[2]
#                print("相似度3: "+str(XiangSiDu3)+"%。")
            if XiangSiDu1 > 60:
                BiJiao_JieGuo1 = get_key(XiangSiDu1)
                for key, value in XinXi_Biao.items():
                    if XiangSiDu1 in value:
                        RenWu = value[0]
                        MingCheng = value[1]
                        break
                for m in MingCheng:
                    if m in r' ()·.《》&_-~@#$%*[]{}":;?,':
                        MingCheng = MingCheng.replace(m,"")
                print("是要听"+RenWu+"的"+re.escape(MingCheng)+"吗")
                os.system("python3 ../yy/bin/zhspeak.py "+"是要听"+RenWu+"的"+re.escape(MingCheng)+"吗")
                return (BiJiao_JieGuo1, Biao)
            else:
                print("好象没有哦！")
                os.system(ZYGL.Shuo+ZYGL.DuiHua[24][0])
                return ""
    else:
        print("没听清，请再说一遍。")
        os.system(ZYGL.Shuo+ZYGL.DuiHua[22][0])
        return ""


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
os.chdir('/home/pi/Documents/yuyinbofang')

PanDuan = ""
MingLing = ""
ZiDian_MingLing = {
    "听歌":"bf_yinyue",
    "放歌":"bf_yinyue",
    "放音乐":"bf_yinyue",
    "放无损":"bf_wusun",
    "放诗词":"bf_shici",
    "放相声":"bf_xiangsheng",
    "放评书":"bf_pingshu",
    "放讲坛":"bf_jiangtan",
    "放朗读":"bf_langdu",
    "听音乐":"bf_yinyue",
    "听无损":"bf_wusun",
    "听诗词":"bf_shici",
    "听相声":"bf_xiangsheng",
    "听评书":"bf_pingshu",
    "听讲坛":"bf_jiangtan",
    "听朗读":"bf_langdu",
    "顺序":"bf_shunxu",
    "单曲":"bf_danqu",
    "随机":"bf_suiji",
    "停止":"bf_ting",
    "继续":"bf_jixu",
    "从头":"bf_congtou",
    "上一":"bf_shangyi",
    "下一":"bf_xiayi",
    "上专辑":"bf_shangzhuanji",
    "下专辑":"bf_xiazhuanji",
    "专辑循环":"bf_zhuanjixunhuan",
    "播放收藏":"bf_shoucang",
    "搜索全部":"js_quanbu",
    "搜索音乐":"js_yinyue_mp3",
    "搜索诗词":"js_shici",
    "搜索无损":"js_yinyue_wav",
    "搜索相声":"js_xiangsheng",
    "搜索评书":"js_pingshu",
    "搜索讲坛":"js_jiangtan",
    "搜索朗读":"js_langdu",
    "添加收藏":"shoucang",
    "清空音乐":"qk_yinyue_mp3",
    "清空无损":"qk_yinyue_wav",
    "清空诗词":"qk_shici",
    "清空相声":"qk_xiangsheng",
    "清空评书":"qk_pingshu",
    "清空讲坛":"qk_jiangtan",
    "清空朗读":"qk_langdu",
    "复制":"fuzhi",
    "关机":"guanji",
    "中文":"zhongwen",
    "日语":"riyu",
    "英语":"yingyu",
    "更新":"gengxin",
    "升级":"shengji",
    "谁唱":"cx_renwu",
    "谁的":"cx_renwu",
    "什么歌":"cx_mingcheng",
    "什么诗":"cx_mingcheng",
    "什么名":"cx_mingcheng",
    "什么相声":"cx_mingcheng",
    "什么评书":"cx_mingcheng",
    "叫什么":"cx_mingcheng",
    "什么专辑":"cx_zhuanji",
    "专辑名":"cx_zhuanji",
    "多少他":"cx_qumu_shu",
    "他多少":"cx_qumu_shu",
    "多少专辑":"cx_zhuanji_shu"
    }
# [ting,danqu,suiji,zhuanjixunhuan],shunxu is default
#MoShi = [True, False, False, False]
try:
    with open(ZYGL.PZ_WenJian) as f:
        lines = f.readlines()
        for line in lines:
            if line.find("MoShi") == 0:
                if re.findall("shunxu", line):
                    MoShi = [False,False,False,False]
                elif re.findall("danqu", line):
                    MoShi = [False,True,False,False]
                elif re.findall("suiji", line):
                    MoShi = [False,False,True,False]
                elif re.findall("zhuanjixunhuan", line):
                    MoShi = [False,False,False,True]
                break
except:
    MoShi = [False, False, False, False]

Thread_BFQ = threading.Thread(target = BFQ.ZhiXing, args =(lambda : MoShi, "bf_jixu"))
Thread_BFQ.start()
while True:
    if GPIO.input(2) == 1:
        sleep(1)
        continue
    LY = LuYin()
    
    pool = ThreadPool(processes=1)
    Thread_MingLing = pool.apply_async(ShiBie_ZiFu)
    Thread_ZiRanYuYan = pool.apply_async(ShiBie_ZiRanYuYan)
    
    JieGuo_MingLing = Thread_MingLing.get()
    if PanDuan == "":
        t = TYZ.TongYinZi(JieGuo_MingLing)
        if t != "":
            JieGuo_MingLing = t
        else:
            JieGuo_MingLing = ChaZiDian(JieGuo_MingLing)
        print("查字典结果是：　"+JieGuo_MingLing)
    if JieGuo_MingLing != "":
        pool.terminate()
        if PanDuan != "":
            if " " in JieGuo_MingLing:
                JieGuo_MingLing = JieGuo_MingLing.replace(" ","")
            if JieGuo_MingLing =="对" or JieGuo_MingLing =="是" or JieGuo_MingLing =="嗯" or JieGuo_MingLing =="没错":
                if PanDuan == "shanchu?":
                    ZYGL.ShanChu()
                else:
                    ZYGL.DianBo(PanDuan)
                    MoShi[0] = False
                    Thread_BFQ = threading.Thread(target = BFQ.ZhiXing, args =(lambda : MoShi, "bf_dianbo"))
                    Thread_BFQ.start()
            else:
                print("未被确认，终止执行。")
                os.system(ZYGL.Shuo+ZYGL.DuiHua[25][0])
                
            PanDuan = ""
            continue    

        MingLing = ZiDian_MingLing[JieGuo_MingLing]
        if MingLing.find("bf",0,2) == 0:
            if MingLing == "bf_yinyue" or MingLing == "bf_shici" or MingLing == "bf_xiangsheng" or MingLing == "bf_jiangtan" or MingLing == "bf_langdu" or MingLing == "bf_pingshu" or MingLing == "bf_wusun" or MingLing == "bf_shunxu" or MingLing == "bf_shoucang" or MingLing == "bf_congtou" or MingLing == "bf_zhuanjixuhuan" or MingLing == "bf_shangzhuanji" or MingLing == "bf_xiazhuanji":
                MoShi[1:] = [False,False,False]
            elif MingLing == "bf_danqu":
                MoShi[1:] = [True,False,False]
            elif MingLing == "bf_suiji":
                MoShi[1:] = [False,True,False]
            elif MingLing == "bf_zhuanjixunhuan":
                MoShi[1:] = [False,False,True]
            elif (MingLing == "bf_shangyi" or MingLing == "bf_xiayi") and MoShi[2]:
                print("这个命令在随机模式下无效。")
                os.system(ZYGL.Shuo+ZYGL.DuiHua[13][0])
                continue
          
            # special satu for stopped threading but MoShi[0] is False
            if threading.active_count() == 1:
                MoShi[0] = True
                
            if MoShi[0]:
                if MingLing == "bf_ting":
                    continue
                MoShi[0] = False
                Thread_BFQ = threading.Thread(target = BFQ.ZhiXing, args =(lambda : MoShi, MingLing))
                Thread_BFQ.start()
            else:
                if MingLing == "bf_ting":
                    MoShi[0] = True
                    Thread_BFQ.join()
                elif MingLing == "bf_suiji" or MingLing == "bf_shangyi" or MingLing == "bf_xiayi" or MingLing == "bf_congtou" or MingLing == "bf_shangzhuanji" or MingLing == "bf_xiazhuanji":
                    MoShi[0] = True
                    Thread_BFQ.join()
                    MoShi[0] = False
                    Thread_BFQ = threading.Thread(target = BFQ.ZhiXing, args =(lambda : MoShi, MingLing))
                    Thread_BFQ.start()                        
                elif MingLing == "bf_yinyue" or MingLing == "bf_shici" or MingLing == "bf_xiangsheng" or MingLing == "bf_jiangtan" or MingLing == "bf_langdu" or MingLing == "bf_pingshu" or MingLing == "bf_wusun" or MingLing == "bf_shoucang":
                    with open(ZYGL.PZ_WenJian) as f:
                        lines = f.readlines()
                        for line in lines:
                            if line.find("MingLing") == 0:
                                if re.match(r'MingLing =(.*)(\n)?', line).group(1).strip(' ""') != MingLing:
                                    MoShi[0] = True
                                    Thread_BFQ.join()
                                    MoShi[0] = False
                                    Thread_BFQ = threading.Thread(target = BFQ.ZhiXing, args =(lambda : MoShi, MingLing))
                                    Thread_BFQ.start()
                                break

        elif MingLing == "guanji":
            if not MoShi[0]:
                MoShi[0] = True
                Thread_BFQ.join()
            os.system("shutdown -h now")
        elif MingLing.find("cx",0,2) == 0:
            HuiDa = ZYGL.ChaXun(MingLing)
            if HuiDa == "":
                continue
            if not MoShi[0]:
                MoShi[0] = True
                Thread_BFQ.join()
                print(HuiDa)
                os.system("python3 ../yy/bin/zhspeak.py "+HuiDa)
                MoShi[0] = False
                Thread_BFQ = threading.Thread(target = BFQ.ZhiXing, args =(lambda : MoShi, "bf_jixu"))
                Thread_BFQ.start()
            else:
                os.system("python3 ../yy/bin/zhspeak.py "+HuiDa)
        elif MingLing == "shoucang":
            ZYGL.ShouCang()                    
        elif MingLing.find("js",0,2) == 0:
            ZYGL.JianSuo(MingLing)
        elif MingLing.find("qk",0,2) == 0:
            ZYGL.QingKong(MingLing)
        elif MingLing == "zhongwen" or MingLing == "riyu" or MingLing == "yingyu":
            ZYGL.DuiHua, ZYGL.Shuo = ZYGL.YuYan(MingLing)
        elif MingLing == "fuzhi":
            os.system('python3 ../gongjv/tianjia.py')
        elif MingLing == "gengxin":
            os.system('python3 ../gongjv/gengxin.py')
        elif MingLing == "shengji":
            os.system('python3 ../gongjv/shengji.py')
            
    else:
        JieGuo_ZiRanYuYan = Thread_ZiRanYuYan.get()
        print("自然语言结果：　",JieGuo_ZiRanYuYan)
        if JieGuo_ZiRanYuYan != "":
            if not MoShi[0]:
                MoShi[0] = True
                Thread_BFQ.join()
            PanDuan = DuiBi(JieGuo_ZiRanYuYan)
        else:
            os.system(ZYGL.Shuo+choice(ZYGL.DuiHua[2][0].split()))
   

