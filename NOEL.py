import datetime
import asyncio, discord
from dice import *
from discord.ext import commands
import os

now = datetime.datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초"

bot = commands.Bot(command_prefix="@")

@bot.event
async def on_ready():
    print("We have loggedd in as {0.user}".format(bot))

@bot.command()
async def hello(ctx):
    await ctx.send("hello")

# 주사위 게임 시스템
@bot.command()
async def 주사위(ctx):
    result, _color, bot, user = dice()
    embed = discord.Embed(title = "주사위 게임 결과", color = _color)
    embed.add_field(name = "Super Bot의 숫자", value = ":game_die: " + bot, inline = True)
    embed.add_field(name = ctx.author.name+"의 숫자", value = ":game_die: " + user, inline = True)
    embed.set_footer(text="결과: " + result)
    await ctx.send(embed=embed)

# 명령어 꼬임 방지 시스템
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어를 찾지 못했습니다")  

#청소 시스템
@bot.event
async def on_message_delete(message):
    channel = client.get_channel(965098412548685894)
    embed = discord.Embed(title=f"삭제됨", description=f"유저 : {message.author.mention} 채널 : {message.channel.mention}", color=0xFF0000)
    embed.add_field(name="삭제된 내용", value=f"내용 : {message.content}", inline=False)
    embed.set_footer(text=f"{message.guild.name} | {time}")
    await channel.send(embed=embed)
        
# 회원가입 시스템
@bot.command()
async def 회원가입(ctx):
    #print(ctx.author.name)
    #print(ctx.author.id)
    if checkName(ctx.author.name, ctx.author.id):
        signup(ctx.author.name, ctx.author.id)
        await ctx.send("회원가입이 완료되었습니다.")
    else:
        await ctx.send("이미 가입하셨습니다.")

bot.run(os.environ['token']) #토큰
