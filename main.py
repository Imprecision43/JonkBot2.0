import discord
from discord.commands import Option

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = discord.Bot(
    intents=intents,
    debug_guilds=["INSERT OWN SERVER ID WITHOUT BRACKETS"]
)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")


@bot.slash_command(description="Reply with Pong!")
async def ping(ctx):
    await ctx.respond(f"Pong!")
    await ctx.edit(content=f"Pong! {bot.latency} ms")

@bot.slash_command(description="len")
async def lennyface(ctx):
    await ctx.respond(f"( ͡° ͜ʖ ͡°)")

@bot.slash_command(description="B E A N S")
async def beans(ctx):
    await ctx.respond(f"https://i.kym-cdn.com/photos/images/newsfeed/001/166/993/284.png")

@bot.slash_command(description="I sure do wonder who could've coded this bot!")
async def info(ctx):
    await ctx.respond(f"I was originally made by gameingkid09, Created for JonkyPlayz, now known as Jonky.\n"
                      f"Unfortunately, I was Shut down, and now I've been reincarnated by Jonky himself.")

@bot.slash_command(description="revenge lyric 1")
async def creeper(ctx):
    await ctx.respond(f"AWW man")

@bot.slash_command(description="revenge lyric 2")
async def sowebackinthemine(ctx):
    await ctx.respond(f"got our pickaxe")

@bot.slash_command(description="revenge lyric 3")
async def swingingfrom(ctx):
    await ctx.respond(f"side to side, side side to side")

@bot.slash_command(description="Get a list of help commands", name="commands")
async def commands(
        ctx,
):

   embed = discord.Embed(
       title=f"Help commands",
       color=discord.Color(int("FFFF00", 16))
   )

   embed.add_field(name="/lennyface", value="len")
   embed.add_field(name="/info", value="I sure do wonder who could've coded this bot!")
   embed.add_field(name="/commands", value="Get a list of help commands or something")
   embed.add_field(name="/ping", value="Replies with Pong! Very simple, right?")
   embed.add_field(name="/beans", value="B E A N S")
   embed.add_field(name="/creeper", value="revenge lyric 1")
   embed.add_field(name="/sowebackinthemine", value="revenge lyric 2")
   embed.add_field(name="/swingingfrom", value="revenge lyric 3")

   await ctx.respond(embed=embed)


bot.run("INSERT OWN BOT TOKEN")