from redbot.core import commands
import discord
import sys
from random import choice
import random
try: # check if BeautifulSoup4 is installed
    from bs4 import BeautifulSoup
    soupAvailable = True
except:
    soupAvailable = False
import aiohttp
import asyncio
import requests
import json

folderPath = "/home/pi/.local/share/Red-DiscordBot/data/GBot/cogs/CogManager/cogs/gansleycog/"

class Gansleycog(commands.Cog):
    """My custom cog"""

    @commands.command(name="randomwords", aliases=["rw"])
    async def randomwords(self, ctx):
        """Generate 3 random words"""

        #Generating random words
        with open(folderPath + 'wordlist.txt', 'r', encoding='utf-8') as fullList:
            RwordList = fullList.readlines()

            rWords = ""

            for i in range(1, 4):
                rWords += " " + random.choice(RwordList)
            
            rWords = rWords.replace("\n",",").rstrip(",")
            
            await ctx.send( 'Your 3 random words are -' + rWords)

    @commands.command(name="makecharacterpublic", aliases=["makecharpub","mcp"])
    async def makecharpub(self, ctx, gender=None):
        """PUBLIC Generate 2d20 and 3 random words with Gansley commentary. For random name, add <f/m>"""

        #Generating random words
        with open(folderPath + 'wordlist.txt', 'r', encoding='utf-8') as fullList:
            RwordList = fullList.readlines()

        randomwords = ""

        for i in range(1, 4):
            randomwords += random.choice(RwordList)

        #NAME GENERATOR
        if (gender != None):
            if gender in ('f', 'F', 'm', 'M'):
                response = requests.get("https://www.behindthename.com/api/random.json?gender=" + gender + "&number=1&randomsurname=yes&key=to868069982")
                allNames = response.json()
                names = allNames["names"][0] + ' ' + allNames["names"][1] + '\n\n'        
            else:
                await ctx.send("Wrong format. Please use !mcp <f/m> <number of middle names or blank>")
                return
        else:
            names = ''

        #ROLLING DICE      
        resultList = [random.randint(1,20), random.randint(1,20) ]

        # Gansley quotes
        if any(x == 1 for x in resultList) and all(x < 6 for x in resultList):
            quote = '\n\nTruly the worst to ever play the sport.'
        elif any(x == 20 for x in resultList) and all(x > 15 for x in resultList):
            quote = ["\n\nTruly the best to ever play the sport.","\n\nTruly the best to ever play the sport. It brings a tear to Dan Gansley's eye."]
            quote = random.choice(quote)
        elif all(x == 10 for x in resultList):
            quote = '\n\nThat is not very polarizing.'
        elif any(x > 17 for x in resultList) and any(x < 3 for x in resultList):
            quote = '\n\nThat is quite polarizing indeed.'
        elif all(x == 13 for x in resultList):
            quote = '\n\nTHE. BEST.'
        elif any(x == 9 for x in resultList) and any(x == 11 for x in resultList):
            quote = ["\n\nToilet Apple bombing was an inside job!","\n\nApples can't melt steel beams!"]
            quote = random.choice(quote)
        else:
             quote = ''
        
        #Bonus roll
        bonus = ["",""]
        for x in range(0,2):
            bonus[x] = " + " + str(random.randint(1,20)) if resultList[x] == 20 else ""

        #Mundie check
        race = 'is a Mundie.' if resultList[1] == 1 else 'can have an Epithet.'
        wordtype = 'Epithet'
        
        #SEND
        await ctx.send('```' + names + 'Character ' + race + '\n\nChoose ' + wordtype + ':\n'
                        + randomwords + "\n" + 'Stamina:     ' + str(resultList[0]) + bonus[0] + '\n'
                        + "Proficiency: " + str(resultList[1]) + bonus[1] + quote + '```')                            

        
    @commands.command(name="makecharacter", aliases=["makechar","mc"], pass_context=True)
    async def makechar(self, ctx, gender=None):
        """PRIVATE Generate 2d20 and 3 random words with Gansley commentary. For random name, add <f/m>"""

        #Generating random words
        with open(folderPath + 'wordlist.txt', 'r', encoding='utf-8') as fullList:
            RwordList = fullList.readlines()

        randomwords = ""

        for i in range(1, 4):
            randomwords += random.choice(RwordList)

        #NAME GENERATOR
        if (gender != None):
            if gender in ('f', 'F', 'm', 'M'):
                response = requests.get("https://www.behindthename.com/api/random.json?gender=" + gender + "&number=1&randomsurname=yes&key=to868069982")
                allNames = response.json()
                names = allNames["names"][0] + ' ' + allNames["names"][1] + '\n\n'        
            else:
                await ctx.send("Wrong format. Please use !mcp <f/m> <number of middle names or blank>")
                return
        else:
            names = ''

        #ROLLING DICE      
        resultList = [random.randint(1,20), random.randint(1,20) ]

        # Gansley quotes
        if any(x == 1 for x in resultList) and all(x < 6 for x in resultList):
            quote = '\n\nTruly the worst to ever play the sport.'
        elif any(x == 20 for x in resultList) and all(x > 15 for x in resultList):
            quote = ["\n\nTruly the best to ever play the sport.","\n\nTruly the best to ever play the sport. It brings a tear to Dan Gansley's eye."]
            quote = random.choice(quote)
        elif all(x == 10 for x in resultList):
            quote = '\n\nThat is not very polarizing.'
        elif any(x > 17 for x in resultList) and any(x < 3 for x in resultList):
            quote = '\n\nThat is quite polarizing indeed.'
        elif all(x == 13 for x in resultList):
            quote = '\n\nTHE. BEST.'
        elif any(x == 9 for x in resultList) and any(x == 11 for x in resultList):
            quote = ["\n\nToilet Apple bombing was an inside job!","\n\nApples can't melt steel beams!"]
            quote = random.choice(quote)
        else:
             quote = ''
        
        #Bonus roll
        bonus = ["",""]
        for x in range(0,2):
            bonus[x] = " + " + str(random.randint(1,20)) if resultList[x] == 20 else ""

        #Mundie check
        race = 'is a Mundie.' if resultList[0] == 1 else 'can have an Epithet.'
        wordtype = 'Core word' if resultList[0] == 1 else 'Epithet/Core word'
        
        #SEND
        await ctx.author.send('```' + names + 'Character ' + race + '\n\nChoose ' + wordtype + ':\n'
                        + randomwords + "\n" + 'Stamina:     ' + str(resultList[0]) + bonus[0] + '\n'
                        + "Proficiency: " + str(resultList[1]) + bonus[1] + quote + '```')


    @commands.command(name="randomname", aliases=["rn"])
    async def randomname(self, ctx, gender):
        """Generates a character name"""

        #NAME GENERATOR
        commandCheck = None

        if gender in ('f', 'F', 'm', 'M'):

            response = requests.get("https://www.behindthename.com/api/random.json?gender=" + gender + "&number=1&randomsurname=yes&key=to868069982")
            allNames = response.json()
        else:
            commandCheck = "```Wrong format. Please use !randomname <f/m>```"

        if commandCheck == None:
            names = allNames["names"]
            await ctx.send('```' + names[0] + " " + names[1] + '```')
        else:
            await ctx.send(commandCheck)


    @commands.command(name="ProficiencyAchievementsPublic", aliases=["profachpub","pap"])
    async def proficiencyachievementspublic(self, ctx, startlvl):
        """Generates randomized proficiency achievement levels up to 100"""
        
        #Your code will go here
        try:

            lvl = 0 + int(startlvl)
            numList = [startlvl]
            number = 0 + int(startlvl)
            achnum = 0 + int(startlvl)
            classnum = 1
            cycle = 1
            start = 2
            stop = 5

            while (cycle < 41) and (lvl < 100) and (lvl > 0):

                number = number + random.randint(start, stop)

                #Building sequence
                if (number < 45):
                    start = 2
                    stop = 4
                elif (number >= 45) and (number < 60):
                    start = 4
                    stop = 7
                elif (number >= 60) and (classnum == 1):
                    classnum = 2
                    number = 60
                elif (number > 60) and (number < 80) and (classnum == 2):
                    start = 4
                    stop = 7
                elif (number >= 80) and (number < 100):
                    start = 10
                    stop = 14
                elif (number >= 100):
                    number = 100

                numList.append(str(number))

                lvl = number
                cycle = cycle + 1

            await ctx.send('Proficiency achievements starting from ' + startlvl + ':\n' + str(numList))

        except:
            await ctx.send('Wrong format')


    @commands.command(name="ProficiencyAchievements", aliases=["profach","pa"], pass_context=True)
    async def proficiencyachievements(self, ctx, startlvl):
        """Generates randomized proficiency achievement levels up to 100. And sends to PM."""
        
        #Your code will go here
        try:

            lvl = 0 + int(startlvl)
            numList = [startlvl]
            number = 0 + int(startlvl)
            achnum = 0 + int(startlvl)
            classnum = 1
            cycle = 1
            start = 2
            stop = 5

            while (cycle < 41) and (lvl < 100) and (lvl > 0):

                number = number + random.randint(start, stop)

                #Building sequence
                if (number < 45):
                    start = 2
                    stop = 4
                elif (number >= 45) and (number < 60):
                    start = 4
                    stop = 7
                elif (number >= 60) and (classnum == 1):
                    classnum = 2
                    number = 60
                elif (number > 60) and (number < 80) and (classnum == 2):
                    start = 4
                    stop = 7
                elif (number >= 80) and (number < 100):
                    start = 10
                    stop = 14
                elif (number >= 100):
                    number = 100

                numList.append(str(number))

                lvl = number
                cycle = cycle + 1

            #user = ctx.message.author
            await ctx.author.send("Proficiency achievements starting from " + startlvl + ":\n" + str(numList))

        except:
            await ctx.send('Wrong format')

    @commands.command(name="roll", aliases=["dice","r"])
    async def roll(self, ctx, dice : str):
        """I will roll dice"""

        #Your code will go here
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        if limit > 1000:
            await ctx.send("I'm afraid I don't have a dice that big. All I have is 30d1000")
        elif rolls > 30:
            await ctx.send("I'm afraid I don't have that many dice. All I have is 30d1000")
        else:
            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))

            randquote = random.randint(1, 20)
            if randquote == 1:
                quote = "*Well Dan Gansley rolls the dice and Dan Gansley is the house.*\n"
            elif randquote == 13:
                quote = "*Let me just swizzle my dizzle.*\n"
            else:
                quote = ""
            await ctx.send(quote + result)   

    @commands.command(name="flip", aliases=["coin"])
    async def flip(self, ctx):
        """Flips a Gansley coin"""

        await ctx.send("*flips a coin and it lands on... " + choice(["GANSLEY!*", "NOT GANSLEY!*"]))

    @commands.command(name="wildmagic", aliases=["wm"])
    async def wildmagic(self, ctx, user : discord.Member=None):
        """Rolls Wild Magic (1d300)"""

        #Your code will go here
        dice = '1d300'
        rolls, limit = map(int, dice.split('d'))

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        result = int(result)

        if user != None:
            selfharm = str(user)
            addquote = random.randint(0,9)

            if  selfharm == 'GansleyBOT#0412':
                target = "Oh yes. This is the feeling I've missed. The feeling of self inflicted harm. *shoots his slot machine gun at* ***himself***\n\n"
            elif addquote == 1:
                target = "I suppose it's time for me to take this baby out for a test run. I hope they weren't to cruel to you in prison my dear. *shoots his slot machine gun at* " + user.mention + "\n\n"
            else:
                target = "*shoots his slot machine gun at* " + user.mention + "\n"
        else:
            target = ""


        with open(folderPath + 'wildlist.txt', 'r', encoding='utf-8') as decList:
            wildList = decList.readlines()
        await ctx.send(target + str(result) + '. ' + wildList[result])

    @commands.command(name="die", aliases=["kill"])
    async def die(self, ctx):
        """Dies"""

        #Your code will go here
        clone = random.randint(0,9)

        if clone != 1:
            await ctx.send('*dies (✖_✖)*')
        elif clone == 1:
            await ctx.send('*dies (✖_✖)*')
            await ctx.send('*another Gansley steps out*\nAh yes, thank you for getting rid of that useless pawn.')
    
    @commands.command(name="quote", aliases=["q"])
    async def quote(self, ctx):
        """Picks a random quote"""

        #Your code will go here


        with open(folderPath + 'quotes.txt', 'r', encoding='utf-8') as qList:
            quoteList = qList.readlines()
            pick = random.randint(0,len(quoteList)-1)
        await ctx.send(quoteList[pick])




#SETUP
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

def setup(bot):
    if soupAvailable:
        bot.add_cog(Gansleycog(bot))
    else:
        raise RuntimeError("You need to run `pip3 install beautifulsoup4`")

