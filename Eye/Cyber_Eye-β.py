import discord

import datetime
import asyncio
import chardet
import subprocess
import sys


loop = asyncio.ProactorEventLoop()
client = discord.Client(loop=loop)
master = 441865412804870144


@client.event
async def on_ready():
    channel = client.get_channel(791952226225750017)
    
    await channel.send(f"{client.user.name} is ready.")
    await channel.send("Hi, Master.")

@client.event
async def on_message(message):
    #if message.author.bot():
        #return

    if message.content.startswith("ce/"):
        if message.author.id == master:
            cmdlist = message.content.strip("ce/").split()
            cmdstr = " ".join(cmdlist)
            print(cmdlist, cmdstr)
            repl = cmdstr.replace(" ", '", "')
            print(f'"{repl}",')

            process = await asyncio.create_subprocess_exec(
                (f'"{repl}"'),
                #"ping", "localhost", "-n", "1", これは動いた。
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                shell=False)

            stdout_data, stderr_data = await process.communicate()
            await message.channel.send(*(d.decode("cp932") for d in [stdout_data]))


client.run("NzkxOTQ3NzgwNDU3MTAzMzky.X-Wk2A.qurX71U3KPEFihgzlXye6tXG51Q")
