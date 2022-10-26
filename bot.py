import os
import discord
import time
from datetime import datetime
import math
from dateutil.relativedelta import relativedelta

TOKEN = 'MTAzNDg5NDU5NjgxMzA5OTA0OA.GK73OT.q5JqV1NPLoQAQbn0k3040QYpKjjqhGZ4T0emJk'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    #if '!countdown start' in message.content:
    if 'a' in message.content:
        now = datetime.now()
        print(now)
        mw2Time = datetime.strptime("27/10/2022 23:00:00", "%d/%m/%Y %H:%M:%S")
        print(mw2Time)
        diff = relativedelta(mw2Time, now)
        firstMessage = '**MW2 IS %d DAY %d HOURS %d MINUTES %d SECONDS AWAY**' % (diff.days, diff.hours, diff.minutes, diff.seconds) 
        botMessage = await message.channel.send(firstMessage)
        time.sleep(30)
        while(True):
            now = datetime.now()
            print(now)
            mw2Time = datetime.strptime("27/10/2022 23:00:00", "%d/%m/%Y %H:%M:%S")
            print(mw2Time)
            diff = relativedelta(mw2Time, now)
            if(diff.days != 0):
                editMessage = '**MW2 IS %d DAY %d HOURS %d MINUTES %d SECONDS AWAY**' % (diff.days, diff.hours, diff.minutes, diff.seconds) 
            else:
                editMessage = '**MW2 IS %d HOURS %d MINUTES %d SECONDS AWAY**' % (diff.hours, diff.minutes, diff.seconds) 
            await botMessage.edit(content=editMessage)
            time.sleep(30)


client.run(TOKEN)
