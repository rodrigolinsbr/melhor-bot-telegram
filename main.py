# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from corpus import student, introdution, lingPython, history, sport

bot = ChatBot('Teste')
bot.set_trainer(ListTrainer)
bot.train(introdution.trainIntrodution)
bot.train(student.trainStudent)
bot.train(lingPython.trainStudent)
bot.train(history.trainHistory)
bot.train(sport.trainSport)
cont = 0
def StartBot(message):
    cont = 0
    while True:

        # quest = input('Você: ')
        response = bot.get_response(message)
        if float(response.confidence) > 0.5:
            return str(response)
        else:
            cont = cont + 1
            if cont == 1:
                return 'Não entendi'

            elif cont == 2:
                return 'Desculpe, não estou entendo.Você sabe?'

            elif cont > 2:
                return 'Caramba, não sei! Você pode me dizer algo sobre isso?.'
