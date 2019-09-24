from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

robot = ChatBot('HAL9000')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

trainer = ListTrainer(robot)
trainer.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = robot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('HAL9000: ', resposta)
    else:
        print('HAL9000: Desculpe, Dave, não posso deixar que isso aconteça.')