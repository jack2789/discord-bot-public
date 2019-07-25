import discord
from discord.ext import commands
import LeagueFunctions
from io import StringIO
import io
import sys
import os

prefix = '#'
bot = commands.Bot(command_prefix=prefix)
def printer(team1,team1Champs,team1Ranks):
    old_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result

    for t1, t2, t3 in zip(team1, team1Champs, team1Ranks):
        print('%-20s %-14s %s' % (t1, t2, t3))

    sys.stdout = old_stdout
    result_string = result.getvalue()
    return result_string

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

    a = printer(team1,team1Champs,team1Ranks)
    b = printer(team2,team2Champs,team2Ranks)

    await ctx.send("""
```
Team1:
{} \nTeam2:\n{}```""".format(a,b))

@bot.command()
async def shower(ctx):
    import random, requests
    randnum = random.randint(0, 99)
    response = requests.get('https://www.reddit.com/r/showerthoughts/top.json?sort=top&t=week&limit=100', headers = {'User-Agent': 'showerbot'})
    result = response.json()
    result = result["data"]["children"][randnum]["data"]

    await ctx.send("""
    ```
{}\n       -{}
    ```
    """.format(result["title"],result["author"]))

bot.run(str(os.environ.get('TOKEN')))
