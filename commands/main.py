import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("hi")

    @commands.group()
    async def codetest(self, ctx):
        pass

    @codetest.command()
    async def python(self, ctx):
        await ctx.send("Python")

    @codetest.command()
    async def java(self, ctx):
        await ctx.send("Java")

    @codetest.command()
    async def cpp(self, ctx):
        await ctx.send("C++")

    @commands.command()
    async def cmdA(self, ctx, num):
        await ctx.send(num)

def setup(bot):
    bot.add_cog(Main(bot))
