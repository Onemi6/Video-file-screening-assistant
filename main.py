import os
import sys
import threading
from time import sleep
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('视频库清理助手 V0.1.0.1')
many = int(0)
quit1 = 0
wait1 = 0
continueY = 0
file_name = '0'
now_dir = '0'
now_name = 0


def control():
    def wait_set():
        global wait1
        wait1 = 1

    def quit_set():
        global quit1
        quit1 = 1
        control_window.destroy()
        killedPotplayer()

    def continue_set():
        global continueY
        continueY = 1

    control_window = tk.Tk()
    control_window.title('请选择是否保留')
    control_window.geometry('250x100')
    control_window.wm_attributes('-topmost', 1)

    delete_bt = tk.Button(control_window, text='删除此视频及同名文件', command=delete)
    quit_bt = tk.Button(control_window, text='停止筛选视频文件', command=quit_set)
    wait_bt = tk.Button(control_window, text='暂停视频筛选', command=wait_set)
    continue_bt = tk.Button(control_window, text='继续视频筛选', command=continue_set)

    delete_bt.pack()
    quit_bt.pack()
    wait_bt.pack()
    continue_bt.pack()

    control_window.mainloop()


def openPotplayer(filename):
    global work_dir
    global dont_dir
    global output_dir
    global many

    os.system('C:\\"Program Files"\DAUM\PotPlayer\PotPlayerMini64.exe ' + filename)


def killedPotplayer():
    os.system('taskkill /f /im PotPlayerMini64.exe')


def mv():
    pass


def delete():
    os.remove(file_name)
    for name in os.listdir(now_dir):
        if name.find(now_name[:-3]) != -1 and (name[-3:] != 'mkv' or name[-3:] != 'mp4' or name[-3:] != 'avi'):
            os.remove(str(now_dir) + '/' + str(name))

def find():
    global work_dir
    global now_dir

    control_run = threading.Thread(target=control)
    control_run.start()

    for root, dirs, files in os.walk(work_dir):
        now_dir = root
        for name in files:
            global many
            global file_name
            global now_name
            global wait1
            global continueY
            global quit1

            filename = os.path.join(root, name)
            if str(filename[-3:]) == 'mp4' or str(filename[-3:]) == 'mkv' or str(filename[-3:]) == 'avi':
                now_name = name
                file_name = filename
                openPotplayer(filename)
                many = many + 1
                if wait1 == 1:
                    while continueY == 0:
                        sleep(0.1)
                    wait1 = 0
            if quit1 == 1:
                break
        else:
            continue
        break
    sys.exit()


# 根据工作目录获取文件列表，是否遍历，等，获取文件目录
def set_dir():
    global WorkDirPrint
    global work_dir
    work_dir = filedialog.askdirectory()
    WorkDirPrint.insert(0, work_dir)


def quit():
    sys.exit()


set_dir_bt = tk.Button(root, text='设置工作目录', command=set_dir)
start_bt = tk.Button(root, text='开始筛选视频文件', command=find)
quit_bt = tk.Button(root, text='退出', command=quit)

WorkDirPrint = tk.Listbox(root)

set_dir_bt.grid(row=0, column=1)
WorkDirPrint.grid(row=0, column=0)
start_bt.grid(row=0, column=2)
quit_bt.grid(row=0, column=3)

root.mainloop()

# ===========================================================================================
