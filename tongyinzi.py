import re

def TongYinZi(JieGuo_ShiBie):
    tongyinzi = ""
    if re.search('听(.){1,3}止', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('停(.){1,3}制', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('听(.){1,3}制', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('评(.){1,3}止', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('评(.){1,3}制', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('关(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "关机"
    elif re.search('关(.){1,3}的', JieGuo_ShiBie):
        tongyinzi = "关机"
    elif re.search('继(.){1,3}曲', JieGuo_ShiBie):
        tongyinzi = "继续"
    elif re.search('机(.){1,3}续', JieGuo_ShiBie):
        tongyinzi = "继续"
    elif re.search('辑(.){1,3}续', JieGuo_ShiBie):
        tongyinzi = "继续"
    elif re.search('机(.){1,3}曲', JieGuo_ShiBie):
        tongyinzi = "继续"
    elif re.search('顺(.){1,3}续', JieGuo_ShiBie):
        tongyinzi = "顺序"
    elif re.search('顺(.){1,3}语', JieGuo_ShiBie):
        tongyinzi = "顺序"
    elif re.search('顺(.){1,3}曲', JieGuo_ShiBie):
        tongyinzi = "顺序"
    elif re.search('随(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "随机"
    elif re.search('一(.){1,3}乐', JieGuo_ShiBie):
        tongyinzi = "音乐"
    elif re.search('相(.){1,3}一', JieGuo_ShiBie):
        tongyinzi = "下一"
    elif re.search('停(.){1,3}歌', JieGuo_ShiBie):
        tongyinzi = "听歌"
    elif re.search('停(.){1,3}音(.){1,3}语', JieGuo_ShiBie):
        tongyinzi = "听音乐"
    elif re.search('听(.){1,3}音(.){1,3}语', JieGuo_ShiBie):
        tongyinzi = "听音乐"
    elif re.search('停(.){1,3}音(.){1,3}乐', JieGuo_ShiBie):
        tongyinzi = "听音乐"
    elif re.search('停(.){1,3}无(.){1,3}损', JieGuo_ShiBie):
        tongyinzi = "听无损"
    elif re.search('停(.){1,3}诗(.){1,3}词', JieGuo_ShiBie):
        tongyinzi = "听诗词"
    elif re.search('停(.){1,3}什(.){1,3}词', JieGuo_ShiBie):
        tongyinzi = "听诗词"
    elif re.search('听(.){1,3}什(.){1,3}词', JieGuo_ShiBie):
        tongyinzi = "听诗词"
    elif re.search('停(.){1,3}相(.){1,3}声', JieGuo_ShiBie):
        tongyinzi = "听相声"
    elif re.search('停(.){1,3}相(.){1,3}上', JieGuo_ShiBie):
        tongyinzi = "听相声"
    elif re.search('停(.){1,3}相(.){1,3}顺', JieGuo_ShiBie):
        tongyinzi = "听相声"
    elif re.search('停(.){1,3}相(.){1,3}单', JieGuo_ShiBie):
        tongyinzi = "听相声"
    elif re.search('听(.){1,3}相(.){1,3}上', JieGuo_ShiBie):
        tongyinzi = "听相声"
    elif re.search('听(.){1,3}相(.){1,3}顺', JieGuo_ShiBie):
        tongyinzi = "听相声"
    elif re.search('听(.){1,3}相(.){1,3}单', JieGuo_ShiBie):
        tongyinzi = "听相声"
    elif re.search('听(.){1,3}评(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "听评书"
    elif re.search('听(.){1,3}停(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "听评书"
    elif re.search('听(.){1,3}停(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "听评书"
    elif re.search('停(.){1,3}评(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "听评书"
    elif re.search('停(.){1,3}停(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "听评书"
    elif re.search('停(.){1,3}评(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "听评书"
    elif re.search('停(.){1,3}讲(.){1,3}坛', JieGuo_ShiBie):
        tongyinzi = "听讲坛"
    elif re.search('听(.){1,3}朗(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "听朗读"
    elif re.search('停(.){1,3}朗(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "听朗读"
    elif re.search('停(.){1,3}朗(.){1,3}读', JieGuo_ShiBie):
        tongyinzi = "听朗读"
    elif re.search('停(.){1,3}朗(.){1,3}的', JieGuo_ShiBie):
        tongyinzi = "听朗读"
    elif re.search('听(.){1,3}朗(.){1,3}的', JieGuo_ShiBie):
        tongyinzi = "听朗读"
    elif re.search('放(.){1,3}音(.){1,3}语', JieGuo_ShiBie):
        tongyinzi = "放音乐"
    elif re.search('放(.){1,3}朗(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "放朗读"
    elif re.search('放(.){1,3}朗(.){1,3}的', JieGuo_ShiBie):
        tongyinzi = "放朗读"
    elif re.search('放(.){1,3}评(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "放评书"
    elif re.search('放(.){1,3}停(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "放评书"
    elif re.search('放(.){1,3}相(.){1,3}单', JieGuo_ShiBie):
        tongyinzi = "放相声"
    elif re.search('放(.){1,3}相(.){1,3}上', JieGuo_ShiBie):
        tongyinzi = "放相声"
    elif re.search('放(.){1,3}相(.){1,3}顺', JieGuo_ShiBie):
        tongyinzi = "放相声"
    elif re.search('放(.){1,3}什(.){1,3}词', JieGuo_ShiBie):
        tongyinzi = "放诗词"
    elif re.search('上(.){1,3}专(.){1,3}机', JieGuo_ShiBie):
        tongyinzi = "上专辑"
    elif re.search('上(.){1,3}专(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "上专辑"
    elif re.search('下(.){1,3}专(.){1,3}机', JieGuo_ShiBie):
        tongyinzi = "下专辑"
    elif re.search('下(.){1,3}专(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "下专辑"
    elif re.search('专(.){1,3}继(.){1,3}名', JieGuo_ShiBie):
        tongyinzi = "专辑名"
    elif re.search('专(.){1,3}机(.){1,3}名', JieGuo_ShiBie):
        tongyinzi = "专辑名"
    elif re.search('讲(.){1,3}什(.){1,3}么', JieGuo_ShiBie):
        tongyinzi = "叫什么"
    elif re.search('什(.){1,3}么(.){1,3}什', JieGuo_ShiBie):
        tongyinzi = "什么诗"
    elif re.search('什(.){1,3}么(.){1,3}相(.){1,3}顺', JieGuo_ShiBie):
        tongyinzi = "什么相声"
    elif re.search('什(.){1,3}么(.){1,3}相(.){1,3}上', JieGuo_ShiBie):
        tongyinzi = "什么相声"
    elif re.search('什(.){1,3}么(.){1,3}相(.){1,3}单', JieGuo_ShiBie):
        tongyinzi = "什么相声"
    elif re.search('什(.){1,3}么(.){1,3}停(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "什么评书"
    elif re.search('什(.){1,3}么(.){1,3}停(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "什么评书"
    elif re.search('什(.){1,3}么(.){1,3}评(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "什么评书"
    elif re.search('什(.){1,3}么(.){1,3}专(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "什么专辑"
    elif re.search('什(.){1,3}么(.){1,3}专(.){1,3}机', JieGuo_ShiBie):
        tongyinzi = "什么专辑"
    elif re.search('复(.){1,3}少(.){1,3}他', JieGuo_ShiBie):
        tongyinzi = "多少他"
    elif re.search('读(.){1,3}少(.){1,3}他', JieGuo_ShiBie):
        tongyinzi = "多少他"
    elif re.search('他(.){1,3}复(.){1,3}少', JieGuo_ShiBie):
        tongyinzi = "他多少"
    elif re.search('他(.){1,3}读(.){1,3}少', JieGuo_ShiBie):
        tongyinzi = "他多少"
    elif re.search('复(.){1,3}少(.){1,3}专(.){1,3}机', JieGuo_ShiBie):
        tongyinzi = "多少专辑"
    elif re.search('多(.){1,3}少(.){1,3}专(.){1,3}机', JieGuo_ShiBie):
        tongyinzi = "多少专辑"
    elif re.search('多(.){1,3}少(.){1,3}专(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "多少专辑"
    elif re.search('读(.){1,3}少(.){1,3}专(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "多少专辑"
    elif re.search('复(.){1,3}少(.){1,3}专(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "多少专辑"
    elif re.search('读(.){1,3}少(.){1,3}专(.){1,3}机', JieGuo_ShiBie):
        tongyinzi = "多少专辑"
    elif re.search('专(.){1,3}机(.){1,3}循(.){1,3}环', JieGuo_ShiBie):
        tongyinzi = "专辑循环"
    elif re.search('专(.){1,3}继(.){1,3}循(.){1,3}环', JieGuo_ShiBie):
        tongyinzi = "专辑循环"
    elif re.search('索(.){1,3}索(.){1,3}全(.){1,3}部', JieGuo_ShiBie):
        tongyinzi = "搜索全部"
    elif re.search('索(.){1,3}索(.){1,3}音(.){1,3}乐', JieGuo_ShiBie):
        tongyinzi = "搜索音乐"
    elif re.search('索(.){1,3}索(.){1,3}无(.){1,3}损', JieGuo_ShiBie):
        tongyinzi = "搜索无损"
    elif re.search('索(.){1,3}索(.){1,3}诗(.){1,3}词', JieGuo_ShiBie):
        tongyinzi = "搜索诗词"
    elif re.search('索(.){1,3}索(.){1,3}什(.){1,3}词', JieGuo_ShiBie):
        tongyinzi = "搜索诗词"
    elif re.search('搜(.){1,3}索(.){1,3}什(.){1,3}词', JieGuo_ShiBie):
        tongyinzi = "搜索诗词"
    elif re.search('搜(.){1,3}索(.){1,3}相(.){1,3}单', JieGuo_ShiBie):
        tongyinzi = "搜索相声"
    elif re.search('搜(.){1,3}索(.){1,3}相(.){1,3}上', JieGuo_ShiBie):
        tongyinzi = "搜索相声"
    elif re.search('索(.){1,3}索(.){1,3}相(.){1,3}声', JieGuo_ShiBie):
        tongyinzi = "搜索相声"
    elif re.search('索(.){1,3}索(.){1,3}相(.){1,3}单', JieGuo_ShiBie):
        tongyinzi = "搜索相声"
    elif re.search('索(.){1,3}索(.){1,3}相(.){1,3}上', JieGuo_ShiBie):
        tongyinzi = "搜索相声"
    elif re.search('索(.){1,3}索(.){1,3}评(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "搜索评书"
    elif re.search('索(.){1,3}索(.){1,3}评(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "搜索评书"
    elif re.search('索(.){1,3}索(.){1,3}停(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "搜索评书"
    elif re.search('索(.){1,3}索(.){1,3}停(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "搜索评书"
    elif re.search('搜(.){1,3}索(.){1,3}停(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "搜索评书"
    elif re.search('搜(.){1,3}索(.){1,3}评(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "搜索评书"
    elif re.search('搜(.){1,3}索(.){1,3}停(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "搜索评书"
    elif re.search('索(.){1,3}索(.){1,3}讲(.){1,3}坛', JieGuo_ShiBie):
        tongyinzi = "搜索讲坛"
    elif re.search('索(.){1,3}索(.){1,3}朗(.){1,3}读', JieGuo_ShiBie):
        tongyinzi = "搜索朗读"
    elif re.search('索(.){1,3}索(.){1,3}朗(.){1,3}的', JieGuo_ShiBie):
        tongyinzi = "搜索朗读"
    elif re.search('搜(.){1,3}索(.){1,3}朗(.){1,3}的', JieGuo_ShiBie):
        tongyinzi = "搜索朗读"
    elif re.search('从(.){1,3}读', JieGuo_ShiBie):
        tongyinzi = "从头"
    elif re.search('哪(.){1,3}上', JieGuo_ShiBie):
        tongyinzi = "哪唱"
    elif re.search('添(.){1,3}加(.){1,3}首(.){1,3}藏', JieGuo_ShiBie):
        tongyinzi = "添加收藏"
    elif re.search('添(.){1,3}加(.){1,3}少(.){1,3}藏', JieGuo_ShiBie):
        tongyinzi = "添加收藏"
    elif re.search('添(.){1,3}加(.){1,3}收(.){1,3}唱', JieGuo_ShiBie):
        tongyinzi = "添加收藏"
    elif re.search('部(.){1,3}放(.){1,3}收(.){1,3}藏', JieGuo_ShiBie):
        tongyinzi = "播放收藏"
    elif re.search('播(.){1,3}放(.){1,3}首(.){1,3}藏', JieGuo_ShiBie):
        tongyinzi = "播放收藏"
    elif re.search('部(.){1,3}放(.){1,3}首(.){1,3}藏', JieGuo_ShiBie):
        tongyinzi = "播放收藏"
    elif re.search('部(.){1,3}放(.){1,3}少(.){1,3}藏', JieGuo_ShiBie):
        tongyinzi = "播放收藏"
    elif re.search('部(.){1,3}放(.){1,3}收(.){1,3}唱', JieGuo_ShiBie):
        tongyinzi = "播放收藏"
    elif re.search('专(.){1,3}机(.){1,3}循(.){1,3}环', JieGuo_ShiBie):
        tongyinzi = "专辑循环"
    elif re.search('专(.){1,3}继(.){1,3}循(.){1,3}环', JieGuo_ShiBie):
        tongyinzi = "专辑循环"
    elif re.search('清(.){1,3}空(.){1,3}相(.){1,3}单', JieGuo_ShiBie):
        tongyinzi = "清空相声"
    elif re.search('清(.){1,3}复(.){1,3}相(.){1,3}单', JieGuo_ShiBie):
        tongyinzi = "清空相声"
    elif re.search('清(.){1,3}空(.){1,3}相(.){1,3}上', JieGuo_ShiBie):
        tongyinzi = "清空相声"
    elif re.search('清(.){1,3}复(.){1,3}相(.){1,3}上', JieGuo_ShiBie):
        tongyinzi = "清空相声"
    elif re.search('清(.){1,3}空(.){1,3}停(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "清空评书"
    elif re.search('清(.){1,3}复(.){1,3}停(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "清空评书"
    elif re.search('清(.){1,3}空(.){1,3}停(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "清空评书"
    elif re.search('清(.){1,3}复(.){1,3}停(.){1,3}书', JieGuo_ShiBie):
        tongyinzi = "清空评书"
    elif re.search('清(.){1,3}空(.){1,3}评(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "清空评书"
    elif re.search('清(.){1,3}复(.){1,3}评(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "清空评书"
    elif re.search('清(.){1,3}空(.){1,3}朗(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "清空朗读"
    elif re.search('清(.){1,3}复(.){1,3}朗(.){1,3}复', JieGuo_ShiBie):
        tongyinzi = "清空朗读"
    elif re.search('清(.){1,3}空(.){1,3}朗(.){1,3}的', JieGuo_ShiBie):
        tongyinzi = "清空朗读"
    elif re.search('清(.){1,3}复(.){1,3}朗(.){1,3}的', JieGuo_ShiBie):
        tongyinzi = "清空朗读"
    elif re.search('清(.){1,3}空(.){1,3}朗(.){1,3}部', JieGuo_ShiBie):
        tongyinzi = "清空朗读"
    elif re.search('清(.){1,3}复(.){1,3}朗(.){1,3}部', JieGuo_ShiBie):
        tongyinzi = "清空朗读"
    elif re.search('升(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('升(.){1,3}机', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('升(.){1,3}辑', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('声(.){1,3}辑', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('声(.){1,3}级', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('声(.){1,3}机', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('声(.){1,3}继', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('更(.){1,3}曲', JieGuo_ShiBie):
        tongyinzi = "单曲"
    elif re.search('歌(.){1,3}新', JieGuo_ShiBie):
        tongyinzi = "更新"
    elif re.search('顺(.){1,3}曲', JieGuo_ShiBie):
        tongyinzi = "顺序"
        
    return tongyinzi