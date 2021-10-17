import random
import os
import asyncio
import sys
import colorama
import discord
from discord.ext import commands
from os import system
from datetime import datetime
from datetime import date
from datetime import datetime
from typing import Optional
from discord import Embed, Member
from discord.ext.commands import Cog
from colorama import init
from discord.utils import find
from discord.ext.commands import CheckFailure
from discord.ext.commands import command, has_permissions
from pypresence import Presence
import time

init()
system('title lunar rpc')

RPC = Presence("856168902803587082") 
RPC.connect() 
RPC.update(large_image="untitled", large_text="https://dsc.gg/kaos", start=time.time())
client = commands.Bot(command_prefix = '.')





def logo():
    print('\033[1;36;40m' + '')
    print('\033[1;36;40m' + '                                            ╔═╗╔═╦══╦═══╦═══╦══╗')
    print('\033[1;36;40m' + '                                            ║║╚╝║╠╣╠╣╔═╗║╔═╗╠╣╠╝')
    print('\033[1;36;40m' + '                                            ║╔╗╔╗║║║║╚═╝║║─║║║║')
    print('\033[1;36;40m' + '                                            ║║║║║║║║║╔╗╔╣╚═╝║║║')
    print('\033[1;36;40m' + '                                            ║║║║║╠╣╠╣║║╚╣╔═╗╠╣╠╗')
    print('\033[1;36;40m' + '                                            ╚╝╚╝╚╩══╩╝╚═╩╝─╚╩══╝v2')
    print('\033[1;36;40m' + '')
    print('\033[1;36;40m' + '                                           ╔════════════════════╗')
    print('\033[1;36;40m' + '                                           ║  Welcome to mirai. ║')
    print('\033[1;36;40m' + '                                           ║    Made by Kaos    ║')
    print('\033[1;36;40m' + '                                           ╚════════════════════╝')
logo()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    now = datetime.now()

    d1 = today.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")
    print("bot started at:", d1, current_time)


@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} Was kicked for "{reason}"')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You Do Not Have The Right Permissions To Use This Command")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} Was Banned for "{reason}"')

@kick.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You Do Not Have The Right Permissions To Use This Command")
        
                   

