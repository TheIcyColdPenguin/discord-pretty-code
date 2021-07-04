from io import BytesIO

import discord
from discord.ext import commands

from config import TOKEN
from helpers import get_code, check_msg_exists
from scraper import get_img

bot = commands.Bot(command_prefix='!', case_insensitive=True)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has logged in!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error


@bot.command(aliases=['p'])
async def prettifier(ctx):
    if ctx.author.bot:
        return

    msg = ctx.message
    code_snippets = get_code(msg.content)[:5]

    if len(code_snippets) == 0:
        return

    await msg.add_reaction("zoomeyes:811110244721098773")
    await msg.channel.send('Pretty code loading!')

    for code_snippet in code_snippets:
        img_content = get_img(code_snippet)
        img_file = discord.File(
            fp=BytesIO(img_content),
            filename="code.png"
        )

        if await check_msg_exists(msg):
            await msg.reply("Here's your code",
                            file=img_file)
        else:
            await msg.channel.send(f"<@{ctx.author.id}>, Here's your code", file=img_file)

bot.run(TOKEN)
