import discord
from discord import app_commands
from discord.ext import commands
import config
import os
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
    if message.content.startswith("$help"):
        await message.channel.send("To generate an image, use the command `!generate <your prompt>`. For example: `!generate a beautiful sunset over the mountains`.")
    if message.content.startswith("!generate"):
        async with message.channel.typing():
            status_message = await message.channel.send("Generating image...")
            download_image(message.content)
            await message.channel.send(file=discord.File(fp='generated_image.jpg'))
            await status_message.delete()
        if os.path.exists('generated_image.jpg'):
            os.remove('generated_image.jpg')
    await bot.process_commands(message)



if __name__ == '__main__':
    bot.run(config.TOKEN)