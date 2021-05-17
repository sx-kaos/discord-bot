import random
import os
import youtube_dl
import discord
from discord.ext import commands
from os import system

client = commands.Bot(command_prefix = '.')

print("bot is up")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
  print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
  print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx,*, question):
  responses = [ 'It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As i see i it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'No.']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=True, send_messages=False, read_message_history=True, read_messages=True)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")


@client.command()
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)
  await ctx.send(f'cleared {amount} messages!')



@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user


    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'unbanned {user.mention}')
      return


@client.event
async def on_ready(): 
  await client.change_presence(status=discord.Status.online, activity=discord.Game('up and running'))

client.remove_command('help')


@client.command()
async def help(ctx):
  
  embed=discord.Embed(title="help", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", description="the current commands are .help  .tool  .8ball .mute .cursed .ban  .kick  .addbot and .clear")
  embed.set_author(name="𝚔𝚊𝚘𝚜 #1807", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  await ctx.send(embed=embed)

@client.command()
async def addbot(ctx):
  await ctx.send(f'https://discord.com/api/oauth2/authorize?client_id=839512470640525373&permissions=8&scope=bot')


@client.command()
async def tool(ctx):

    embed=discord.Embed(title="multi tool <----- click this", url="https://cdn.discordapp.com/attachments/839508203665621014/843432813978189834/mutli_tool_WIP.bat", description="multi tool made by kaos", color=0)
    await ctx.send(embed=embed)
    



@client.command()
async def sx_true(ctx):
        await ctx.send(f'https://cdn.discordapp.com/attachments/829034757341970544/841762760886321172/vOw1Q6HF1N2jciWhim-D32jkDyY398uJOItzYSntGF2Ss7lLooi1KPSPVNKRO_k6SRRFhBXt5b_-rquOCAbsFYmZ7zeU9myezAG6.png')
 


@client.command(aliases=['cursed'])
async def _cursed(ctx):
  responses = [ 'https://preview.redd.it/zlsa4jr1emy61.jpg?width=640&crop=smart&auto=webp&s=73bc5b7f0856098089ea8c6e168cf7a518066140',
                'https://cdn.discordapp.com/attachments/829034757341970544/842832443068383272/8e1b7ae12212f38e211fd58348905181.jpg',
                'https://cdn.discordapp.com/attachments/829034757341970544/842832411678998528/23-of-the-best-meaning-worst-cursed-images-ever-3.png',
                'https://cdn.discordapp.com/attachments/829034757341970544/842832230316245002/e53708261b88be57a552fbc34662dddc.png',
                'https://cdn.discordapp.com/attachments/829034757341970544/842832278212444190/spongebob-real-life.jpg',
                'https://preview.redd.it/pc806icjnky61.jpg?width=640&crop=smart&auto=webp&s=316a59178ab9ac7a8facde8849b0a9ab99ae557e',
                'https://preview.redd.it/wy3nln9ps4y61.jpg?width=640&crop=smart&auto=webp&s=91f3dc0cb07dd627a99c7c667fd1b6d3b9120bc3',
                'https://preview.redd.it/iw7lksspo4z61.jpg?width=640&crop=smart&auto=webp&s=075deda0005812e5ccbbc7b8c1c3511a23b59973',
                'https://i.redd.it/d4q68pxobxy61.png',
                'https://preview.redd.it/1hlbhqnvaby61.jpg?width=640&crop=smart&auto=webp&s=0cb81116ea0e31f12b00ed8e89abc7e68923e5f5',
                'https://i.redd.it/4fekx602rzw61.jpg',
                'https://preview.redd.it/6wci59ovgpw61.jpg?width=960&crop=smart&auto=webp&s=b6289c4bedc4ef6be594d1498571acb57a864f2e',
                'https://preview.redd.it/iwictx3gf8w61.jpg?width=640&crop=smart&auto=webp&s=93bba3af47c26145d6e4e6df4fa74e3134eabbc7',
                'https://i.redd.it/86c3cm7772w61.jpg']
  await ctx.send(f'{random.choice(responses)}')
  


client.run('TOKEN')
