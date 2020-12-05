import discord
from discord.ext import commands
client = commands.Bot(command_prefix = '!')
# kanala ekleme linki = https://discord.com/api/oauth2/authorize?client_id=768854225756225607&permissions=8&scope=bot
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

client.run('NzY4ODU0MjI1NzU2MjI1NjA3.X5GhTA.jHdeXoosf2HsntMgc3PPHhG8B-0')
