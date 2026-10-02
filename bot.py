import discord
from discord import app_commands
from discord.ext import commands
import config
from ai import download_image

bot = commands.Bot(
    command_prefix=config.prefix, intents=discord.Intents.all()
)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello! I'm a bot that can generate images based on your prompts. Use the command `$generate <your prompt>` to create an image.")
    if message.content.startswith("!generate"):
        download_image(message.content)
        await message.channel.send(file=discord.File(fp='generated_image.jpg'))


if __name__ == '__main__':
    bot.run(config.TOKEN)