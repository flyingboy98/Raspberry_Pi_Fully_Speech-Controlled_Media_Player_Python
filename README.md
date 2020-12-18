　　树莓派全语音控制媒体播放器(Fully Speech-Controlled Media Player)



主要特点：

　　＊全程无外设操作。可以在无鼠标键盘显示器等外设的情况下(Headless)，完全通过麦克风输入语音命令来控制媒体播放。从导入媒体文件，播放，查询，停止，到关机全程语音控制。

　　＊通过硬件开关控制语音输入。

　　＊同音字处理，提高命令识别率。

　　＊分类媒体播放。音乐，诗词，有声读物，评书，相声，讲坛等各类资源分别播放。

　　＊分类媒体检索。可以一次性检索全部各类媒体，也可以分类检索。

　　＊可选择输出设备，3.5mm耳机插孔和HDMI切换。

　　＊断点续播。系统启动后自动继续上次的播放，每次停止后继续播放也是从上次停止的时间点开始。

　　＊添加收藏。可以把喜欢的媒体添加到收藏，集中播放。

　　＊除基本的上下曲选择，单曲，随机，顺序播放模式外，还可以选择上下专辑和专辑
循环模式。新增加点播模式，可按人名或作品名称点播。

　　＊语音命令列表：分为特定字符识别和自然语言识别两部分。详见mingling_liebiao文件。

　　＊特定字符命令为模糊识别，即只要包含关键字即可。例如想播放上一首歌可以说＂上一首＂，＂上一曲＂，＂上一个＂，＂播放上一首＂等，但多余字符与关键字符的距离不能超过两个字。自然语言被识别后会反问确认，可回答“是|对|没错”确认，其它内容则被认为否认，将终止执行。



硬件环境：

　　＊Raspberry Pi 3，4测试通过。

　　＊USB麦克风一个。

　　＊按键开关一个。用于硬件控制语音输入，可用两根排线代替。



软件环境：

　　＊系统RaspberryPi OS 10(Buster) with desktop(2020-05-27)。64位系统没有omxplayer，用mplayer代替测试有问题。

　　＊语音录制采用sphinx的speech_recognition模块。也可用arecord加参数设置录制时间，格式，码率的方式。

　　＊语音识别采用vosk。目前只做了对汉语普通话的识别，vosk本身支持多种语言识别。

　　＊数据库采用sqlite3。用于管理媒体资源和系统语音提示。

　　＊系统语音提示TTS(text-to-speech)采用余音ekho(汉语), open-JTalk(日语)和espeak(英语)三种语言，可选择。

　　＊媒体播放采用omxplayer，aplay和mplayer，分别用于不同场景的媒体播放。



安装步骤：

　　＊按键开关的两根线连接到Pi上的GPIO 2(BCM)和任一接地(Ground)。

　　＊默认系统用户pi，系统更新：

　　　sudo update

　　　sudo upgrade

　　＊安装相关软件及依赖：

　　　sudo apt install python-pip python3-pip python-pyaudio python3-pyaudio pulseaudio libpulse-dev libgfortran3 libgfortran3-armhf-cross libportaudio2 libvdpau-dev libmagic-dev mplayer espeak
   
　　　sudo usermod -aG gpio pi

　　　sudo usermod -aG audio pi
   

　　　升级pip并安装相关模块：为实现"headless"(无外设)，要用systemctl使系统启动后自动进入后台守护进程(daemon)，"pip3 install"前必须加"sudo"！如果连接外设手动启动程序，可以不加。如果用pip3安装太慢可以到PyPI手动下载安装。

　　　sudo -H pip3 install --upgrade pip

　　　sudo pip3 install RPi.GPIO

　　　sudo pip3 install PyAudio

　　　sudo pip3 install pyttsx3



　　　安装sphinx：

　　　sudo pip install SpeechRecognition



　　　安装本软件和vosk:

　　　cd /home/pi/Documents

　　　git clone https://github.com/flyingboy98/Raspberry_Pi_Fully_Speech-Controlled_Media_Player_Python.git

　　　mv Raspberry_Pi_Fully_Speech-Controlled_Media_Player_Python/ yuyinbofang/

　　　mv ./yuyinbofang/gongjv ./

　　　wget -O yy.zip https://github.com/flyingboy98/Ekho_Mandarin_Only/raw/main/yy.zip

　　　unzip yy.zip

　　　sudo rm yy.zip

　　　下载vosk和中文model：

　　　sudo pip3 install vosk

　　　cd yuyinbofang/

　　　wget -O vosk-model-small-cn-0.3.zip http://alphacephei.com/vosk/models/vosk-model-small-cn-0.3.zip

　　　unzip vosk-model-small-cn-0.3.zip

　　　mv vosk-model-small-cn-0.3/ model/

　　　rm vosk-model-small-cn-0.3.zip

　　　mkdir tmp

　　　mkdir /home/pi/Music/mp3 /home/pi/Music/wav

　　　mkdir /home/pi/Music/mp3/shici /home/pi/Music/mp3/yinyue /home/pi/Music/mp3/pingshu /home/pi/Music/mp3/langdu

　　　chmod 755 echo

　　　chown -R pi:pi /home/pi/Documents

　　　chown -R pi:pi /home/pi/Music

　　　cd ~


