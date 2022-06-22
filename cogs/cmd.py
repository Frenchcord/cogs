from bot import bot
@bot.command
def hello(ctx):
  ctx.send('Hello, world!')
