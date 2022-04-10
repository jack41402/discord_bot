import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension


class React(Cog_Extension):
    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")


def setup(bot):
    bot.add_cog(React(bot))
