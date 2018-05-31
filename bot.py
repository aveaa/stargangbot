# Tutbot by Da532

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='/')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def invite(ctx):
    embed = discord.Embed(color=0x00ff00)
    await bot.say("casa vin eu la tine - https://discordapp.com/api/oauth2/authorize?client_id=444201659053375488&permissions=8&scope=bot casa vi tu la mine - https://discord.gg/HeUeFpy")
    print ("invie +1")

@bot.command(pass_context=True)
async def giveway(ctx):
    embed = discord.Embed(color=0x00ff00)
    await bot.say("@everyone un nou giveway s-a deschis apăsați sus pe :tada: ")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(color=0x00ff00)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say("Membrul acesta a fost banat".format(user.name))
    await bot.kick(user)
    print ("baned")

bot.run(TOKEN)
