import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')
client = discord.Client()

@bot.event
async def on_ready():
    print("[SB] Le bot est connecté au discord")

def Ischannel(channel):
    channelId = channel
    targetChannel = 847036972547440660

    if channelId != targetChannel:
        return False
    else:
        return True

async def SetUserRole(nameRole, user, context,message ):
        await SetRole(user, nameRole)
        await context.message.delete()
        await context.send(embed=embed(message))


def embed(message):
    embed = discord.Embed(description=message, colour=0xCC0000)
    return embed

def SetRole(nameUser,nameRole):
    user = nameUser
    role = nameRole
    return user.add_roles(discord.utils.get(user.guild.roles, name=role))

@bot.command()
async def role(ctx: commands.Context, arg: str = ""):
    channel = ctx.message.channel.id
    user = ctx.author
    roles = ctx.author.roles
    userRoles : list =[]
    context = ctx
    message : string = ("**" + str(user) + "** s'est ajouté le grade **" + str(arg) + "**")

    if Ischannel(channel) == False:
        await ctx.message.delete()
        return

    for role in roles:
        userRoles.append(role.name)

    devrole = ["developpeur","Developpeur","développeur","Développeur"]
    javarole = ["java","Java"]
    pythonrole = ["python","Python"]
    javascriptrole = ["Javascript","javascript","JavaScript"]
    juniorrole = ["junior","Junior"]
    seniorrole = ["Senior","Senior"]

    for java in javarole:
        if arg == java and not "Java" in userRoles:
            await SetUserRole("Java",user,context,message)
            return
        elif arg == java and "Java" in userRoles:
            await ctx.message.delete()
            return

    for dev in devrole:
        if arg == dev and not "Développeur" in userRoles:
            await SetUserRole("Développeur",user,context,message)
            return
        elif arg == dev and "Développeur" in userRoles:
            await ctx.message.delete()
            return

    for python in pythonrole:
        if arg == python and not "Python" in userRoles:
            await SetUserRole("Python",user,context,message)
            return
        elif arg == python and "Python" in userRoles:
            await ctx.message.delete()
            return

    for js in javascriptrole:
        if arg == js and not "JavaScript" in userRoles:
            await SetUserRole("JavaScript",user,context,message)
            return
        elif arg == js and "JavaScript" in userRoles:
            await ctx.message.delete()
            return

    for junior in juniorrole:
        if arg == junior and not "Junior" in userRoles:
            await SetUserRole("Junior",user,context,message)
            return
        elif arg == junior and "Junior" in userRoles:
            await ctx.message.delete()
            return

    for senior in seniorrole:
        if arg == senior and not "Senior" in userRoles:
            await SetUserRole("Senior",user,context,message)
            return
        elif arg == senior and "Senior" in userRoles:
            await ctx.message.delete()
            return

    message = ("Erreur! Veuillez entrer le grade souhaité")
    await ctx.message.delete()
    await context.send(embed=embed(message))

bot.run("")
