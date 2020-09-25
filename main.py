import os
import tkinter as tk

root = tk.Tk
root.title('视频库清理助手 V0.1')

control_window = tk.Tk
control_window.title('请选择是否保留')
control_window.wm_attributes('-topmost', 1)

work_dir = []
dont_dir = []
output_dir = []
many = int(0)


def openPotplayer(filename):
    global work_dir
    global dont_dir
    global output_dir
    global many

    os.system('C:\\"Program Files"\DAUM\PotPlayer\PotPlayerMini64.exe ' + filename)


def killedPotplayer():
    pass


def mv():
    pass


def delete():
    pass


def main():
    # 根据工作目录获取文件列表，是否遍历，等，获取文件目录
    # 先处理工作目录下的
    global many
    file_list = os.listdir(work_dir)

    for root,dirs,files in os.walk(file_list)
        for name in files:
            global many
            filename = os.join(root,name)
            if filename[-3,] == 'mp4' & filename[-3] == 'mkv' & filename[-3,] == 'avi':
                openPotplayer(filename)
                control_window.mainloop()
                many = many + 1


#  for filename in file_list:
#     if os.path.isfile(os.path.join(work_dir, filename)):
#        if filename[-3,] == 'mp4' & filename[-3,] == 'mkv':
#                openPotplayer(filename)
#               control_window.mainloop()
#                many = many + 1
