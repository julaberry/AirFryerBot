import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
from PIL import Image

load_dotenv("config.env")
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix='$')

bottom = Image.open('bottomtext.png')

#https://note.nkmk.me/en/python-pillow-concat-images/
def get_concat_v_resize(im1, im2, resample=Image.BICUBIC, resize_big_image=False):
	if im1.width == im2.width:
		_im1 = im1
		_im2 = im2
	elif (((im1.width > im2.width) and resize_big_image) or
		  ((im1.width < im2.width) and not resize_big_image)):
		_im1 = im1.resize((im2.width, int(im1.height * im2.width / im1.width)), resample=resample)
		_im2 = im2
	else:
		_im1 = im1
		_im2 = im2.resize((im1.width, int(im2.height * im1.width / im2.width)), resample=resample)
	dst = Image.new('RGB', (_im1.width, _im1.height + _im2.height))
	dst.paste(_im1, (0, 0))
	dst.paste(_im2, (0, _im1.height))
	return dst


@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))


@bot.command()
async def clearly(ctx, imagenum = 0):
	try:
		message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
	except:
		await ctx.send("Reply to an image with this command.", delete_after=10)
		return
	try:
		attachment = message.attachments[0]
		await attachment.save("tempimage")
		#await ctx.send(message.attachments[0])
	except Exception as e:
		print(e)
		await ctx.send("Attachment " + str(imagenum) + " does not exist", delete_after=10)
		return
	try:
		top = Image.open("tempimage")
		get_concat_v_resize(top, bottom).save("meme.jpg")
		await ctx.send(file=discord.File('meme.jpg'))
	except Exception as e:
		print(e)
		await ctx.send("Error in processing.")
		return
	finally:
		if os.path.exists("tempimage"):
			os.remove("tempimage")
		if os.path.exists("meme.jpg"):
			os.remove("meme.jpg")
   


bot.run(TOKEN)
