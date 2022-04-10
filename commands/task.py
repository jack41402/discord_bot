import discord
import json
import asyncio
import datetime
from discord.ext import commands
from core.classes import Cog_Extension

jfile = "F:/github/helper/setting.json"


class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        print(ch)
        json.dump({"bot_channel": ch}, open(jfile, 'w'))
        await ctx.send(f"Set Channel: {self.channel.mention}")


def setup(bot):
    bot.add_cog(Task(bot))
