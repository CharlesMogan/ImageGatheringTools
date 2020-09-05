# classifierbot.py
import os
import requests
from dotenv import load_dotenv
from discord.ext import commands
from PIL import Image

from classifier import prepare_image2 , predict_image

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='itar ')




@bot.event
async def on_ready():
    print(f'I am ready')




@bot.command(name='classify', help='I will do my best to tell you what kind of rodent is in your picture')
async def slime_this(ctx, *args):
    for attachment in ctx.message.attachments:
        attachment_url = attachment.url
        print(attachment_url)
        file_name = "imageToTest"
        response = requests.get(attachment_url, stream=True)
        #copyfileobj(response, out_file)
        img = Image.open(response.raw)
        preped_image = prepare_image2(img)
        prediction = predict_image(preped_image)
        await ctx.send(f"I think this is a picture of a {prediction}")




bot.run(TOKEN)

