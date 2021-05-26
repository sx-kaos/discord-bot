import random
import os
import asyncio
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
async def help(ctx, user: discord.Member = None):
    if user is None:
      user = ctx.author
    embed=discord.Embed(color=1752220)
    embed.add_field(name=".ping", value="displays ping", inline=True)
    embed.add_field(name=".ban (@example)", value="bans the member @'d", inline=False)
    embed.add_field(name=".kick (@example)", value="kicks the member @'d", inline=False)
    embed.add_field(name=".mute (@example)", value="mutes the member @'d", inline=True)
    embed.add_field(name=".8ball (question)", value="answers the question asked", inline=False)
    embed.add_field(name=".tool", value="links a download to kaos's multi tool", inline=True)
    embed.add_field(name=".meme ", value="sends a random meme", inline=False)
    embed.add_field(name=".cursed", value="sends a cursed/weird image", inline=True)
    embed.add_field(name=".addbot", value="sends a link to add the bot", inline=False)
    embed.add_field(name=".toes", value="sends a random pic of toes", inline=True)
    embed.add_field(name=".clear (amount)", value="deletes the specified the amount of messages", inline=False)
    embed.add_field(name=".rng", value="sends a randomly generated numer", inline=True)
    embed.add_field(name=".twitch (what you want to search on twitch)", value="provides a channel link to the name given (e.g .twitch sx_kaos)", inline=False)
    embed.add_field(name=".sx_true ", value="takes you to sx_trues twitch channel (no this is not the owner of the bot)", inline=True)
    embed.add_field(name=".about", value="take a guess", inline=False)
    embed.add_field(name=".youtube (what you want to search on youtube) ", value="takes you to the search result on youtube for whatever you said", inline=True)
    embed.add_field(name=".shalom", value="shalom", inline=False)
    embed.add_field(name=".github", value="takes you to my github", inline=True)
    embed.set_footer(text="bot made by kaos#1807")
    await user.send(embed=embed)
   



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
    embed = discord.Embed(title = "Random Number", description = (random.randint(1, 101)), color = (0xF85252))
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
async def porn(ctx):
    await ctx.send(f'https://tenor.com/view/excited-loading-please-wait-gif-13934660')


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
async def about(ctx):
    await ctx.send(f'this is a multi purpose discord bot made by kaos. for a list of commands try .help')


@client.command(aliases=['youtube'])
async def _youtube(ctx,*, question):
    await ctx.send(f'https://www.youtube.com/results?search_query={question}')


@client.command()
async def sx_true(ctx):
    await ctx.send(f'https://twitch.tv/sx_true')




client.run('TOKEN')
