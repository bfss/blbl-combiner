# blbl-combiner
Combine bilibili audio and video

合并手机哔哩哔哩缓存的音视频文件

哔哩哔哩在安卓手机的缓存目录为：

Android/data/tv.danmaku.bili/download

一个缓存好的视频目录结构如下

* download
  * av号
    * 1p
      * 视频类型
        * audio.m4s
        * index.json
        * video.m4s
      * danmaku.xml
      * entry.json
   
将整个download文件夹复制到项目的download文件夹中，运行combiner.py

即可在output文件夹获得合并好的文件