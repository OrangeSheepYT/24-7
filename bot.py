import discord
import asyncio
import logging

bot = discord.Client()
bot.logger=logging.getLogger("discord")
bot.logger.setLevel(logging.DEBUG)
bot.handler=logging.FileHandler(filename="discord.log",encoding="utf-8",mode='w')
bot.handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s"))
bot.logger.addHandler(bot.handler)

async def update_config_task():
    await bot.wait_until_ready()
    
    while not bot.is_closed:
        await asyncio.sleep(60)

@bot.event
async def on_message(message):
    pass

@bot.event
async def on_ready():
    print("Connected")
    print("As {}")
    print("_________")

@bot.event
async def on_member_join(member):
    msg = "Hello and welcome {}! Take your time and join our partnering server where you can find more awesome friends and a family friendly community.... New comers will be rewarded with a cookie... uwu :cookie:  Invite: https://discord.gg/VHaNn72 we also need staff".format(member.mention)
    await bot.send_message(member, msg)	


bot.run("mattd.123@yahoo.com","24/7bot")
