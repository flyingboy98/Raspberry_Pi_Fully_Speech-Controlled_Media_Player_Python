import os
import re
import sqlite3

SJK_DuiHua = "/home/pi/Documents/yuyinbofang/duihua.db"

SJK_DuiHua_LianJie = sqlite3.connect(SJK_DuiHua)
SJK_DuiHua_YouBiao = SJK_DuiHua_LianJie.cursor()
#SJK_DuiHua_YouBiao.execute('CREATE TABLE IF NOT EXISTS yuyan([XuHao] INTEGER PRIMARY KEY, [ZhongWen] text, [RiYu] text, [YingYu] text)')

def TianJia():
    while True:
        ZhongWen = input("请输入中文：")
        RiYu = input("请输入日语：")
        YingYu = input("请输入英语：")
        data = (ZhongWen, RiYu, YingYu)
        SJK_DuiHua_YouBiao.execute('INSERT INTO yuyan(ZhongWen, RiYu, YingYu) VALUES(?,?,?)', data)
        SJK_DuiHua_LianJie.commit()
        QueRen = input("是否继续添加(y/n)：")
        if QueRen == "y":
            continue
        else:
            SJK_DuiHua_LianJie.close()
            break
            
def XiuGai():
    while True:
        YuZhong = {"1":"ZhongWen","2":"RiYu","3":"YingYu"}
        key = input("中文1，日语2，英语3，请输入相应数字： ")
        num = input("请输入条目序号： ")
        SJK_DuiHua_YouBiao.execute('SELECT '+YuZhong[key]+' FROM yuyan WHERE XuHao='+num)
        data = SJK_DuiHua_YouBiao.fetchone()[0]
        print(data)
        QueRen = input("是否要修改(y/n)： ")
        if QueRen == "y":
            data = (input("请输入修改内容： "), )
            print("修改后内容为：\n\n",data)
            QueRen = input("\n是否正确(y/n)： ")
            if QueRen == "y":
                SJK_DuiHua_YouBiao.execute('UPDATE yuyan SET '+YuZhong[key]+'=? WHERE XuHao='+num,data)
                SJK_DuiHua_LianJie.commit()
                print("修改完毕！\n\n",)
                SJK_DuiHua_YouBiao.execute('SELECT '+YuZhong[key]+' FROM yuyan WHERE XuHao='+num)
                data = SJK_DuiHua_YouBiao.fetchone()[0]
                print(data,"\n")
                QueRen = input("是否继续修改(y/n)：")
                if QueRen == "y":
                    continue
                else:
                    SJK_DuiHua_LianJie.close()
                    break
            else:
                SJK_DuiHua_LianJie.close()
                break
        else:
            SJK_DuiHua_LianJie.close()
            break
#XiuGai()
#TianJia()