　　　yy文件夹是经过简化处理的余音(ekho)，只保留了汉语普通话。如果需要其它语言可在余音官网下载完整版(www.eguidedog.net/cn/ekho_cn.php)。


　　　安装open-JTalk:

　　　sudo apt install open-jtalk open-jtalk-mecab-naist-jdic

　　　sudo mkdir /usr/share/hts-voice/

　　　cd /usr/share/hts-voice/

　　　sudo git clone https://github.com/icn-lab/htsvoice-tohoku-f01.git

　　　cd ~


　　＊全部安装完成后/home/pi/Documents下应该包含yuyinbofang，gongjv，yy三个并列的文件夹。yuyinbofang文件夹下应该包括model，tmp两个子文件夹和bofangqi.py，duihua.db，echo，tongyinzi.py，zhukong.py，ziyuanguanli.py，wannianli.py等文件。


使用方法：

　　＊准备媒体文件：

　　　！！！媒体文件名格式：人名 - 文件名.扩展名

　　　文件名中间的空格和横杠都是英文半角字符。文件名中如果有圆括号，也必须是半角字符且要放在最后，也就是说括号后就是".扩展名"，不能再有其它任何字符！

　　　请务必按以上格式修改文件名，否则无法导入！

　　　全部修改完文件名后，用gongjv文件夹下的jiancha_mingcheng.py检查有无错误。方法是启动文件后，手动输入要检查的文件夹路径(input)。如果提示有错误，具体查看媒体文件夹下生成的文件xiugai.txt，并再次修改。



　　＊媒体文件拷贝到USB存储设备：这步适用于语音命令＂复制＂自动拷贝，手动拷贝可省略。

　　　在USB存储设备上建立文件夹Music(注意大写)，然后在Music下建立mp3和wav两个子文件夹，再在mp3下建立yinyue，shici, langdu，pingshu四个子文件夹。把准备好的媒体文件分类拷贝到各个文件夹中。



　　＊从存储卡拷贝媒体文件到Pi：手动拷贝省略。

　　　启动yuyinbofang/zhukong.py，打开语音开关，等待语音提示说完。输入语音命令＂复制＂。听到＂好的＂语音提示后关闭开关。如果识别有误，再次输入语音命令。

　　　对于Pi 3A+，因为只有一个USB口，复制媒体，更新，升级这类需要接入U盘的动作，在命令发出后有十五秒的时间拔下麦克风，插入U盘并识别。

　　　对于Pi 3B/4B，如果不想等待十五秒钟，可以删除或注释掉gongjv文件夹下的gengxin.py，shengji.py和tianjia.py三个文件头部的"sleep(15)"语句。

　　　完成后语音提示添加完成，可以取下U盘了。



　　＊检索媒体：使用命令＂搜索全部＂或其它分类检索命令。等待语音提示完成检索。在Pi 3A+上检索7000个媒体文件大概需要三十秒。



　　＊至此，已完成所有准备工作，可以正常使用了。




目前问题：

　　＊首次运行建议连接外设，出现问题便于处理。
  
　　＊vosk经常警告(warning)内存问题，会卡住十几到几十秒的时间。如长时间无反应需要重启。
  
　　＊打开语音开关后要等待三到五秒加载录音模块。系统启动后只有初次输入语音命令前有语音提示＂有事您说话＂，之后没有这个提示。有没有提示都要等待三到五秒。

　　＊由于发音，周围环境，输入时机和麦克质量的关系，命令识别会有错误发生。
  
  
  

设置开机自启动：

　　＊系统音频设置：

　　　sudo vi /usr/share/alsa/alsa.conf
   
　　　修改defaults.pcm.card 0 的值为2

　　　修改defaults.pcm.subdevice -1 的值为0
     
　　　建立文件：
     
　　　sudo vi /etc/alsa/asound.conf
     
　　　添加下列内容：
     
     pcm.!default {
     
       type asym
       
       playback.pcm
       
       {
       
         type hw
         
         card 1
         
         device 0
         
       }
       
     }
     
     
　　＊建立自启动服务：
  
　　　sudo systemctl edit --force --full yuyinbofang

　　　添加下列内容：

　　　[Unit]

　　　Description=yuyinbofang

　　　After=multi-user.target


　　　[Service]

　　　WorkingDirectory=/home/pi/Documents/yuyinbofang

　　　ExecStart=/usr/bin/python3 zhukong.py


　　　[Install]

　　　WantedBy=multi-user.target

　　　Ctrl-x，"Y"保存退出。


　　　启动服务：调试无误后再启动。

　　　sudo systemctl daemon-reload

　　　sudo systemctl enable yuyinbofang.service

　　　临时停止服务：

　　　sudo systemctl stop yuyinbofang.service

　　　终止服务：

　　　sudo systemctl disable yuyinbofang.service





完整系统映像压缩包(Pi 3/4适用)：

　　＊链接: https://pan.baidu.com/s/1AHgMTt2HKm0RcD47uLf-Zg 提取码: 9wbe
  
　　＊无密码，解压后映像文件大小：7969177600字节。
  
　　＊映像系统包括本软件和四轮驱动小车(https://github.com/flyingboy98/Raspberry_Pi_4WD_Cart_With_Voice_Broadcast_Controlled_Via_VNC_Python_Opencv.git)。
  
　　＊映像中的文件为旧版本，删除后按上述安装方式安装新版本即可。



