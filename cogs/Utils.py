import discord
from discord.utils import get
from discord.ext import commands
import random
import sys
import discord
from discord.utils import get
from discord.ext import commands
import random
import http.client
from datetime import timedelta
import os
import json
import pprint
import requests as r
import base64
from dotenv import load_dotenv
import json
import re


class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Utils.cog READY")

    
    @commands.command()
    async def ping(self, ctx):
        """Check ping/latency of your connection to the bot"""
        embed = discord.Embed(title="Pong!", color=0x000000)
        embed.add_field(name="Latency: ", value=f'{round(self.bot.latency * 1000)} ms')
        await ctx.reply(embed=embed)


async def setup(bot):
    await bot.add_cog(Utils(bot))
