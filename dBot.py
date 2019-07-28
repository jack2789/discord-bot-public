import discord
from discord.ext import commands
import LeagueFunctions
from io import StringIO
import io
import sys
import os
import datetime
import creepy

prefix = '#'
bot = commands.Bot(command_prefix=prefix)

def printer(team1):
    old_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result

    for t1 in zip(team1):
        print('%-s' % t1)

    sys.stdout = old_stdout
    result_string = result.getvalue()
    return result_string

def displayembed(Title):
    embed = discord.Embed(title=Title, colour = discord.Color.blue())
    return embed

@bot.command
async def creepy(ctx):
    a = getRandomCreepy(creepy)
    await ctx.send(a)
    
@bot.event
async def on_ready():
    print("Ready when you are xc")
    print("I am running on " + bot.user.name)
    print("With the ID: " + str(bot.user.id))

@bot.command()
async def info(ctx, user: discord.Member):
    await ctx.send("The users name is: {}".format(user.name))
    await ctx.send("The users ID is: {}".format(user.id))
    await ctx.send("The users status is: {}".format(user.status))
    await ctx.send("The user joined at: {}".format(user.joined_at))

@bot.command()
async def game(ctx, *,summoner):
    summoner = summoner.replace(" ", "_")
    print(summoner)
    league = LeagueFunctions.LoL()
    ID = league.findSummonerID(summoner)
    currentGame = league.getCurrentMatchSummoners(ID)
    summonerList = currentGame[0]
    idList = currentGame[1]
    teamIds = currentGame[2]
    championIDs = currentGame[3]
    teamRanks = currentGame[4]

    teamSet = league.teammaker(summonerList, teamIds, championIDs, teamRanks)
    team1 = teamSet[0]
    team2 = teamSet[1]
    team1Champs = teamSet[2]
    team1Ranks = teamSet[4]
    team2Champs = teamSet[3]
    team2Ranks = teamSet[5]

    a1 = printer(team1)
    a2 = printer(team1Champs)
    a3 = printer(team1Ranks)
    b1 = printer(team2)
    b2 = printer(team2Champs)
    b3 = printer(team2Ranks)
    summoner=summoner.replace("_"," ")
    
    embed = displayembed('Live Match Data for ' + summoner)
    embed.add_field(name = 'Blue Team', value= a1, inline = True)
    embed.add_field(name = 'Champion', value = a2, inline = True)
    embed.add_field(name = 'Rank', value = a3, inline = True)
    
    embed.add_field(name = 'Red Team ', value = b1, inline = True)
    embed.add_field(name = 'Champion', value = b2, inline = True)
    embed.add_field(name = 'Rank', value = b3, inline = True)
    
    currentDT = datetime.datetime.now()
    embed.set_footer(text=ctx.author.name + ' | ' + currentDT.strftime("%a, %b %d, %Y") + ' at ' + currentDT.strftime("%I:%M %p"), icon_url = ctx.author.avatar_url)
    
    
    await ctx.send(embed=embed)

@bot.command()
async def shower(ctx):
    import random, requests
    randnum = random.randint(0, 99)
    response = requests.get('https://www.reddit.com/r/showerthoughts/top.json?sort=top&t=week&limit=100', headers = {'User-Agent': 'showerbot'})
    result = response.json()
    result = result["data"]["children"][randnum]["data"]

    await ctx.send("""
    ```
{}\n       -{}```
""".format(result["title"],result["author"]))


bot.run(str(os.environ.get('TOKEN')))
