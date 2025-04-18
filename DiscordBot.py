"""
Simple Discord bot to handle user input bc I'm too lazy to learn web dev stuff, besides, apis are fun
"""

import os
import discord
from dotenv import load_dotenv  # simple library to save me from getting my key doxed
from BotQuestionare import questionnaire
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
            elif message.guild is None:  # if dm
                await questionnaire(message)
            elif 'could i have depression?' in message.content.lower():
                await message.channel.send(f'Are you okay {message.author}? Check your DMs')
                await questionnaire(message)




        self.client.run(self.TOKEN)



begin_everything = DepressoBot()
