import asyncio, discord
from dice import *
from discord.ext import commands

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

bot.run("OTY0OTI5MzE3NjgxMzczMjM0.YlrydA.z7z4_WX9b0h4_J5c-oGqz5AbQQY") #토큰