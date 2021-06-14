import discord 
from discord.ext import commands
import asyncpraw

# Getting things from reddit
reddit = asyncpraw.Reddit(client_id='client_id',
                     client_secret='client_secret',
                     user_agent='user_agent')
# Discord bot stuff
client = discord.Client()

@client.event
# If user types "/get"
async def on_message(message):
	if message.content.startswith("/get"):
		sort = message.content[5:6]
		redditval = message.content[7:]
		print(sort)
		print(redditval)
		await message.channel.send("Please enter a valid subreddit and sort by, otherwise nothing will appear")
		submission = await reddit.subreddit(redditval)
		if (sort == "h"):
			sort = "hour"
		elif (sort == "d"):
			sort = "day"
		elif (sort == "w"):
			sort = "week"
		elif (sort == "m"):
			sort = "month"
		elif (sort == "y"):
			sort = "year"
		elif (sort == "a"):
			sort = "all"
		submissions = await reddit.subreddit(redditval)
		posts = submissions.top(limit=1)
		async for post in posts:
			url = post.url
			if (url.endswith(('.jpg', '.png', '.gif', '.jpeg'))):
				embed = discord.Embed(title= post.title)
				embed.set_image(url=post.url)
				await message.channel.send(embed=embed)

# If user types "/help" 
	if (message.content == ("/help")):
		embed = discord.Embed(title= "Commands", discription= "Below are the commands that you can use with this bot", color=discord.Color(15105570))
		embed.set_footer(text="Please use (.) before each command")
		embed.add_field(name=".get (enter the way you want to sort by) (enter a subreddit name)", value="Gets 1 picture from the way you want to sort of your chosen subreddit", inline=True)
		await message.channel.send(embed=embed)

client.run(TOKEN)