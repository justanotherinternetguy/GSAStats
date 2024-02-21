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

load_dotenv()
FTC_USERNAME = os.getenv("FTC_USERNAME")
FTC_TOKEN = os.getenv("FTC_TOKEN")

class FTC(commands.Cog):
    """"ALOT OF STUFF DOESNT WORK LMAO"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("FTC.cog READY")
    
    @commands.command()
    async def search(self, ctx, teamNumber: int):
        """Get information about an FTC team by its team number"""
        data = r.get("https://ftc-api.firstinspires.org/v2.0/2022/teams?teamNumber={0}".format(int(teamNumber)), auth=(FTC_USERNAME, FTC_TOKEN))
        json = data.json()
        embed = discord.Embed(title="**{0}**".format("FTC Team Search by ID"), color=0xffffff)
        # embed.add_field(name="Stats (Raw): ", value="{0}".format(json), inline=False)
        embed.add_field(name="Team Number: ", value="{0}".format(json["teams"][0]["teamNumber"]), inline=True)
        embed.add_field(name="Full Name: ", value="{0}".format(json["teams"][0]["nameShort"]), inline=True)
        embed.add_field(name="School: ", value="{0}".format(json["teams"][0]["nameFull"]), inline=True)
        embed.add_field(name="Located in: ", value="{0}, {1}, {2}".format(json["teams"][0]["city"], json["teams"][0]["stateProv"], json["teams"][0]["country"]), inline=False)
        embed.add_field(name="Rookie Year: ", value="{0}".format(json["teams"][0]["rookieYear"]), inline=False)
        await ctx.reply(embed=embed)


        
async def setup(bot):
    await bot.add_cog(FTC(bot))
