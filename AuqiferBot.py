
from functools import wraps
import os 
import discord
from discord.ext import commands
import Config
import asyncio
from random import randint
import random 

intents=intents=discord.Intents.all()
intents = discord.Intents.default()
intents.messages = True



bot = commands.Bot(command_prefix='-')


# @bot.event 
# async def on_member_update(before, after): 
#     n = after.nick 
#     if n: # Это проверка сменил ли кто то определенный ник
#         if n.lower().count("Ego") > 0: # Эта хуйня проверяет именнно ник эго
#             last = before.nick
#             if last: # Если до смены ника у какого либо чела был ник  "Ego"
#                 await after.edit(nick=last)
#             else: # "FUCK YOU"
#                 await after.edit(nick="Пошел нахуй Эго")


# def has_monkey_role(coro):
#     @wraps(coro)
#     async def wrapper(before, after):
#         role = discord.utils.get(before.guild.roles, name="Горилла")
#         if after in role.members:
#             await coro(before, after)
#     return wrapper


# @bot.event
# @has_monkey_role # Without calling it, it's hardcoded
# async def on_member_update(before, after):
#     await member.edit(nick="Макака ебанная")


# @bot.event
# @has_role("Горилла")
# async def on_member_update(nick, member):
#     await member.edit(nick="Макака ебанная ")

@bot.event
async def on_member_update(before, after):
    role = discord.utils.get(before.guild.roles, name="Горилла")
    if after in role.members:
        await member.edit(nick=nick)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print('Я включился')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('Негмат'):
        await message.channel.send("Негмат ебанный шизойд, держу вас в курсе")   

    if message.content.startswith('Щетина'):
        await message.channel.send('Эй, ты упомянул пуcсибоя в своем сообщений, будешь хуй ?')    

    if message.content.startswith('hi'):
        await message.channel.send(f' {message.author.mention} Hi!')

    if message.content.startswith(message.author.mention): 
        await message.channel.send('Не упоминай аукифера, сука') 

    # If bot is mentioned, reply with a message
    if bot.user in message.mentions:
        await message.channel.send("Не тэгай меня, уебище")
        return


@bot.command()
async def sum(ctx, x:int, y:int):
    await ctx.send(x+y)

@bot.command()
async def clear(ctx, count: int):
    await ctx.channel.purge(limit=count+1)
    await ctx.send(f"Было удалено {count} сообщений")

@bot.command(pass_content=True)
async def changenick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Имя измененно на {member.mention} ')

@bot.command(pass_context=True)
async def myid(ctx):
    await ctx.send("{} is your id".format(ctx.message.author.id))

@bot.command(pass_context = True)
async def rnumber(ctx):
    embed = discord.Embed(title = "Random Number", description = (random.randint(1, 101)), color = (0xf85252))
    await ctx.send(embed = embed)

@bot.command(pass_context = True)
async def churka(ctx):
    await ctx.send(    """
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠋⠉⠈⠉⠉⠉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿
    ⣿⣿⣿⢏⣴⣿⣷⠀⠀⠀⠀⠀⢾⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿
    ⣿⣿⣟⣾⣿⡟⠁⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣷⢢⠀⠀⠀⠀⠀⠀⠀⢸⣿
    ⣿⣿⣿⣿⣟⠀⡴⠄⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣿
    ⣿⣿⣿⠟⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⢴⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿
    ⣿⣁⡀⠀⠀⢰⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⡄⠀⣴⣶⣿⡄⣿
    ⣿⡋⠀⠀⠀⠎⢸⣿⡆⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⠗⢘⣿⣟⠛⠿⣼
    ⣿⣿⠋⢀⡌⢰⣿⡿⢿⡀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣧⢀⣼
    ⣿⣿⣷⢻⠄⠘⠛⠋⠛⠃⠀⠀⠀⠀⠀⢿⣧⠈⠉⠙⠛⠋⠀⠀⠀⣿⣿⣿⣿⣿
    ⣿⣿⣧⠀⠈⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠀⠀⠀⢀⢃⠀⠀⢸⣿⣿⣿⣿
    ⣿⣿⡿⠀⠴⢗⣠⣤⣴⡶⠶⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡸⠀⣿⣿⣿⣿
    ⣿⣿⣿⡀⢠⣾⣿⠏⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠀⣿⣿⣿⣿
    ⣿⣿⣿⣧⠈⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿
    ⣿⣿⣿⣿⡄⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣦⣄⣀⣀⣀⣀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠙⣿⣿⡟⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠁⠀⠀⠹⣿⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⠿⠛⠉⠉⠁⠀⢻⣿⡇⠀⠀⠀⠀⠀⠀⢀⠈⣿⣿⡿⠉⠛⠛⠛⠉⠉
    ⣿⡿⠋⠁⠀⠀⢀⣀⣠⡴⣸⣿⣇⡄⠀⠀⠀⠀⢀⡿⠄⠙⠛⠀⣀⣠⣤⣤⠄
    
    Да я ебу чурок, как ты узнал ?
    """)


bot.run(Config.token)