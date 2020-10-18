#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
from time import sleep
import RPi.GPIO as GPIO
import speech_recognition as sr
import threading
import sqlite3
import json
import os
import re
import bofangqi as BFQ
import tongyinzi as TYZ
import ziyuanguanli as ZYGL


def LuYin():
    YuYinLuZhi = sr.Recognizer()
    if MingLing == "":os.system(ZYGL.Shuo+ZYGL.DuiHua[0][0])
    print("start Listening ...")
    with sr.Microphone(device_index = 1, sample_rate = 16000, chunk_size = 512) as source:
               YuYinLuZhi.adjust_for_ambient_noise(source)
               audio = YuYinLuZhi.listen(source)
    with open("yuyin.wav", "wb") as f:
        f.write(audio.get_wav_data())
        os.system(ZYGL.Shuo+ZYGL.DuiHua[1][0])
        
def ShiBie():
    wenben = ""
    model = Model("model")
    rec = KaldiRecognizer(model, 16000, "继 续 检 搜 索 全 部 无 损 播 放 音 乐 停 止 诗 词 单 曲 专 辑 循 环 顺 序 随 评 书 朗 读 关 机 复 制 上 下 一 首 个 从 头 添 加 收 藏 中 文 日 语 英 更 新 升 级")
    WaveWenJian = open("yuyin.wav", "rb")
    WaveWenJian.read(44)
    while True:
        data = WaveWenJian.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            wenben = res['text']

    res = json.loads(rec.FinalResult())
    
    if wenben == "":
        wenben = res['text']

    return wenben
    
def ChaZiDian(data):
    for key in ZiDian_MingLing:
        words = list(key)
        check_word = []
        for word in words:
            if word in data:
                check_word.append(word)
        if check_word == words:
            return "".join(words)
            break
    return ""    

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN)
os.chdir('/home/pi/Documents/yuyinbofang')

MingLing = ""
ZiDian_MingLing = {
    "播放音乐":"bf_yinyue",
    "播放无损":"bf_wusun",
    "播放诗词":"bf_shici",
    "播放评书":"bf_pingshu",
    "播放朗读":"bf_langdu",
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
    "搜索评书":"js_pingshu",
    "搜索朗读":"js_langdu",
    "添加收藏":"shoucang",
    "复制":"fuzhi",
    "关机":"guanji",
    "中文":"zhongwen",
    "日语":"riyu",
    "英语":"yingyu",
    "更新":"gengxin",
    "升级":"shengji"
    }

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
    JieGuo_ShiBie = ShiBie()
    if TYZ.TongYinZi(JieGuo_ShiBie) != "":
        JieGuo_ChaZiDian = TYZ.TongYinZi(JieGuo_ShiBie)
    else:
        JieGuo_ChaZiDian = ChaZiDian(JieGuo_ShiBie)
    print("命令是：　"+JieGuo_ChaZiDian)
    if JieGuo_ChaZiDian == "":
        os.system(ZYGL.Shuo+ZYGL.DuiHua[2][0])
    else:
        MingLing = ZiDian_MingLing[JieGuo_ChaZiDian]
        if MingLing.find("bf",0,2) == 0:
            if MingLing == "bf_yinyue" or MingLing == "bf_shici" or MingLing == "bf_langdu" or MingLing == "bf_pingshu" or MingLing == "bf_wusun" or MingLing == "bf_shunxu" or MingLing == "bf_shoucang" or MingLing == "bf_congtou" or MingLing == "bf_zhuanjixuhuan" or MingLing == "bf_shangzhuanji" or MingLing == "bf_xiazhuanji":
                MoShi[1:4] = [False,False,False]
            elif MingLing == "bf_danqu":
                MoShi[1:4] = [True,False,False]
            elif MingLing == "bf_suiji":
                MoShi[1:4] = [False,True,False]
            elif MingLing == "bf_zhuanjixunhuan":
                MoShi[1:4] = [False,False,True]
            elif (MingLing == "bf_shangyi" or MingLing == "bf_xiayi") and MoShi[2]:
                print("这个命令在随机模式下无效。")
                os.system(ZYGL.Shuo+ZYGL.DuiHua[13][0])
                continue

            if threading.active_count() == 1:
                MoShi[0] = True
                
            if MoShi[0]:
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
                elif MingLing == "bf_yinyue" or MingLing == "bf_shici" or MingLing == "bf_langdu" or MingLing == "bf_pingshu" or MingLing == "bf_wusun" or MingLing == "bf_shoucang":
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
        elif MingLing == "shoucang":
            ZYGL.ShouCang()                    
        elif MingLing.find("js",0,2) == 0:
            ZYGL.JianSuo(MingLing)
        elif MingLing == "zhongwen" or MingLing == "riyu" or MingLing == "yingyu":
            ZYGL.DuiHua, ZYGL.Shuo = ZYGL.YuYan(MingLing)
        elif MingLing == "fuzhi":
            os.system('python3 ../gongjv/tianjia.py')
        elif MingLing == "gengxin":
            os.system('python3 ../gongjv/gengxin.py')
        elif MingLing == "shengji":
            os.system('python3 ../gongjv/shengji.py')
   
