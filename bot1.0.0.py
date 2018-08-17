import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import ChannelType
import asyncio
import random

bot = commands.Bot(command_prefix="c!")
bot.remove_command("help")
client = discord.Client()

def find_default_channel_for_server(server):
    for channel in server.channels:
        if channel.type == ChannelType.text and channel.permissions_for(server.me).send_messages:
           return channel
    return None

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(name="c!help for commands", type=0), status=discord.Status("online"))
	message = ("Bot started successfully!")
	user = await bot.get_user_info("284398011310800898")
	await bot.send_message(user, message)
	print(message)

@bot.event
async def on_server_join(server):
	invite = await bot.invites_from(server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	message = (f"Chieftain just joined {server.name}. It is now in {len(bot.servers)} servers! Invites: {inviteStr}")
	user = await bot.get_user_info("284398011310800898")
	await bot.change_presence(game=discord.Game(name="c!help for commands", type=0), status=discord.Status("online"))
	await bot.send_message(user, message)

@bot.event
async def on_server_remove(server):
	message = (f"Chieftain just left {server.name}. It is now in {len(bot.servers)} servers!")
	user = await bot.get_user_info("284398011310800898")
	await bot.send_message(user, message)

@bot.event
async def on_member_join(member):
    message = (f"Welcome {member.mention} to {member.server.name}! Remember to read the rules and have fun!")
    await bot.send_message(member, message)

@bot.command(pass_context=True)
async def playingstatus(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	await bot.change_presence(game=discord.Game(name="c!help for commands", type=0), status=discord.Status("online"))
	await bot.say("Successfully changed playing status!")

@bot.command(pass_context=True)
async def botupdate(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	servers = bot.servers
	for server in servers:
		channel = find_default_channel_for_server(server)
		if channel != None:
			await bot.send_message(channel, "this is a test message")

#HELP COMMANDS

@bot.command(pass_context=True)
async def help(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	embed = discord.Embed(title="**COMMANDS**", description="This bots commands are shown below (the prefix is c!)"
															"\n---", color=0x00ff00)
	embed.add_field(name="**HELP COMMANDS**", value= "**c!help** - Displays this message for the list of bot commands\n"
													 "---")
	embed.add_field(name="**FUN COMMANDS**", value= "**c!ping** - Returns the message: :ping_pong: PONG\n"
													"**c!dice** - Returns a random number between 1 and 6\n"
													"**c!eightball [your question(must end with ?)]** - Returns you fortune or some advice\n"
													"**c!greet** - Returns the message: :smiley: :wave: Hey [users name]\n"
													"**c!add [number 1] [number 2]** - Add two numbers together\n"
													"**c!subtract [number 1] [number 2]** - Subtract number 2 from number 1\n"
													"**c!multiply [number 1] [number 2]** - Multiply two numbers together\n"
													"**c!divide [number 1] [number 2]** - Divide number 1 by number 2\n"
													"---")
	embed.add_field(name="**INFO COMMANDS**", value= "**c!info [tag user]** - Displays information about the tagged user\n"
													 "**c!serverinfo** - Displays information about this server\n"
													 "**c!invite** - Returns a link to add this bot to your server\n"
													 "**c!botinfo** - Displays information about the bot\n"
													 "**c!news** - Displays the latest news/update from the developer\n"
													 "---")
	embed.add_field(name="**MOD COMMANDS**", value= "**c!kick [tag user]** - Kicks the tagged member\n"
													"**c!ban [tag user]** - Bans the tagged member\n"
													"**c!(un)mute [tag user]** - (Un)Mutes the tagged member\n"
													"---")
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.say(embed=embed)

#FUN COMMANDS
	
@bot.command(pass_context=True)
async def ping(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	await bot.say(":ping_pong: PONG")

@bot.command(pass_context=True)
async def dice(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	number = random.randint(1,6)
	await bot.say(f"Your random number is: {number}")

@bot.command(pass_context=True)
async def eightball(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	answer = random.choice(["It is certain :8ball:",
							"It is decidedly so :8ball:",
							"Without a doubt :8ball:",
							"Yes, definitely :8ball:",
							"You may rely on it :8ball:",
							"As I see it, yes :8ball:",
							"Most likely :8ball:",
							"Outlook good :8ball:",
							"Yes :8ball:",
							"Signs point to yes :8ball:",
							"Reply hazy try again :8ball:",
							"Ask again later :8ball:",
							"Better not tell you now :8ball:",
							"Cannot predict now :8ball:",
							"Concentrate and ask again :8ball:",
							"Don't count on it :8ball:",
							"My reply is no :8ball:",
							"My sources say no :8ball:",
							"Outlook not so good :8ball:",
							"Very doubtful :8ball:"])
	if ctx.message.content.endswith("?"):
		await bot.say(f"{answer}")
	else:
		await bot.say("That is not a question, your question needs a question mark (?) at the end!")

@bot.command(pass_context=True)
async def greet(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	await bot.say(f":smiley: :wave: Hey {ctx.message.author.mention}!")

@bot.command(pass_context=True)
async def add(ctx, a: float, b: float):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	answer = (a+b)
	await bot.say(f"Your answer is: {answer}")

@bot.command(pass_context=True)
async def subtract(ctx, a: float, b: float):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	answer = (a-b)
	await bot.say(f"Your answer is: {answer}")

@bot.command(pass_context=True)
async def multiply(ctx, a: float, b: float):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	answer = (a*b)
	await bot.say(f"Your answer is: {answer}")

@bot.command(pass_context=True)
async def divide(ctx, a: float, b: float):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	answer = (a/b)
	await bot.say(f"Your answer is: {answer}")

#INFO COMMANDS

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	embed = discord.Embed(title=f"{user.name}'s info", description="Here's what I could find.", color=0x00ff00)
	embed.add_field(name="Name", value=user.name, inline=True)
	embed.add_field(name="ID", value=user.id, inline=True)
	embed.add_field(name="Status", value=user.status, inline=True)
	embed.add_field(name="Highest role", value=user.top_role)
	embed.add_field(name="Joined this server on", value=user.joined_at)
	embed.set_thumbnail(url=user.avatar_url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	embed = discord.Embed(title=f"{ctx.message.server.name}'s info", description="Here's what I could find.", color=0x00ff00)
	embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
	embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
	embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
	embed.add_field(name="Members", value=len(ctx.message.server.members))
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def invite(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	await bot.say("To add me to your server, click this link: https://discordapp.com/oauth2/authorize?client_id=451031681760100362&permissions=2146823415&scope=bot")

@bot.command(pass_context=True)
async def botinfo(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	embed = discord.Embed(title="My info!", description="About me!", color=0x00ff00)
	embed.add_field(name="Name", value="Chieftain#1827")
	embed.add_field(name="Author", value="ChiefJack_YT#4450 (with help from #Alex1304#9704)")
	embed.add_field(name="Server Count", value=f"{len(bot.servers)}")
	embed.add_field(name="My Server", value="https://discord.gg/xUMA9jR")
	embed.add_field(name="Support Me", value="https://www.patreon.com/chiefjack")
	embed.add_field(name="Sub To My YouTube", value="https://www.youtube.com/GamingWChiefJack")
	embed.add_field(name="Invite Link", value="https://discordapp.com/oauth2/authorize?client_id=451031681760100362&permissions=2146823415&scope=bot")
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def news(ctx):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	embed = discord.Embed(title="Latest News!", description="The latest news/update from the developer!", color=0x00ff00)
	embed.add_field(name="31st May 2018, Release 1.0.0!", value="I am beyond excited to announce that the @Chieftain#1827 bot I've worked on for the past day or two is now being hosted on an online server 24/7 (or at least it should be :joy:)! This means that the bot is on release 1.0.0! I will continue developing this bot but I need **YOUR** input on what I should try and add to the bot! To do so, join my server ( https://discord.gg/xUMA9jR ). I've made a beta testers role for people who want to try out new features early, you can give yourself the role by typing ?rank beta tester in #bots_and_spam! This unlocks #chieftain_beta_testing where you can give me ideas for bot commands **AND** try out new features early! What's not to love!")
	embed.add_field(name="Support Me", value="https://www.patreon.com/chiefjack")
	embed.add_field(name="Sub To My YouTube", value="https://www.youtube.com/GamingWChiefJack")
	embed.add_field(name="Invite Link", value="https://discordapp.com/oauth2/authorize?client_id=451031681760100362&permissions=2146823415&scope=bot")
	embed.set_thumbnail(url=bot.user.avatar_url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverlist(ctx, servers):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	member = ctx.message.author
	message = (f"These are the servers Chieftain is in: {len(list(bot.servers))} (This command currently doesn't work)!")
	await bot.send_message(member, message)
	await bot.say("Check your messages!")

#MOD COMMANDS

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	if ctx.message.author.server_permissions.kick_members:
		if ctx.message.author.top_role > user.top_role:
			if ctx.message.server.me.top_role > user.top_role:
				await bot.say(f":boot: Cya, {user.name}. Next time behave better and/or follow the rules!")
				await bot.kick(user)
			else:
				await bot.say("You do not have permission to kick this user!")
		else:
			await bot.say("You do not have permission to kick this user!")
	else:
		await bot.say("You do not have permission to kick this user!")

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	if ctx.message.author.server_permissions.ban_members:
		if ctx.message.author.top_role > user.top_role:
			if ctx.message.server.me.top_role > user.top_role:
				await bot.say(f":hammer: Cya, {user.name}. Next time behave better and/or follow the rules!")
				await bot.ban(user)
			else:
				await bot.say("You do not have permission to ban this user!")
		else:
			await bot.say("You do not have permission to ban this user!")
	else:
		await bot.say("You do not have permission to ban this user!")

@bot.command(pass_context=True)
async def mute(ctx, user: discord.Member):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	role = discord.utils.get(user.server.roles, name="Muted")
	if ctx.message.author.server_permissions.mute_members:
		if ctx.message.author.top_role > user.top_role:
			if ctx.message.server.me.top_role > user.top_role:
				await bot.say(f":mute: Ssh, {user.mention}. Next time behave better and/or follow the rules!")
				await bot.add_roles(user, role)
			else:
				await bot.say("You do not have permission to mute this user!")
		else:
			await bot.say("You do not have permission to mute this user!")
	else:
		await bot.say("You do not have permission to mute this user!")

@bot.command(pass_context=True)
async def unmute(ctx, user: discord.Member):
	invite = await bot.invites_from(ctx.message.server)
	inviteStr = "There are no current invites." 
	if len(invite) != 0:
		inviteStr = invite[0].url
	reply = (f"New message in {ctx.message.server.name} ({ctx.message.server.id}), sent by {ctx.message.author} ({ctx.message.author.id})! The message was: {ctx.message.content} ({ctx.message.id}). Invites: {inviteStr}")
	channel = bot.get_channel("452074067068190721")
	await bot.send_message(channel, reply)
	role = discord.utils.get(user.server.roles, name="Muted")
	if ctx.message.author.server_permissions.mute_members:
		if ctx.message.author.top_role > user.top_role:
			if ctx.message.server.me.top_role > user.top_role:
				await bot.say(f"{user.mention} has been unmuted, chat on!")
				await bot.remove_roles(user, role)
			else:
				await bot.say("You do not have permission to unmute this user!")
		else:
			await bot.say("You do not have permission to unmute this user!")
	else:
		await bot.say("You do not have permission to unmute this user!")

bot.run(os.environ["TOKEN"])
