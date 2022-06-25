import frenchcord
bot = frenchcord.Robot('Token')
bot.process_folder('cogs', logs=True, excepte=['in_dev'])
bot.run(['?'])
