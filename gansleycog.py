import discord
from discord.ext import commands
import random
from random import choice
try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False
import aiohttp

class Gansleycog:
	"""My custom cog that does stuff!"""

	def __init__(self, bot):
		self.bot = bot

	'''
	@commands.command()
	async def punch(self, user : discord.Member):
		"""I will puch anyone! >.<"""

		#Your code will go here
		await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")

	'''
	
	@commands.command()
	async def roll(self, dice : str):
		"""I will roll dice"""

		#Your code will go here
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await self.bot.say('Format has to be in NdN!')
			return

		result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		await self.bot.say(result)

	@commands.command()
	async def flip(self):
		"""Flips a coin... or a user.

		Defaults to coin.
		"""
		await self.bot.say("*flips a coin and it lands on... " + choice(["GANSLEY!*", "NOT GANSLEY!*"]))

	@commands.command()
	async def randomwords(self):
		"""Generate 3 random words"""

		#Your code will go here
		url = "https://www.randomlists.com/random-words" #build the web adress
		async with aiohttp.get(url) as response:
			soupObject = BeautifulSoup(await response.text(), "html.parser")
		try:
			allWords = soupObject.find('div', 'tidy--new ol')
			word1 = allWords.li.get_text()
			word2 = allWords.li.next_sibling.get_text()
			word3 = allWords.li.next_sibling.next_sibling.get_text()
			#word2 = soupObject.find_next_sibling('span').get_text()
			await self.bot.say( ' Your 3 random words are - ' + word1 + ', ' + word2 + ', ' + word3)
		except:
			await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")



	@commands.command()
	async def makecharpub(self):
		"""PUBLIC Generate 2d20 and 3 random words with Gansley commentary"""

		#Your code will go here
		url = "https://www.randomlists.com/random-words" #build the web adress
		async with aiohttp.get(url) as response:
			soupObject = BeautifulSoup(await response.text(), "html.parser")
		try:
			allWords = soupObject.find('div', 'tidy--new ol')
			word1 = allWords.li.get_text()
			word2 = allWords.li.next_sibling.get_text()
			word3 = allWords.li.next_sibling.next_sibling.get_text()
			randomwords = ' ```Oh yes. I remember those three random words quite well. \n' + word1 + '\n' + word2 + '\n'  + word3 + '\n' + '\n'

			dice = '1d20'
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await self.bot.say('Format has to be in NdN!')
			return

		result1 = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		result1 = int(result1)
		result2 = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		result2 = int(result2)

		if result1 == 1 and result2 < 5:
			quote = '\n\nTruly the worst to ever play the sport.'
		elif result2 == 1 and result1 < 5:
			quote = '\n\nTruly the worst to ever play the sport.'
		
		elif result1 == 20 and result2 > 15:
			quote = '\n\nTruly the best to ever play the sport.'
		elif result2 == 20 and result1 > 15:
			quote = '\n\nTruly the best to ever play the sport.'
		
		elif result1 == 10 and result2 == 10:
			 quote = '\n\nThat is not very polarizing.'
		
		elif result1 > 17 and result2 < 3:
			 quote = '\n\nThat is quite polarizing indeed.'
		elif result2 > 17 and result1 < 3:
			 quote = '\n\nThat is quite polarizing indeed.'
		else:
			 quote = ' '

		await self.bot.say(randomwords + 'Your dice results are:\n' + str(result1) + '\n' + str(result2) + quote + '```')

	'''
	@commands.command(pass_context=True)
	async def pm(self, ctx, member : discord.Member=None):
		"""Send PM to sender"""

		#Your code will go here
		if member is None:
			member = ctx.message.author
			user = member

		await self.bot.send_message(user, 'test')
	'''


	@commands.command(pass_context=True)
	async def makechar(self, ctx, member : discord.Member=None):
		"""PRIVATE Generate 2d20 and 3 random words with Gansley commentary"""

		#Your code will go here
		if member is None:
			member = ctx.message.author
			user = member

		url = "https://www.randomlists.com/random-words" #build the web adress
		async with aiohttp.get(url) as response:
			soupObject = BeautifulSoup(await response.text(), "html.parser")
		try:
			allWords = soupObject.find('div', 'tidy--new ol')
			word1 = allWords.li.get_text()
			word2 = allWords.li.next_sibling.get_text()
			word3 = allWords.li.next_sibling.next_sibling.get_text()
			randomwords = ' ```Oh yes. I remember those three random words quite well. \n' + word1 + '\n' + word2 + '\n'  + word3 + '\n' + '\n'

			dice = '1d20'
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await self.bot.say('Format has to be in NdN!')
			return

		result1 = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		result1 = int(result1)
		result2 = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		result2 = int(result2)

		if result1 == 1 and result2 < 5:
			quote = '\n\nTruly the worst to ever play the sport.'
		elif result2 == 1 and result1 < 5:
			quote = '\n\nTruly the worst to ever play the sport.'
		
		elif result1 == 20 and result2 > 15:
			quote = '\n\nTruly the best to ever play the sport.'
		elif result2 == 20 and result1 > 15:
			quote = '\n\nTruly the best to ever play the sport.'
		
		elif result1 == 10 and result2 == 10:
			 quote = '\n\nThat is not very polarizing.'
		
		elif result1 > 17 and result2 < 3:
			 quote = '\n\nThat is quite polarizing indeed.'
		elif result2 > 17 and result1 < 3:
			 quote = '\n\nThat is quite polarizing indeed.'
		else:
			 quote = ' '

		await self.bot.send_message(user, randomwords + 'Your dice results are:\n' + str(result1) + '\n' + str(result2) + quote + '```')


	@commands.command()
	async def wildmagic(self):
		"""Send PM to sender"""

		#Your code will go here
		dice = '1d300'
		rolls, limit = map(int, dice.split('d'))

		result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		result = int(result)

		file = open('data/wildlist/wildlist.txt', 'r')
		wildList = file.readlines()
		await self.bot.say(str(result) + '. ' + wildList[result])




def setup(bot):
	bot.add_cog(Gansleycog(bot))