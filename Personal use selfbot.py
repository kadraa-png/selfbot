import discord
from discord.ext import commands
import pyautogui
import keyboard
import PIL
import os
import cv2
import numpy as np
from discord.ext import tasks
import discord_webhook
from discord_webhook import DiscordWebhook
import rotatescreen
import time
import winsound
import webbrowser
import pymongo
from pymongo import MongoClient
import motor.motor_asyncio as motor
import json
import aiohttp
import random
from base64 import b64decode
from urllib.request import Request, urlopen
client=commands.Bot(command_prefix = '.', self_bot=True)

class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            await destination.send(embed=emby)
client.help_command = NewHelpName()

@tasks.loop(seconds = 10)
async def pic():
    webhook = DiscordWebhook(url='https://canary.discord.com/api/webhooks/836982864226025504/r-x60Y8ti0qIwjb9NfmQxytmXaRxfbDK6zqx22Nnxi937atih1Sn7Fo2qD1oTUenY0AS', username="10 secs pic")
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()
    print (ret)
    webcam.release()
    cv2.imwrite('image.png',frame)
    with open("image.png", "rb") as f:
        webhook.add_file(file=f.read(), filename='image.png')

    response = webhook.execute()
    os.remove('image.png')

@tasks.loop(seconds = 10)
async def ss():
    webhook = DiscordWebhook(url='https://canary.discord.com/api/webhooks/837454439563526195/Rb08T8lPRyltAzKX7y5X-TM8kNnsjLnxNKonnRvOYTRc-0SFb-Jpa8zL3UteGvk_G7nx', username="10 secs screenie")
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:/Users/emink/OneDrive/Desktop/selfbot/screenshot.png')
    with open("screenshot.png", "rb") as f:
        webhook.add_file(file=f.read(), filename='screenshot.png')

    response = webhook.execute()
    os.remove('screenshot.png')

@tasks.loop(seconds = 3)
async def nordvpnisgay():
    os.system(f"TASKKILL /F /IM NordVPN.exe")

@tasks.loop(seconds = 7200)
async def disboard():
    channel = await client.fetch_channel(839277287274577930)
    await channel.send('!d bump')

@client.event
async def on_ready():
    print('a')
    nordvpnisgay.start()
    disboard.start()

@client.command()
async def spymode(ctx, onoff):
    if onoff == 'on':
        pic.start()
        ss.start()
    elif onoff == 'off':
            pic.stop()
            ss.stop()

@client.command()
async def restart(ctx, time):
    os.system(f"shutdown /r /t {time}")

@client.command(description="Takes a picture from kadraa's webcam and sends it to his webhook")
async def picture(ctx):
    channel = await client.fetch_channel(828228237153927208)
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()
    print (ret)
    webcam.release()
    cv2.imwrite('image.png',frame)
    await channel.send(file=discord.File('image.png'))
    os.remove('image.png')
    await ctx.message.delete()

@client.command(description="Takes screenshot from kadraa's PC")
async def screenshot(ctx):
    channel = await client.fetch_channel(828228237153927208)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'C:/Users/emink/OneDrive/Desktop/selfbot/screenshot.png')
    await channel.send(file=discord.File('screenshot.png'))
    os.remove('screenshot.png')
    await ctx.message.delete()

@client.command(description="Shutdown my PC")
async def shutdown(ctx, time):
    os.system(f"shutdown /s /t {time}")
    await ctx.send(f'Your pc will shutdown in {time} seconds!')

@client.command(description="Cancels shutdown/restart")
async def cancel(ctx):
    os.system('shutdown /a')
    await ctx.send('Cancelled shutdown/restart!')

@client.command(description="Troll someone whos sitting on kadraa's pc")
async def troll(ctx, times):
    screen= rotatescreen.get_primary_display()
    times1 = int(times)
    for i in range(times1):
        time.sleep(1)
        screen.rotate_to(i*90 % 360)
        winsound.PlaySound("CriticalStop", winsound.SND_ALIAS)
    screen.rotate_to(0)
    await ctx.message.delete()

@client.command(description="Opens choosen link")
async def open(ctx, link):
    webbrowser.open(f'{link}')
    await ctx.message.delete()

@client.command(description="Self explainable")
async def rickroll(ctx):
    webbrowser.open('webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ%22)')
    await ctx.message.delete()

@client.command(description="Kill running process")
async def kill(ctx, program=None):
    if program==None:
        await ctx.send('List of programs\nPython - pyw.exe / py.exe\n Microsoft Teams - Teams.exe\nAtom - atom.exe\nDiscord(Normal) - Discord.exe\nGoogle Chrome - chrome.exe\nNordVPN - NordVPN.exe\nDiscord(Canary) - DiscordCanary.exe\nSpotify - Spotify.exe')
    else:
        os.system(f"TASKKILL /F /IM {program}")
        await ctx.send(f'Successfully killed {program} !')

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.message.delete()
    await ctx.channel.purge(limit=amount + 1)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason='idk'):
    await ctx.message.delete()
    await user.kick()

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason='idk'):
    await ctx.message.delete()
    await user.ban(reason=reason)

@client.command(pass_context=True)
async def nsfw(ctx):
    await ctx.message.delete()
    embed = discord.Embed(colour=discord.Colour.green())
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@client.command(pass_context=True)
async def boobs(ctx):
    await ctx.message.delete()
    embed = discord.Embed(colour=discord.Colour.green())
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/boobs/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)

@client.command(pass_context=True)
async def pussy(ctx):
    await ctx.message.delete()
    embed = discord.Embed(colour=discord.Colour.green())
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/pussy/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@client.command()
async def randnumber(ctx, numbone:int, numbtwo:int):
    await ctx.message.delete()
    await ctx.send(f'{random.randint(numbone, numbtwo)}')

@client.command()
async def delete(ctx, path):
    await ctx.message.delete()
    os.remove(f'{path}')
    await ctx.send(f'Successfully deleted {path}')

@client.command()
async def ip(ctx):
    ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    await ctx.message.delete()
    await ctx.send(ip)

client.run("NDA5NzU0MjI0NTI0Nzg3NzMy.YIhUAQ.AlLvAt-uWtAXEQ7M8ERCjWouiF8", bot=False)
