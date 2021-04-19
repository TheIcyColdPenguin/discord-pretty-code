import discord

from config import TOKEN
from helpers import get_code
from scraper import delete_img, save_img

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has logged in!')


@client.event
async def on_message(msg: discord.Message):

    if msg.author == client.user or msg.author.bot:
        return

    if not msg.content.lower().startswith('!p'):
        return

    code_snippets = get_code(msg.content)[:10]

    if len(code_snippets) == 0:
        return

    await msg.add_reaction("zoomeyes:811110244721098773")
    await msg.channel.send('Pretty code loading!')

    for code_snippet in code_snippets:
        filename = save_img(code_snippet)
        await msg.reply("Here's your code",
                        file=discord.File(filename))
        delete_img(filename)

client.run(TOKEN)
