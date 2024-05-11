import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():
    url: "https://random.dog/woof.json"""
    res = requests.get(url)
    data = res.json()
    return data["url"]

def get_fox_image_url():
    url: "https://randomfox.ca/floof/"""
    res = requests.get(url)
    data = res.json()
    return data["url"]

@bot.command()
async def animal(ctx):
    '''Cada vez que se llama a la solicitud de un animal, el programa llama a las funciones get_duck/dog/fox_image_url, aleatoriamente.'''
    image_url = random.choice(get_duck_image_url(), get_dog_image_url(), get_fox_image_url())
    await ctx.send(image_url)


@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('BOTSXL\images'))
    with open(f'BOTSXL\images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)


bot.run("Token")
