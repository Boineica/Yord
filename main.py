import discord
import random
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix='y!')

@bot.command()
async def about(ctx):
    print("The command \"y!about\" was used ") # The purpose for this is to track. This is optional.
    await ctx.send('Hi!\nI\'m Yord!\nI\'m some bot that uhh...\n ||Want to join the support server? Soon! || \nI\'m a bot made by User#0000!\n||More to come soon!||')

@bot.command()
async def chitchot(ctx):
    print("The command \"y!chitchot\" was used ")
    await ctx.send("Whoa! You found me! I chose the name \"chitchot\" because i ran out of ideas for names. This is a upcoming command. See ya!\nBy User#0000.")
    
@bot.command()
async def yord2ten(ctx):
    print("The command \"y!yord2ten\" was used ")
    await ctx.send("Not again!")
    
@bot.command()
async def randomnumber(ctx):
    print("The command \"y!randomnumber\" was used ")
    rndnu = random.randint(1, 9999999)

    print("A random number is generating")
    await ctx.send("Random number is generating.")
    
    print("The random number was generated")
    await ctx.send("Your generated number is: {}!".format(rndnu))

bot.run("ODYzOTg2MDk1MTc5MTY5Nzky.YOu3wQ.Zp3qreyWXQYAfPbw-ni0oTDM2fg")












# If you think this token is the original yord token. You're screwed! Screwed! HAHAHAHAHAHAHAHAHAHAHAHAHA! Log-in into this bot and you're screwed! HAHAHAHAHA!
