import discord
import json
import datetime
from discord.ext import commands
from datetime import timezone
from core.classes import Cog_Extension

with open("setting.json", 'r', encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Event(Cog_Extension):
    # 成員加入訊息
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["bot_channel"]))
        print(f"{member} join!")
        await channel.send(f"{member} join!")

    # 成員離開訊息
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["bot_channel"]))
        print(f"{member} leave!")
        await channel.send(f"{member} leave!")

    # 刪除伺服器中的訊息
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

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, data):
        # 新增反應獲取身分組
        if data.emoji.name == "🟩":
            print(123456789)
            guild = self.bot.get_guild(data.guild_id)
            role = guild.get_role(875829371854798859)
            await data.member.add_roles(role)
        if data.emoji.name == "🟥":
            print(123456789)
            guild = self.bot.get_guild(data.guild_id)
            role = guild.get_role(875829371854798858)
            await data.member.add_roles(role)
        print(data.emoji)
        print(data.member)

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        count = 0
        async for auditlog in msg.guild.audit_logs(action=discord.AuditLogAction.message_delete):
            if count == 0:
                await msg.channel.send(auditlog.user.name)
                count += 1
        await msg.channel.send("刪除訊息內容："+str(msg.content))
        await msg.channel.send("訊息作者：" + str(msg.author))


def setup(bot):
    bot.add_cog(Event(bot))
