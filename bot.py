import discord
import datetime
import asyncio
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from discord.ext import commands


bot = commands.Bot(command_prefix=commands.when_mentioned_or('botprefix'), case_insensitive=True)
TOKEN = "bottoken"

@bot.event
async def on_ready():
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url('webhookurlhere', adapter=AsyncWebhookAdapter(session))
    print(f"I am online!  {bot.user.name}")
    await bot.change_presence(status=discord.Status.online, activity = discord.Game("Watching people's mouths, prefix is c!"))
    await webhook.send(f" <:online:754362486177660969> I am online, logged in as {bot.user.name} <:online:754362486177660969>")
    
@bot.listen()
async def on_message(message: discord.Message):
    banned_words = ["word1","word2"]
    if any(word.lower() in message.content.lower() for word in banned_words):
      if message.author.bot: return
      await message.author.ban(reason=f"reason")

@bot.event
async def on_command_error(context, exception):
      await context.send(str(exception))

bot.load_extension("jishaku")
bot.load_extension("cogs.member")
bot.load_extension("cogs.moderation")
bot.load_extension("cogs.DevTools")
bot.load_extension("guildmanager")
bot.load_extension("cogs.utils")
bot.load_extension("riftgun")
bot.run(TOKEN)
