import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
import random
import http.client
from datetime import timedelta
import os
import json
import pprint
import requests as r
import base64
import json
import re
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
FTC_USERNAME = os.getenv("FTC_USERNAME")
FTC_TOKEN = os.getenv("FTC_TOKEN")

bot = commands.Bot()

socials = {
  "8405": ["https://www.instagram.com/millburnftc/"],
  "23650": ["https://www.instagram.com/millburnftc/"],
  "207": ["https://www.instagram.com/ftc207/"],
  "13302": ["https://linktr.ee/mkarobotics/", "https://instagram.com/mkarobotics"],
}

@bot.slash_command(
  name="first_slash",
  guild_ids=[1085701258687565854]
)
async def first_slash(ctx): 
  await ctx.respond("You executed the slash command!")

@bot.slash_command(
  name="search",
  description="Get information about an FTC team by its team number",
  guild_ids=[1085701258687565854]
)
async def search(ctx, team_number: int):
  """Get information about an FTC team by its team number"""
  try:
    data = r.get("https://ftc-api.firstinspires.org/v2.0/2022/teams?teamNumber={0}".format(int(team_number)), auth=(FTC_USERNAME, FTC_TOKEN))
    json = data.json()
    embed = discord.Embed(title="**{0}**".format("FTC Team Search by ID"), color=0xffffff)
    # embed.add_field(name="Stats (Raw): ", value="{0}".format(json), inline=False)
    embed.add_field(name="Team Number: ", value="{0}".format(json["teams"][0]["teamNumber"]), inline=True)
    embed.add_field(name="Full Name: ", value="{0}".format(json["teams"][0]["nameShort"]), inline=True)
    embed.add_field(name="School: ", value="{0}".format(json["teams"][0]["nameFull"]), inline=True)
    embed.add_field(name="Located in: ", value="{0}, {1}, {2}".format(json["teams"][0]["city"], json["teams"][0]["stateProv"], json["teams"][0]["country"]), inline=False)
    embed.add_field(name="Rookie Year: ", value="{0}".format(json["teams"][0]["rookieYear"]), inline=False)

    if str(team_number) in socials:
      social_links = socials[str(team_number)]
      if social_links:
        socials_string = "\n".join(social_links)
        embed.add_field(name="Socials", value=socials_string, inline=False)

    await ctx.respond(embed=embed)
  except Exception as e:
    embed = discord.Embed(title="**https://ftcscout.org/teams/{0}**".format(int(team_number)), color=0xffffff)
    if str(team_number) in socials:
      social_links = socials[str(team_number)]
      if social_links:
        socials_string = "\n".join(social_links)
        embed.add_field(name="Socials", value=socials_string, inline=False)
    await ctx.respond(embed=embed)

def get_ym_joke():
  resp = r.get("https://www.yomama-jokes.com/api/v1/jokes/random/")
  data = json.loads(resp.text)
  return data

def get_cat_image():
  resp = r.get("https://api.thecatapi.com/v1/images/search")
  json_data = json.loads(resp.text)
  quote = json_data[0]["url"]
  return quote


@bot.slash_command(
  name="ur_mom",
  description="haha funi",
  guild_ids=[1085701258687565854]
)
async def yourmom(ctx):
  joke = get_ym_joke()
  embed = discord.Embed(title="*{0}*".format(joke['joke']), color=0xff3300)
  await ctx.respond(embed=embed)
@bot.slash_command(
  name="cat",
  description="haha funi",
  guild_ids=[1085701258687565854]
)
async def cat(ctx):
  img = get_cat_image()
  
  embed = discord.Embed(title="**CAT IMAGE**", color=0x000000)
  embed.set_image(url=img)
  await ctx.respond(embed=embed)

bot.run(DISCORD_TOKEN)