@client.command()
async def ping(ctx):
  await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx,*, question):
  responses = [ 'It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'one can dream',
                'quit joking yourself',
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
  await client.change_presence(status=discord.Status.online, activity=discord.Game('.help'))

client.remove_command('help')
client.remove_command('rename')

@client.command()
async def help(ctx):
        embed=discord.Embed(color=1752220)
        embed.add_field(name=".ping", value="displays ping", inline=True)
        embed.add_field(name=".ban (@example)", value="bans the member @'d", inline=False)
        embed.add_field(name=".kick (@example)", value="kicks the member @'d", inline=False)
        embed.add_field(name=".mute (@example)", value="mutes the member @'d", inline=True)
        embed.add_field(name=".say (what u want to say)", value="says whatever u want (e.g .say hello)", inline=False)
        embed.add_field(name=".tool", value="links a download to kaos's multi tool", inline=True)
        embed.add_field(name=".meme ", value="sends a random meme", inline=False)
        embed.add_field(name=".cursed", value="sends a cursed/weird image", inline=True)
        embed.add_field(name=".addbot", value="sends a link to add the bot", inline=False)
        embed.add_field(name=".toes", value="sends a random pic of toes", inline=True)
        embed.add_field(name=".clear (amount)", value="deletes the specified the amount of messages", inline=False)
        embed.add_field(name=".rng", value="sends a randomly generated numer", inline=True)
        embed.add_field(name=".twitch (what you want to search on twitch)", value="provides a channel link to the name given (e.g .twitch sx_kaos)", inline=False)
        embed.add_field(name=".about", value="take a guess", inline=True)
        embed.add_field(name=".youtube (what you want to search on youtube) ", value="takes you to the search result on youtube for whatever you said", inline=False)
        embed.add_field(name=".shalom", value="shalom", inline=True)
        embed.add_field(name=".github", value="takes you to my github", inline=False)
        embed.add_field(name=".suggest (suggestion)", value="sends the suggestion to me (kaos, the owner)", inline=True)
        embed.add_field(name=".support", value="takes you to the discord bot support server", inline=False)
        embed.add_field(name=".rename (name)", value="names the server whatever is inputted", inline=True)
        embed.add_field(name=".hash", value="generates a random hash that is ether 8, 16, 32,64 or 128 bit. just type .hash(8, 16, 32, 64 or 128)", inline=False)
        embed.add_field(name=".bitcoin", value="claim a free bitcoin!", inline=True)
        embed.add_field(name=".instagram", value="my instagram", inline=False)
        embed.add_field(name=".twitter", value="my twitter", inline=True)
        embed.add_field(name=".bored", value="try it if your bored", inline=False)
        embed.add_field(name=".alphabet", value="sends the english alphabet (in case you forgot it)", inline=True)
        embed.set_footer(text="bot made by 『𝚔𝚊𝚘𝚜』#1565 on discord (there are secret commands btw have fun finding them)")
        await ctx.send(embed=embed)

        embed=discord.Embed(title="help 2", description="help 2", color=1752220)
        embed.add_field(name=".count", value="sends a mesage that counts ", inline=False)
        embed.add_field(name=".user", value="sends user info", inline=True)
        embed.add_field(name=".serverinfo", value="sends server info", inline=False)
        embed.add_field(name=".rn", value="sends the date and time", inline=True)
        embed.add_field(name=".setup", value="setups up a server with text, voice and admin channels", inline=False)
        embed.add_field(name=".info", value="information about the bot", inline=True)
        embed.set_footer(text="bot made by 『𝚔𝚊𝚘𝚜』#1565 on discord (there are secret commands btw have fun finding them)")
        await ctx.send(embed=embed)


@client.command()
async def addbot(ctx):
  await ctx.send(f'https://discord.com/api/oauth2/authorize?client_id=839512470640525373&permissions=8&scope=bot')


@client.command()
async def tool(ctx):

    embed=discord.Embed(title="multi tool <----- click this", url="https://github.com/sx-kaos/multi-tool", description="multi tool made by kaos", color=0)
    await ctx.send(embed=embed)





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
                'https://cdn.discordapp.com/attachments/747795625852272762/868606783583830036/Women-dancing-naked-in-a--007.png',
                'https://i.redd.it/86c3cm7772w61.jpg']
  await ctx.send(f'{random.choice(responses)}')


@client.command(aliases=['meme'])
async def _meme(ctx):
    responses = [ 'https://preview.redd.it/oy4nqdoudoz61.jpg?width=640&crop=smart&auto=webp&s=3df0e04fa81bfba97f457af7d9b46e60cca80380',
                  'https://preview.redd.it/iufury6njnz61.jpg?width=640&crop=smart&auto=webp&s=d393ed6ccb951722743dff2181aaf5e7e09d074f',
                  'https://preview.redd.it/zju1xt921mz61.jpg?width=640&crop=smart&auto=webp&s=07ebbafad02b21e9ff8bb94e88fbd2b4180d8da8',
                  'https://pbs.twimg.com/profile_images/3417714567/46298b9ed1c056537d7a0ab67176ffd7_400x400.jpeg',
                  'https://cdn.discordapp.com/attachments/839508203665621014/843910798988410921/2Q.png',
                  'https://cdn.discordapp.com/attachments/839508203665621014/843910886225084417/funnyrapememe.png',
                  'https://64.media.tumblr.com/e66ac627fbd5824bc9fd579b06fc9cde/tumblr_owziyjVRna1ub0po4o1_400.jpg',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcG5T7X4oteJyFK8RkHwe7Zh74TejRzm_57w&usqp=CAU',
                  'https://www.dailymoss.com/wp-content/uploads/2017/12/1F42DE2C-D7F4-467C-A3CC-F916DD1229E1.jpg',
                  'https://pics.me.me/me-posts-an-offensive-meme-me-people-who-enjoy-dark-46889882.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846084875924668488/3a728efcfc2ab94ef46cc6d4e6adc05a.png',
                  'https://i.pinimg.com/originals/17/25/62/1725628658704672a5c5ce86bacf854a.jpg',
                  'https://pbs.twimg.com/media/DXUQOCYW4AA0p9n.jpg',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLVzY9DcY6IcarwoyTtWao2HDrQc1s3mEKMg&usqp=CAU',
                  'https://i.pinimg.com/736x/ec/43/8c/ec438c21d17d10931793755c26313ce5.jpg',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ__MHDSSeaQY_G9MHn3-TEPmuSkPy1uyVBBQ&usqp=CAU',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVGfIMJD9Ge-EfgYPgcTE14MjEHLzhTXWuvw&usqp=CAU',
                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ87uGRWr2tyQlM83H4MdwTWWx2FHw_pt4UFA&usqp=CAU',
                  'https://cdn.discordapp.com/attachments/829034757341970544/843912733253959741/zn87xed0f4251.png',
                  'https://pbs.twimg.com/media/DTmET1gVMAAx93x.jpg']
    await ctx.send(f'{random.choice(responses)}')



