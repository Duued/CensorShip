import discord
import asyncio
from discord.ext import commands



class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ping(self, ctx):
        """Tests the latency of the bot"""
        embed = discord.Embed(title="Ping!", description=f"\U0001f3d3: Pong! `{round(self.bot.latency * 1000)} ms`", color=0x3bff00)
        await ctx.send(embed=embed)

    @commands.command(name="Invite", Aliases=['addbot'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def invite(self, ctx):
        """Invite the bot or join the support server!"""
        embed = discord.Embed(title="Invites", description=f"invite the bot [here](https://discord.com/oauth2/authorize?client_id=739125103505309747&permissions=126159&redirect_uri=https%3A%2F%2Fdiscord.gg%2FCyDDBpf&response_type=code&scope=bot%20identify), or join the support server [here](https://discord.gg/CyDDBpf)", color=0x3bff00)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def credits(self, ctx):
        """See the important people that help make the bot possible!"""
        embed = discord.Embed(title="Credits", description=f"The inspiration for me to start my first bot, <@421698654189912064>, the very first person to help me with a bot, <@344878404991975427>, debugging help <@511655498676699136>, <@438733159748599813>, <@317731855317336067>, and finally <@421698654189912064> himself!", color=0xfaff00)
        embed2 = discord.Embed(title="One last thing...", description=f"One last person to thank, {ctx.author.mention} for using my bot! If you like it, please suggest it to your friends, if not, please join the support server with `c!support` and then suggest it to the developer (server owner)", color=0xfaff00)
        await ctx.send(embed=embed)
        await ctx.send(embed=embed2)

    @commands.command(name="required_permissions", aliases=['perms'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def required_permissions(self, ctx):
        """View the permissions that the bot needs to function correctly!"""
        embed = discord.Embed(title="Bot's Required Permissions", description="Permissions needed: `kick_members`, `ban_members`, `embed_links`, `attach_files`, `create_instant_invite`, `view_audit_logs`, and `manage_messages`. `Administrator` isn't required but unlocks more functionality", color=0xeeff00)
        await ctx.send(f"If you can't see the embed message below, please give me `embed_links` and try again!")
        await ctx.send(embed=embed)
        
    @commands.command()
    @commands.cooldown(1, 180, commands.BucketType.user)
    async def feedback(self, ctx,* , message):
        embed = discord.Embed(title="Feedback", description=f"{ctx.author} (`{ctx.author.id}`) sent feedback! Their feedback is **{message}**", color=0x00ff00)
        embed2 = discord.Embed(title="Feedback Sent!", description=f"Your feedback has been launched!", color=0x00ff00)
        feedback = ctx.bot.get_channel(channelid)
        await ctx.send(embed=embed2)
        await feedback.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 180, commands.BucketType.user)
    async def suggest(self, ctx,* , suggestion):
        embed = discord.Embed(title="Suggestion", description=f"{ctx.author} (`{ctx.author.id}`) sent a suggestion, their suggestion is **{suggestion}**", color=0x00ff00)
        embed2 = discord.Embed(title="Feedback Sent!", description=f"Your suggestion has been launched!", color=0x00ff00)
        suggestions = ctx.bot.get_channel(channelid)
        await ctx.send(embed=embed2)
        await suggestion.send(embed=embed)

    @commands.command(name="git")
    @commands.cooldown(1, 25, commands.BucketType.user)
    async def github(self, ctx):
        """Get the link to this github repository!"""
        embed = discord.Embed(title="My GitHub!", description="https://github.com/Duued/CensorShip", color=0x00ff00)
        await ctx.send(embed=embed)
        
    #@commands.command()
    #@commands.cooldown(1, 2, commands.BucketType.user)
    #async def lyrics(self, ctx, *, songname):
        #async with aiohttp.ClientSession() as session:
            #token = "C7OkacZ08cNUBeyYMS5kEngRgLJGf92k" # Put token here
            #async with session.get(f'https://api.ksoft.si/lyrics/search?q={songname}&limit=1', headers={'Authorization': f'{token}') as response:
                #response = await response.text()
            #embed = discord.Embed(title="Song Lyrics", color=0x728da)
            #embed.add_field(name="Lyrics", value=f"{response}", inline=False)            
            #embed.set_footer(text="Lyrics Provided by Ksoft.Si API")
            #await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Member(bot))
