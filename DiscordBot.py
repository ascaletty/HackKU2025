"""
Simple Discord bot to handle user input bc I'm too lazy to learn web dev stuff, besides, apis are fun
"""

import os
import discord
from dotenv import load_dotenv  # simple library to save me from getting my key doxed
from BotQuestionare import questionaire
from discord.ext import commands


class DepressoBot:
    def __init__(self):
        load_dotenv()  # loads the .env file
        self.TOKEN = str(os.getenv('DISCORD_TOKEN'))  # retrieves the discord token

        intents = discord.Intents.default()
        intents.message_content = True
        intents.dm_messages = True
        self.client = discord.Client(intents=intents)
        self.start_listening()

    def start_listening(self):
        @self.client.event
        async def on_ready():  # discord runs this whenever it connects to the bot
            print("I LIVE")

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return
            if message.guild is None:  # if the message is a dm
                await message.author.send('You have been singled out')
                questionaire(message)

            if 'could i have depression?' in message.content.lower():
                user = message.author
                await user.send('Sick')
                await message.channel.send('who knows?')




        self.client.run(self.TOKEN)



begin_everything = DepressoBot()