@client.command()
async def give(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)
        await ctx.send(f'successfully given {role.mention} to {user.mention}.')

@client.command()
async def remove(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.remove_roles(role)
        await ctx.send(f'successfully removed {role.mention} to {user.mention}.')

@client.command()
async def nuke(ctx):
    await ctx.send(f'lol what?')

@client.command()
async def wizz(ctx):
    await ctx.send(f'you thought')


@client.command(pass_context = True)
async def rng(ctx):
    embed = discord.Embed(title = "Random Number", description = (random.randint(1, 100)), color = (0xF85252))
    await ctx.send(embed = embed)

@client.command(aliases=['toes'])
async def _toes(ctx):
    responses = [ 'https://cdn.discordapp.com/attachments/800789841859575810/846084292874600488/R9405adf8a327f6f484cf54f765942bd1.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846084350369071114/foot-fetish-485826.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846084487711686656/R5bf41d5d7c3f1b0f634c367d80d979f8.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846084705216102440/auGp9GHNnhJqa9zfgt76rNntYxGYpQgc57a6UcFqJqw.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846084800757628958/R152b5c23c76921a80e6b784fca1ee7d5.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846084875924668488/3a728efcfc2ab94ef46cc6d4e6adc05a.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846085133608943616/OIP.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846085238735634451/R972936c14da10ea92a668cfb081d0311.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846085517279232080/OIP.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846085633835008070/cursed-images-beans-6.jpg',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846086155283595304/0c251449de7fe9b0e3833626d7c69454.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846086284535529483/R6d1437ffcc959f8d299573e022c1dd43.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846086949701812264/R264c9b211a989a724ecb1c8c42c5bda0.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846087150205403217/baby-feet-cold-fb.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846087387750334504/R9f610c717d5b25ee90fee9907be2f7ad.png',
                  'https://cdn.discordapp.com/attachments/800789841859575810/846087476471660584/adrien-broner-feet-800x424.png',]
    await ctx.send(f'{random.choice(responses)}')



@client.command()
async def shalom(ctx):
    await ctx.send(f'shalom jackie!')


@client.command()
async def github(ctx):
    await ctx.send(f'https://github.com/sx-kaos')


@client.command(aliases=['twitch'])
async def _twitch(ctx,*, question):
    await ctx.send(f'https://twitch.tv/{question}')


@client.command()
async def rules(ctx):
    embed=discord.Embed(color=1752220)
    embed.add_field(name="1.", value="offensive jokes are fine just dont go to far", inline=False)
    embed.add_field(name="2.", value="dont be a homophobe/racist/transphobe/asshole", inline=True)
    embed.add_field(name="3.", value="dont act as if you are admin. if you have an issue contact either kaos or an admin", inline=False)
    embed.add_field(name="4.", value="admins have the final say", inline=True)
    embed.add_field(name="5.", value="dont earrape", inline=False)
    embed.add_field(name="6.", value="dont do anything illegal", inline=True)
    embed.add_field(name="7.", value="follow discord tos", inline=False)
    embed.add_field(name="8.", value="have common sense", inline=True)
    await ctx.send(embed=embed)


@client.command()
async def about(ctx):
    await ctx.send(f'this is a multi purpose discord bot made by kaos. for a list of commands try .help')


@client.command(aliases=['youtube'])
async def _youtube(ctx,*, question):
    await ctx.send(f'https://www.youtube.com/results?search_query={question}')


@client.command()
async def sx_true(ctx):
    await ctx.send(f'https://twitch.tv/sx_true')

@client.command(aliases=['suggest'])
async def _suggest(ctx,*, question):
    print(f"{question}")

@client.command()
async def support(ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
      await user.send(f'https://dsc.gg/kaos')


@client.command()
async def baguette(ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
    await ctx.send(f':flag_fr:')

@client.command()
async def tea(ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
    await ctx.send(f':flag_gb:')

@client.command()
async def rename(ctx,*, question):
    await ctx.guild.edit(name=question)

@client.command()
async def code(ctx):
    await ctx.send(f'you can find the code for the bot on my github')

@client.command()
async def hash(ctx):
    await ctx.send(f'its .hash(8,16,32,64 or 128)')


@client.command()
async def hash8(ctx):
    hash = random.getrandbits(8)
    await ctx.send("hash value: %2x" %hash)


@client.command()
async def hash16(ctx):
    hash = random.getrandbits(16)
    await ctx.send("hash value: %2x" %hash)

@client.command()
async def hash32(ctx):
    hash = random.getrandbits(32)
    await ctx.send("hash value: %2x" %hash)

@client.command()
async def hash64(ctx):
    hash = random.getrandbits(64)
    await ctx.send("hash value: %2x" %hash)

@client.command()
async def hash128(ctx):
    hash = random.getrandbits(128)
    await ctx.send("hash value: %2x" %hash)

@client.command()
@commands.has_permissions(manage_channels = True)
async def lockdown(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send( ctx.channel.mention + " ***is now in lockdown.***")

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(ctx.channel.mention + " ***has been unlocked.***")

@client.command()
async def instagram(ctx):
    embed=discord.Embed(title="instagram", url="https://www.instagram.com/not.kaos.420/")
    await ctx.send(embed=embed)

@client.command()
async def twitter(ctx):
    embed=discord.Embed(title="twitter", url="https://twitter.com/Kaos99260353")
    await ctx.send(embed=embed)

@client.command()
async def bitcoin(ctx):
    await ctx.send(f' heres your free bitcoin! <:bit:853613154432057354>')

@client.command()
async def bored(ctx):
    await ctx.send(f' if your bored then why not try learning a new skill such as programming or learning to draw')


@client.command()
async def alphabet(ctx):
    await ctx.send(f' a b c d e f g h i j k l m n o p q r s t u v w x y z')

@client.command()
async def say(ctx, *, question):
      await ctx.send(f'{question}')



@client.command()
async def rn(ctx):

    now = datetime.now()
    today = datetime.today()
    d1 = today.strftime("%d/%m/%Y")
    current_time = now.strftime("%H:%M:%S")

    embed=discord.Embed(color=1752220)
    embed.add_field(name="current time is:", value=current_time, inline=False)
    embed.add_field(name="current date is:", value=d1, inline=True)
    await ctx.reply(embed=embed)



@client.command()
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = ""


  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)

  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.add_field(name="Server ID", value=id, inline=False)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.reply(embed=embed)



@client.command()
async def user(ctx, target: Optional[Member]):
    target = target or ctx.author
    embed = Embed(title="User information",
    colour=target.colour,
    timestamp=datetime.utcnow())
    embed.set_thumbnail(url=target.avatar_url)
    fields = [("Name", str(target), True),
    ("ID", target.id, True),
    ("Bot?", target.bot, True),
    ("Top role", target.top_role.mention, True),
    ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
    ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
    ("Boosted", bool(target.premium_since), True)]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)

    await ctx.send(embed=embed)

@client.command()
async def count(ctx):
  message = await ctx.send("starting counting")
  await asyncio.sleep(1)
  x = 1
  while True:
      await message.edit(content=(x))
      await asyncio.sleep(2)
      x += 1


@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send(f'**thank you for adding mirai a bot made by not.kaos.420 on instagram**\n to get started try using the help command.\n ***the bots prefix is (.) minus the brackets.***')


@client.command()
async def clip(ctx, member : discord.Member):
    responses = [ 'get pinged',
                  'pinged',
                  'u like my pings?',
                  'pinged?',
                  'pinged lol']
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
    await ctx.send(f'{member.mention}{random.choice(responses)}')
    asyncio.sleep(0.5)
     
    
@client.command()
async def info(ctx):
    embed=discord.Embed(title="about the bot:", color=0x5af589)
    embed.add_field(name="mirai was created at:", value="Wed, 05 May 2021 14:42:50 UTC", inline=False)
    embed.add_field(name="mirai was created by: ", value="746758674067750952 (discord id)", inline=True)
    embed.add_field(name="mirai's named after:", value="a powerful botnet also called mirai, no its not named after the anime", inline=False)
    embed.set_footer(text="bot created by not.kaos.420 on instagram")
    await ctx.send(embed=embed)




@client.command()
async def load(ctx):
    message = await ctx.send("starting loading")
    await asyncio.sleep(0.2)
    one = "[■ ] 10%"
    two = "[■■ ] 20%"
    three = "[■■■ ] 30%"
    four = "[■■■■ ] 40%"
    five = "[■■■■■ ] 50%"
    six = "[■■■■■■ ] 60%"
    seven = "[■■■■■■■ ] 70%"
    eight = "[■■■■■■■■ ] 80%"
    nine = "[■■■■■■■■■ ] 90%"
    ten = "[■■■■■■■■■■] 100%"

    await message.edit(content=(one))
    await asyncio.sleep(2)
    await message.edit(content=(two))
    await asyncio.sleep(2)
    await message.edit(content=(three))
    await asyncio.sleep(2)
    await message.edit(content=(four))
    await asyncio.sleep(2)
    await message.edit(content=(five))
    await asyncio.sleep(2)
    await message.edit(content=(six))
    await asyncio.sleep(2)
    await message.edit(content=(seven))
    await asyncio.sleep(2)
    await message.edit(content=(eight))
    await asyncio.sleep(2)
    await message.edit(content=(nine))
    await asyncio.sleep(2)
    await message.edit(content=(ten))
    await asyncio.sleep(2)
    await message.edit(content="finished loading")

@client.command()
async def hack(ctx):
    message = await ctx.send("starting hacking")
    await asyncio.sleep(0.2)
    await message.edit(content=("loading scary dark web..."))
    await asyncio.sleep(2)
    await message.edit(content=("loaded black market..."))
    await asyncio.sleep(2)
    await message.edit(content=("successfully bought copious amounts of ketamine..."))
    await asyncio.sleep(2)
    await message.edit(content=("hacking government..."))
    await asyncio.sleep(2)
    await message.edit(content=("hacked the government..."))
    await asyncio.sleep(2) 
    await message.edit(content=("nuclear launch codes found..."))
    await asyncio.sleep(2)
    await message.edit(content=("sending nukes to north korea..."))
    await asyncio.sleep(2)
    await message.edit(content=("hack finished"))

        

@client.command()
async def send(ctx):
    await ctx.channel.purge(limit=2)
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    message = input("enter message here: ")
    await ctx.send(f"{message}")
    system('cls' if os.name == 'nt' else 'clear')
    logo()
    
@client.command()
async def children(ctx):
    await ctx.send(f"fucking nonce")

@client.command()
async def kids(ctx):
    await ctx.send(f"creep")


client.run(token)



