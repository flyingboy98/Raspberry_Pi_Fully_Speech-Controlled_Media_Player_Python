import sqlite3

SJK_DuiHua = "/home/pi/Documents/yuyinbofang/duihua.db"
SJK_LianJie = sqlite3.connect(SJK_DuiHua)
SJK_YouBiao = SJK_LianJie.cursor()
SJK_YouBiao.execute('DROP TABLE IF EXISTS hanzi')
SJK_LianJie.commit()
SJK_YouBiao.execute('CREATE TABLE IF NOT EXISTS hanzi([HanZi] text, [PinYin] text, [WuBi] text, [BiHuaShu] integer)')
SJK_LianJie.commit()

data = []
with open('hanzibianma_utf8.txt') as f:
    lines = f.readlines()
for line in lines:
    tp = (line.split()[0], line.split()[1], line.split()[2], line.split()[6])
    data.append(tp)
    
SJK_YouBiao.executemany('INSERT INTO hanzi VALUES (?,?,?,?)', data)
SJK_LianJie.commit()
SJK_LianJie.close()
