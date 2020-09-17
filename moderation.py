import discord
import asyncio
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ban", aliases=['b'])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Assists people in leaving the server. For those extra stubborn people who can't find the leave button,
    so continue to annoy you into making them leave. But along side leaving, its also locking the door.
        """
        if member.top_role >= ctx.author.top_role:
            await ctx.send("This user can't be banned due to hierachry.")
        else:
            await member.ban(reason=reason)
            await ctx.send("Banned")

    @commands.command()
    @commands.bot_has_guild_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"k")
                return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.guild)
    async def softban(self, ctx, member: discord.Member, *, reason="reason"):
                await member.ban(reason=reason)
                await member.unban(reason=reason)
                await ctx.send(f"softbanned {member}")

    @commands.command(name="purge", aliases=['boom','delete','clear'])
    @commands.bot_has_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=5):
        embed = discord.Embed(title="Messages Purged", description=f"{ctx.author} purged {amount} messages!")
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(embed=embed)

    @commands.command(name="kick", aliases=['assistedLeave'])
    @commands.bot_has_guild_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Assists people in leaving the server. For those extra stubborn people who can't find the leave button,
    so continue to annoy you into making them leave.
        """
        if member.top_role >= ctx.author.top_role:
            await ctx.send("This user can't be kicked due to hierachry.")
        else:
            await member.kick(reason=reason)
            await ctx.send("Kicked")

def setup(bot):
    bot.add_cog(Moderation(bot))