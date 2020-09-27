import os
import subprocess
import sys
import threading
from time import sleep
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('视频库清理助手 V0.1.2')
many = int(0)
quit1 = 0
wait1 = 0
continueY = 0
potONorOFF = 0
file_name = '0'
now_dir = '0'
now_name = 0
work_dir = tk.StringVar()
pot_dir = tk.StringVar()
pot_dir.set('C:\\"Program Files"\DAUM\PotPlayer\PotPlayerMini64.exe ')


def control():
    def wait_set():
        global wait1
        wait1 = 1

    def quit_set():
        global quit1
        global continueY

        control_window.destroy()
        if potONorOFF == 1:
            killedPotplayer()
        continueY = 1
        quit1 = 1

    def continue_set():
        global continueY
        continueY = 1

    control_window = tk.Tk()
    control_window.title('请选择是否保留')
    control_window.geometry('300x150')
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
    global potONorOFF

    potONorOFF = 1
    subprocess.call(pot_dir.get() + filename, shell=True)
    # os.system(pot_dir.get() + filename)
    potONorOFF = 0


def killedPotplayer():
    subprocess.call('taskkill /f /im PotPlayerMini64.exe', shell=True)
    #os.system('taskkill /f /im PotPlayerMini64.exe')


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

    for root, dirs, files in os.walk(work_dir.get()):
        now_dir = root
        for name in files:
            global many
            global file_name
            global now_name
            global wait1
            global continueY
            global quit1
            global continueY

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
                    continueY = 0
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
    work_dir.set(filedialog.askdirectory())


def set_pot_dir():
    global pot_dir
    pot_dir.set(filedialog.askopenfilename())


def quit():
    sys.exit()


set_dir_bt = tk.Button(root, text='设置工作目录', command=set_dir)
start_bt = tk.Button(root, text='开始筛选视频文件', command=find)
quit_bt = tk.Button(root, text='退出', command=quit)
set_pot_dir_bt = tk.Button(root, text='设置potplayer程序位置', command=set_pot_dir)

WorkDirPrint = tk.Label(root, textvariable=work_dir)
pot_dir_print = tk.Label(root, textvariable=pot_dir)

pot_dir_print.grid(row=0, column=1)
set_pot_dir_bt.grid(row=0, column=0)
set_dir_bt.grid(row=1, column=0)
WorkDirPrint.grid(row=1, column=1)
start_bt.grid(row=2, column=0)
quit_bt.grid(row=2, column=1)

root.mainloop()

# ===========================================================================================
