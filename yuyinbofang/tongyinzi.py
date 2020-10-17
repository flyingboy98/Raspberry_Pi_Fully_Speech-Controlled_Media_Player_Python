import re

def TongYinZi(JieGuo_ShiBie):
    tongyinzi = ""
    if re.search('听(.)*止', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('停(.)*制', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('听(.)*制', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('听(.)*诗', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('评(.)*止', JieGuo_ShiBie):
        tongyinzi = "停止"
    elif re.search('关(.)*继', JieGuo_ShiBie):
        tongyinzi = "关机"
    elif re.search('继(.)*曲', JieGuo_ShiBie):
        tongyinzi = "继续"
    elif re.search('机(.)*续', JieGuo_ShiBie):
        tongyinzi = "继续"
    elif re.search('辑(.)*续', JieGuo_ShiBie):
        tongyinzi = "继续"
    elif re.search('机(.)*曲', JieGuo_ShiBie):
        tongyinzi = "继续"
    elif re.search('顺(.)*续', JieGuo_ShiBie):
        tongyinzi = "顺序"
    elif re.search('随(.)*继', JieGuo_ShiBie):
        tongyinzi = "随机"
    elif re.search('一(.)*乐', JieGuo_ShiBie):
        tongyinzi = "音乐"
    elif re.search('上(.)*专(.)*机', JieGuo_ShiBie):
        tongyinzi = "上专辑"
    elif re.search('上(.)*专(.)*继', JieGuo_ShiBie):
        tongyinzi = "上专辑"
    elif re.search('下(.)*专(.)*机', JieGuo_ShiBie):
        tongyinzi = "下专辑"
    elif re.search('下(.)*专(.)*继', JieGuo_ShiBie):
        tongyinzi = "下专辑"
    elif re.search('索(.)*索(.)*全(.)*部', JieGuo_ShiBie):
        tongyinzi = "搜索全部"
    elif re.search('从(.)*读', JieGuo_ShiBie):
        tongyinzi = "从头"
    elif re.search('添(.)*加(.)*首(.)*藏', JieGuo_ShiBie):
        tongyinzi = "添加收藏"
    elif re.search('部(.)*放(.)*收(.)*藏', JieGuo_ShiBie):
        tongyinzi = "播放收藏"
    elif re.search('播(.)*放(.)*首(.)*藏', JieGuo_ShiBie):
        tongyinzi = "播放收藏"
    elif re.search('部(.)*放(.)*首(.)*藏', JieGuo_ShiBie):
        tongyinzi = "播放收藏"
    elif re.search('部(.)*放(.)*音(.)*乐', JieGuo_ShiBie):
        tongyinzi = "播放音乐"
    elif re.search('部(.)*放(.)*无(.)*损', JieGuo_ShiBie):
        tongyinzi = "播放无损"
    elif re.search('部(.)*放(.)*诗(.)*词', JieGuo_ShiBie):
        tongyinzi = "播放诗词"
    elif re.search('部(.)*放(.)*评(.)*书', JieGuo_ShiBie):
        tongyinzi = "播放评书"
    elif re.search('部(.)*放(.)*朗(.)*读', JieGuo_ShiBie):
        tongyinzi = "播放朗读"
    elif re.search('专(.)*机(.)*循(.)*环', JieGuo_ShiBie):
        tongyinzi = "专辑循环"
    elif re.search('专(.)*继(.)*循(.)*环', JieGuo_ShiBie):
        tongyinzi = "专辑循环"
    elif re.search('升(.)*继', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('升(.)*机', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('升(.)*辑', JieGuo_ShiBie):
        tongyinzi = "升级"
    elif re.search('歌(.)*新', JieGuo_ShiBie):
        tongyinzi = "更新"
        
    return tongyinzi