# Video-file-screening-assistant
A simple video file screening assistant. 帮助绅士筛选本地视频，减少开关文件夹，以及处理大量视频文件与相关字幕/视频信息文件的时间。

v0.1

已经勉强实现的功能：

1.指定文件夹

2.调用potplayer播放：mkv/mp4/avi 格式的视频

3.在第二窗口中，实现了删除功能按钮 （仅删除当前播放视频，以及同文件夹下与其同名且非’mkv''mp4''avi'后缀的文件）

存在的问题：
1.全是问题

显著的问题：

1.遍历视频播放过程中，如果需要退出，main.py会显示未响应，且继续遍历视频播放，需要强制关闭。

2.GUI
