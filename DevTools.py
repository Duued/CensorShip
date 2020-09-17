import discord
import asyncio
from discord.ext import commands

class Devtools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def quit(self, ctx):
        await ctx.send(f"Quit Activated, Quitting!")
        await ctx.bot.logout()

    @commands.command()
    @commands.is_owner()
    async def disable(self, ctx, command):
        embed = discord.Embed(title="Devtools, Disabled command", description=f"Disabled command!", color=0x1500ff)
        ctx.bot.get_command(command).update(enabled=False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def enable(self, ctx, command):
        embed = discord.Embed(title="Devtools, Enabled command", description=f"Enabled command!", color=0x1500ff)
        ctx.bot.get_command(command).update(enabled=True)
        await ctx.send(embed=embed)

    @commands.command(name="botperms")
    @commands.is_owner()
    async def permissions(self, ctx):
        perms = [x for x,y in dict(ctx.channel.permissions_for(ctx.me)).items() if y]
        nice_perms = ""
        for perm in perms:
            nice_perms = nice_perms + "`" + perm + "`\n"
        await ctx.send(embed=discord.Embed(title="All of the bot's permissions:", description=nice_perms, color=0x0cff00))

def setup(bot):
    bot.add_cog(Devtools(bot))