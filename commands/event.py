import discord
import json
import datetime
from discord.ext import commands
from datetime import timezone
from core.classes import Cog_Extension

with open("setting.json", 'r', encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["bot_channel"]))
        print(f"{member} join!")
        await channel.send(f"{member} join!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["bot_channel"]))
        print(f"{member} leave!")
        await channel.send(f"{member} leave!")

    # @commands.Cog.listener()
    # async def on_message(self, msg):
    #     if msg.startswith == 123 and msg.author != self.bot.user:
    #         await msg.channel.send(msg.content)

    @commands.command()
    async def em(self, ctx):
        embed = discord.Embed(title="jack41402", url="https://www.facebook.com/jack41402", description="none",
                              color=0x00ccff, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Jack", url="https://www.facebook.com/jack41402", icon_url="https://imgur.com/a/38DFlbf")
        embed.add_field(name="11", value="1111", inline=True)
        embed.add_field(name="22", value="2222", inline=True)
        embed.add_field(name="33", value="3333", inline=True)
        embed.add_field(name="44", value="4444", inline=True)
        embed.set_footer(text="123456789")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)

    # 處理"指令"發生的錯誤 Error Handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("判斷正確")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("沒這指令啦")
        await ctx.send(error)


def setup(bot):
    bot.add_cog(Event(bot))
