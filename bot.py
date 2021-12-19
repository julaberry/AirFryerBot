import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
from PIL import Image

load_dotenv("config.env")
TOKEN = getenv("TOKEN")

bot = commands.Bot(command_prefix='$')



#im1 = Image.open('data/src/lena.jpg')
im2 = Image.open('data/src/rocket.jpg')


@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def clearly(ctx, imagenum = 0):
    message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    try:
    	message.attachments[0].url
    	await ctx.send(message.attachments[0])
    except:
    	await ctx.send("Attachment " + str(imagenum) + " does not exist")
   


bot.run(TOKEN)
