import discord
import asyncio
import Bear as Bear
import os
import sys
from datetime import datetime
from discord.ext import tasks
import pytz
import traceback
from bear_interactions import *
from collections import deque
message_history = deque(maxlen=5)
from discord.voice_client import VoiceClient
class CustomVoiceClient(VoiceClient):
    pass
intents = discord.Intents.all()
TOKEN = 'MTEwOTU0NDM1NDQ4MzI5NDIzOA.GkdK66.R8mwk_aHon3YserNu0QJncZT64AF2TIMo77kPI'
name = "肚肚"
newBear = Bear.Bear(name)
bot = discord.Client(intents=intents)
last_bath = 180
last_feed = 240
from datetime import datetime, time
import pytz

def check_sleep():
    eastern = pytz.timezone('US/Eastern')
    current_time = datetime.now(eastern)
    morning_time = current_time.replace(hour=3, minute=0, second=0)
    evening_time = current_time.replace(hour=11, minute=0, second=0)

    if morning_time <= current_time < evening_time:
        newBear.activity_log = []
        return True
    return False

def check_bath():
    if last_bath >= 180: 
        return True
    return False
def check_feed():
    if last_feed >= 240:
        return True
    return False

async def perform():
    global last_bath, last_feed, newBear
    try:
        current_time = datetime.now(pytz.timezone('US/Eastern'))
        current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        sleep = 5
        result = 0
        channel = None
        if check_sleep():
            channel = bot.get_channel(1075548628338343988)
            sleep = 8*60
            newBear.change_mood('sleep',-1)
            newBear.move_to_location('肚肚的小床')
        elif check_feed():
            channel = bot.get_channel(1106000475297415219)
            sleep = 30
            last_feed = 0
            last_bath += sleep
            newBear.change_mood('hungry',-1)
            newBear.move_to_location('大餐厅')
        elif check_bath():
            channel = bot.get_channel(1109555208796786718)
            sleep = 2
            last_bath = 0
            last_feed += sleep
            newBear.change_mood('dirty',-1)
            newBear.move_to_location('肚肚的厕所')
        else: 
            result = await generate_activity({"happy":str(newBear.happy),"date":current_time_str,"history":str(newBear.activity_log)})
            if result !=0:
                channel = bot.get_channel(int(result['channel_id'])) 
                sleep = result['duration']
                newBear.add_activity(str(result)+' time:'+current_time_str+'\n')
                newBear.remove_activity()
                newBear.change_mood(result['mood'],result['effect'])
                newBear.move_to_location(result['channel_name'])
                last_bath += sleep
                last_feed += sleep
        if channel is not None:
            if bot.voice_clients:
                for vc in bot.voice_clients:
                    await vc.disconnect()
            await channel.connect()
            await asyncio.sleep(sleep*60)
            print("sleep complete")
    except Exception as e:
        print(f'An error occurred: {e}')
        traceback.print_exc()
    finally:
        bot.loop.create_task(perform())
@bot.event
async def on_ready():
   bot.loop.create_task(perform()) 
@bot.event
async def on_message(message):
    global message_history
    channel_id = 1105763643502633002
    print(message.author.name + ':' + message.content)
    if message.author == bot.user:
        return
    if message.content == 'restart':
        await message.channel.send("肚肚重启中")
        args = sys.argv[:]
        args.insert(0, sys.executable)
        os.execv(sys.executable, args)
            
    if check_sleep():
        return
    
    if message.channel.id == channel_id and '肚肚' or'小宝宝' in message.content:
        if message.author.name == '16' or message.author.name == 16:
            author = '妈妈'
        elif message.author.name == 'Lovetg':
            author = '宝宝'
        else:
            author = message.author.name
        message_history_str = '\n'.join(list(message_history))
        result = await send_message({"author":author,"content":message.content,"happy":str(newBear.happy),"activity_log":str(newBear.activity_log),"mood":newBear.mood,"history":message_history_str,"location":newBear.location})
        if result !=0:
            message_history.append(author + ':' + message.content + '\n')
            message_history.append('肚肚:' + result + '\n')
            await message.channel.send(result)
        
   

bot.run(TOKEN)
