import frenchcord
bot = frenchcord.Robot('Token')
bot.process_folder('cogs', logs=True, excepte=['in_dev'])
bot.connexion(['?'])
'''
One line bot method
import frenchcord; bot = frenchcord.Robot('token'); bot.process_folder('cogs', logs=True, excepte=['in_dev']); bot.connexion(['?'])
'''
