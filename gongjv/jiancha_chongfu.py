words = "继 续 检 搜 索 全 部 无 损 听 歌 播 放 音 乐 停 止 诗 词 单 曲 专 辑 循 环 顺 序 随 相 声 评 书 讲 坛 朗 读 关 机 复 制 上 下 一 首 个 从 头 收 藏".split()

def check(words):
    for word in words:
        if words.count(word) > 1:
            print("reduplicative word is:",word)
            words.remove(word)
    print("finished!")
            
check(words)
